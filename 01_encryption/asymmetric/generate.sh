ssh-keygen -t rsa -b 4096 -m PEM

echo "convert public and private key to .pem format..."

ssh-keygen -f ~/.ssh/id_rsa.pub -e -m PKCS8 > ~/.ssh/id_rsa.pem
openssl rsa -in ~/.ssh/id_rsa -outform pem > ~/.ssh/id_rsa_pr.pem


daniel0101@LAPTOP-7AHLURIH:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   9800   604 ?        Ssl  13:53   0:00 /init
root         7  0.0  0.0   9796   300 tty1     Ss   13:53   0:00 /init
daniel0+     8  0.0  0.0  18460  4116 tty1     S    13:53   0:01 -bash