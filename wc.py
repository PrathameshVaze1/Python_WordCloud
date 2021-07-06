
# Import Required Packages

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io,sys

    
def make_wordcloud(file):
    # Punctuation if comes with words it might create duplicate words
    
    punctuations = '''!@#$%^&*()_+?/'";:}{[]\|'''

    #Common words should also be removed as they are repeated used to make sentences meanningful

    common_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    
    punctuation_free_text=""

    for char in file:
        if char not in punctuations:
            punctuation_free_text= punctuation_free_text + char
    words=punctuation_free_text.split()

    clean_words=[]
    frequencies={}

    for word in words:
        if word.isalpha():
            if word not in common_words:
                clean_words.append(word)

    for alpha_word in clean_words:
        if alpha_word not in frequencies:
            frequencies[alpha_word]=1
        else:
            frequencies[alpha_word]+=1

    # Making Wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

file=open("wordcloud_data.txt","r").read()
cloud_image = make_wordcloud(file)
plt.imshow(cloud_image,interpolation ='nearest')
plt.axis('off')
plt.show()
    
