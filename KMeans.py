#KMeans.py
#This is a class which implmets the k-means algorithm for unsupervised classification
import numpy as np
class KMeansClassifier:
    def __init__(self, data, number_of_classes=2):
        self.data=data
        self.number_of_classes=number_of_classes
        self.clusters={}
    def classify(self):
        #Initialize cluster centroids these are numpy vectors with random entries in a range
        centroids={}
        for i in range(0, number_of_classes):
            centroids[i]=np.random.random((1, len(data[0])))
            self.clusters[i]=None
        while k<50:
            
            for i in data:
                self.clusters[get_nearest_centroid(centroids, i)]=i   
            for m in centroids:
               centroids[m] = barycenter(centroids, clusters, m)
            k+=1
        return clusters 
    def barycenter(centroids, clusters, cclass):
        sums=np.zeroes(len(centroids[cclass][0]))
        for i in clusters[cclass]:
            sums += i
        return sums/len(clusters[cclass])
        
    def get_nearest_centroid(centroids, vector):
        
        
        sort=sorted(centroids, key=lambda x: np.sqrt(np.dot((x-vector), (x-vector))) )
        return sort.keys()[0]
        
        
