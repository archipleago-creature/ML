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
        for k in textin:
            
            if k in ord_dic:
                features[ord_dic.index(k)]=1
            n+=1 
            #print 'getting features from file', n
        self.features=features
        for f in range(0, len(features)):
            if features[f]==1:
                self.sparse_vec[f]=1 
    
