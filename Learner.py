#Learner.py
#Abstract class for various learners
import TrainingSet as TS
import numpy as np
class Learner:
    def __init__(self, training_set=None, method=None):
        self.training_set=training_set
        self.method=method
 
    def get_data(self,points, values):
        
        self.training_set=TS.TrainingSet(np.loadtxt(points), np.loadtxt(values))
        

        
