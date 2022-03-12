#! /bin/bash
#I suggested 2 solutions, this solution (yourSolution2.sh) in case wget isn't needed.
directory=secretDir/
if  [ -d "$directory" ]; then
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