# Git and Pycharm ex-1
Due date: 15/05/2022 23:59

 
## Preliminaries

1. Open [our shared git repo](https://github.com/alonitac/DevOpsJan22) in PyCharm and pull the repository in branch **main** to get an up-to-date version
2. Checkout **new** branch `origin/git_ex1_<alias>` where `<alias>` is replaced by your name
3. Under `07_git_exercises` create a directory called `<alias>_ex1` 
4. In dir `<alias>_ex1` create a file called `README`.

All your answers, including commands and free text should be written in `README`.
This file will be checked manually (won't be executed) so no worries about combining code and text.

Submit your exercise by creating a Pull Request from your branch into **main**.

### Git Basics (commit, diff, branches)

In your GitHub account, create a new repo, clone it locally via PyCharm (Git -> Clone...). From now on, unless otherwise specified, execute all git commands in **Pycharm Terminal** opened from your private cloned repo. 

![Terminal](/img/terminal.png)

1. Copy `07_git_exercises/basics.sh` from our shared repo into your newly created repo, in project root directory, add and commit it. Run it by `./basics.sh`  
2. In branch `main`, create a file called `abc.txt` containing the text `1` in it
3. What is the color of file `abc.txt` in Pycharm's Project view?
4. Add the file to the index (What is the color now?) and commit the changes (it's recommended to use `git status` in between steps)
5. Append the line `2` to the end of `abc.txt` to change the state of this file in the working tree
6. What is the color of file `abc.txt` in Pycharm's Project view?
7. What is the command to show changes between the working tree to branch `main`?
8. Why does `git diff --staged` print nothing?
9. Why does `git diff master` print error?
10. Add `abc.txt` to the index
11. What does `git diff` print? why?
12. What is the command to show changes between the index and branch `main`?
13. Append the line `3` to the end of `abc.txt` to change the state of this file in the working tree
14. Would `git diff --staged` and `git diff main` commands print the same output? why?
15. Why does `abc.txt` appear twice in the output of `git status`? 
16. **Unstage** the changes in your index and working tree (don't commit the changes)

### Resolve conflicts 

Your manager decided that you'll lead the development of a feature called "lambda migration". 
You are told that John Doe and Narayan Nadella, your team colleagues, have already been worked on that area of the project in the past. 
You decide to create a new branch called `feature/lambda_migration` and merge the previous work of John and Narayan to your branch.

17. List all existed branches this repo (print them)
18. Create a new branch called `feature/lambda_migration` and switch to this branch
19. Merge branch `feature/version1` into `feature/lambda_migration`, observe the merged changes
20. **Using PyCharm UI** - merge branch `feature/version2` in `feature/lambda_migration`, resolve the conflict as following:
    1. On the opened conflict tool, choose the conflicted file and click Merge  
       ![Conflict](/img/conflict.png)
    2. First click All to merge all changes for which there is no any conflict  
       ![All](/img/conflict-all.png)
    3. Right click on right and left pages and choose _Annotate with Git Blame_
    4. Accept John Doe's port number (8081)
    5. Accept the function name of Narayan Nadella (get_profile_picture)
21. Are there any added commits for `feature/lambda_migration` after all merges were completed? what are those commits?

### Cherry picking

`git cherry-pick` is a powerful command that enables arbitrary Git commits to be picked by reference and appended to the current working HEAD.
Let's say you've implemented a great working but 

29. Checkout `feature/lambda_migration` (if you don't there yet)
30. In Pycharm Git tab (bottom left), navigate to tab Log
31. (TBD from main exercise)


### Changes in working tree and switch branches

A very common issue for Git beginners is switching branches while there are changes in the working tree. We will now simulate this scenario and discuss common practices. 

22. Make sure you are in branch different than `dev` (you should be in `feature/lambda_migration` if you follow the exercise in the order it's written)
23. Create a new file called `take.txt`, write some lines in it and add it to the index (don't commit, only add).
24. Now you have uncommitted changes in the working
25. Checkout to `dev`, which error do you get? What are the two suggested approaches by git? Read about `git stash` command from the [Official Git Docs](https://git-scm.com/docs/git-stash). Feel clueless? ask your teacher to discuss git stash in class.
26. **Using PyCharm UI** try to checkout to `dev` again. On the prompted dialog click **Force Checkout**
27. Does `take.txt` contain your changes when you're now in `dev`?
28. Checkout back to the branch you've come from, do you have your `take.txt` there? So what does **Force Checkout** do? 

### Reset

25. Checkout `reset_question` branch
26. Run the following commands line by line, after each command, observe what happened to your working tree and explain why
    1. `git reset --soft HEAD~1`
    2. `git reset --mixed HEAD~1`
    3. `git reset --hard HEAD~1`
    4. `git revert HEAD~1`
27. Explain the notation `HEAD~1` in git reset command


# Good Luck

Don't hesitate to ask any questions