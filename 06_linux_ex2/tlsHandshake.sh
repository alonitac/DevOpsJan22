curl -i -X POST -H "Content-Type: application/json" -d '{"clientVersion":"3.2","message":"Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello
curl  -X POST -H "Content-Type: application/json" -d '{"clientVersion":"3.2","message":"Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverCert' > cert.pem

VERIFICATION_RESULT=$( openssl verify -CAfile cert-ca-aws.pem cert.pem )
if [ "$VERIFICATION_RESULT" != "cert.pem: OK" ]; then
  echo "Server Certificate is invalid."
  exit 1
fi
openssl rand -base64 32 >masterKey.txt

SESSION_ID=$(cat sessionID)
MASTER_KEY=$(cat masterKey.txt)
curl -i -X POST -H "Content-Type: application/json" -d '{"sessionID":"'${SESSION_ID}'","masterKey":"'${MASTER_KEY}'","sampleMessage":"Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange



