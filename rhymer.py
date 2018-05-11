import pronouncing, nltk

# download tagger
try:
    nltk.find("taggers/averaged_perceptron_tagger")
except:
    nltk.download('averaged_perceptron_tagger')

# load common nouns
with open("nounlist.txt") as f:
    common_nouns = set(f.read().split("\n"))
with open("bad-words.txt") as f:
    bad_words = set(f.read().split("\n"))

"""
Creates a sentence using the elf on the shelf template
"""
def make_sentence(query):
    global common_nouns
    rhymes = set(pronouncing.rhymes(query))
    choice_nouns = list(rhymes)
    choice_nouns = list(rhymes - bad_words)

    return choice_nouns
