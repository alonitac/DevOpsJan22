#!/bin/bash
echo "1.Creating the directory 'secretDir'"
mkdir secretDir

echo "2.Deleting malicious folders\files\links"
rm -r maliciousFiles
rm important.link

echo "3.Creating the file '.secret'"
touch secretDir/.secret

echo "4.Granting permissions"
chmod 600 secretDir/.secret
chmod 700 yourSolution.sh
chmod 700 generateSecret.sh

echo "5.Generating your secret..."
./generateSecret.sh