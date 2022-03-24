#TLS communication
#Step 1 - Client Hello (Client -> Server).

curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello

#Step 2 - Server Hello (Server -> Client)

curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverCert' > cert.pem

curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverCert' > sessionID.txt

wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem

openssl verify -CAfile cert-ca-aws.pem cert.pem

#cert.pem: OKVERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]
then

  echo "Server Certificate is invalid."
  exit 1

fi

# create mastekey.txt 32 bytes file

dd if=/dev/urandom of=masterKey.txt bs=32 count=1

MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)

SESSION_ID=$(curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.sessionID'

curl -X POST -H 'Content-Type: application/json' -d '{ "sessionID": "'$SESSION_ID'", "masterKey": "'$MASTER_KEY'", "sampleMessage":"Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange | jq -r ' .encryptedSampleMessage' > encryptedSampleMessage.txt

cat  encryptedSampleMessage.txt | base64 -d > encSampleMsgReady.txt

openssl -enc -d -aes-256-cbc -pbkdf 2 -kfile masterKey.txt -in encSampleMsgReady.txt -out decryptedSampleMassage.txt | base64 -w 0

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ];
then

  echo "Server symmetric encryption using the exchanged master-key has failed."
exit 1

  else echo "Client-Server TLS handshake has been completed successfully"

fi
