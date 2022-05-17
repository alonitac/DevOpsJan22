Git Basics:
############
1. touch abc.txt
2. color red
3.git add abc.txt -> now color is green -> git status -> git commit -m "adding the abc.txt file"
4.echo 2 >> abc.txt
5.color is blue
6.git status -> git diff
7.git diff --staged shows the differences between the staging (index) and the HEAD (the the last commit) and right now they are the same (we didn't add the modified abc.txt file to the staging).
8.there is no file/path/commit/blob named stage2
9.git add . || git add abc.txt
10."git diff" command shows the differences between the working tree and the staging area, after adding the file to the staging area by using "git add" command there is no differences between the w.d area and staging area, so it prints nothing.
11.the "git diff main" will shows the diff' between the working tree to the last commit of the main branch also if the HEAD points to the last commit in the main branch we can use the "git status --staged" as we seen before.
12.echo3 >> abc.txt
13.no, the state of the file in working tree (has the lines 2 and 3) is different than the state in the staging area (only line 2) and the state of the file in the last commit is different (empty),
so as the "diff --stage" command compare the staging file state to the last main commit - (HEAD) (2 -> empty), and "diff main" compare the w.d to the las main commit (2 and 3 -> empty).
14. we didn't commit our changes in the last staged abc.txt file, then we did some more changes in our file on our working tree ares, so git telling as: 1.theres is a file state that we didn't commit and 2.more modification that we didn't put on staging.
15.git reset --hard.


Resolve Conflicts:
##################

1. git branch -a
2. git branch feature/lambda_migration \ git checkout feature/lambda_migration
3. git merge feature/lambda_migration
4.done
5.done
6.there is 6 new commits added, 3 of the John's branch using "version1" branch 1 of Narayan's using "version2" branch, and 2 more commits of the last 2 branches merging.

Cherry picking
##############

1.git branch feature/lambda_migration2
2.done
3.done
4. '.env', 'config.json'
5.yes -  if there a feature that was involved depends on the previous commits that can raise problems.

Changes in working tree and switch branches
############################################
1.done
2.echo "devops"/"is the"/"best" >> take.txt
3.  """ error: Your local changes to the following files would be overwritten by checkout:
              take.txt
        Please commit your changes or stash them before you switch branches. """
4.done
5.no no effect on the dev branch branch
6.force checkout abort all uncommitted changes - all working tree and stage modification are lost.

Reset
#####
1.git reset --soft HEAD~1 -> this command don't effect files in the staging and working tree area but rest the the the HEAD point to 1 commit before.
2.git reset --mixed HEAD~1 -> this command don't effect files in working tree area but remove changes from the staging area + rest the HEAD point to 1 commit before.
3.git reset --hard HEAD~1 ->  rest any changes from the working tree and the staging area to the last commit + rest the HEAD point to 1 commit before.
4.git revert HEAD~1 -> rest the change on HEAD pointer to "state" of the last commit but as a new commit with a different commit ID num.
5.HEAD~n notation means the reference to the commit on the HEAD's pointer previous n'th generations back ; HEAD~1 -> 1th generation back.