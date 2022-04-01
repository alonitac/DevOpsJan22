# installing tool to transform jason data to readable text
sudo apt install jq

# sending hello HTTP client request to a server and creating a response text file
curl -d '{"clientVersion":"3.2", "message":"Client Hello"}' -H "Content-Type: application/json" -X POST http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello  --> response.txt

# sorting the retrieved response
cat response.txt | jq -r '.serverVersion' > serverVersion.txt
cat response.txt | jq -r '.sessionID' > sessionID.txt
cat response.txt | jq -r '.serverCert' > cert.pem

# creating a variable SESSION_ID
export SESSION_ID=$(cat sessionID.txt)

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

