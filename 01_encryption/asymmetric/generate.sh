ssh-keygen -t rsa -b 4096 -m PEM

echo "convert public and private key to .pem format..."

ssh-keygen -f ~/.ssh/id_rsa.pub -e -m PKCS8 > ~/.ssh/id_rsa.pem
openssl rsa -in ~/.ssh/id_rsa -outform pem > ~/.ssh/id_rsa_pr.pem
