curl -X POST -H 'Content-Type: application/json' -d '{"clientVersion": "3.2","message": "Client Hello"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clienthello -o response.json

jq -r '.serverCert' response.json >cert.pem
jq -r '.sessionID' response.json >.sessionID.txt

#c2fd8f1b-3fc7-416e-bc5c-b7e6b760daca
SESSION_ID=$(jq -r '.sessionID' response.json)
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/cert-ca-aws.pem
openssl rand -base64 23 >masterKey.txt
#echo $SESSION_ID
#c2fd8f1b-3fc7-416e-bc5c-b7e6b760daca
MASTER_KEY=$(openssl smime -encrypt -aes-256-cbc -in masterKey.txt -outform DER cert.pem | base64 -w 0)
#echo $MASTER_KEY
#MIIDIAYJKoZIhvcNAQcDoIIDETCCAw0CAQAxggKoMIICpAIBADCBizBzMQswCQYDVQQGEwJJTDESMBAGA1UECAwJSmVydXNhbGVtMRIwEAYDVQQHDAlKZXJ1c2FsZW0xGjAYBgNVBAoMEURldk9wc0NvdXJzZUphbjIyMQwwCgYDVQQDDANCb2IxEjAQBgkqhkiG9w0BCQEWA0JvYgIUFGsmv5h7aZPD9aleGh5y1v96KVkwDQYJKoZIhvcNAQEBBQAEggIAfpG4eKy9QNwW6rnTGSJrXSqIx5l3B9LKMsQrvIIV7q1V7UnC61m1vw1oXPuzixWCFvM1MTrpH1V0YiSl3AIrTpcs2Y510N2jPBcOT8h+1Nczu3V4Fndb3/rhlmDkLs+FLy6YROjFwMprj4FNaCmhPqjmDFM0hcMd/aJMqnnv35qN2kLGE6R/Suu67k9QnHehfsXS6XNy6LQNX0yXs188shGk4O/W0GbOeVKJR4/kgZ+VdqV5djmtE3bleLrv9616Ar94kgC42yckW6Oy/SuHJ7Vdgx643Zryj8LcuOvOItJDeDqMCj19Cr0lBKmgntiP0rpiZpLpzuLyTdH7y4T10cF8ojEZHT1B2sX2nGl4OuzW27v9SLLdJXG61gumjflKHpRAnRr2JgvZ3vwTT5Hyy0uI+49aRahXRnYPP9m5fl1ZiUPTjVW5Wy1UnF0UDIp7kV/RskSbJ+hFBIFy0Xt0yHwKWrYZx7ldpowlqTUhO5NPxJ91q6dZEf+ZaV7sVg1vdHMj4efZyKF9S0xty/R593wHynVWSKzmbXp2yqAPmW/1rfa7xo/L/SiaD9czfcr0X1vYojgOdytio9WDKUp6xM1+NoeKv4+aqOQEAdoYLOsMI0DXCtbBDxnLdqIYuGTuPzcToO9eiEZvGpJcEpCa+5MwUcx6S3p5NFROKNciQ4MwXAYJKoZIhvcNAQcBMB0GCWCGSAFlAwQBKgQQuSjxRGWisPDBYc11cz8sFYAwTK69/WUhWNlXFqJ1FDCEemHKot6fmP+af85LEB0mW7eboAOAVqSMcI4DDDr2Urqa
curl -X POST -H 'Content-Type: application/json' -d '{"sessionID": "'$SESSION_ID'","masterKey": "'$MASTER_KEY'","sampleMessage": "Hi server, please encrypt me and send to client!"}' http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/keyexchange -o encSampleMsg.json
jq -r '.encryptedSampleMessage' encSampleMsg.json >encSampleMsg.txt
cat encSampleMsg.txt | base64 -d > encSampleMsgReady.txt
#openssl enc -e -aes-256-cbc -pbkdf2 -k myKey -in secret -out encrypted_secret
openssl enc -d -aes-256-cbc -pbkdf2 -kfile masterKey.txt -in encSampleMsgReady.txt -out encrypted_secret
DECRYPTED_SAMPLE_MESSAGE=$(<encrypted_secret)
if [ "$DECRYPTED_SAMPLE_MESSAGE" != "Hi server, please encrypt me and send to client!" ]; then
  echo "Server symmetric encryption using the exchanged master-key has failed."
  exit 1
else
  echo "Client-Server TLS handshake has been completed successfully"
fi
#Client-Server TLS handshake has been completed successfully
