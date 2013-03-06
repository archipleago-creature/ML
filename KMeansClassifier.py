#KMeans.py
#This is a class which implmets the k-means algorithm for unsupervised classification
import numpy as np
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
        for i in range(0, self.number_of_classes):
            centroids.setdefault(i, np.random.random((1, self.dim)))
            self.clusters[i]=[]
        k=0
        while k<30:
            print self.data
            for s in self.clusters:
                self.clusters[s]=[]
            for i in self.data:
                p=self.get_nearest_centroid(centroids, i)
                self.clusters.setdefault(p, []).append(i)
                #for l in self.clusters:
                #    if (not l==p) and (i in self.clusters[l]):
                #        self.clusters[l].remove[i]
                           
            for m in centroids:
               centroids[m] = self.barycenter(centroids, self.clusters, m)
            k+=1
        return self.clusters 
    def barycenter(self,centroids, clusters, cclass):
        sums=np.zeros(self.dim)
        for i in clusters[cclass]:
            print 'in barycenter', sums, i
            sums += i[0]
        return sums/len(clusters[cclass])
        
    def get_nearest_centroid(self, centroids, vector):
        #print centroids[0], vector
        print centroids.values()
        #sort=sorted(centroids, key=lambda x: self.norm((centroids[x][0]-vector)))
        temp=0
        d=self.norm(centroids[0][0]-vector)
        for m in centroids:
            print 'norms', (self.norm(centroids[m][0] -vector))
            if  self.norm((centroids[m][0] -vector)) < d:
                d=self.norm(centroids[m][0]-vector)
                temp=m
              
        
        
        return temp
    def norm(self, vec):
        n=0
        for i in range(0, len(vec)):
            print 'vecs', vec[i]
            n+=vec[0,i]*vec[0,i]
        return np.sqrt(n)
   
        
def main():

    blues=[]
    reds=[]

    for i in range(0,50):
        v=np.random.random((1,2))+0.5
        w=np.random.random((1,2)) +0.75
        z=np.random.random((1,2))+1
        blues.append(v)
        reds.append(w)
        reds.append(z)
    #print reds + blues
    classify=KMeansClassifier(blues +reds, 3, 2)
    dic=classify.classify()
    print 'class 0', dic[0]
    print 'class 1', dic[1]
    print 'class 2', dic[2]

    matplotlib.rcParams['axes.unicode_minus'] = False
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for q in dic[0]:
        print q[0]
        ax.plot(q[0][0],q[0][1], 'o', color='red')
    for h in dic[1]:
        ax.plot(h[0][0],h[0][1], 'o', color='blue')
    for t in dic[2]:
        ax.plot(t[0][0],t[0][1], 'o', color='green')
    ax.set_title('classes')
    plt.show()

if __name__ == "__main__":
    main()
