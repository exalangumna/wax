#~~~       outline                                                  
#       input srt output worksheets                                 
##              import modules                                      
##              declare locations                                   
##              prep srt file                                       
###                         srtclean                                
##              convert cleantext into dictionaries and indices     
###                         freqcheck                               
###                         makesentindex                           
###                         dictdivide                              
###                         makewordindex                           
###                         indexdict                               
##              use indexes to produce worksheets                   
###                         selectwords                             
###                         makeworksheet                           
#                                                                   

# input srt output worksheets   

##import modules                
import random

##declare locations             
jj='C:/Users/lol/Desktop/Game.of.Thrones.S01E01.2011.720p.HDTV.PFT.mkv.srt'
home = 'C:/Users/lol/Documents/worksheet'
#file0 = input('location_of_file: ')    
file0=jj

##prep srt file

###convert srt four-row format to sentence1=line1 txt  

#Easy, boy.                                                                                             
#One lot steals a goat from another lot, before you know it they're ripping each other to pieces.       
#I've never seen wildlings do a thing like this.                                                        
#I never seen a thing like this, not ever in my life.                                                   
#How close did you get?                                                                                 
#Do the dead frighten you?                                                                              
#Our orders were to track the wildlings.                                                                
#We tracked them.                                                                                       
#They won't trouble us no more.                                                                         
#You don't think he'll ask us how they died?                                                            
#Get back on your horse.                                                                                

def srtclean():
    x = 'C:/Users/lol/Documents/worksheet/bin/1/cleantext.txt'
    file0b = open(file0,"rb")
    list0=[]
    for line in file0b:
        if str(chr(line[0])).isalpha()==True:
            list0.append((line))
    file0b.close()
    cleantext = open(x, "wb")
    aggstring=b""
    for line in list0:
        if line[-3] == 33 or line[-3]== 46 or line[-3]== 63:
            line = aggstring + b' '+ line
            cleantext.write(line)
            aggstring = b""
        else:
            aggstring = aggstring + b' ' + line
            aggstring = aggstring[0:-2]
            print (aggstring)        
    cleantext.close()

##convert cleantext into dictionaries and indices                               

###turn sentline txt into |frequency integer + ' ' + 'word'| as line in txt     

#1 above            
#1 accept           
#1 accomplishment   
#1 act              
#1 advice           
#   [...]           
#28 it              
#29 for             
#30 he              
#50 a               
#61 to              
#69 you             
#94 the             

def freqcheck():
    x = 'C:/Users/lol/Documents/worksheet/bin/1/cleantext.txt'
    y = 'C:/Users/lol/Documents/worksheet/bin/1/freqdict.txt'
    cleantext=open(x,'rt')
    rawwordlist=[]
    for line in cleantext:
        line = line.split()
        for i in line:
            if i.islower() == False:
                line.remove(i)
            elif i[-3:len(i)]=='---':
                i=i[:-3]
                rawwordlist.append(i)
            elif i[-3:len(i)]=="'re":
                i=i[:-3]
                rawwordlist.append(i)
            elif i[-3:len(i)]=="'ve":
                i=i[:-3]
                rawwordlist.append(i)
            elif i[-3:len(i)]=="'ll":
                i=i[:-3]
                rawwordlist.append(i)
            elif i[-3:len(i)]=='...':
                i=i[:-3]
                rawwordlist.append(i)
            elif i[-2:(len(i))]=="'d":
                i=i[:-2]
                rawwordlist.append(i)
            elif i[-2:(len(i))]=="'s":
                i=i[:-2]
                rawwordlist.append(i)
            elif i[0]=='<':
                i=i[3:len(i)]
                rawwordlist.append(i)
            elif i[-1]=='>':
                i=i[:-4]
                rawwordlist.append(i)
            elif i[-1]=='?':
                i=i[:-1]
                rawwordlist.append(i)
            elif i[-1]==',':
                i=i[:-1]
                rawwordlist.append(i)
            elif i[-1]=='!':
                i=i[:-1]
                rawwordlist.append(i)
            elif i[-1]=='.':
                i=i[:-1]
                rawwordlist.append(i)
            elif i[-1]=='"':
                i=i[:-1]
                rawwordlist.append(i)
            else:
                rawwordlist.append(i)
    statfreqtuplelist=[]
    dynfreqtuplelist=[]
    for i in rawwordlist:
        statfreqtuplelist.append(tuple([i,rawwordlist.count(i)]))
    statfreqtuplelist.sort()
    for i in statfreqtuplelist:
        if i in dynfreqtuplelist:
            print (i)
        else:
            dynfreqtuplelist.append(i)
    reversedynfreqtuplelist = []
    for i in dynfreqtuplelist:
        reversedynfreqtuplelist.append([i[1],i[0]])
    reversedynfreqtuplelist.sort()
    freqtext = open(y,'wt')
    for i in reversedynfreqtuplelist:
        freqtext.write(str(i[0]) + ' ' + str(i[1]))
        freqtext.write('\n')
    freqtext.close()

