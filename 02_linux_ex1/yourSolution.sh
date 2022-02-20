cd src
mkdir secretDir
cd maliciousFiles
rm amIMaliciousOrNot.whoKnows  someFileIsLinkingToMe.BeAware
cd ..
rmdir maliciousFiles
cd secretDir
touch .secret
chmod 600 .secret
cd ..
rm important.link
/bin/bash generateSecret.sh
cd secretDir
cat .secret