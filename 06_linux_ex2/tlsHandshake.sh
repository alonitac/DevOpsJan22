echo "installing tool to transform jason data to readable text"
sudo apt install jq

echo "sending hello HTTP client request to a server and creating a response text file"
curl -d '{"clientVersion":"3.2", "message":"Client Hello"}' -H "Content-Type: application/json" -X POST http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello  --> response.txt

echo "sorting the retrieved response"
cat response.txt | jq -r '.serverVersion' > serverVersion.txt
cat response.txt | jq -r '.sessionID' > sessionID.txt
cat response.txt | jq -r '.serverCert' > cert.pem

echo "creating a variable SESSION_ID"
export SESSION_ID=$(cat sessionID.txt)

echo "importing certificate authority essential file"
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem

echo "verifying the certificate"
openssl verify -CAfile cert-ca-aws.pem cert.pem