### count the lines in cleantext, convert the value to 0xxx format, assign those values to create a sentence index  

#0000  Easy, boy.                                                                                           
#0001  One lot steals a goat from another lot, before you know it they're ripping each other to pieces.     
#0002  I've never seen wildlings do a thing like this.                                                      
#0003  I never seen a thing like this, not ever in my life.                                                 
#0004  How close did you get?                                                                               
#0005  Do the dead frighten you?                                                                            
#0006  Our orders were to track the wildlings.                                                              

def makesentindex():
    cleanfile='{a}/bin/{b}/cleantext.txt'.format(a=home,b=1)
    indexfile='{a}/bin/{b}/sentindex.txt'.format(a=home,b=1)
    clean = open(cleanfile, 'rt')
    sentindex = {}
    counter = 0
    for i in clean:
        sentindex[counter] = i
        counter +=1
    clean.close()
    index = open(indexfile, 'wt')
    for i in sentindex:
        if i <=9:
            index.write('000'+str(i))
        elif i <=99:
            index.write('00'+str(i))
        elif i <=999:
            index.write('0'+str(i))
        else:
            index.write(str(i))
        index.write(' ')
        index.write(sentindex[i])
    index.close()

###divide masterdict into 3 levels, filters minor   
    
def dictdivide():
    masterdictfile='C:/Users/lol/Documents/worksheet/bin/1/freqdict.txt'
    outmajor = '{a}/bin/{b}/majordict.txt'.format(a=home, b=1)
    outplural = '{a}/bin/{b}/pluraldict.txt'.format(a=home, b=1)
    outminor = '{a}/bin/{b}/minordict.txt'.format(a=home, b=1)
    filterfile='{a}/lib/filter.txt'.format(a=home, b=1)
    masterdict=open(masterdictfile, 'rt')
    majorlist=[]
    plurallist=[]
    minorlist=[]
    for i in masterdict:
        print (i[0])
        if int(i[0]) == 1:
            if i[1]== " ":
                majorlist.append(i[2:len(i)])
            else:
                minorlist.append(i[3:len(i)])
        elif int(i[0])==2:
            if i[1] == " ":
                plurallist.append(i[2:len(i)])
            else:
                minorlist.append(i[3:len(i)])
        elif int(i[0])<= 9:
            if i[1] == " ":
                minorlist.append(i[2:len(i)])
            else:
                minorlist.append(i[3:len(i)])
    masterdict.close()
    print (len(majorlist))
    print (len(plurallist))
    print (len(minorlist))
    filterlist=[]
    filterwords=open(filterfile,"rt")
    for i in filterwords:
        filterlist.append(i)
    filterwords.close()
    majordict = open(outmajor, 'wt')
    for i in majorlist:
        if i in filterlist:
            print (i)
        else:
            majordict.write(i)
    majordict.close()
    pluraldict = open(outplural, 'wt')
    for i in plurallist:
        if i in filterlist:
            print (i)
        else:
            pluraldict.write(i)
    pluraldict.close()
    minordict = open(outminor, 'wt')
    for i in minorlist:
        if i in filterlist:
            print (i)
        else:
            minordict.write(i)
    minordict.close()

