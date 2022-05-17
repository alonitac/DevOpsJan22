preliminaries
~~~~~~~~~~~~~

git clone https://github.com/mkshamir/git_ex1

Git Basics
~~~~~~~~~~~

1- touch abc.txt
   echo 1 >> abc.txt
   cat abc.txt
   git status

2- red

3- git add abc.txt
   now the color is green
   git status
   git commit -m "adding and editing abc.txt"
   now the color is white
   git status

4- echo 2 >> abc.txt

5- now the color is green again

6- git diff HEAD..main (or just git diff main)

7- the change to abc.txt was made. but it wasn't added to the index, and it wasn't committed to the workingtree.
   'git diff --staged' shows the difference between the HEAD and the index. at this point there is no difference
   so the command prints nothing.

8- 'git diff staged2' prints an error for two reasons. firstly because there must be '--' before the name of the
   index/commit we are comparing to, as a syntax convention. secondly because the path for a second staging act
   between commits won't be called staged2 by default. the terminal doesn't recognize that name.

9- git add abc.txt
   git status

10- 'git diff' prints all the merge conflicts. currently, there aren't any, so it prints nothing.

11- git diff --staged main

12- echo 3 >> abc.txt
    cat abc.txt
    git status

13- 'git diff --staged' only shows +2 as the difference with HEAD, while 'git diff main' shows +2 and +3.
    this is because both changes were made since last commit. but only +2 was added to the index.

14- abc.txt shows up twice with 'git status' because there are both changes to be committed and to be staged.

15- git restore --staged abc.txt

resolve conflicts
~~~~~~~~~~~~~~~~~

1-