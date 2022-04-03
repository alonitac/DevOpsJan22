mkdir secretDir/
rm -r maliciousFiles
cd secretDir/
touch .secret
chmod 600 .secret
rm important.link
ln -s CONTENT_TO_HASH  important.link
/bin/bash yourSolution.sh


#814c5723c21e7e90a3eae36c8df3c513