import img_edit
import img_search
import rhymer

import random
import sys

"""
Main
"""
if __name__ == "__main__":

    if len(sys.argv) == 2:

        # do the meme
        query = sys.argv[1]
        nouns = rhymer.make_sentence(query)
        chosen_noun = nouns[random.randint(0, len(nouns)-1)]

        img_list = img_search.get_img_from_search(chosen_noun)
        img_edit.construct_img(query, img_list[random.randint(0, len(img_list)-1)], 500)

        if len(nouns) > 0:
            print("You've heard of Elf on the Shelf. Now get ready for...")
            print(query + " on a " + chosen_noun)

    else:
        print("No query provided")
