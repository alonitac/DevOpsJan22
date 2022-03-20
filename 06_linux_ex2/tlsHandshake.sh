echo "Starting Client Hello"
curl
http://devops-jan22-1273001359.eu-north-1.elb.amazonaws.com:8080
POST /clienthello
{
  "clientVersion": "3.2",
  "message": "Client Hello"
}