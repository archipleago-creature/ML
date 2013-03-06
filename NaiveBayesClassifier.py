#NaiveBayesClassifier.py
#This is a class for a naive Bayes classifier.
import TrainingSet as ts

class NaiveBayesClassifier:
    def __init__(self, classes=[], training_data=None, data=None):
        self.training_data=training_data
        self.data=data
        self.classes=classes

    def train(self, training_set=None):
        return None
    def classify(self, example):
        max1=0
        max_class=self.classes[0]
        for y in self.classes:
            temp=self.max_lik_class_given_example(example, y)
            if temp >= max1:
                max1=temp
                max_class=y
        return (max_class, max1)
    def lik_example(self, example):
        s=0
        prod1=1
        
        for k in self.classes:
            prod1=1
            for xi in example:
                temp=self.max_likelihood_feature_given_y(xi, k)
                if not temp==0:
                   prod1*=self.max_likelihood_feature_given_y(xi, k)
            s+=prod1*self.class_likelihood(k)        
        return s

    def max_lik_class_given_example(self, example, class1):
        num=1
        for xi in example:
            num*=self.max_likelihood_feature_given_y(xi, class1)
            c=self.lik_example(example)
        if not c==0:
            return num*self.class_likelihood(class1)/c
        else:
            return 0
    
    def class_likelihood(self,class1):
        return self.training_data.classes.count(class1)/len(self.training_data.classes)
    def max_likelihood_feature_given_y(self,feature , class1):
        num=0
        den=0
        count=0
        for item in self.training_data.pairs:
            if item[1]==class1:
                den+=1
                if item[0].data[feature]==1:
                    num +=1 
            count +=1
            print count   
        return num/den
