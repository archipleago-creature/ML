#FreqTextDict.py
#This is a dictionary which takes a list of strings and creates a libray with frequencies
import string
class FreqTextDict:
    def __init__(): 
        dic={}

    def populate(self,text_file):
        text=split(open(text_file).read(), ' ')
        for t in text:
            if dic.has_key(t):
                dic[t]=int(dic[t])+1
            else:
                dic[t]=1
