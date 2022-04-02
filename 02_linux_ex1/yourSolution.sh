#!/bin/bash
mkdir secretDir
rm -r maliciousFiles
touch ./secretDir/.secret
rm important.link
.generateSecret.sh