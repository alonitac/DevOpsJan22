# Linux ex-1
Due date: 12/03/22 23:59

## Preliminaries

1. Make sure your Pycharm terminal is configured to run Git Bash (not Powershell)
2. Open (or clone if you didn't do it yet) [our shared git repo](https://github.com/alonitac/DevOpsJan22) in PyCharm and pull the repository ![Pull Button](/img/pull.png) to get an up-to-date version
3. From Pycharm button right bar, create your own git branch (Git branches will be discussed later):

![New Branch](/img/branch.png)

Then change <alias\> to your nickname. e.g. `linux_ex1/alonit`. The branch name must start with `linux_ex1/`

![Branch Name](/img/branch2.png)

### Submission

At the end of this exercise, under `02_linux_ex1` directory, you should commit and push **only** 2 files as your solution:

- `README` file with your email at the first line, your generated secret (see last question below), and open answers for the first two questions below, as following:
```text
name@example.com
< your secret here >


Kernel System Calls
-------------------
< Your Answer >


Binary Numbers
--------------
< Your Answer >

```

- Your bash script solution in `yourSolution.sh` file (see last question below)

```shell
mkdir blabla
touch blabla
...
rm blabla
...

```

## Questions

### Kernel System Calls
(20 Points)

We've discussed in class about the Linux kernel - the main component of a Linux OS which functions as the core interface between a computer’s hardware and its processes.

But how does it work exactly? what exact commands (or **system calls**) do we pass to the kernel from programs such as `ls` or `chmod` (or any other program)?

The goal of this question is to help you become familiar with the `strace` command. strace
is a Linux command, which traces system calls and signals of a program. It is an important tool
to debug your programs in advanced cases.
In this assignment, you should follow the strace of a program in order to understand what it
does. You can assume that the program does only what you can see by using strace.
To run the program, do the following:

- Open a linux terminal in an empty directory and perform:
```shell
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/whatIdo
chmod 700 ./whatIdo
```
The `wget` command is able to retrieve data from the internet.

- Run the program using `strace`.
- Follow strace output. Tip: many lines in the beginning are part of the load of the
program. The first “interesting” lines comes only at the end of the output

Your assignment is to supply a brief description of what the program does in the README file

### Binary Numbers
(20 Points)

1. Convert the following binary numbers to a decimals: 
111, 100, 10110
2. What is the available decimal range represented by a 8 bits binary number?
3. Given a 9 bits binary number, suggest a method to represent a negative numbers between 0-255
4. Suggest a method to represent a floating point numbers (e.g. 12.3,  15.67, 0.231) using a 8 bits binary numbers

### File System Manipulations
(60 points)

- Open a linux terminal and perform:
```shell
wget https://devops-jan22.s3.eu-north-1.amazonaws.com/secretGenerator.tar.gz
```

- Use `tar` to extract the compressed file. `cd` to *src* directory. Explore the files and their content.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
- Your goal is to generate a secret. The secret can be generated using `/bin/bash generateSecret.sh`.

- Once you've generated it, copy it to the designated place in the README file (33 characters). 

- Use `nano` or your preferred text editor, and **write a complete commands set** that let you to generate the secret in `yourSolution.sh` file (single command in each line).
At the end, given a clean version of *src* directory (without the changes you've made) you should be able to run `/bin/bash yourSolution.sh` and the secret should be generated without any errors. 
- Copy the content of `yourSolution.sh` into the same file in the Git repo (_02_linux_ex1/yourSolution.sh_). 
- Commit ![Commit Button](/img/commit.png) **ONLY** *02_linux_ex1/README* and *02_linux_ex1/yourSolution.sh* files **ONLY**. by:

![Commit Msg](/img/commitmsg.png)

- Push ![Push Button](/img/push.png) your changes, and wait for results :-)


# Good Luck

Don't hesitate to ask any questions