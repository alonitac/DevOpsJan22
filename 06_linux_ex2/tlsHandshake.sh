#!/bin/bash


# FIXME Perfect implementation

# Remove files and environment variables from previous run

unset MY_MASTER_KEY
unset SESSION_ID
unset MASTER_KEY
unset DECRYPTED_SAMPLE_MESSAGE
rm -f cert-ca-aws.pem
rm -f decSampleMsgReady.txt
rm -f encryptedmasterKey.txt
rm -f encSampleMsgReady.txt
rm -f encSampleMsg.txt
rm -f export2.txt
rm -f export.txt
rm -f masterKey.txt
rm -f serverVersion.txt
rm -f sessionID.txt
rm -f cert.pem

# Install jq package for parsing and saving specific keys from the JSON response

if which jq >/dev/null; then
    echo
else
    echo "jq isn't installed, you might be asked to enter your password in order to install it"
    sudo apt install -y jq
fi

# Step 1 - Client Hello (Client -> Server)

curl -H "Content-Type: application/json" -d '{"clientVersion": "3.2","message": "Client Hello"}' -X POST http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello > export.txt

# Step 2 - Server Hello (Server -> Client)

cat export.txt | jq -r '.serverVersion' > serverVersion.txt
cat export.txt | jq -r '.sessionID' > sessionID.txt
cat export.txt | jq -r '.serverCert' > cert.pem
export SESSION_ID=$(cat sessionID.txt)

# Steps 3-6  Server Certificate Verification --> Client-Server master-key exchange --> Server verification message --> Client verification message

wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem
openssl verify -CAfile cert-ca-aws.pem cert.pem >> verify.log
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )
if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  	echo "Server Certificate is invalid."
  	exit 1
else
        openssl rand -base64 32 > masterKey.txt
        export MY_MASTER_KEY=$(cat masterKey.txt)
        openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0 > encryptedmasterKey.txt
        export MASTER_KEY=$(cat encryptedmasterKey.txt)
        curl -d '{"sessionID": "'$SESSION_ID'","masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}' -H "Content-Type: application/json" -X POST http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange > export2.txt
        cat export2.txt | jq -r '.encryptedSampleMessage' > encSampleMsg.txt
        cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt
        openssl enc -d -aes-256-cbc -pbkdf2 -k $MY_MASTER_KEY -in encSampleMsgReady.txt -out decSampleMsgReady.txt
fi

DECRYPTED_SAMPLE_MESSAGE=$(cat decSampleMsgReady.txt)
if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  	echo "Server symmetric encryption using the exchanged master-key has failed."
  	exit 1
else
  	echo "Client-Server TLS handshake has been completed successfully"
fi