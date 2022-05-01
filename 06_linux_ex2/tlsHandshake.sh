#!/bin/bash

echo "curl to send the following Client Hello HTTP request to the server"

curl  -X POST -H "Content-Type: application/json" -d '{"clientVersion":"3.2","message":"Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello |jq -r '.sessionID' > SESSION_ID

echo "variable called SESSION_ID for later usage"

cat SESSION_ID
# FIXME calling twice /clienthello endpoint is redundant -5
curl  -X POST -H "Content-Type: application/json" -d '{"clientVersion":"3.2","message":"Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello |jq -r ".serverCert" > cert.pem

echo "save the server cert in a file called cert.pem"

cat cert.pem

# FIXME echo is redundant here... try to keep you script clean as organized
echo
echo

wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem
echo
echo
cat cert-ca-aws.pem
echo
echo
cat cert.pem
echo
echo
openssl verify -CAfile cert-ca-aws.pem cert.pem
echo
echo

VERIFICATION_RESULT=$(openssl verify -CAfile cert-ca-aws.pem cert.pem)
echo
echo
openssl verify -CAfile cert-ca-aws.pem cert.pem
echo
echo
VERIFICATION_RESULT=`openssl verify -CAfile cert-ca-aws.pem cert.pem`
echo
echo
VERIFICATION_RESULT=$(openssl verify -CAfile cert-ca-aws.pem cert.pem)
echo
echo
echo $VERIFICATION_RESULT
echo

if [[ $VERIFICATION_RESULT != "cert.pem: OK" ]]; then
  echo "Server Certificate is invalid."
  exit 1
fi
echo
echo
openssl rand -base64 23 > masterKey.txt
echo
echo
cat masterKey.txt
echo
echo
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)
echo
echo
echo $MASTER_KEY
echo
echo
# FIXME why didn't you use the SESSION_ID file created above? you should have called /clienthello only once the whole script -2
SESSION_ID=$(curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.sessionID')
echo
echo
curl -X POST -H 'Content-Type: application/json' -d '{ "sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage":"Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange | jq -r ' .encryptedSampleMessage' > encryptedSampleMessage.txt
echo
echo
cat  encryptedSampleMessage.txt | base64 -d > encSampleMsgReady.txt
echo
echo
openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt -out answer.txt
echo
echo
DECRYPTED_SAMPLE_MESSAGE=$(<answer.txt)
echo
echo
if [[ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else   echo "Client-Server TLS handshake has been completed successfully"
fi