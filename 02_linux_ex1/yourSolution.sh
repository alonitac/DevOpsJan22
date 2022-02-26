cd src
mkdir secretDir
rm amIMaliciousOrNot.whoKnows  someFileIsLinkingToMe.BeAware
rmdir maliciousFiles
touch .secret
chmod 600 secretDir/.secret
rm important.link
/bin/bash generateSecret.sh


