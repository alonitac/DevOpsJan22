----------------Git Basics (commit, diff, branches)----------------
1Q.1A) abc.txt created with The command nano abc.txt write 1 and exit.

2Q.2A) The color is: red which means the file did not stage yet.

3Q.3A) After adding the file to the index, the color of the file is now green,
      I will use git status first, and then commit it.

4Q.4A) Using command nano abc.txt and in the text hit Enter (to show line 2)key and exit
    To change the state of this file in the working tree.

5Q.5A) The color of the file abc.txt in Pycharm's Project view is blue

6Q.6A) command to show changes between the working tree to branch Main is: git diff HEAD

7Q.7A) The reason it doesn’t print anything it's because
      git diff --staged only show the differences between branch main --> staging index.

8Q.8A) The reason is print error, is because there is no such a command.

9Q.9A) Using the command git add abc.txt to add it to the index.

10Q.10A) The reason git diff print nothing it's because  all the changes have already cached.
        which means, it's stored in staging index.

11Q.11A) The command that shows the changes between the index and branch main is: git diff --staged


12Q.12A) Using command nano abc.txt and in the text hit Enter (to show line 3)key and exit
        To change the state of this file in the working tree.

13Q.13A) command: git diff (main or HEAD) show the changes from main --> working tree.
        (Which will show only the changes in working directory. and not the staged ones)

        command : Git diff --staged show the changes from main--> staging index
        (Which will show the changes from last commit from the HEAD)

        The status right now is : "1" in abc.txt in Main( already commit )
                              The "2" change, is in the Index Staging.
                              and "3" is in the Working Directory.

14Q.14A) Why does abc.txt appear twice in the output of git status?
In the command git status abc.txt appear twice because:
abc.txt have 1st version in Index Staging (contain: "1" and "2")
and 2nd version in Working directory (contain: “1”, “2” and “3”)

15Q.15A)  Using command: git restore --staged --worktree abc.txt

--------------------Resolve conflicts----------------
1.List all existed branches:
Using command : 'git branch'
                            bugfix/fix_readme_typo
                            bugfix/open_kibana_port
                            dev
                            feature/data_retention_policy
                            feature/elasticsearch_helm_chart
                            feature/lambda_migration  (my new branch)
                            feature/upgrade_angular_version
                            feature/version1
                            feature/version2

Using PyCharm UI follow the instructions:

2)create new branch called feature/lambda_migration and switched to.
3)Merge branch feature/version1 into feature/lambda_migration.
  (no conflict)
4)merge branch 'feature/version2' into 'feature/lambda_migration'
  (popup window conflict)

5)First I click All to merge all changes (for which there is no any conflict)
  Right click on each panel to reveal 'Annotate with Git Blame'
  Accept John Doe's port number (8081), deny Narayan's port (8082)
  Accept the function name of Narayan Nadella (get_profile_picture), Block John's name.

6)The commits that have been added after the merge are:
'Merge branch 'feature/version1' into feature/lambda_migration'
'Merge branch 'feature/version2' into feature/lambda_migration'

--------------------------cherry-pick-------------------

Follow the instructions:
1) Created a clean fresh branch feature/lambda_migration2 from main.

2) Reached to bottom left to 'git tab' (in the UI) navigated to tab log, filter Branch,
to make only the feature/lambda_migration shown.

3) chose Cherry-pick icon to use pick the commits in the followed order:
    *)"use correct lock type in reconnect()"
    **)"Restrict the extensions that can be disabled"

4)The files that have been added to the branch as a result of the commits are :
    (1) config.json  (2) .env

5)The reason it is important to use cherry-pick in the correct order
 because commits, are related to each other.

--------Changes in working tree and switch branches------

1)I follow the exercise in the order it is written
therefore,I am in feature/lambda_migration2

2)I have created a new file with command :'nano take.txt'
write some lines inside and add it to the index with command: 'git add take.txt'

3) I tried checkout, and it pops up a window with the options:
   1. Force checkout 2. Smart checkout 3. Don't Checkout

'git stash' is a command that let you save all the changes you have made
outside the repository of the current working tree and index with a SHA value.
that let you bring up these changes when you will be back to the branch.

4) I tired again checkout but this time using the command :'git checkout --force dev'

5) take.txt does not contain the changes.

6) I have checked out to the last branch and there are no changes.

------------------------Reset-----------------------
1) I have checkout reset_question branch

2.1)  git reset --soft HEAD~1 move the last commit to Index (10 marked in green) and remove the commit. (HEAD is now the previous commit)
2.2)  git reset --mixed HEAD~1 move the current Index and last commit to unstaged (10 and 9 marked in RED) (HEAD is now the previous commit)
2.3)  git reset --hard HEAD~1 delete all committed files from the last commit. (HEAD is now the previous commit)
2.4)  git revert HEAD~1 delete the files from the last commit and create new commit. (HEAD is now the new commit) 

3) HEAD~1 goes to the previous commit.