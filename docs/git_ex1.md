# Git ex-1
Due date: 31/04/2022 23:59

 
## Preliminaries

1. Open [our shared git repo](https://github.com/alonitac/DevOpsJan22) in PyCharm and pull the repository in branch **main** to get an up-to-date version
2. Checkout branch `origin/git_ex1`
3. Under `07_git_exercises` create a directory called `<alias>_ex1` while `<alias>` should be replaced by your name
4. In `<alias>_ex1` create a file called `README`.

## Questions

All your answers, including commands and free text should be written in `README`.
This file will be checked manually (won't be executed) so no worries about combining code and text.
At the end, commit


### Git Basics (commit, diff, branches)

1. Create GitHub repo in your account, clone it locally via PyCharm (Git -> Clone...)
2. Run `basics.sh`
3. In branch `main`, create a file called `abc.txt` containing the text `abc` in it.
4. Add the file to the index and commit the changes (it's recommended to use `git status` in between steps)
5. Print the content of `abc.txt` to stdout
6. Append the line `2` to the end of `abc.txt` to change the state of this file in the working tree
7. (README) What is the command to show changes between the working tree to branch `main`?
8. Why does `git diff --staged` print nothing?
9. Why does `git diff master` print error?
10. Add `abc.txt` to the index
11. What does `git diff` print? why?
12. What is the command to show changes between the index and branch `main`
13. Append the line `3` to the end of `abc.txt` to change the state of this file in the working tree
14. Would `git diff --staged` and `git diff main` commands print the same output? why?
15. Why does `abc.txt` appear twice in the output of `git status`? 
16. Unstage the changes in your index and working tree (don't commit the changes)
17. Which branches exists in this repo? print them
18. Create a new branch called `mybranch` and switch to this branch
19. Merge branch `feature/version1` in `mybranch`, observe the merged changes
20. Using PyCharm UI (!!) - merge branch `feature/version2` in `mybranch`, resolve the conflict the same way we did in class
21. Are there any added commits for `mybranch`? what are those commits?
22. Create a new file called `take.txt`, don't add or commit it
23. Checkout to `main`
24. What happened to `take.txt` you've just created in `mybranch`? why?

### Reset

25. Run `reset.sh`
26. Run the following commands line by line, after each command, observe what happened to your working tree and explain why
    1. `git reset --soft HEAD~1`
    2. `git reset --mixed HEAD~1`
    3. `git reset --hard HEAD~1`
    4. `git revert HEAD~1`
27. Explain the notation `HEAD~1` in git reset command


### Cherry picking

`git cherry-pick` is a powerful command that enables arbitrary Git commits to be picked by reference and appended to the current working HEAD

28. Run `cherry.sh`
29. In Pycharm Git tab (bottom left), navigate to tab Log 

### Protected branches in GitHub

30. In your GitHub repo

# Good Luck

Don't hesitate to ask any questions