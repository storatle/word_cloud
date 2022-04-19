#!/usr/bin/env python
"""
Using custom colors
===================

Using the recolor method and custom coloring functions.
"""

import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
import argparse
from wordcloud import WordCloud, STOPWORDS

parser = argparse.ArgumentParser()
parser.add_argument('input', help="Name of text for reading")

parser.add_argument('-m', '--mask', type=str,
                    help="Name of mask picture")

parser.add_argument('-bg', '--background', type=str, default='black',
                    help="background color")

parser.add_argument('-w', '--maxword', type=int, default=1000,
                    help="Max word")

parser.add_argument('-sw', '--stopword', nargs='+', default='a',
                    help="Stop words")


parser.add_argument('-sf', '--stopfile', type=str, default='stoppord',
                    help="File with stopword")

args = parser.parse_args()
text_file = args.input
mask_file = args.mask
bg = args.background
max_word = args.maxword
stop = args.stopword
stop_file = args.stopfile
print(stop)
stops = []
d = path.dirname(__file__)
if stop_file:
    stops = open(path.join(d, stop_file), encoding="utf8").readlines()
 



def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/star%20wars/storm-trooper.gif
# movie script of "a new hope"
# http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html
# May the lawyers deem this fair use.
text = open(path.join(text_file), encoding="utf8").read()
#text = open(path.join(d, 'a_new_hope.txt')).read()

# preprocessing the text a little bit
#text = text.replace("HAN", "Han")
#text = text.replace("LUKE'S", "Luke")

# adding movie script specific stopwords
stopwords = set(STOPWORDS)
for s in stops:
    s=s.strip('\n')
    stopwords.add(s)

for i in stop:
    # print(i) 
    stopwords.add(i)
if mask_file:
    print(mask_file)
    mask = np.array(Image.open(path.join(d, mask_file)))
#mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))
    wc = WordCloud(background_color=bg, mask=mask, max_words=max_word, stopwords=stopwords, margin=10,
               random_state=1).generate(text)
else:
    print('No mask')
    wc = WordCloud(width=2000, height=2100,background_color=bg, max_words=max_word, stopwords=stopwords, margin=10,
               random_state=1).generate(text)

# store default colored image
default_colors = wc.to_array()
wc.to_file(text_file.rsplit('.')[0]+'-1.png')

plt.figure( figsize=(20,10),facecolor='k')
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
wc.to_file(text_file.rsplit('.')[0]+'-2.png')
plt.axis("off")
plt.tight_layout(pad=0)
plt.title("Default colors")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
#plt.savefig('tmp.png', dpi=1000)
plt.show()
