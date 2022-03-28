curl  -X POST -H "Content-Type: application/json" -d '{"clientVersion":"3.2","message":"Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverCert' > cert.pem

wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem --ca-certificate=cert-ca-aws.pem

VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi

openssl rand -base64 32 > masterKey.txt

SESSION_ID=$(curl  -X POST -H "Content-Type: application/json" -d '{"clientVersion":"3.2","message":"Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.sessionID')

MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc  -in masterKey.txt -outform DER cert.pem | base64 -w 0)

curl  -X POST -H "Content-Type: application/json" -d '{"sessionID":"'"${SESSION_ID}"'","masterKey":"'"${MASTER_KEY}"'","sampleMessage":"Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.am>

cat SampleMessage.txt | base64 -d > SampleMessageReady.txt

openssl enc -d -aes-256-cbc -pbkdf2  -kfile masterKey.txt -in SampleMessageReady.txt -out decrypted_secret.txt

DECRYPTED_SAMPLE_MESSAGE=$(cat decrypted_secret.txt)

if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi

