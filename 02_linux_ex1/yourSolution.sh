#! /bin/bash

# Dima`s soulution:
# execute this bash script

wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
tar -xf secretGenerator.tar.gz
cd src
rm -r maliciousFiles/ important.link
mkdir secretDir
touch secretDir/.secret
chmod 774 secretDir && chmod 600 secretDir/.secret
/bin/bash generateSecret.sh
printf "This is my secret: "
cat secretDir/.secret


