from facebook_scraper import get_posts
import requests
import time

class Webhook:
    def __init__(self, url, page_id, mention, check_time):
        self.wh_url = url
        self.fb_page = page_id
        self.mention = mention
        self.check_time = check_time

    def start(self):
        print("[LOG] Webhook started.")
        while True:
            self.handle_post()
            time.sleep(self.check_time)

    def handle_post(self):
        post = None
        for tmp in get_posts(self.fb_page, pages = 2):
            post = tmp
            break
        if post == None:
            print("[LOG] Couldn't find posts.")
            return
        if str(post['post_id']) != self.get_last():
            self.send_msg(post)

    def send_msg(self, post):
        data = {'content' : f"{self.mention} **New post from {self.fb_page} facebook page**.\n"}
        if len(post['text']) > 1000:
            data['content'] += post['text'][:1500]
        else:
            data['content'] += post['text']
        data['content'] += "\n\nTo know more, visit " + post['post_url']

        if post['image_lowquality'] != None:
            data['embeds'] = [{
                "image" : {
                    "url" : post['image_lowquality']
                }
            }]

        result = requests.post(self.wh_url, json = data)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print("[LOGS] ", err)
        else:
            print("[LOGS] Payload delivered successfully, code {}.".format(result.status_code))
            self.write_last(post['post_id'])

    def get_last(self):
        try:
            with open("last.txt", 'r') as file:
                return file.read()
        except:
            return ""

    def write_last(self, last):
        with open("last.txt", 'w') as file:
            file.write(str(last))