###records words locations in the file denoted by the sentence index

#steals 1       
#a 1            
#goat 1         
#from 1         
#another 1      
#lot 1          
#before 1       
#   [...]       
#climber 455    
#aren't 455     
#you 455        
#for 456        
#love 456       

def makewordindex():
    cleanfile='{a}/bin/{b}/cleantext.txt'.format(a=home,b=1)
    wordindexfile='{a}/bin/{b}/wordindex.txt'.format(a=home,b=1)
    cleantext=open(cleanfile,'rt')
    rawwordlist=[]
    counter = 0
    for line in cleantext:
        line = line.split()
        for i in line:
            if i.islower() == False:
                line.remove(i)
            elif i[-3:len(i)]=='---':
                i=i[:-3]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-3:len(i)]=="'ve":
                i=i[:-3]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-3:len(i)]=="'re":
                i=i[:-3]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-3:len(i)]=="'ll":
                i=i[:-3]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-3:len(i)]=='...':
                i=i[:-3]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-2:(len(i))]=="'d":
                i=i[:-2]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-2:(len(i))]=="'s":
                i=i[:-2]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[0]=='<':
                i=i[3:len(i)]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-1]=='>':
                i=i[:-4]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-1]=='?':
                i=i[:-1]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-1]==',':
                i=i[:-1]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-1]=='!':
                i=i[:-1]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-1]=='.':
                i=i[:-1]
                rawwordlist.append(i + ' '+ str(counter))
            elif i[-1]=='"':
                i=i[:-1]
                rawwordlist.append(i + ' '+ str(counter))
            else:
                rawwordlist.append(i + ' '+ str(counter))
        counter+=1
    cleantext.close()
    wordindex=open(wordindexfile, 'wt')
    for i in rawwordlist:
        wordindex.write(i)
        wordindex.write('\n')
    wordindex.close()

###uses both indexs in conj with the masterdict(in 3 pieces) to give sent locations for each word   

#throne 191,240,261,402,417
#wall 56,77,310,323,347
#bastard 309,326,329,330,331,335
#dead 5,81,117,130,170,303

def indexdict():
    majord = '{a}/bin/{b}/majordict.txt'.format(a=home, b=1)
    plurald = '{a}/bin/{b}/pluraldict.txt'.format(a=home, b=1)
    minord = '{a}/bin/{b}/minordict.txt'.format(a=home, b=1)
    outmajord = '{a}/bin/{b}/outmajordict.txt'.format(a=home, b=1)
    outplurald = '{a}/bin/{b}/outpluraldict.txt'.format(a=home, b=1)
    outminord = '{a}/bin/{b}/outminordict.txt'.format(a=home, b=1)
    sentindexfile='{a}/bin/{b}/sentindex.txt'.format(a=home,b=1)
    wordindexfile='{a}/bin/{b}/wordindex.txt'.format(a=home,b=1)
    indexdict={}
    wordindex = open(wordindexfile,'rt')
    for i in wordindex:
        i = i.split()
        if i[0] in list(indexdict.keys()):
            indexdict[i[0]] = indexdict[i[0]] + ',' + i[1]
        else:
            indexdict[i[0]] = i[1] 
    wordindex.close()
    major=open(majord,'rt')
    outmajor=open(outmajord,'wt')
    for i in major:
        outmajor.write((i[:-1]) + ' ' + indexdict[i[:-1]])
        outmajor.write('\n')
    major.close()
    outmajor.close()
    plural=open(plurald,'rt')
    outplural=open(outplurald,'wt')
    for i in plural:
        outplural.write((i[:-1]) + ' ' + indexdict[i[:-1]])
        outplural.write('\n')
    plural.close()
    outplural.close()
    minor=open(minord,'rt')
    outminor=open(outminord,'wt')
    for i in minor:
        outminor.write((i[:-1]) + ' ' + indexdict[i[:-1]])
        outminor.write('\n')
    minor.close()
    outminor.close()
    
