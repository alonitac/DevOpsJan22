#!/bin/bash

#Dima`s Solution
set -xe
rm -rf ./certs/
mkdir -p ./certs/

#http request for endpoint /clienthello
curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2","message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello > ./certs/clientHelloResponse.txt

cat ./certs/clientHelloResponse.txt | jq -r '.serverCert' > ./certs/cert.pem

cat ./certs/clientHelloResponse.txt | jq -r '.sessionID' > ./certs/sessionID.txt

#amazon certificate downlaod
wget -P ./certs/ https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem

#certificat verification
VERIFICATION_RESULT=$( openssl verify -CAfile ./certs/cert-ca-aws.pem ./certs/cert.pem )

if [ "$VERIFICATION_RESULT" != "./certs/cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
  else
  printf "Valid Certificate\n"
fi

#generate 32 bytes string
openssl rand -base64 32 > ./certs/masterKey.txt

#insert bash variables
SESSION_ID=$(cat ./certs/sessionID.txt)
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in ./certs/masterKey.txt -outform DER ./certs/cert.pem | base64 -w 0)

#http request for  endoint /keyexchange
curl -X POST -H 'Content-Type: application/json' -d '{"sessionID":"'${SESSION_ID}'","masterKey":"'${MASTER_KEY}'","sampleMessage":"Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange | jq -r '.encryptedSampleMessage' > ./certs/encSampleMsg.txt

#encode it to binary  (base 64 decrypt)
cat ./certs/encSampleMsg.txt | base64 -d > ./certs/encSampleMsgReady.txt

#decrypt the message
openssl enc -d -aes-256-cbc -pbkdf2 -kfile ./certs/masterKey.txt -in ./certs/encSampleMsgReady.txt -out ./certs/decSampleMsg.txt

#Final Stage
DECRYPTED_SAMPLE_MESSAGE=$(cat ./certs/decSampleMsg.txt)
if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi

#end

