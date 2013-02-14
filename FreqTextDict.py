#FreqTextDict.py
#This is a dictionary which takes a list of strings and creates a libray with frequencies
import string as st
import os
import glob
class FreqTextDict:
    def __init__(self, size_limit=25000): 
        self.dic={}
        self.size_limit=size_limit
    def populate_from_file(self,text_file):
        text=st.split(open(text_file).read(), ' ')
        for t in text:
            if self.dic.has_key(t):
                self.dic[t]=int(self.dic[t])+1
            else:
                self.dic[t]=1
         
    def populate_from_dir(self, path):
        for f in glob.glob(os.path.join(path, '*.txt')):
            self.populate_from_file(f)


    def trim_to_size(self, size):
        count=0
        trimmed={}
        temp=sorted(self.dic, key=lambda x :self.dic[x], reverse=True)
        for t in temp:
           if count < size:
               trimmed[t]=self.dic[t]
           else:
               break
           count+=1
        self.dic=trimmed       
