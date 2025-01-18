#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

f = open(path.join(d, 'stoppord.txt'))
stop = f.readlines()

stopwords = set(STOPWORDS)
for s in stop:
    s=s.strip('\n')
    # s = s.decode("utf-8")
    #print(s)
    stopwords.add(s)




# Read the whole text.
#text = open(path.join(d, 'constitution.txt')).read()
text = open(path.join(d, 'out.txt')).read()

wordcloud = WordCloud(background_color="white", max_words=2000, stopwords=stopwords)
# generate word cloud
wordcloud.generate(text)


# Generate a word cloud image
#wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40, stopwords=stopwords).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
