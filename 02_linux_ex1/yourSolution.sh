#!/bin/bash
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
tar -xf secretGenerator.tar.gz
cd src/
mkdir secretDir
rm -r maliciousFiles/
touch ./secretDir/.secret
chmod 600 ./secretDir/.secret
rm important.link
chmod 766 generateSecret.sh
./generateSecret.sh
cat secretDir/.secret