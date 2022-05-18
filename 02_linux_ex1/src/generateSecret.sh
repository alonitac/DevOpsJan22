#!/bin/bash

# practice dir creation
if [ ! -d "secretDir" ]; then
  echo "Failed to generate secret. The directory 'secretDir' must exist before."
  exit 1
fi

# practice dir deletion and file move
if [ -d "maliciousFiles" ]; then
  echo "Failed to generate secret. The directory 'maliciousFiles' contains some malicious files... it must be removed before."
  exit 1
fi

# practice file creation
if [ ! -f "secretDir/.secret" ]; then
  echo "Failed to generate secret. The directory 'secretDir' must contain a file '.secret' in which the secret will be stored."
  exit 1
fi

# practice change permissions
OCTAL_PERMISSIONS=$(stat -c "%a" secretDir/.secret)
if [ "$OCTAL_PERMISSIONS" != "600" ]; then
  echo "Failed to generate secret. The file 'secretDir/.secret' must have read and write permission only."
  exit 1
fi

# practice file linking understanding
if [ -L 'important.link' ] && [ ! -e 'important.link' ]; then
  echo "Failed to generate secret. Secret can not be generated when broken file link exists. Please do something..."
  exit 1
fi

cat ./CONTENT_TO_HASH | xargs | md5sum > secretDir/.secret && echo "Done! Your secret was stored in secretDir/.secret"
