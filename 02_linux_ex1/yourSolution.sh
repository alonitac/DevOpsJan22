mkdir secretDir
rm maliciousFiles/ -r
touch secretDir/.secret
chmod 600 secretDir/.secret
rm important.link
