#BayesFeatureVector.py
#implements a feature vector for use in naive Bayes
import FeatureVector
import FreqTextDict
import numpy as np
import string as st
class BayesFeatureVector(FeatureVector.FeatureVector):


    def get_features_from_file(self,dic,txtfile):
        textin=st.split(open(txtfile).read(), " ")
        features=np.linspace(0,0, len(dic.dic))
        ord_dic=sorted(dic.dic, key=lambda x: dic.dic[x], reverse=True)
        n=0
        for k in ord_dic:
            
            if k in textin:
                features[n]=1
            n+=1 
            
        self.data=features
        
    