##use indexes to produce worksheets

### select 10 words, index. this minor function is seperate to conserve memory

#throne 240     
#guests 238     
#rode 405       
#meant 318      
#yourselves 93  
#horses 283     
#oath 42        
#imp 204        
#royal 309      
#leave 295      
    
def selectwords():
    #level = input('plural OR minor OR major: ')
    level = 'minor'
    germanedictfile = '{a}/bin/{b}/out{c}dict.txt'.format(a=home,b=1,c=level) 
    outputsheetfile = '{a}/bin/{b}/rawsheet.txt'.format(a=home,b=1)
    chosendict={}
    chosen=[]
    choices=[]
    germanedicttxt=open(germanedictfile,'rt')
    for i in germanedicttxt:
        i=i.split()
        i[1]=i[1].split(',')
        choices.append(i)
    germanedicttxt.close()
    while len(chosen) <=9:
        choice= random.choice(choices)
        if choice in chosen:
            print (choice)
        else:
            chosen.append(choice)
    for i in chosen:
        print (i)
        chosendict[i[0]]=(int(random.choice(i[1])))
        print (chosendict[i[0]])
    print (chosendict)
    outputsheet=open(outputsheetfile,'wt')
    for i in chosendict:
        outputsheet.write(i)
        outputsheet.write(' ')
        if chosendict[i]<=9:
            outputsheet.write('000'+str(chosendict[i]))
        elif chosendict[i]<=99:
            outputsheet.write('00'+str(chosendict[i]))
        elif chosendict[i]<=999:
            outputsheet.write('0'+str(chosendict[i]))
        else:
            outputsheet.write(str(chosendict[i]))
        outputsheet.write('\n')
    outputsheet.close()

###use chosenwords to make worksheet

def makeworksheet():
    inputsheetfile = '{a}/bin/{b}/rawsheet.txt'.format(a=home,b=1)
    outputsheetfile = '{a}/out/sheet.txt'.format(a=home)
    sentindexfile='{a}/bin/{b}/sentindex.txt'.format(a=home,b=1)
    sentdict={}
    inputlist=[]
    sentindex=open(sentindexfile,'rt')
    for i in sentindex:
        i = i.split(' ',1)
        sentdict[i[0]]=i[1]
    sentindex.close()
    inputsheet=open(inputsheetfile,'rt')
    for i in inputsheet:
        inputlist.append(i.split())
    inputsheet.close()
    outputsheet=open(outputsheetfile,'wt')
    for i in inputlist:
        print (i[1])
        if int(i[1])<=1:
            outputsheet.write(sentdict[i[1]])
            outputsheet.write('\n')
        elif int(i[1])<=8:
            outputsheet.write(sentdict['000'+str((int(i[1]))-1)])
            outputsheet.write(sentdict[i[1]])
            outputsheet.write(sentdict['000'+str((int(i[1]))+1)])
            outputsheet.write('\n')
        elif int(i[1])<=10:
            outputsheet.write(sentdict[i[1]])
            outputsheet.write(sentdict['00'+str((int(i[1]))+1)])
            outputsheet.write('\n')
        elif int(i[1])<=98:
            outputsheet.write(sentdict['00'+str((int(i[1]))-1)])
            outputsheet.write(sentdict[i[1]])
            outputsheet.write(sentdict['00'+str((int(i[1]))+1)])
            outputsheet.write('\n')
        elif int(i[1])<=100:
            outputsheet.write(sentdict[i[1]])
            outputsheet.write(sentdict['0'+str((int(i[1]))+1)])
            outputsheet.write('\n')
        elif int(i[1])<=998:
            outputsheet.write(sentdict['0'+str((int(i[1]))-1)])
            outputsheet.write(sentdict[i[1]])
            outputsheet.write(sentdict['0'+str((int(i[1]))+1)])
            outputsheet.write('\n')
        else:
            outputsheet.write(sentdict[i[1]])            
    for i in inputlist:
        outputsheet.write(i[0])
        outputsheet.write('          ')
    outputsheet.close()