# installing tool to transform jason data to readable text
sudo apt install jq

# sending a client hello HTTP request to a server and creating a response text file
curl -d '{"clientVersion":"3.2", "message":"Client Hello"}' -H "Content-Type: application/json" -X POST http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello  --> response.txt

#observing response content
cat response.txt

# sorting the retrieved response into text files
cat response.txt | jq -r '.sessionID' > sessionID.txt
cat response.txt | jq -r '.serverCert' > cert.pem

# importing certificate authority essential file
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem

# verifying the certificate
openssl verify -CAfile cert-ca-aws.pem cert.pem

# making sure the verification result is 'cert.pem: OK'
VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

#if we have reached this far than the certificate is valid and the exit command didn't run

#generating a random 32 bit string
openssl rand -out masterKey.txt -base64 32

#encrypting the generated master-key secret with the server certificate
openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0

# creating variables and checking they were assigned the correct values
export SESSION_ID=$(cat sessionID.txt)
printenv SESSION_ID
export MASTER_KEY=$(cat masterKey.txt)
printenv MASTER_KEY

#sending another HTTP post request to a server and creating a response2 text file
curl -d '{"sessionID": "'$SESSION_ID'","masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}' -H "Content-Type: application/json" -X POST http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange >response2.txt

#observing response2 content
cat response2.txt

#sorting relevant retrieved response into a text file
cat response2.txt | jq -r '.encryptedSampleMessage' > encSampleMsg.txt

#the content of encryptedSampleMessage is stored in a file called encSampleMsg.txt
cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt
#file encSampleMsgReady.txt is ready now to be used in "openssl enc...." command

#decrypting sample message and storing the it in a new variable
openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt -out decrypted.txt
cat decrypted.txt
export DECRYPTED_SAMPLE_MESSAGE=$(cat decrypted.txt)
printenv DECRYPTED_SAMPLE_MESSAGE

#checking decryption was successful
if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi