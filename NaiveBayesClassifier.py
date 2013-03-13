#NaiveBayesClassifier.py
#This is a class for a naive Bayes classifier.
import decimal as dc

class NaiveBayesClassifier:
    def __init__(self, classes=[], vector_class_pairs=None, data=None):
        self.vector_class_pairs=vector_class_pairs
        self.data=data
        self.classes=classes
        self.features=[l for l in range(0, len(vector_class_pairs[0][0].features)-1)]
        self.class_prob={}
        self.feature_probs={}
        self.class_counts={}
        self.trained=False
    
    def get_class_prob(self):
        for k in classes:
            self.class_prob[k]=self.class_likelihood(k)
            
    
    def train(self, training_set=None):
        self.get_class_counts()
        #print 'class counts', self.class_counts
        for k in self.classes:
            self.class_prob[k]=self.class_likelihood(k)
        #print 'class probabilities', self.class_prob
        ###get feature priors
        for f in self.features:
            for k in self.classes:       
                if not self.feature_probs.has_key((f,k)):
                    #print 'setting feature prob', f, k ,'.'
                    self.feature_probs.setdefault((f,k),[]).append(self.likelihood_feature_given_class(f,k)) 
        #print self.feature_probs
        self.train=True
        return None
    def classify(self, feature_vector):
        max1=0.0
        max_class=self.classes[0]
        for y in self.classes:
            temp=self.max_lik_class_given_example(feature_vector, y)
            #print 'a check in classify method', feature_vector.sparse_vec, temp
            if temp > max1:
                max1=temp
                max_class=y
        return (max_class, max1)
    
    def lik_example(self, feature_vector):
        #s=1.0
        #prod1=1.0
        s=dc.Decimal(0.0)
        for k in self.classes:
            prod1=dc.Decimal(1.0)
            for xi in feature_vector.sparse_vec:#range(0, len(feature_vector)):
            #    print 'checking prob of feature', xi
                if self.feature_probs.has_key((xi,k)):
           #         print 'had feature', xi 
                    temp=dc.Decimal(self.feature_probs[(xi,k)][0])
          #          print 'with prob', temp, 'for class', k
                    
                    prod1 *= temp
         #           print prod1
            s+=prod1*dc.Decimal(self.class_prob[k])
        #print 'crux' , s
        return s

    def max_lik_class_given_example(self, feature_vector, class1):
        num=dc.Decimal(1.0000)
        c=self.lik_example(feature_vector)
        #if c<.00000000000000000001:
        #    print feature_vector.sparse_vec
        #    for xi in feature_vector.sparse_vec:
        #        print 'liklihood of ', xi,  self.feature_probs[(xi, class1)]  
        for xi in feature_vector.sparse_vec: #range(0,len(feature_vector)):
            if self.feature_probs.has_key((xi, class1)) and not self.feature_probs[(xi, class1)][0]==0:
                
                num*=dc.Decimal(self.feature_probs[(xi, class1)][0])
                #print 'probability of feature' , xi, 'in class', class1, ':' ,self.feature_probs[(xi, class1)]
                #c=self.lik_example(feature_vector)
        
        
        if not c==0:
            #print 100000.00*num*self.class_likelihood(class1)/(c*100000.00)
            #print 'in this class we will have', num, '*', self.class_prob[class1], 'over', c, 'without Laplace smoothing'
            return (num*dc.Decimal(self.class_prob[class1]))/(c)
        else:
        #    print 'sumfin went rong heya' 
            return 0
    def get_class_counts(self):
        for k in self.classes:
            count=0
            for (v,c) in self.vector_class_pairs:
                if k==c:
                    count+=1 
             
            self.class_counts.setdefault(k, []).append(count)
    def class_likelihood(self,class1):
        return 1000.00*self.class_counts[class1][0]/(1000.00*len(self.vector_class_pairs))
       
    def likelihood_feature_given_class(self, feature, qclass):
        count=0
        for (v,p) in self.vector_class_pairs: 
            if p==qclass:
                if v.sparse_vec.has_key(feature):
                    count+=1     
        return dc.Decimal(count)/dc.Decimal(self.class_counts[qclass][0])
