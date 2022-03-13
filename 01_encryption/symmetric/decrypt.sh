# -e              Encrypt file
# -aes-256-cbc    The algo name
# -k              The key
# -in             The input file
# -out            The output file

openssl enc -d -aes-256-cbc -pbkdf2 -k myKey -in encrypted_secret -out decrypted_secret