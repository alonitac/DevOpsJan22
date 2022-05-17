Git Basics
~~~~~~~~~~~~~~~
#after creating a repo in GitHub I cloned it to a new proj in pycharm
1- git clone https://github.com/mkshamir/git_ex1
   git status
   git add git_ex1

#after copying the file init.sh to my proj and running it
#I add the files to the index and commit
2- git add .
   git commit -m "adding generated files"

#after adding a file abc.txt and writing into it I add it to the index and commit
3+4- git status
     git add abc.txt
     git status
     git commit "adding abc.txt"
     git status

5- cat abc.txt

6- echo -e \n2 >> abc.txt

7- git diff HEAD..main (or just git diff main)

8- git diff --staged doesn't show anything because there are no added (staged) files since last I commited.

9- git diff master gives an error because git syntax was changed from master to main. master is no longer recognized.

10- git add abc.txt

11- at this point git diff doesn't print anything because there are no changes made relative to the index after adding abc.txt

12- git diff --cached       or      git diff --staged

#after appending the line '3' to abc.txt
13+14- the commands 'git diff main' and 'git diff --staged' don't show the same thing. In the main branch the change
(line '3') is updated.
However, in the index that change has yet to be added.

15- Using 'git status' it is shown that abc.txt has been modified. The file appears twice after running the command.
Once to indicate that there are changes to be committed. And once to indicate that said changes haven't been staged
to be committed.

16- git restore --staged abc.txt

17- git branch -a
  bugfix/fix_readme_typo
  bugfix/open_kibana_port
  dev
  feature/data_retention_policy
  feature/elasticsearch_helm_chart
  feature/upgrade_angular_version
  feature/version1
  feature/version2
* main
  reset_question


18- git checkout -b mybranch

19- git merge feature/version1

20- git merge feature/version2
to enter the pycharm UI I entered: Git > resolve conflict > added all the changes(left and right)

21- Using 'git status' it is shown that there are commits to be made. Firstly, app.py was modified and is ready
to be committed. Secondly abc.txt has been modified and has yet to be staged. And lastly main.py is listed as
an untracked file that needs to be added as well.

22- touch take.txt

23- git checkout main

24- using 'git status' take.txt no longer appears as an unstaged file. this is a change that was made in a separate branch.

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

