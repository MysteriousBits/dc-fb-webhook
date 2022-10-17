from config import *
import webhook

# For running 24/7 in replit
if replit:
    from keep_alive import keep_alive
    keep_alive()

wh = webhook.Webhook(wh_url, fb_page, mention, check_time)
wh.start()