#KMeans.py
#This is a class which implmets the k-means algorithm for unsupervised classification
import numpy as np
import copy
import matplotlib
import matplotlib.pyplot as plt
class KMeansClassifier:
    def __init__(self, data, number_of_classes=2, dim=2):
        self.data=data
        self.number_of_classes=number_of_classes
        self.dim=dim
        self.clusters={}
    def classify(self):
        #Initialize cluster centroids these are numpy vectors with random entries in a range
        centroids={}
        old_centroids={}
        for i in range(0, self.number_of_classes):
            centroids.setdefault(i, np.random.random((1, self.dim)))
            print centroids[i][0]
            self.clusters[i]=[]
        k=0
        
        error=100
        tol=0.0001
        while error>tol:
            
            for s in self.clusters:
                self.clusters[s]=[]
            for i in self.data:
                p=self.get_nearest_centroid(centroids, i)
                self.clusters.setdefault(p, []).append(i)
                                         
            for m in centroids:
               if old_centroids.has_key(m):
                   del(old_centroids[m])
               old_centroids.setdefault(m,[]).append(centroids[m][0])
               del(centroids[m])
               temp=self.barycenter(self.clusters, m)
               print temp[0], temp[1]
               if (not np.isnan(temp[0])) and (not np.isnan(temp[1])):
                   centroids.setdefault(m,[]).append(temp)
               else:
                   centroids.setdefault(m,[]).append(old_centroids[m][0])
               print 'centroids', centroids[m]
               print 'old centroids', old_centroids[m]
            error=self.getError(centroids, old_centroids)
            k+=1
            print error
            print '*'
        print k, 'iteration until convergence'
        return self.clusters 
    def getError(self,centroids, old_centroids):
        err=0
        for k in range(0, self.number_of_classes):
            err+=np.linalg.norm(centroids[k][0]-old_centroids[k][0])
            print err
        return err
    def barycenter(self, clusters, cclass):
        sums=np.zeros(self.dim)
        count=0
        for i in clusters[cclass]:
            sums += i[0]
            count +=1
        return sums/count
        
    def get_nearest_centroid(self, centroids, vector):
      
        temp=0
        d=np.linalg.norm(centroids[0][0]-vector)
        for m in centroids:
            val=np.linalg.norm(centroids[m][0] -vector)
           
            if  val < d:
                d=val
                temp=m
        return temp
    
    def norm(self, vec):
      return np.linalg.norm(vec)
   
        
def main():

    blues=[]
    reds=[]

    for i in range(0,1000):
        v=np.random.random((1,2))+0.5
        w=np.random.random((1,2)) +1.5
        z=np.random.random((1,2))+1
        blues.append(v)
        reds.append(w)
        reds.append(z)
    #print reds + blues
    classify=KMeansClassifier(blues +reds, 4, 2)
    dic=classify.classify()
    #print 'class 0', dic[0]
    #print 'class 1', dic[1]
    #print 'class 2', dic[2]

    matplotlib.rcParams['axes.unicode_minus'] = False
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for q in dic[0]:
        
        ax.plot(q[0][0],q[0][1], 'o')
    for h in dic[1]:
        ax.plot(h[0][0],h[0][1], 'x')
    for t in dic[2]:
        ax.plot(t[0][0],t[0][1], '+')
    for f in dic[3]:
        ax.plot(f[0][0], f[0][1], '^')
    ax.set_title('classes')
    plt.show()

if __name__ == "__main__":
    main()
