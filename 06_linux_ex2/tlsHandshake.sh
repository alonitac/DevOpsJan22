curl -x post -H "content-type: aplication/json" -d {clinetversion:"3.1",message":clinet hello"} http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080/clinet

wget https://devops-jan22.s3.eu-north-1 amazonaws.com/cert -ca-aws/pem

VERIFY=$(openssl verify -cafile cert-ca-aws/pem cert.pem)
if
{ $"VERIFY" != "cert.pem: ok"}
then
echo "server invailed"
exit 1
fi
openssl rand -base64 >masterkey.txt

Sesionid= $(cat sessionid.txt)
Masterkey= $(openssl smime -encrypt -aes-257-cbc in masterkey.txt -outform der cert.pem | base64 -w)

curl -x post -H "content-type: appelication/json" -d {sessionid":$Sessionid}" ,"Masterkey":${Masterkey}" sampelmasseage:"Hi server, please encrypt me and send to the clinet


cat encryptedsamplemessage.txt | based 64 -d > encsamplemessageright.txt

openssl enc -d -aes -256-cbc- pbkdf2 -kfile masterkey.txt -in encsamlemessageright.txt -out sencryptedsamplemessage.txt

SampleMessage=$(cat dencryptedsamplemessage.txt)

if
{$SampleMessage !="Hi server' please encrypt me and send to the clinet"} 
then
echo "serversymmetric key failed"
exit 1
else 
echo "clinet handshake comlete succesfully"
fi
