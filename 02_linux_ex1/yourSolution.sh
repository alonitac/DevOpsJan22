#! /bin/bash
#I suggested 2 solutions, this solution (yourSolution.sh) in case wget is needed.
directory=secretDir/
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
tar -xf secretGenerator.tar.gz
rm -r secretGenerator.tar.gz
cd src/
if  [ -d "$directory" ]; then
        rm -r maliciousFiles/
        rm important.link
        /bin/bash generateSecret.sh
        printf "My secret is: "
        cat secretDir/.secret
else
        mkdir secretDir
        rm -r maliciousFiles/
        touch secretDir/.secret
        chmod 600 secretDir/.secret
        rm important.link
        /bin/bash generateSecret.sh
        printf "My secret is: "
        cat secretDir/.secret
fi