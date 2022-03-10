wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
tar -xvf secretGenerator.tar.gz
chmod 777 src
cd src
mkdir secretDir
rm -r maliciousFiles
cd secretDir
touch .secret
chmod 600 .secret
cd ..
find -xtype l
find -xtype l -delete
chmod +x ./generateSecret.sh
./generateSecret.sh








