def main():

    # needed libraries
    import re
    import time
    import collections
    from collections import Counter
    import nltk
    from nltk import word_tokenize
    from nltk.util import ngrams
    from nltk import FreqDist
    from collections import Counter
    from textblob import TextBlob
    from textblob.classifiers import NaiveBayesClassifier
    from textblob.sentiments import NaiveBayesAnalyzer


    # send the ngrams to the ladies


    #variables
    fname = "00T6000005aSQ7PEAW.txt"
    custTurn = 0
    salesTurn = 0
    num_lines = 0
    num_chars = 0
    countCustomer = 0
    countSalesPerson = 0
    train = [
        ('I love this sandwich.', 'pos'),
        ('this is an amazing place!', 'pos'),
        ('I feel very good about these beers.', 'pos'),
        ('this is my best work.', 'pos'),
        ("what an awesome view", 'pos'),
        ('I do not like this restaurant', 'neg'),
        ('I am tired of this stuff.', 'neg'),
        ("I can't deal with this", 'neg'),
        ('he is my sworn enemy!', 'neg'),
        ('my boss is horrible.', 'neg'),
        ('yeah', 'pos')]
    test = [
        ('the beer was good.', 'pos'),
        ('I do not enjoy my job', 'neg'),
        ("I ain't feeling dandy today.", 'neg'),
        ("I feel amazing!", 'pos'),
        ('Gary is a friend of mine.', 'pos'),
        ("I can't believe I'm doing this.", 'neg')]

    cl = NaiveBayesClassifier(train)
    cl.accuracy(test)




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


    for line in hand:
        line = line.rstrip()
        num_lines += 1
        num_chars += len(line)
        x = re.findall('\](.*?)\[', line)
        time = re.findall('\[(.*?)\]', line)
        countNonSpeechTotal = re.findall('#', line)
        # print(time)
        # m = re.split(r'\](.*?)\[', line)[0]
        if len(x) > 0:
            bigram = ngrams(x.__getitem__(0).split(), n=2)
            trigram = ngrams(x.__getitem__(0).split(), n=3)
            quadgram = ngrams(x.__getitem__(0).split(), n=4)
            pentgram = ngrams(x.__getitem__(0).split(), n=5)
            sentiment = TextBlob(x.__getitem__(0))
            sentimentInDepth = TextBlob(x.__getitem__(0), analyzer=NaiveBayesAnalyzer())
            tokens = nltk.word_tokenize(x.__getitem__(0))

            # Create your bigrams
            bgs = nltk.bigrams(tokens)

            # compute frequency distribution for all the bigrams in the text
            fdist = nltk.FreqDist(bgs)
            # fdisttri = nltk.FreqDist(trigram)
            # fdistqad = nltk.FreqDist(quadgram)
            # fdistpent = nltk.FreqDist(pentgram)
            for k, v in fdist.items():
                print(k, v)
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
                print("Number of Words in Turn:", num_words)
                print('Number of NonSpeechWords:', len(countNonSpeechTotal) / 2)
                print("Length of Turn: ", time.__getitem__(0),",", time.__getitem__(1))
                print(list(bigram))
                print(list(trigram))
                print(list(quadgram))
                print(list(pentgram))
                print(cl.classify(sentiment))
                print(sentiment.sentiment)
                print(sentimentInDepth.sentiment)
                print("----------------------------------------------\n")
            if line.find("Salesperson:") != -1:
                countSalesPerson = countSalesPerson + 1
                salesTurn = salesTurn + 1
                num_words = len(x.__getitem__(0).split())
                # bigram = ngrams(x.__getitem__(0).split(), n=2)
                print("----------------------------------------------\n")
                print("Salesperson Turn #:", salesTurn)
                print("Line Location in File:", num_lines)
                print("Salesperson Said:", "\"", x.__getitem__(0), "\"")
                print("Number of Words in Turn:", num_words)
                print('Number of NonSpeechWords:', len(countNonSpeechTotal) / 2)
                print("Length of Turn: ", time.__getitem__(0), ",", time.__getitem__(1))
                print(list(bigram))
                print(list(trigram))
                print(list(quadgram))
                print(list(pentgram))
                print(cl.classify(sentiment))
                print(sentiment.sentiment)
                print(sentimentInDepth.sentiment)
                print("----------------------------------------------\n")


    # display file information
    print("------- ADDITIONAL FILE INFORMATION ----------")
    print("             Lines in the File: ", num_lines)
    print("             Salesperson: ", countSalesPerson)
    print("             Customer: ", countCustomer)
    print("----------------------------------------------")









main()