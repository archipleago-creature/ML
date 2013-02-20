#NaiveBayesClassifier.py
#This is a class for a naive Bayes classifier.
import TrainingSet as ts

class NaiveBayesClassifier:
    def __init__(self, classes=[], training_data=None, data=None):
        self.training_data=training_data
        self.data=data
        self.classes=[]

    def train(self, training_set=None):

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
        
        for k in classes:
            prod1=1
            for xi in example:
                prod1*=self_likelihood_feature_given_y(xi, k)
            s+=prod1*self.class_liklihood(k)        
        return s

    def max_lik_class_given_example(self, example, class):
        num=1
        for xi in example:
            num*=self.max_likelihood_feature_given_y(xi, class)
        return num*self.class_likelihood(class)/self.lik_example(example)
    
    def class_likelihood(self,class):
        return self.training_data.values.count(class)/len(self.training_data.values)
    def max_likelihood_feature_given_y(self,feature , class):
        num=0
        den=0
        for item in self.training_data.pairs:
            if item[1]==class:
                den+=1
                if item[0][feature]==1:
                    num +=1    
        return num/den
