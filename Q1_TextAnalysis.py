#import libraries
from nltk.probability import FreqDist
from nltk.collocations import *
from nltk.tokenize import RegexpTokenizer
import re

#store paragraph to a variable
text1 = "As a term, data analytics predominantly refers to an assortment of " \
        "applications, from basic business intelligence (BI), reporting and " \
        "online analytical processing (OLAP) to various forms of advanced " \
        "analytics. In that sense, it's similar in nature to business " \
        "analytics, another umbrella term for approaches to analyzing data -- " \
        "with the difference that the latter is oriented to business uses, " \
        "while data analytics has a broader focus. The expansive view of the " \
        "term isn't universal, though: In some cases, people use data analytics " \
        "specifically to mean advanced analytics, treating BI as a separate " \
        "category. Data analytics initiatives can help businesses increase " \
        "revenues, improve operational efficiency, optimize marketing campaigns " \
        "and customer service efforts, respond more quickly to emerging market " \
        "trends and gain a competitive edge over rivals -- all with the " \
        "ultimate goal of boosting business performance. Depending on the " \
        "particular application, the data that's analyzed can consist of either " \
        "historical records or new information that has been processed for " \
        "real-time analytics uses. In addition, it can come from a mix of " \
        "internal systems and external data sources. At a high level, data " \
        "analytics methodologies include exploratory data analysis (EDA), which " \
        "aims to find patterns and relationships in data, and confirmatory data " \
        "analysis (CDA), which applies statistical techniques to determine " \
        "whether hypotheses about a data set are true or false. EDA is often " \
        "compared to detective work, while CDA is akin to the work of a judge " \
        "or jury during a court trial -- a distinction first drawn by " \
        "statistician John W. Tukey in his 1977 book Exploratory Data Analysis. " \
        "Data analytics can also be separated into quantitative data analysis " \
        "and qualitative data analysis. The former involves analysis of " \
        "numerical data with quantifiable variables that can be compared or " \
        "measured statistically. The qualitative approach is more interpretive " \
        "-- it focuses on understanding the content of non-numerical data like " \
        "text, images, audio and video, including common phrases, themes and " \
        "points of view."

#declare parameter used to split paragraph to lines
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"
tokenizer = RegexpTokenizer(r'[\w\']+')

#function to split paragraph to lines
def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

#Answer to Question ii.a
#declare a counter for number of line
count = 1
#split the paragraph to sentences
sentences = split_into_sentences(text1)
#tokenize words for each line
for s in sentences:
    lines = tokenizer.tokenize(s)
    #print(lines)
    #print word distribution
    fdist2 = FreqDist(lines)
    print("Probability of word [data] occuring in line " + str(count) + " is " + str((fdist2.freq('data') + fdist2.freq('Data'))))
    #increment to next line number
    count += 1

print("\n")

#Answer to Question ii.b
text2 = tokenizer.tokenize(text1.lower())
fdist3 = FreqDist(text2)
#print(fdist3)
print("The distribution of distinct word counts across the lines is as follows:")
for sample in fdist3:
    print(sample + " " + str(fdist3[sample]))

print("\n")

#Answer to Question ii.c
#declare variable to store counts of data bigram and data analytics
c = 0
d = 0
#function to generate bigram distribution
finder = BigramCollocationFinder.from_words(text1.lower().split())
for x,y in finder.ngram_fd.items():
    #data as the first word
    if "data" in x[0]:
        #analytics as the second word
        if "analytics" in x[1]:
            d = d+y
        #any other second word beside analytics
        else:
            #print(x,y)
            c = c+y

print("The probability of the word [analytics] occuring after the word [data] is: " + str(d/(d+c)))
