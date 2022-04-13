a, b, c = (1, 2, 3)

import urllib.request
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
# bg = "asf"
# for i in bg:
#     print(i)

def generate_five_letter_words():
    ### So the thing is, the word "akhgd" doesn't make sense, yeah, so it's quite unguessable. So i would be using this function to generate an exhaustive list of five letter words. Of course, there might be some words not in it. But it's better than nothing. As for the challenge, on reading the prompt again, I realized it's not neccessary. But i'll go on to do it anyway, since i'll be pushing the code to my github###
    list_of_valid_five_letter_word = []
    word_site = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
    response = urllib.request.urlopen(word_site)
    txt = response.read()
    WORDS = txt.splitlines()

    for word in WORDS:
        # if len(word.decode("utf-8")) == 5:
        #     list_of_valid_five_letter_word.append(word.decode("utf-8"))
        if word.decode("utf-8").lower() == "thyme":
            print('Yes!')
    #return list_of_valid_five_letter_word



print(generate_five_letter_words())
