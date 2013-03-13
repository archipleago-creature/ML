#SpamFilter

import Learner, TrainingSet, regressionLearner, NaiveBayesClassifier, FreqTextDict, BayesFeatureVector
import numpy as np
import ClassifierTrainingSet as cts
import glob, os
def main():
    #create a dictionary of words
    dic=FreqTextDict.FreqTextDict()
    dic.populate_from_dirs(['nonspam-train', 'spam-train'])
    dic.trim_to_size(2000)
   
    print len(dic.dic)
    #get training set from data files
    spam=[]
    nonspam=[]    
   #build a classifier
    print 'getting nonspam training data' 
    for f in glob.glob(os.path.join('nonspam-train', '*.txt')):
        v=BayesFeatureVector.BayesFeatureVector()
        v.get_features_from_file(dic, f)
        nonspam.append(v)
        print '.....................................................'
    print 'getting spam training data'
    for f in glob.glob(os.path.join('spam-train', '*.txt')):
        v=BayesFeatureVector.BayesFeatureVector()
        v.get_features_from_file(dic, f)
        spam.append(v)
        print '.......................................................'

    print 'got training data' 
    pairs=[]
    for s in spam:
        pairs.append((s,1))
    for n in nonspam:
        pairs.append((n,0))
    #for t in pairs:
    #    print t
    print 'done adding to pairs'
    print 'constructing taining set' 
    #tr=cts.ClassifierTrainingSet(pairs, [1,0])
    print 'constructing a classifier'
    classifier=NaiveBayesClassifier.NaiveBayesClassifier([0,1], pairs)
    classifier.train()
    print 'getting test data'
    spamcount=0
    for f in glob.glob(os.path.join('spam-test', '*.txt')):
        
        v1=BayesFeatureVector.BayesFeatureVector()
        #print 'getting features for file', f
        v1.get_features_from_file(dic, f)
        #print 'got that feature vector'
        print classifier.classify(v1), 'blah spam'

    for f in glob.glob(os.path.join('nonspam-test', '*.txt')):
        v2=BayesFeatureVector.BayesFeatureVector()
        v2.get_features_from_file(dic, f)
        print classifier.classify(v2), 'blah nonspam'
   #make a prediction
if __name__ == "__main__":
    main()
