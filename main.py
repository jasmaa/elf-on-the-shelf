import img_edit
import img_search
import rhymer

import random
import sys
import os
import time
import tweepy

def file2list(file_name):
    with open(file_name, 'r') as f:
        return f.read().split("\n")

"""
Main
"""
if __name__ == "__main__":

    creds = file2list("creds.txt")

    CONSUMER_KEY = creds[0]
    CONSUMER_SECRET = creds[1]
    ACCESS_KEY = creds[2]
    ACCESS_SECRET = creds[3]
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    # bot loop
    while True:
        # do the meme
        query_list = file2list("query_list.txt")
        query = query_list[random.randint(0, len(query_list)-1)]
        nouns = rhymer.make_sentence(query)

        if len(nouns) <= 0:
            continue

        chosen_noun = nouns[random.randint(0, len(nouns)-1)]

        # load images
        img_list = img_search.get_img_from_search(chosen_noun)

        # keep trying until valid img
        #got_img = False
        #while not got_img:
        #    try:
        img_edit.construct_img(query, img_list[random.randint(0, len(img_list)-1)], 500)
        #got_img = True
        #    except:
        #        pass

        # post
        fn = os.path.abspath("./images/out.png")
        msg = "#blairsilverstrea\nYou've heard of Elf on the Shelf. Now get ready for..."

        print(query + " on a " + chosen_noun)

        #api.update_with_media(fn, msg)
        break

        time.sleep(1200)

    else:
        print("No query provided")
