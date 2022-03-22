#!/bin/bash
echo "Initializing random number generator..."
openssl rand -out masterKey.txt -base64 32
if [ $? -gt 0 ]
then
        echo "couldn't generate key 32 based"
        exit 1
fi
curl  -X POST -H "Content-Type: application/json" -d '{"clientVersion":"3.2","message":"Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverCert,.sessionID' >tmp.txt
STATUS=$?
if [ $STATUS -gt 0 ]
then
        echo "run \"man curl|jq\" end check for details for error status number $STATUS"
        # for example: "error 20 at 0 depth lookup: unable to get local issuer certificate"
        # This is Eve that is the reason error 20 is unlisted in curl
        exit 1
fi
# Instead could be used /clienthello -o (>) tmp.txt and use twice jq -r on cert.pem and sessionID
head --lines=-1 tmp.txt>cert.pem
export SESSION_ID=$( tail -1 tmp.txt )
rm -f tmp.txt
export VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]
then
        echo "Server Certificate is invalid."
        exit 1
fi

MASTER_KEY=$( openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0 )
curl -X POST -H 'Content-Type: application/json' -d '{"sessionID": "'$SESSION_ID'","masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange  | jq -r '.encryptedSampleMessage' > encSampleMsg.txt
STATUS=$?
if [ $STATUS -gt 0 ]
then
        echo "run \"man curl|jq\" end check for details for error status number $STATUS"
        exit 1
fi
cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt
openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt -out decrypted_secret.txt
export DECRYPTED_SAMPLE_MESSAGE=`cat decrypted_secret.txt`
if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi