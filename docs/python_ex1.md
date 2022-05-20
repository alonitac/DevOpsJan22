# Poly YouTube Telegram Bot
Due date: 20/06/2022 23:59  

**Can be done in pairs!**

# Background

Your goal in this exercise is to design and develop Telegram bot which will serve YouTube content. 

## Part 1 - Create the environment

1. Fork [The PolyBot](https://github.com/alonitac/PolyBot) repo (learn about [forking a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) in GitHub)
2. Clone your **forked repo** locally into PyCharm (Git -> Clone...)
3. [Create Python venv](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) for the project
4. Install requirements by `pip install -r requirements.txt`


## Part 2 - Create a Telegram Bot

1. <a href="https://desktop.telegram.org/" target="_blank">Download</a> and install telegram desktop (you can use your phone app as well).
2. Once installed, follow <a href="https://core.telegram.org/bots#6-botfather">this section</a> to create a bot. You should follow until “Generating an authentication token” (not including that section)

   ![telegramBot](/img/telegramToken.png)

At this point, you should have your own bot, as well as the API token. **Never** commit sensitive data like secrets in Git repo. For now, save the token in a file called `.telegeamToken` and add this file to `.gitignore` to exclude it completely from Git index. We will later learn that the place to store sensitive data is the cloud (AWS in our case).



## Part 3 - Running a simple “echo” Bot

### The class _Bot_
Under `bot.py` you are given a class called `Bot`. This class handles a simple telegram bot, as follows:  

The constructor `__init__` gets `token` arg which is the bot token you have just received from Telegram. Inside the constructor, an Updater object is created, and the function `self._message_handler` is set as main msg handler, this function is getting called whenever a new message will be sent to the bot.

The default behaviour of Bot class is to “echo” the incoming messages. 
Run the program and send a message to the bot via Telegram app, observe the response and get an idea of how `_message_handler` is functioning (it's recommended to run in debug mode with breakpoints).

## Part 4 - Extending the echo bot

### The class _QuoteBot_

In `bot.py` you are given a class called `QuoteBot` which inherits from `Bot`. Upon incoming messages, this bot echoing the message while quoting the original message, unless the user is asking politely not to quote.
Run this bot and check its behavior.

## Part 5 - Build your YouTube Bot

### The class _YoutubeBot_

In `bot.py` you are given a class called `YoutubeBot` which inherits from `Bot`.
Upon incoming messages, this class will take the message text, search and download corresponding Youtube video(s), the bot will then send the video file to the user.

1. Inside `YoutubeBot` class, override `_message_handler` method and implement the functionality that is needed to download video from youtube and send it to the user (utilize `search_download_youtube_video` in `utils.py`).
2. Remember that by inheriting the Bot class, you can use all of its methods (such as send_video or send_text).
3. (Optional) Feel free to add more functionality e.g. implement a logic that caches videos that have already been downloaded, such that it will use the local copy when user requests the same video again. 

## Part 6 - Containerize your app 
1. In your root directory of you repo, open `Dockerfile` and fill out the file such that the Bot app can be run as a Docker container
2. Build and run the container locally, make sure it works well. 

## Part 7 - Run your app "as a service" in an Amazon EC2 instance
1. In the course AWS account, create an Amazon Linux free tier EC2 instance.
2. Connect to the VM using SSH
3. Install [docker engine](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html#create-container-image-install-docker) in it 
4. Get your code there by `git clone...` (install git on the VM if needed).
5. Build you app with Docker (`docker build -t ...`)
6. Run your container "as a service", which means (1) in the background, and (2) the container will start running automatically after reboot. (Hint: read about [`--detach`](https://docs.docker.com/engine/reference/commandline/run/#options) and [`--restart`](https://docs.docker.com/engine/reference/commandline/run/#restart-policies---restart) options)
7. **You must validate that everything is running correctly!** Communicate with your bot and check the response, reboot your machine and validate that the bot is up and running after.

## Submission guidelines
1. Add the below public key to `~/.ssh/authorized_keys` file in your VM (in a separate line), so course stuff will be able to connect and see your work.
2. You don't need to keep the VM running. When your work is done, Stop the machine (don't Terminate it!)
3. In your forked repo, in `SUBMISSION` file, write _your mails_, the _Instance id_ and _region_ of your EC2 instance. Don't forget to commit and push it so it is visible to course stuff: 
```text
student1@gmail.com
student2@gmail.com

Instance: i-09bfad1e9a92275f9
region: eu-north-1
```

No need to send your forked repo link since GitHub is automatically monitoring who forked the repo.

##### Course public RSA key

```text
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8uOWjEcG0wFKSYbgEv/rDS6vyu1oZNfS7AWX35I0ozoNSJXEYiGW8Kw9VYE7TIEDCzBag61DbQyTDVlQpYVCw7uzDMTrgOAGQQIm8USOyFm2STRCeMa1sKivlDYynXhhtMS5k3e0a9Bo0hCbFRvVqjpixG/g/6wVA+vFjeWTo5bKjh9ekoSd3wdOu22PR6GjT0+NK5xlqhjKCnl19BFiIRptqcUkFuCgXqktrcwix0Cq2QhaQvYfIv/VA68OaClCX8wPDNXbO2VHK4170Kg5ubTrqx4ppP7Q0Gasz8CUCSGhf+njmhj3TnqhZ2UFsohyTIH4xV7e7wtNxDxdJ/r+T DevOpsCourseStuff
```
# Good Luck

Don't hesitate to ask any questions