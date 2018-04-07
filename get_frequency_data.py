def main():
    # import libraries
     import re
     # import sys
     import os
     import glob
     #import csv
     #import datetime

   # Read all txt files
     path = '/venv/'
    # writeto= open('diction')
     from os.path import isfile
     files = filter(isfile,glob.glob('%s/*'%path))

     files_text = [i for i in files if i.endswith(''.txt)]
     print(files_text)

    # initialize variables
     ct = 0
     minp = 0;secondp = 0;msp = 0
     pausemin = 0; pausesecond = 0;pausems = 0
     cmindiff = 0;cseconddiff = 0;cmsdiff = 0
     list = []
     p1m = 0;  p1s = 0; p1ms = 0
     cmindiff = 0;  csecondiff = 0;  cmsdiff = 0
     ctmindiff = 0;   ctseconddiff = 0; ctmsdiff = 0
     ct1mindiff = 0;ct1seconddiff = 0;ct1msdiff = 0
     ct2mindiff = 0;ct2seconddiff = 0;ct2msdiff = 0
     ct3mindiff = 0;ct3seconddiff = 0;ct3msdiff = 0
     ct4mindiff = 0;ct4seconddiff = 0;ct4msdiff = 0
     ct5mindiff = 0;ct5seconddiff = 0;ct5msdiff = 0
     round = 0
     #pause = 0
     pflag = 0
     begin = 0
     counter = 0
     c = ""
     flag = ''
     pausetype = ''
     fname = "test_1.txt"
     # open output file & instruction
     resultFile = open("test_1.csv", "w+")
     resultFile.write("This file includes time frequency data of transcript.\n")
     resultFile.write("This file has the same name to transcript, and name extension is 'csv'(transcript name extension is '.txt')\n")
     resultFile.write("Each row is one round. Each round starts at a salesperson, and end at the next salesperson\n")
     resultFile.write("1th column is talking time of salesperson\n")
     resultFile.write("2th column is time of last pause of each round\n")
     resultFile.write("3th column is talking time of customer\n")
     resultFile.write("4th column is time of all pauses except for the last pause within each round\n")
     resultFile.write("5th column is crosstalk type#1 C -> C\n")
     resultFile.write("6th column is crosstalk type#2 C -> S\n")
     resultFile.write("7th column is crosstalk type#3 S -> C\n")
     resultFile.write("8th column is crosstalk type#4 S -> S\n")
     resultFile.write("9th column is crosstalk type#5 S -> END\n\n")
    # open transcript
    # getting index of each turn with identify (R,S,C,[)
     with open(fname, "r") as f:
        for line1 in f:
            if (line1.find("*inaudible*") != -1):
                continue
            if(line1[0] != '\n'):
             list.append(line1[0])
     f.close()
    # close and reopen transcript
     with open(fname, "r") as f:
        # main loop
        for line in f:
            if (line.find("*inaudible*") != -1):
                continue    # skip inaudible
            # loop in each line
            for c in line:
                # set flags based on speaker
                if (c.isalpha() or c == '['):
                    if (c == '['):
                        c = "#T: "
                        pflag = 1
                    if (c == 'C'):
                        c = "#C:"
                        pflag = 1
                    if (c == 'S'):
                        c = "#S:"
                        begin = 1
                        pflag = 2
                    if (c == 'R'):
                        c = "#R: "
                        pflag = 1
                    if (begin != 1):
                        continue
                    # extract original time data
                    counter = counter + 1
                    line = line.rstrip()
                    time = re.findall('\[(.*?)\]', line)
                    time1 = " ".join(time)
                    # get start time
                    min = time1[0:2]
                    second = time1[3:5]
                    ms = time1[6:9]
                    # get end time
                    min1 = time1[10:12]
                    second1 = time1[13:15]
                    ms1 = time1[16:19]
                    # identify pause type
                    if (pflag == 2):
                        pausetype = "#p:"    # end pause for each round
                        p1m = pausemin    # 'P1' pause duration for each round
                        p1s = pausesecond
                        p1ms = pausems
                        # print("#p1:", pausemin, pausesecond, pausems)
                        pausemin = 0    # clear buffer
                        pausesecond = 0
                        pausems = 0
                    else:
                        pausetype = "#P1"    # all pausees within each round
                    # calculate pause duration
                    if (minp != 0 and secondp != 0 and msp != 0):
                        pausemin = pausemin + int(min) - int(minp)
                        if (second >= secondp):
                            pausesecond = pausesecond + int(second) - int(secondp)
                            if (pausesecond >= 60):
                                pausesecond = pausesecond - 60
                                pausemin = pausemin + 1
                        else:
                            pausesecond = pausesecond + int(second) + 60 - int(secondp)
                            pausemin = pausemin - 1
                            if (pausesecond >= 60):
                                pausesecond = pausesecond - 60
                                pausemin = pausemin + 1
                        if (ms >= msp):
                            pausems = pausems + int(ms) - int(msp)
                            if (pausems >= 1000):
                                pausems = pausems - 1000
                                pausesecond = pausesecond + 1
                        else:
                            pausems = pausems + int(ms) + 1000 - int(msp)
                            pausesecond = pausesecond - 1
                            if (pausems >= 1000):
                                pausems = pausems - 1000
                                pausesecond = pausesecond + 1
                    # calculate customer duration
                    if (c == "#C:"):
                        cmindiff = cmindiff + int(min1) - int(min)
                        if (second1 >= second):
                            cseconddiff = cseconddiff + int(second1) - int(second)
                        else:
                            cseconddiff = cseconddiff + int(second1) + 60 - int(second)
                            cmindiff = cmindiff - 1
                        if (cseconddiff >= 60):
                            cseconddiff = cseconddiff - 60
                            cmindiff = cmindiff + 1
                        if (ms1 >= ms):
                            cmsdiff = cmsdiff + int(ms1) - int(ms)
                        else:
                            cmsdiff = cmsdiff + int(ms1) + 1000 - int(ms)
                            cseconddiff = cseconddiff - 1
                        if (cmsdiff >= 1000):
                            cmsdiff = cmsdiff - 1000
                            cseconddiff = cseconddiff + 1
                    #calculate crosstalk duration
                    if (c == "#T: "):
                       # print(list[counter])
                        ctmindiff = ctmindiff + int(min1) - int(min)
                        if (second1 >= second):
                            ctseconddiff = ctseconddiff + int(second1) - int(second)
                        else:
                            ctseconddiff = ctseconddiff + int(second1) + 60 - int(second)
                            ctmindiff = ctmindiff - 1
                        if (ctseconddiff >= 60):
                            ctseconddiff = ctseconddiff - 60
                            ctmindiff = ctmindiff + 1
                        if (ms1 >= ms):
                            ctmsdiff = ctmsdiff + int(ms1) - int(ms)
                        else:
                            ctmsdiff = ctmsdiff + int(ms1) + 1000 - int(ms)
                            ctseconddiff = ctseconddiff - 1
                        if (ctmsdiff >= 1000):
                            ctmsdiff = ctmsdiff - 1000
                            ctseconddiff = ctseconddiff + 1
                        # identify crosstalk type
                        if ((len(list) - 1) == counter and list[(len(list) - 1)] == '['):
                            ct = "#CR5:"
                            ct5mindiff = ctmindiff; ct5seconddiff = ctseconddiff; ct5msdiff = ctmsdiff
                        elif (list[counter - 1] == 'C' and list[counter + 1] == 'C'):
                            ct = "#CR1:"
                            ct1mindiff = ctmindiff;ct1seconddiff = ctseconddiff;ct1msdiff = ctmsdiff
                        elif (list[counter - 1] == 'C' and list[counter + 1] == 'S'):
                            ct = "#CR2:"
                            ct2mindiff = ctmindiff;ct2seconddiff = ctseconddiff;ct2msdiff = ctmsdiff
                        elif (list[counter - 1] == 'S' and list[counter + 1] == 'C'):
                            ct = "#CR3:"
                            ct3mindiff = ctmindiff;ct3seconddiff = ctseconddiff;ct3msdiff = ctmsdiff
                        else:  # (list[counter - 1] == 'S' and list[counter + 1] == 'S'):
                            ct = "#CR4:"
                            ct4mindiff = ctmindiff; ct4seconddiff = ctseconddiff;ct4msdiff = ctmsdiff
                    # clear buffer
                    ctmindiff = 0
                    ctseconddiff = 0
                    ctmsdiff = 0
                    # calculate salesperson duration
                    mindiff = int(min1) - int(min)
                    if (second1 >= second):
                        seconddiff = int(second1) - int(second)
                    else:
                        seconddiff = int(second1) + 60 - int(second)
                        mindiff = mindiff - 1
                    if (ms1 >= ms):
                        msdiff = int(ms1) - int(ms)
                    else:
                        msdiff = int(ms1) + 1000 - int(ms)
                        seconddiff = seconddiff - 1
                    # print information at the end of each round
                    if (minp != 0 and secondp != 0 and msp != 0 and pausetype == "#p:"):
                        resultFile.write(" %s%02d:%02d:%03d " % ("#p:", pausemin, pausesecond, pausems))
                        resultFile.write(" %s%02d:%02d:%03d " % ("#P1:", p1m, p1s, p1ms))
                        resultFile.write(" %s%02d:%02d:%03d " % ("#C:", cmindiff, cseconddiff, cmsdiff))
                        resultFile.write(" %s%02d:%02d:%03d " % ("#CR1 ", ct1mindiff, ct1seconddiff, ct1msdiff))
                        resultFile.write(" %s%02d:%02d:%03d " % ("#CR2 ", ct2mindiff, ct2seconddiff, ct2msdiff))
                        resultFile.write(" %s%02d:%02d:%03d " % ("#CR3 ", ct3mindiff, ct3seconddiff, ct3msdiff))
                        resultFile.write(" %s%02d:%02d:%03d " % ("#CR4 ", ct4mindiff, ct4seconddiff, ct4msdiff))
                        resultFile.write(" %s%02d:%02d:%03d \n" % ("#CR5 ", ct5mindiff, ct5seconddiff, ct5msdiff))
                    # print information at the beginning of each round
                    if (c == "#S:"):
                        round = round + 1
                        resultFile.write("%d %s%02d:%02d:%03d " % (round,"#S:", mindiff, seconddiff, msdiff))
                    # After calculating in this round, save time data as previous time data
                    minp = min1
                    secondp = second1
                    msp = ms1
                    # clear buffer & reset variable at the end of each round
                    if (pausetype == "#p:"):
                        pausemin = 0;pausesecond = 0;pausems = 0
                        cmindiff = 0;cseconddiff = 0;cmsdiff = 0
                        ctmindiff = 0;ctseconddiff = 0;ctmsdiff = 0
                        ct1mindiff = 0;ct1seconddiff = 0;ct1msdiff = 0
                        ct2mindiff = 0;ct2seconddiff = 0;ct2msdiff = 0
                        ct3mindiff = 0;ct3seconddiff = 0;ct3msdiff = 0
                        ct4mindiff = 0;ct4seconddiff = 0;ct4msdiff = 0
                        ct5mindiff = 0;ct5seconddiff = 0;ct5msdiff = 0
                        ct = ""
                    if (c != "#T: "):
                        flag = c
                    # done with each round, go to the next round
                    break
     # print information at the end of the file
     resultFile.write(" %s%02d:%02d:%03d " % ("#p:", 0, 0, 0))
     resultFile.write(" %s%02d:%02d:%03d " % ("#P1:", pausemin, pausesecond, pausems))
     resultFile.write(" %s%02d:%02d:%03d " % ("#C:", cmindiff, cseconddiff, cmsdiff))
     resultFile.write(" %s%02d:%02d:%03d " % ("#CR1 ", ct1mindiff, ct1seconddiff, ct1msdiff))
     resultFile.write(" %s%02d:%02d:%03d " % ("#CR2 ", ct2mindiff, ct2seconddiff, ct2msdiff))
     resultFile.write(" %s%02d:%02d:%03d " % ("#CR3 ", ct3mindiff, ct3seconddiff, ct3msdiff))
     resultFile.write(" %s%02d:%02d:%03d " % ("#CR4 ", ct4mindiff, ct4seconddiff, ct4msdiff))
     resultFile.write(" %s%02d:%02d:%03d \n" % ("#CR5 ", ct5mindiff, ct5seconddiff, ct5msdiff))
     f.close()
     resultFile.close()
main()