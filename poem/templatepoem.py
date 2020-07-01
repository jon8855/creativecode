import random
from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# loading and blobifying the text file
with open("birds_of_australia.txt") as f:
  bird_text = f.read()

bird_blob = TextBlob(bird_text)


singular_nouns = []
plural_nouns = []
adjectives = []

for word,pos in bird_blob.tags:
  if(pos == 'NN'):
    singular_nouns.append(word)

  if(pos == 'NNS'):
    plural_nouns.append(word)
    
  if(pos == 'JJ'):
    adjectives.append(word)


print("\n\nThis is just to say")
print("I have eaten")
print("the " + random.choice(plural_nouns))
print("that " + random.choice(adjectives) + " were in")
print("the " + random.choice(singular_nouns))
print("")
print("and which")
print("you were probably")
print("saving")
print("for breakfast")
print("")
print("Forgive me")
print("they were " + random.choice(adjectives))
print("so " + random.choice(adjectives))
print("and so " + random.choice(adjectives))
