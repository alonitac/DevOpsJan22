mkdir secretDir
rm r maliciousfiles
cd secretDir
touch .secret
chmod 600 .secret
cd ..
rm important.link
cd src
bash generetsecret.sh
cd secretDir
cat .secret
