#Pulling initial data from server.
  echo "Performing Client Hello"
  #tput setaf 3; SERVERVERSIONVAR=$(curl -X POST -H "Content-Type: application/json" -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverVersion')
  tput setaf 3; SESSIONIDVAR=$(curl -X POST -H "Content-Type: application/json" -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.sessionID')
  tput setaf 3; curl -X POST -H "Content-Type: application/json" -d '{"clientVersion": "3.2", "message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello | jq -r '.serverCert' >servercert.pem
  tput sgr0

echo ""
sleep 1
#Checking if CA file exists, if not download it.
  echo "Downloading relevant AWS CA file"
  if [ ! -f /cert-ca-aws.pem ]; then
      tput setaf 3; wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem
      tput sgr0
      tput setaf 2; echo "CA Does not exist, downloading"
  fi
  tput sgr0

echo ""
sleep 1
#Verify our received certificate against the CA file.
  echo "verifying certificate"
  is_OK=$(openssl verify -CAfile cert-ca-aws.pem servercert.pem | grep "servercert.pem: OK")
  if [ "servercert.pem: OK" = "$is_OK" ]; then
      tput setaf 2; echo "Certificate Verified"
  else
      tput setaf 1; echo "Certificate not verified, exiting"
      exit 1
  fi
  tput sgr0

echo ""
sleep 1
#Generate master key string to file and encrypt it.
  echo "Generating the master key and ecrypting it"
  openssl rand -base64 32 > masterKey.txt
  MASTERKEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER servercert.pem  | base64 -w 0)
  echo "$MASTERKEY" > masterKeyEnc.txt

echo ""
sleep 1
#Send key to server and receive encrypted example msg.
  echo "Exchanging key with server and receiving example msg"
  tput setaf 3; curl -X POST -H "Content-Type: application/json" -d '{"sessionID": "'$SESSIONIDVAR'", "masterKey": "'$MASTERKEY'", "sampleMessage": "Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange | jq -r '.encryptedSampleMessage' > encryptedmsg.txt
  tput sgr0

echo ""
sleep 1
#Convert encrypted msg from base64 to binary.
  echo "converting the encrypted msg from base64 to binary"
  cat encryptedmsg.txt | base64 -d > encryptedmsgready.txt


echo ""
sleep 1
#Decrypt the example msg and check if matches the unencrypted.
  echo "decrypting sample msg"
  openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encryptedmsgready.txt -out decryptedmsg.txt

  decryptedmsg=$(cat decryptedmsg.txt)
  if [ "$decryptedmsg" != "Hi server, please encrypt me and send to client!" ]; then
    tput setaf 1; echo "Server symmetric encryption using the exchanged master-key has failed."
    exit 1
  else
    tput setaf 2; echo "Client-Server TLS handshake has been completed successfully"
  fi
  tput sgr0
  exit 1