#regressionLearner.py
#implements linear and logistic regression learners
import TrainingSet
import Learner
import numpy as np
import math 
import copy
class regressionLearner(Learner.Learner):
    def __init__(self,training_set=None, method=None):
        Learner.Learner.__init__(self, training_set, method)
        self.theta=None

    def linear_regression(self):
        alpha=0.01
        m=len(self.training_set.examples)
        test_points=copy.copy(self.training_set.examples)
        test_values=copy.copy(self.training_set.values)
        test_points=[np.matrix(np.fromstring(x, sep=',')) for x in test_points]
        test_values=[np.matrix(np.fromstring(y, sep=',')) for y in test_values]
        
        theta=np.copy(test_points[0])
        theta.fill(0)
        
    def linear_hypothesis(self,x, theta):
        return theta*x.T
    ###TO DO weighted linear regression, softmax, preceptron
    def log_hypothesis(self, x, theta):
        return 1/(np.exp(-1*(theta*x.T)))
    def diffJ_log(self,m, theta,test_points, test_values):
        sum=0
        
        for i in(1, len(test_points)-1):
            #print i
            sum += ( -1.0*self.log_hypothesis(test_points[i], theta) + test_values[i])* test_points[i]
          
        return sum
  
    def diffJ(self,m,theta,test_points, test_values):
        sum=0
        for i in(1, len(test_points)-1):
            #print i
            sum += ( self.linear_hypothesis(test_points[i], theta) - test_values[i])* test_points[i]
          
        return sum

    def stoch_descent(self):
        alpha=0.01
        tolerance=0.0001
        m=len(self.training_set.examples)
        test_points=copy.copy(self.training_set.examples)
        test_values=copy.copy(self.training_set.values)
        theta=np.copy(test_points[0])
        theta.fill(0)
        
        error=100
        counttest=0
        while error>tolerance:
            print theta
            counttest+=1
            temp=theta
            theta=theta + alpha*self.diffJ_log(m,theta, test_points, test_values)
            print str(theta)
            error=np.linalg.norm(theta-temp)
        print counttest                 
        return str(theta)
    

    def gradient_descent(self):
        alpha=0.01
        tolerance=0.0001
        m=len(self.training_set.examples)
        test_points=copy.copy(self.training_set.examples)
        test_values=copy.copy(self.training_set.values)
        theta=np.copy(test_points[0])
        theta.fill(0)
        
        error=100
        counttest=0
        while error>tolerance:
            print theta
            counttest+=1
            temp=theta
            theta=theta-alpha*self.diffJ(m,theta, test_points, test_values)
            print str(theta)
            error=np.linalg.norm(theta-temp)
        print counttest                 
        return str(theta)
    
