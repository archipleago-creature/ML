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
                if 1:#not self.feature_probs.has_key((f,k)):
                    #print 'setting feature prob', f, k ,'.'
                    temp=self.likelihood_feature_given_class(f,k)
                    if not temp==dc.Decimal(0.0):
                        self.feature_probs.setdefault((f,k),[]).append(temp) 
        print 'for debugging we show everything we got under the training time.'
        #print 'features',self.features
        print 'classes', self.classes
        print 'class probabilities', self.class_prob
        #print 'feature_probs', self.feature_probs
        print 'class counts', self.class_counts 
        #print self.feature_probs
        self.train=True
        return None

    def classify(self, feature_vector):
        max1=self.log_lik_example_cond_class(feature_vector,self.classes[0]) +dc.Decimal(self.class_prob[0]).ln()
        max_class=self.classes[0]
        for y in self.classes:
            #    
            #temp=self.max_lik_class_given_example(feature_vector, y)
            temp=self.log_lik_example_cond_class(feature_vector, y) +dc.Decimal(self.class_prob[y]).ln()
            if temp > max1:
                max1=temp
                max_class=y
        return (max_class, max1.exp())
    def log_lik_example_cond_class(self, feature_vector, qclass):
        #prod=dc.Decimal(1.0)
        prod=dc.Decimal(0.0)
        for xi in feature_vector.sparse_vec:
            if self.feature_probs.has_key((xi, qclass)):
                prod+=dc.Decimal(self.feature_probs[(xi, qclass)][0]).ln()
        return prod         
    def lik_example(self, feature_vector):
 
        s=dc.Decimal(0.0)
        for k in self.classes:
            prod1=dc.Decimal(1.0)
            for xi in feature_vector.sparse_vec:
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
        for xi in feature_vector.sparse_vec:
            if self.feature_probs.has_key((xi, class1)) :
                num*=dc.Decimal(self.feature_probs[(xi, class1)][0])
        if not c==0:
            return (num*dc.Decimal(self.class_prob[class1]))/(dc.Decimal(c))
        else:
            return 0

    def get_class_counts(self):
        for k in self.classes:
            count=0
            for (v,c) in self.vector_class_pairs:
                if k==c:
                    count+=1 
             
            self.class_counts.setdefault(k, []).append(count)

    def class_likelihood(self,class1):
        return dc.Decimal(self.class_counts[class1][0])/dc.Decimal(len(self.vector_class_pairs))
       
    def likelihood_feature_given_class(self, feature, qclass):
        count=0
        for (v,p) in self.vector_class_pairs: 
            if p==qclass:
                if v.sparse_vec.has_key(feature):
                    count+=1     
        return dc.Decimal(count)/dc.Decimal(self.class_counts[qclass][0])
