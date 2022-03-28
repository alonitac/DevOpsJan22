#!/bin/bash
sudo apt-get install jq
echo "send client hello using JSON via HTTP request to the server"
curl  -X POST -H "Content-Type: application/json" -d '{"clientVersion":"3.2","message":"Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello |jq -r '.sessionID' > SESSION_ID
echo "create SESSION_ID"
curl  -X POST -H "Content-Type: application/json" -d '{"clientVersion":"3.2","message":"Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello |jq -r ".serverCert" > cert.pem
echo "save server certification as PEM certification"
cat cert.pem
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem
cat cert-ca-aws.pem
cat cert.pem
openssl verify -CAfile cert-ca-aws.pem cert.pem

VERIFICATION_RESULT=$(openssl verify -CAfile cert-ca-aws.pem cert.pem)
openssl verify -CAfile cert-ca-aws.pem cert.pem
VERIFICATION_RESULT=`openssl verify -CAfile cert-ca-aws.pem cert.pem`
VERIFICATION_RESULT=$(openssl verify -CAfile cert-ca-aws.pem cert.pem)
echo $VERIFICATION_RESULT

if [[ $VERIFICATION_RESULT != "cert.pem: OK" ]]; then
  echo "Server Certificate is invalid."
  exit 1
fi
echo
echo
openssl rand -base64 23 > masterKey.txt
cat masterKey.txt
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)
echo $MASTER_KEY
SESSION_ID=$(curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.sessionID')
curl -X POST -H 'Content-Type: application/json' -d '{ "sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage":"Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange | jq -r ' .encryptedSampleMessage' > encryptedSampleMessage.txt
cat encryptedSampleMessage.txt | base64 -d > encSampleMsgReady.txt
openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt -out answer.txt
DECRYPTED_SAMPLE_MESSAGE=$(<answer.txt)
if [[ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else   echo "Client-Server TLS handshake has been completed successfully"
fi
