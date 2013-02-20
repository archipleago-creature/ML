#MLproblem 1 

import Learner, TrainingSet, regressionLearner
import numpy as np

def main():

    learner=regressionLearner.regressionLearner()
    learner.get_data('q1x.dat', 'q1y.dat')
    print learner.gradient_descent()
    print learner.stoch_descent()
if __name__ == "__main__":
    main()
