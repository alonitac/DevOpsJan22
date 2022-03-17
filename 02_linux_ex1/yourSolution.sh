#!/bin/bash
mkdir secretDir
rm -r maliciousFiles
touch ./secretDir/.secret
chmod 600 ./secretDir/.secret
rm important.link
. generateSecret.sh
