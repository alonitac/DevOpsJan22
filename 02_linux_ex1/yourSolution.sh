chmod 777 src/generateSecret.sh
mkdir src/secretDir
rm -r src/maliciousFiles/
touch src/secretDir/.secret
chmod 600 src/secretDir/.secret
unlink src/important.link
cd src
./generateSecret.sh