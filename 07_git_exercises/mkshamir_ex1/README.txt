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

17- git branch
  bugfix/fix_readme_typo
  bugfix/open_kibana_port
  dev
  feature/data_retention_policy
  feature/elasticsearch_helm_chart
  feature/upgrade_angular_version
  feature/version1
  feature/version2
* main

18- git checkout -b feature/lambda_migration

19- git merge feature/version1

20+21- merging and resolving feature/version2 into feature/lambda_migration using the Pycharm UI.

22- git status
    it's shown that 'app.py' is set to be committed now that the merge conflicts have been resolved.
    also, 'abc.txt' is to be staged before committing.
    git commit -m "adding app.py after resolving merge conflicts"

cherry picking
~~~~~~~~~~~~~~

1- git checkout main
   git checkout -b feature/lambda_migration2

2+3- using the pycharm UI to cherry-pick specific commits from feature/lambda_migration branch.

4- '.env' and 'config.json' were added as result of the cherry-picking.

5- the order in which commits are picked matters, and I should care about it, because the commits build on top of each
   other. it's possible that a commit that is ahead in the git history tree won't make sense unless an earlier commit
   is picked first. moreover, if I pick commits in a backward order I might delete wanted progress.
   also, the order in which I pick commits determines which commit will ultimately be the HEAD.

changes in working tree and switch branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

22- using 'git status' it is shown that I'm on 'feature/lambda_migration2' branch (which isn't 'dev').

23- touch take.txt
    ls
    echo "take your time, look around" >> take.txt
    cat take.txt
    git status
    git add take.txt
    git status

24- git checkout dev
    the solutions proposed by git terminal are committing or stashing before checking out.

25- using the pycharm UI to force checkout into dev branch.

26- 'take.txt' has a completely different text in it now that I've force checked out. (a b c)

27- git checkout feature/lambda_migration2
    'take.txt' no longer exists in this branch. it can be inferred that force checkout allows switching branches without
    committing or stashing therefore causing the loss of progress.

reset
~~~~~