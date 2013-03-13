##FeatureVector.py
#base class for feature vectors

class FeatureVector:

    def __init__(self, data=None):
        self.data=data    
        self.sparse_vec={}
