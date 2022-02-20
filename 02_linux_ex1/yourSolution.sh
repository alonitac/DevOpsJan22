wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
tar -xvf secretGenerator.tar.gz
cd src
mkdir secretDir
rm -r maliciousFiles
touch secretDir/.secret
chmod 600 secretDir/.secret
rm important.link
/bin/bash generateSecret.sh



