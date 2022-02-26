mkdir secretDir
rm -r maliciousFiles
cat > .secret
chmod 600 /.secret
rm important.link
/bin/bash generateSecret.sh
