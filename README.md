# dc-fb-webhook
A python script to integrate your facebook page with discord server using discord webhooks without facebook api.  

### What it does
This script needs to run 24/7. Because it searches for new post in the given facebook page every 5 minutes by default. If new post is available, it executes a webhook post request including the post's text and image to your specified discord webhook. Then discord show the message in specified server channel.

### How to run
- Install dependecies: `pip install -r requiremens.txt`  
- Configure the project in *config.py*.  
- Run `python main.py`  
And you are good to go!