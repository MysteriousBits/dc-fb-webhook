from config import *
import webhook

wh = webhook.Webhook(wh_url, fb_page, mention, check_time)
wh.start()