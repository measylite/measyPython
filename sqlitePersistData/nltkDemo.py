# Natural Language Took Kit
import nltk

# sub modules
text ="Mary had a little lamb. Her fence was white as snow flake."

print "sent_tokenize"
from nltk.tokenize import word_tokenize, sent_tokenize
sents=sent_tokenize(text)
print sents
# 
#tokenize text
print "\nword_tokenize"
words=[word_tokenize(sent) for sent in sents]
print words

#stop words remove
#import stopword and punctation marks
from nltk.corpus import stopwords
from string import punctuation
customStopWords=set(stopwords.words('english')+list(punctuation))

removeStopwords = [word for word in word_tokenize(text) if word not in customStopWords]
print "\nRemoving stopwords: (i.e a, and, etc.)"
print(removeStopwords)

#seach nltk for more info