cd ./src
echo "Create the SecretDir folder, enter it and create the '.secret' file."
mkdir secretDir
cd ./secretDir
touch .secret
chmod 600 .secret
echo "Return to src."
cd ../
echo "Remove the 'MaliciousFiles' folder."
rm -rf ./maliciousFiles
echo "Unlink the link file."
unlink important.link
echo "Generate the secret."
/bin/bash generateSecret.sh
echo "Display the secret."
cd ./secretDir/
cat .secret