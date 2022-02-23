#!/bin/bash

# practice dir creation
if [ ! -d "secretDir" ]
then
        mkdir secretDir
        if [ $? -gt 0 ]
        then
                echo "Failed to generate secret. The directory 'secretDir' must exist before." >&2
                exit 1
        else
                echo "Directory secretDir created successfully."
        fi
fi

# practice dir deletion and file move
export DIR_TO_REMOVE="maliciousFiles"
if [ -d $DIR_TO_REMOVE ]; then
        rm -rf $DIR_TO_REMOVE
        if [ $? -gt 0 ]
        then
                echo "Failed to remove directory $DIR_TO_REMOVE" >&2
                echo "Failed to generate secret. The directory 'maliciousFiles' contains some malicious files... it must be removed before." >&2
                exit 1
        else
                echo "Directory $DIR_TO_REMOVE removed successfully."
        fi
fi

# practice file creation
export SECRET_FILE="secretDir/.secret"
if [ ! -f $SECRET_FILE ]
then
        touch $SECRET_FILE
        if [ $? -gt 0 ]
        then
                echo "Failed to generate secret. The directory 'secretDir' must contain a file '.secret' in which the secret will be stored." >&2
                exit 1
        else
                echo "File $SECRET_FILE cretaed successfully."
        fi
fi

# practice change permissions
OCTAL_PERMISSIONS=$(stat -c "%a" secretDir/.secret)
if [ "$OCTAL_PERMISSIONS" != "600" ]
then
        chmod 600 $SECRET_FILE
        if [ $? -gt 0 ]
        then
                ehco "Failed to chmod to $SECRET_FILE." >&2
                echo "Failed to generate secret. The file $SECRET_FILE must have read and write permission only." >&2
                exit 1
        else
                echo "Permissions changed successfully."
                ls -l $SECRET_FILE
        fi
fi

# practice file linking understanding
export LINK="important.link"
if [ -L $LINK ] && [ ! -e $LINK ]
then
        rm $LINK
        if [ $? -gt 0 ]
        then
                echo "Failed to delete $LINK." >&2
                exit 1
        else
                echo "Bad link $LINK removed"
                echo "I'll try to link it to $SECRET_FILE"
                ln -s $SECRET_FILE $LINK
                if [ $? -gt 0 ]
                then
                        echo "Failed to generate a link to $SECRET_FILE" >&2
                elif [ -L $LINK ]
                then
                        echo "Link $LINK created successfully."
                        echo "Running md5sum to create my secret."
                        md5sum ./CONTENT_TO_HASH > $SECRET_FILE
                        if [ $? -eq 0 ]
                        then
                                echo "Done! Your secret was stored in $SECRET_FILE"
                        else
                                echo "Error occured while generating secret."
                        fi
                else
                        echo "Some error occured while trying to create link $LINK."
                        echo "Failed to generate secret. Secret can not be generated when broken file link exists. Please do something..."
                        exit 1
                fi
        fi
fi