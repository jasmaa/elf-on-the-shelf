import pronouncing, nltk
import random
import sys

# download tagger
try:
    nltk.find("taggers/averaged_perceptron_tagger")
except:
    nltk.download('averaged_perceptron_tagger')

# load common nouns
with open("nounlist.txt") as f:
    common_nouns = set(f.read().split("\n"))

"""
Creates a sentence using the elf on the shelf template
"""
def make_sentence(query):
    global common_nouns
    rhymes = set(pronouncing.rhymes(query))
    choice_nouns = list(rhymes.intersection(common_nouns))

    return choice_nouns

"""
Main
"""
if __name__ == "__main__":

    if len(sys.argv) == 2:
        
        # do the meme
        query = sys.argv[1]
        nouns = make_sentence(query)

        if len(nouns) > 0:
            print("You've heard of Elf on the Shelf. Now get ready for...")
            print(query + " on a " + nouns[random.randint(0, len(nouns)-1)])

    else:
        print("No query provided")
