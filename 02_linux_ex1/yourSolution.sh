cd src
mkdir seretDir
rm -r maliciousFiles
cd secretDir
touch .secret
chmod 600 .secret
cd ..
rm important.link
cd src
bash generateSecret.sh
cd secretDir
cat .secret