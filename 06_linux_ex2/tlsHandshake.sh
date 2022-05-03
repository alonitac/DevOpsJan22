#!/bin/bash


# FIXME Great!

curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2","message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello -o res_server.json


jq -r '.serverCert' res_server.json > cert.pem


SESSION_ID=$(jq -r '.sessionID' res_server.json)

#openssl verify -CAfile cert-ca-aws.pem cert.pem

VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi


openssl rand -base64 23 > masterKey.txt


#openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0

MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)

curl -X POST -H 'Content-Type: application/json' -d '{"sessionID": "'$SESSION_ID'","masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange -o encSampleMsg.json

jq -r '.encryptedSampleMessage' encSampleMsg.json > encSampleMsg.txt

cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt

openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt -out encrypted_secret

DECRYPTED_SAMPLE_MESSAGE=$(<encrypted_secret)

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi

