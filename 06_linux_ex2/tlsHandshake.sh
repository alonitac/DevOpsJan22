#!/bin/bash

curl -X POST -H "Content-Type: application/json" -d '{ "clientVersion": "3.2", "message": "Client Hello" }' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello > temp.json #temp.json saving 1st 'POST' request
# ^^ 1st post - Hello (source below) ^^
# ^^ Found in: google.com\how to post using curl > linuxize\Specifying the Content-Type ^^
jq -r '.serverCert' temp.json > cert.pem #saving servers json response - ".serverCert parameter" to cert.pem
SESSION_ID=$( jq -r '.sessionID' temp.json ) # sessionID storage in a variable

wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem #Downlaod of original cert for later verification
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem ) #Verification command (hinted) output saved into a variable
if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi
    echo "Server Certificate is valid."

openssl rand -base64 23 > masterKey.txt #Generating master-key (source below)
# ^^ Found in: google.com\how to generate a random bytes bash > linuxhint/generate-random-string-bash/Method_5 ^^
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)
# ^^Encrypting the generated master-key secret with the server certificate and saving output to a variable ^^
curl -X POST -H 'Content-Type: application/json' -d '{ "sessionID": "'$SESSION_ID'","masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange > temp_2.json
# ^^ 2nd post - Message ^^
jq -r '.encryptedSampleMessage' temp_2.json > enc_msg.txt #exclude the encrypted message parameter & saving to a file
cat enc_msg.txt | base64 -d > bin_msg.txt #Binary conversion for later decryption

openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in bin_msg.txt -out dec_scrt.txt #Decryption
DECRYPTED_SAMPLE_MESSAGE=$( < dec_scrt.txt) #Storage of decrypted output in a variable

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi
echo '(...Removing files)'
rm cert.pem cert-ca-aws.pem dec_scrt.txt bin_msg.txt enc_msg.txt masterKey.txt temp.json temp_2.json
#Cleaning directory