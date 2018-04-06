import csv
import nltk
import re
import os
from collections import Counter
import glob
from nltk.util import ngrams

path = '/Users/moe/PycharmProjects/researchProject/Transcripts'

writeTo = open('dictionary.txt', 'w')

from os.path import isfile
files=filter(isfile,glob.glob('%s/*'%path))

files_txt = [i for i in files if i.endswith('.txt')]
# print(files_txt)
for file in files_txt:
    hand = open(file, "r", encoding='latin2')
    # writeTo = open(file, 'w')
    for line in hand:
        line = line.rstrip()
        x = re.findall('\](.*?)\[', line)
        # punctuationRemoved = re.sub('[12345678890\-.\,!;%@#$]', '', str(x))
        time = re.findall('\[(.*?)\]', line)
        countNonSpeechTotal = re.findall('#', line)
        # print(punctuationRemoved)
        writeTo.write('\n---------------FILE:' + file + "------------------\n")
        if len(x) > 0:
            bigram = ngrams(x.__getitem__(0).split(), n=2)
            trigram = ngrams(x.__getitem__(0).split(), n=3)
            quadgram = ngrams(x.__getitem__(0).split(), n=4)
            pentgram = ngrams(x.__getitem__(0).split(), n=5)
            if line.find("Customer:") != -1:
                print()
                num_words = len(x.__getitem__(0).split())
                writeTo.write("\nCustomer Said:" + "\"" + str(x.__getitem__(0)) + "\"\n")
                writeTo.write('\nNumber of NonSpeechWords:' + str(len(countNonSpeechTotal) / 2) + '\n')
                writeTo.write(('\n----------BIGRAMs----------------'))
                writeTo.write('\n' + str(list(bigram)))
                writeTo.write('\n\n')
                writeTo.write(('---------- TRIGRAMs----------------'))
                writeTo.write('\n' + str(list(trigram)))
                writeTo.write('\n\n')
                writeTo.write(('---------- QUADGRAMs----------------'))
                writeTo.write('\n' + str(list(quadgram)))
                writeTo.write('\n\n')
                writeTo.write(('---------- PENTGRAMs----------------'))
                writeTo.write('\n' + str(list(bigram)))
                writeTo.write('\n\n')
hand.close()
print("DONE")
# s = 'Receptionist: [00:14:371] Teraldy Engineering [00:15:362]'
# regex - regular expression:
# dissect = re.findall('\](.*?)\[', s)
# tokens = nltk.word_tokenize(dissect.__getitem__(0).split())
# bigram = ngrams(dissect.__getitem__(0).split(), n=2)
# print(list(bigram).__getitem__(0))


# fname = "00T6000005aSQ7PEAW.txt"
# hand = open(fname, "r")
# for line in hand:
#     line = line.rstrip()
#     x = re.findall('\](.*?)\[', line)
#     punctuationRemoved = re.sub('[.,!;@#$]', '', str(x))
#     time = re.findall('\[(.*?)\]', line)
#     countNonSpeechTotal = re.findall('#', line)
#     if len(x) > 0:
#         bigram = ngrams(x.__getitem__(0).split(), n=2)
#         trigram = ngrams(x.__getitem__(0).split(), n=3)
#         quadgram = ngrams(x.__getitem__(0).split(), n=4)
#         pentgram = ngrams(x.__getitem__(0).split(), n=5)
#         if line.find("Customer:") != -1:
#                 num_words = len(x.__getitem__(0).split())
#                 writeTo.write("Customer Said:" + "\"" + str(x.__getitem__(0)) + "\"\n")
#                 writeTo.write('Number of NonSpeechWords:' + str(len(countNonSpeechTotal) / 2) + '\n' )
#                 writeTo.write(('\n----------BIGRAMs----------------'))
#                 writeTo.write('\n' + str(list(bigram)))
#                 writeTo.write('\n\n')
#                 writeTo.write(('---------- TRIGRAMs----------------'))
#                 writeTo.write('\n' + str(list(trigram)))
#                 writeTo.write('\n\n')
#                 writeTo.write(('---------- QUADGRAMs----------------'))
#                 writeTo.write('\n' + str(list(quadgram)))
#                 writeTo.write('\n\n')
#                 writeTo.write(('---------- PENTGRAMs----------------'))
#                 writeTo.write('\n' + str(list(bigram)))
#                 writeTo.write('\n\n')
# hand.close()
