#KMeans.py
#This is a class which implmets the k-means algorithm for unsupervised classification
import numpy as np
class KMeansClassifier:
    def __init__(self, data, number_of_classes=2, dim=2):
        self.data=data
        self.number_of_classes=number_of_classes
        self.dim=dim
        self.clusters={}
    def classify(self):
        #Initialize cluster centroids these are numpy vectors with random entries in a range
        centroids={}
        for i in range(0, self.number_of_classes):
            centroids.setdefault(i, np.random.random((1, self.dim)))
            self.clusters[i]=None
        k=0
        while k<50:
            print self.data
            for i in self.data:
                self.clusters[self.get_nearest_centroid(centroids, i)]=i   
            for m in centroids:
               centroids[m] = barycenter(centroids, clusters, m)
            k+=1
        return clusters 
    def barycenter(centroids, clusters, cclass):
        sums=np.zeroes(len(centroids[cclass][0]))
        for i in clusters[cclass]:
            sums += i
        return sums/len(clusters[cclass])
        
    def get_nearest_centroid(self, centroids, vector):
        #print centroids[0], vector
        print centroids.values()
        #sort=sorted(centroids, key=lambda x: self.norm((centroids[x][0]-vector)))
        temp=0
        d=self.norm(centroids[0]-vector)
        for m in centroids:
            if (self.norm(centroids[m][0] -vector)<d ):
                d=self.norm(centroids[m][0]-vector)
                temp=m
              
        
        
        return temp
    def norm(self, vec):
        n=0
        for v in vec:
            n+=v*v
        return np.sqrt(n)
   
        
def main():

    blues=[]
    reds=[]

    for i in range(0,100):
        v=np.random.random((1,2))
        w=np.random.random((1,2)) +10
        blues.append(v)
        reds.append(w)
    #print reds + blues
    classify=KMeansClassifier(blues +reds, 2, 2)
    dic=classify.classify()
    print dic

if __name__ == "__main__":
    main()
