#changing to linux user
pwd
cd //wsl$/Ubuntu/home/mkshamir
pwd

#retreiving data from the web and extracting data
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
ls
tar -xf secretGenerator.tar.gz
ls
cd src
ls

#investigating src content
cat generateSecret.sh

#following directions
#making directory
mkdir secretDir
ls
echo "Failed to generate secret. The directory 'secretDir' must exist before."

#removing directory
rm -r maliciousFiles
ls
echo "Failed to generate secret. The directory 'maliciousFiles' contains some malicious files... it must be removed before."

#creating file
touch secretDir/mysec.secret
ls secretDir
echo "Failed to generate secret. The directory 'secretDir' must contain a file '.secret' in which the secret will be stored."

#managing file permissions
ls -l secretDir
chmod 600 secretDir/mysec.secret
ls -l secretDir
echo "Failed to generate secret. The file 'secretDir/.secret' must have read and write permission only."

#removing symlink
rm important.link
ls

#reading content
cat ./CONTENT_TO_HASH
#With the sun in my hand
 #Gonna throw the sun
 #Way across the land-
 #Cause I’m tired,
 #Tired as I can be

 #loved this!

#using xargs to pass the poem as an argument to md5sum
#using md5sum to hash the poem into designated file and discovering the secret
cat ./CONTENT_TO_HASH | xargs | md5sum > secretDir/mysec.secret
echo "Done! Your secret was stored in secretDir/.secret"

#reading secret
cat secretDir/mysec.secret

#the secret(integrity of the generated text): 814c5723c21e7e90a3eae36c8df3c513
