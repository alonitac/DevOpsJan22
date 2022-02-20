wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
tar -xzvf secretGenerator.tar.gz
mkdir secretDir
touch secretDir/.secret
chmod 600 secretDir/.secret
mkdir maliciousFilesnew
mv /home/nati/src/maliciousFiles/* /home/nati/maliciousFilesnew
/bin/bash /home/nati/src/generateSecret.sh
cat /home/nati/secretDir/.secret