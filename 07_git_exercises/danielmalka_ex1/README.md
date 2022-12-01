# Git Basics:
1. echo "1" > abc.txt
2. red 
3. after git add command on abc.txt - the color changed to green 
4. echo "2" >> abc.txt 
5. the color changed to red again (using git status command)
6. use the command git diff
7. because we did not add the changes in abc.txt to the index
8. because there is no branch called stage2
9. git add abc.txt
10. still does not show differences since we did not commit the change yet
11. git diff --cached 
12. echo "3" >> abc.txt
13. git diff --staged shows "2" added to the file while git diff main shows that "3" has also added to the file since we did not commit anything yet.
14. once green for when we added "2" to the index, second red for not staged change "3"
15. use git reset

# Resolve Conflicts:
1. list all existing branches using git branch -a
2. create and switch to the new branch: git checkout -b feature/lambda_migration
3. merge feature/version1 to feature/lambda_migration and observe the merged changes using: git merge feature/version1
4. using PyCharm - select git > merge > feature/version2
5. select app.py and click merge > click on all to show all files > use annonate git blame on both version and accept left (port 8081)
6. there is no added commits after completing with merges

# Cherry Picking
1. first switch to main: git checkout main then create a clean branch: git checkout -b feature/lambda_migration2
2. git tab > log > double click on lambda_migration
3. select reconnect() commit and click on cherry-picking, then on restrict extensions and click on cherry-picking
4. two files: app.py and config.json
5. the cherry-picking order matters since if we will go back to an older commit the newer will not be available

# Changes in the working tree and switch branches
1. git branch -a shows we are in feature/lambda_migration2
2. create a new file: echo "newfile" > take.txt then add it to the index git add take.txt 
3. the error we got is because we didn't commit take.txt, there are 2 approaches - to commit the changes or stash them. to stash a change is to temporarily save it without the need to commit it, so you can work on another branch and get back to it later.
4. select git > branches > dev > force checkout
5. no
6. force checkout let you switch to another branch even if you did not stage your changes but makes a local copy of the file.

# Reset
1. use the command: git checkout reset_question
2. commands:
a. git reset --soft HEAD~1 - undo the last commit (paint 10 in green) without touching the index file or the working tree
b. git reset --mixed HEAD~1 - change 10 and 9 to red - resets also the index but not the working tree
c. git reset --hard HEAD~1 - resets also the index and the working tree to a certain commit
d. git revert HEAD~1 - reverse the effect of HEAD~1 commit
3. HEAD~1 refers to a previous commit 

