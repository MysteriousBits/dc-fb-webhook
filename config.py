import os

# Discord webhook url
# Set an environment variable name WH_URL in the environment you are hosting
# You can paste directly if running locally
wh_url = os.getenv('WH_URL')
# Facebool page name or id
fb_page = "bdMOC"
# Check for new post after every 5 minutes = 300 seconds
check_time = 300
# Role to mention in every message. Use "" to mention none.
mention = "@everyone"
# Set True if hosting in replit, False otherwise
replit = False