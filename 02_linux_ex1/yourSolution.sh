wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
tar -pzxvf secretGenerator.tar.gz
cd src/
mkdir secretDir
rm -Rf maliciousFiles
touch secretDir/.secret
chmod 600 secretDir/.secret
ln -L secretDir/.secret secretDir/important.link
chmod +x generateSecret.sh
