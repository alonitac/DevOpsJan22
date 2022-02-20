cd src
mkdir secretDir
touch secretDir/.secret
chmod 600 secretDir/.secret
rm -r maliciousFiles/
rm impotrent.link
/bin/bash /home/nati/src/generateSecret.sh
cat /home/nati/secretDir/.secret