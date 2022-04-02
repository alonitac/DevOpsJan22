elkan316@gmail.com
814c5723c21e7e90a3eae36c8df3c513


Kernel System Calls
-------------------
the program is doing the following
1. checking folder with name "welcomeToDevOpsJan22" exist using the system call "stat"
2. if folder doesn't exist create using "mkdir"
3. create a file inside the folder name "GoodLuck"
4. write the test "There you go... tell me what I do..." into the file


Binary Numbers
--------------
1. 111=7, 100=4, 10110=22
2. 0-22
3. the fits bit will be the sign bit, 0 for positive and 1 for negative. the remaining 8 but will hold the numeric value.

Yoursoloution:
#!/bin/bash
mkdir secretDir
rm -r maliciousFiles
touch ./secretDir/.secret
rm important.link
.generateSecret.sh