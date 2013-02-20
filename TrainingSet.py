#TrainingSet.py 
#Implements a class for training sets for machine learning


class TrainingSet:
    def __init__(self, examples, values):
        self.examples=examples
        self.values=values
        self.pairs=[(examples[i],values[i]) for i in examples ]
