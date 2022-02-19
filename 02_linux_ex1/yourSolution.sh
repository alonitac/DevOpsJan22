cd src
rm -r maliciousFiles
rm important.link
mkdir secretDir
cd secretDir
touch .secret
chmod 600 .secret
cd ..
/bin/bash generateSecret.sh
