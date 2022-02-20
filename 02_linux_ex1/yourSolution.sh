cd /usr/src
sudo wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz --no-check-certificate
sudo tar -xvf secretGenerator.tar.gz
sudo chmod 777 src
cd src
mkdir secretDir
rm -r maliciousFiles
cd secretDir
touch .secret
sudo chmod 600 .secret
cd ..
find -xtype l
find -xtype l -delete
sudo chmod +x ./generateSecret.sh
sudo ./generateSecret.sh
