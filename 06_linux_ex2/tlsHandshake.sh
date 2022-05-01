#!/bin/bash

# Client Hello
# FIXME calling /clienthello endpoint many times is redundant -5
curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello

# store sessionID into sessionID text file
curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.sessionID' > session.txt

# store serverCert into cert.pem text file

curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverCert' > cert.pem

# store serverVersion into serverVersion text file
curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverVersion' > serverVersion.txt

# get Certificate from Certificate Authority via wget

wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem

# verify the certificate
openssl verify -CAfile cert-ca-aws.pem cert.pem

# snippet to exit the program if the certificate validation failed
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

#  generate a 32 random bytes string and save it to masterKey.txt text file
openssl rand -base64 32 > masterKey.txt

# Create sessionid bash var
SESSION_ID=`cat session.txt`

# Encrypt master key to file encrypt_key
openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0 > encrypt_key

# Create encrypted master key bash var
MASTER_KEY=`cat encrypt_key`

# curl and save encryptedSampleMessage to file encSampleMsg.txt
curl -X POST -H 'Content-Type: application/json' -d '{"sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!" }' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange | jq -r '.encryptedSampleMessage' > encSampleMsg.txt

# encoding
cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt

# decrypt message (copy paste from Alexey's solution because i did not find the right notaion)
openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt -out decrypt.txt

VERIFICATION_RESULT=$( openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt -out decrypt.txt
 )

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi