wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
tar -xf secretGenerator.tar.gz
cd src/
rm -r important.link && rm -r maliciousFiles/
mkdir secretDir
cd secretDir/
touch .secret
chmod 600 .secret
cd ..
/bin/bash generateSecret.sh
cd secretDir/
cat .secret