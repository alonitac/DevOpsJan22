curl -X POST -H "Content-Type: application/json" -d '{ "clientVersion": "3.2",  "message": "Client Hello"}'  http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello
##jq command got messy do I have pasted the cert. data with nano
nano cert.pem
#"-----BEGIN CERTIFICATE-----\n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\n-----END CERTIFICATE-----\n\n"
nano serverVersion.txt
#3.2
cat >> session.id.txt
#f6ea6304-7c94-48ab-b2b2-7dbdaf53d05b

wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem
openssl verify -CAfile cert-ca-aws.pem cert.pem


VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )

if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi
##generate a 32 random bytes string
head -c32 /dev/random
cat >> masterKey.txt
##VoizjsXaXZUSiMhdgAvSclea

#setting a variable
$ sudo vim /etc/environment
export SESSION_ID=f0f29caa-9af3-451f-980a-1abda115f0d0
export MASTER_KEY=VoizjsXaXZUSiMhdgAvSclea

curl -X POST -H "Content-Type: application/json" -d '{ "sessionID": "'$SESSION_ID'",  "masterKey": "'$MASTER_KEY'", "sampleMessage": "Hi server, please encrypt me and send to client!" }' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange
cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt
openssl smime -encrypt -aes-256-cbc -in encSampleMsgReady.txt -outform DER cert.pem | base64 -w 0