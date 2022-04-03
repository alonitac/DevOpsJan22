# client hello request
curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello
#output : {"serverVersion": "3.2", "sessionID": "9824252f-dba9-41ea-821f-b0e6c8e4d795", "serverCert": "-----BEGIN CERTIFICATE----- ..}

# touch Cert.pem = the value in serverCert save in the file Cert.pem
curl -X POST -H "Content-Type: application/json" -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverCert' > Cert.pem

# touch SessionID.txt = the value in serverCert save in the file Cert.pem
curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.sessionID' > SessionID.txt

#download amazon web services cert
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem

VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem Cert.pem )

if [ "$VERIFICATION_RESULT" != "Cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi
# To make sure it works properly
openssl verify -CAfile cert-ca-aws.pem Cert.pem

#generate a 32 bytes randomly
openssl rand -base64 32 > masterKey.txt
#encrypt the generated master-key secret with the server certificate
openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER Cert.pem | base64 -w 0

SESSION_ID=$(cat SessionID.txt)
#הורס את המפתיח שלי דרך המפתח הגלובאלי של אמזון ואז אמזון יכול לפתוח עם המפתח הפרטי שלו
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER Cert.pem | base64 -w 0)

#touch encryptedSampleMessage.txt
curl -X POST -H 'Content-Type: application/json' -d '{"sessionID": "'${SESSION_ID}'", "masterKey": "'${MASTER_KEY}'", "sampleMessage": "Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange | jq -r .'encryptedSampleMessage' > encryptedSampleMessage.txt

touch encSampleMsgReady.txt
cat encryptedSampleMessage.txt | base64 -d > encSampleMsgReady.txt

# -d = decrypt
# -kfile infile = Read passphrase from file
# -aes-256-cbc    The algo name
# -in             The input file
# -out            The output file
#touch decryptedSampleMessage.txt
openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt -out decryptedSampleMessage.txt

DECRYPTED_SAMPLE_MESSAGE=$(cat decryptedSampleMessage.txt)

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi



