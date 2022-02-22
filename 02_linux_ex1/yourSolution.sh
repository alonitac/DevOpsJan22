chmod 700 generateSecret.sh
mkdir secretDir
cd maliciousFiles
rm amIMaliciousOrNot.whoKnows
rm someFileIsLinkingToMe.BeAware
rmdir maliciousFiles
cp CONTENT_TO_HASH secretDir
mv CONTENT_TO_HASH secret
