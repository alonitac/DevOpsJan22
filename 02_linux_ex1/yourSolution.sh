tar -xzf secretGenerator.tar.gz
cd src/
mkdir secretDir
rm -r maliciousFiles/
touch secretDir/.secret
chmod 600 secretDir/.secret
ls -la
rm important.link