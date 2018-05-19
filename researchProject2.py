def main():

    # needed libraries
    import re
    import time
    import collections
    import glob
    from collections import Counter
    import nltk
    import csv
    from nltk import word_tokenize
    from nltk.util import ngrams
    from nltk import FreqDist
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    from collections import Counter
    from textblob import TextBlob
    from textblob.classifiers import NaiveBayesClassifier
    from textblob.sentiments import NaiveBayesAnalyzer
    from nltk import FreqDist




    # relational words on salesperson
    # LDA --- work with Latent  Dirchetlay Analysis Modeling Topic Modeling

    # send the ngrams to the ladies

    #variables
    fname = "00T600005HJIw9EAH.txt"
    custTurn = 0
    salesTurn = 0
    num_lines = 0
    num_chars = 0
    countCustomer = 0
    countSalesPerson = 0
    # ipath = '/Volumes/My Passport for Mac/Research/Transcriptions\ -\ Most\ up\ to\ date/'  # input folder
    # opath = '/Volumes/My Passport for Mac/Research/output.csv'  # output folder .contains

    # output = open('/Volumes/My Passport for Mac/Research/xyz.txt', 'w')

    train = [
        ('annoying', 'neg'),
        ('already', 'neg'),
        ('basically', 'neg'),
        ('don\t have an ', 'pos'),
        ('have any needs', 'neg'),
        ('I don\'t really', 'neg'),
        ('I don\'t think', 'neg'),
        ('I\'m fine', 'neg'),
        ('I\'m gonna pass', 'neg'),
        ('I\'m good thanks', 'neg'),
        ('I\'ve already ', 'neg'),
        ('keep calling', 'neg'),
        ('kinda doubt it', 'neg'),
        ('literally', 'neg'),
        ('make any changes', 'neg'),
        ('no need', 'neg'),
        ('no reason' ,'neg'),
        ('not been able', 'neg'),
        ('not buying	', 'neg'),
        ('not going to change', 'neg'),
        ('not going to consider', 'neg'),
        ('not', 'pos'),
        ('not looking', 'neg'),
        ('not really', 'neg'),
        ('the problem is', 'neg'),
        ('this road before', 'neg'),
        ('unreasonable', 'neg'),
        ('waste time', 'neg'),
        ('we don\'t do?', 'neg'),
        ('we don\'t use	', 'neg'),
        ('we don\'t wanna', 'neg'),
        ('we really don\'t', 'neg'),
        ('we\'re not adding', 'neg'),
        ('won\'t be looking	', 'neg'),
        ('all set', 'neg'),
        ('covered', 'neg'),
        ('don\'t outsource', 'neg'),
        ('have our own', 'neg'),
        ('in house', 'neg'),
        ('kinda set', 'neg'),
        ('local', 'neg'),
        ('locally', 'neg'),
        ('mechanic', 'neg'),
        ('our own', 'neg'),
        ('owner operator', 'neg'),
        ('taken care of ', 'neg'),
        ('they do it all ', 'neg'),
        ('we do everything', 'neg'),
        ('we do it all ourselves', 'neg'),
        ('we have enough', 'neg'),
        ('we own', 'neg'),
        ('we\’re pretty happy', 'neg'),
        ('well set', 'neg'),
        ('we\'re all set up', 'neg'),
        ('we\'re fine', 'neg'),
        ('we\'re good', 'neg'),
        ('we\'re okay', 'neg'),
        ('works well' ,'neg'),
        ('any time soon', 'neg'),
        ('at this point', 'neg'),
        ('at this time', 'neg'),
        ('currently', 'neg'),
        ('don\'t currently lease', 'neg'),
        ('gonna wait', 'neg'),
        ('I just signed', 'neg'),
        ('just had' ,'neg'),
        ('more years left', 'neg'),
        ('near future', 'neg'),
        ('not a great time', 'neg'),
        ('not at this time', 'neg'),
        ('not right now', 'neg'),
        ('not too often', 'neg'),
        ('quite some time', 'neg'),
        ('rarely', 'neg'),
        ('right now', 'neg'),
        ('still', 'neg'),
        ('under contract', 'neg'),
        ('we just bought', 'neg'),
        ('we just signed', 'neg'),
        ('we\'ve already', 'neg'),
        ('awesome', 'pos'),
        ('be fine', 'pos'),
        ('fantastic', 'pos'),
        ('fine for you', 'pos'),
        ('great', 'pos'),
        ('I can be flexible', 'pos'),
        ('I can talk' ,'pos'),
        ('I could', 'pos'),
        ('I guess', 'pos'),
        ('I think we' ,'pos'),
        ('I would say', 'pos'),
        ('I\'d love to', 'pos'),
        ('if you know', 'pos'),
        ('I\'ll be', 'pos'),
        ('I\'ll look forward', 'pos'),
        ('I\'m free', 'pos'),
        ('let me ', 'pos'),
        ('let me check', 'pos'),
        ('let\'s', 'pos'),
        ('let\'s see	', 'pos'),
        ('look fine', 'pos'),
        ('looks good', 'pos'),
        ('may I help you', 'pos'),
        ('no big deal', 'pos'),
        ('of course', 'pos'),
        ('perfect', 'pos'),
        ('should be able to' ,'pos'),
        ('should be good', 'pos'),
        ('shouldn\'t be a problem', 'pos'),
        ('sounds good', 'pos'),
        ('that should work', 'pos'),
        ('that would be fine', 'pos'),
        ('that would be great', 'pos'),
        ('that\'ll work', 'pos'),
        ('that\'s fine', 'pos'),
        ('this is a good time', 'pos'),
        ('very good', 'pos'),
        ('we could', 'pos'),
        ('what day', 'pos'),
        ('what time', 'pos'),
        ('what works best', 'pos'),
        ('when are you', 'pos'),
        ('when you thinking?', 'pos'),
        ('why not', 'pos'),
        ('will do', 'pos'),
        ('works', 'pos'),
        ('would be fine', 'pos'),
        ('yeah I do ', 'pos'),
        ('better make it', 'pos'),
        ('check back later', 'pos'),
        ('check with them', 'pos'),
        ('have him call', 'pos'),
        ('have him stop by', 'pos'),
        ('it\'d have to be', 'pos'),
        ('just send that', 'pos'),
        ('reach out to me', 'pos'),
        ('send me', 'pos'),
        ('send somebody here to show', 'pos'),
        ('can I have you', 'pos'),
        ('can reach out	', 'pos'),
        ('can we schedule', 'pos'),
        ('can you', 'pos'),
        ('could we', 'pos'),
        ('drop in	', 'pos'),
        ('give you my', 'pos'),
        ('How about	', 'pos'),
        ('how I like to do', 'pos'),
        ('I can schedule	', 'pos'),
        ('I\'d rather meet	', 'pos'),
        ('if we could 	', 'pos'),
        ('if you can 	', 'pos'),
        ('if you have thought about	', 'pos'),
        ('if you want	', 'pos'),
        ('information on	', 'pos'),
        ('is there any information	', 'pos'),
        ('just wanted to 	', 'pos'),
        ('number I can reach you	', 'pos'),
        ('probably better	', 'pos'),
        ('see if I\'m 	', 'pos'),
        ('tell you what	', 'pos'),
        ('to come by	', 'pos'),
        ('we may have to ', 'pos'),
        ('welcome to stop in' ,'pos'),
        ('why don\'t you	', 'pos'),
        ('will you	', 'pos'),
        ('would be better for me	', 'pos'),
        ('would probably be best	', 'pos'),
        ('you can	', 'pos'),
        ('you can send	', 'pos'),
        ('you can stop by	', 'pos'),
        ('you may want to 	', 'pos'),
        ('I wanna hear some details	', 'pos'),
        ('I would talk to somebody	', 'pos'),
        ('I\'ll look at it	', 'pos'),
        ('I\'ve been thinking	', 'pos'),
        ('like to talk 	', 'pos'),
        ('take a look	', 'pos'),
        ('we can review	', 'pos'),
        ('we can see	', 'pos'),
        ('we\’d be', 'pos'),
        ('ed in looking', 'pos'),
        ('we\'ll keep it in mind', 'pos'),
        ('anything different', 'pos'),
        ('coming up this year', 'pos'),
        ('competitive price	', 'pos'),
        ('has your pricing changed', 'pos'),
        ('if there\'s a good deal	', 'pos'),
        ('if there\'s an opportunity	', 'pos'),
        ('if we could figure something out', 'pos'),
        ('I\'m looking for', 'pos'),
        ('is that something you', 'pos'),
        ('it depends	', 'pos'),
        ('may be looking', 'pos'),
        ('never hurts	', 'pos'),
        ('resources for what', 'pos'),
        ('see who\'s gonna provide	', 'pos'),
        ('we are looking to sell 	', 'pos'),
        ('we have a need	', 'pos'),
        ('we like to know	', 'pos'),
        ('we may need	', 'pos'),
        ('we\'re always looking	', 'pos'),
        ('we\'re looking for	', 'pos'),
        ('what kind of programs	', 'pos'),
        ('what type of ', 'pos'),
        ('you would be able', 'pos'),
        ('from where', 'pos'),
        ('give me an idea', 'pos'),
        ('talking about	', 'pos'),
        ('this in regards to', 'pos'),
        ('what about', 'pos'),
        ('what are you', 'pos'),
        ('what does your company do	', 'pos'),
        ('what was', 'pos'),
        ('what\'s the name', 'pos'),
        ('where are you', 'pos'),
        ('where ya\'ll ', 'pos'),
        ('where you guys at	', 'pos'),
        ('which location	', 'pos'),
        ('which office do you', 'pos'),
        ('who are you with	', 'pos'),
        ('who would be the person	', 'pos'),
        ('you got one?	', 'pos'),
        ('you got somebody	', 'pos'),
        ('you mean	', 'pos'),
        ('you\'re with' ,'pos'),
        ('go ahead	', 'pos'),
        ('I have a minute', 'pos'),
        ('I have a moment', 'pos'),
        ('I have a second', 'pos'),
        ('what can I do', 'pos'),
        ('what do you got', 'pos'),
        ('what do you have', 'pos'),
        ('what do you sell', 'pos'),
        ('whatcha got', 'pos'),
        ('whatcha need', 'pos'),
        ('what\'s going on?', 'pos'),
        ('What\'s up', 'pos'), ]
    test = [
        ('what do you sell', 'pos'),
        ('we do it all ourselves', 'neg'),
        ('I ain\'t feeling dandy today.', 'neg'),
        ('whatcha got', 'pos'),
        ('What\'s up', 'pos'),
        ('don\'t outsource', 'neg')]

    cl = NaiveBayesClassifier(train)
    cl.accuracy(test)
    # print(cl.accuracy(test))
    print(cl.show_informative_features(20))




    # test it out
    # line = 'Salesperson: [00:27:715] Hey Gerald, this is Blyce, I\'m calling from #uh# Penske at the corporate office #um# just had a quick question if you have a second, I\'ll keep it real brief for ya #um# what else I was trying to arrange was #um# #uh# getting a you know, meeting with #uh# the local rep. Not lease discussion but more about #um# if we could help you with maintenance #um# you probably have % [00:51:411]'
    # x = re.findall('\](.*?)\[', line)
    # sentiment = TextBlob(x.__getitem__(0))
    # sentimentInDepth = TextBlob(x.__getitem__(0), analyzer=NaiveBayesAnalyzer())
    # print(cl.classify(sentiment))
    # print(sentiment.sentiment)
    # print(sentimentInDepth.sentiment)
    # Each word in the lexicon has scores for:
    # 1)     polarity: negative vs. positive    (-1.0 => +1.0)
    # 2) subjectivity: objective vs. subjective (+0.0 => +1.0)
    # 3)    intensity: modifies next word?      (x0.5 => x2.0)
    # tokens = nltk.word_tokenize(sentence)
    # evaluate_classifier(tokens)
    # print(tokens)

    # working with one string
    # s = 'Receptionist: [00:14:371] Teraldy Engineering [00:15:362]'
    # regex - regular expression:
    # dissect = re.findall('\[(.*?)\]', s)
    # print(dissect.__getitem__(0), dissect.__getitem__(1))


    # reading in our file
    hand = open(fname, "r")

    # files = glob.glob(ipath)
    # # iterate over the list getting each file
    # for fle in files:
    #     # open the file and then call .read() to get the text
    #     with open(fle) as f:
    #         text = f.read()
    for line in hand:
        line = line.rstrip()
        num_lines += 1
        num_chars += len(line)
        x = re.findall('\](.*?)\[', line)
        # wordsToCount .add(line)
        # print(wordsToCount)
        # words_to_count = (word for word in x.__getitem__(0) if word[:1].isupper())
        # c = Counter(words_to_count)
        # print(c.most_common(3))
        time = re.findall('\[(.*?)\]', line)
        countNonSpeechTotal = re.findall('#', line)
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(x.__getitem__(0))
        # print(ss)

        # print(time)
        # m = re.split(r'\](.*?)\[', line)[0]
        if len(x) > 0:
            bigram = ngrams(x.__getitem__(0).split(), n=2)
            trigram = ngrams(x.__getitem__(0).split(), n=3)
            quadgram = ngrams(x.__getitem__(0).split(), n=4)
            pentgram = ngrams(x.__getitem__(0).split(), n=5)
            sentimentInDepth = TextBlob(x.__getitem__(0), analyzer=NaiveBayesAnalyzer())
            a = (sentimentInDepth.sentiment)
            if a.__getattribute__("p_pos") > a.__getattribute__("p_neg"):
                tag = str(a.__getattribute__("classification"))
                sentiment = str(a.__getattribute__("p_pos"))
            elif a.__getattribute__("p_pos") < a.__getattribute__("p_neg"):
                tag = str(a.__getattribute__("classification"))
                sentiment = str(a.__getattribute__("p_neg"))
            elif a.__getattribute__("p_pos") == a.__getattribute__("p_neg"):
                tag = "N"
                sentiment = "0.5"
            else:
                tag = "N"
                sentiment = "0"

            feelings = TextBlob(x.__getitem__(0))
            tokens = nltk.word_tokenize(x.__getitem__(0))
            # Create your bigrams
            bgs = nltk.bigrams(tokens)
            # compute frequency distribution for all the bigrams in the text
            fdist = nltk.FreqDist(bgs)
            freqDist = FreqDist(bgs)
            fdisttri = nltk.FreqDist(trigram)
            fdistqad = nltk.FreqDist(quadgram)
            fdistpent = nltk.FreqDist(pentgram)
            # for k, v in fdist.items():
            #     print(k, v)
            # for k, v in fdisttri.items():
            #     print(k, v)
            # for k, v in fdistqad.items():
            #     print(k, v)
            # for k, v in fdistpent.items():
            #     print(k, v)

            if line.find("Customer:") != -1:
                countCustomer = countCustomer + 1
                num_words = len(x.__getitem__(0).split())
                custTurn = custTurn + 1
                print("----------------------------------------------\n")
                print("Customer Turn #:", custTurn)
                print("Line Location in File:", num_lines)
                print("Customer Said:", "\"", x.__getitem__(0), "\"")
                print("Sentence with Tagged",feelings.tags)
                print("Language Detected:",feelings.detect_language())
                print("Number of Words in Turn:", num_words)
                print('Number of NonSpeechWords:', len(countNonSpeechTotal) / 2)
                # print("Length of Turn: ", time.__getitem__(0), ",", time.__getitem__(1))
                print(list(bigram))
                print(list(trigram))
                print(list(quadgram))
                print(list(pentgram))
                # output.write((list(bigram)))

                print("Classification Functions Result:", cl.classify(feelings))
                print("Sentiment Analysis Function Result:", feelings.sentiment)
                # print("Accuracy:")
                print("Neutral Detection:", a)
                print("NLTK Sentiment Analysis:", format(ss))
                # print(sentimentInDepth.sentiment)
                print("----------------------------------------------\n")
            # if line.find("Salesperson:") != -1:
            #     countSalesPerson = countSalesPerson + 1
            #     salesTurn = salesTurn + 1
            #     num_words = len(x.__getitem__(0).split())
            #     # bigram = ngrams(x.__getitem__(0).split(), n=2)
            #     print("----------------------------------------------\n")
            #     print("Salesperson Turn #:", salesTurn)
            #     print("Line Location in File:", num_lines)
            #     print("Salesperson Said:", "\"", x.__getitem__(0), "\"")
            #     print("Number of Words in Turn:", num_words)
            #     print('Number of NonSpeechWords:', len(countNonSpeechTotal) / 2)
            #     print("Length of Turn: ", time.__getitem__(0), ",", time.__getitem__(1))
            #     print(list(bigram))
            #     print(list(trigram))
            #     print(list(quadgram))
            #     print(list(pentgram))
            #     print(cl.classify(sentiment))
            #     print(sentiment.sentiment)
            #     # print(sentimentInDepth.sentiment)
            #     print("----------------------------------------------\n")

        # display file information
    print("------- ADDITIONAL FILE INFORMATION ----------")
    print("             Lines in the File: ", num_lines)
    print("             Salesperson: ", countSalesPerson)
    print("             Customer: ", countCustomer)
    print("Most Common Words",list(fdist.most_common(100)))
    print("----------------------------------------------")
    print("DONE")


main()