import clusters
# blognames,words,data=clusters.readfile('blogdata.txt')
# print blognames
# print words
# print data
# clust=clusters.hcluster(data)
# clusters.printclust(clust,labels=blognames)
# clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')

# word similary?  is useful??
# rdata = clusters.rotatematrix(data)
# print rdata
# clusters.drawdendrogram(clusters.hcluster(rdata),words,jpeg='wordclust.jpg')

# clusters_point,clusters = clusters.kcluster(data,k=4)
# for c in clusters:
# 	print c
# 	for r in c:
# 		print "\t"+blognames[r] 
# print "---------------------------------------------------------"
# for point in clusters_point:
# 	print point

# **********************************************************************************************************************
# tanimoto fit to has or not (1 or 0) case, pearson fit to has actual data, like words in blog, or score by user make.
# **********************************************************************************************************************

# wants,people,data=clusters.readfile('zebo.txt')
# clust=clusters.hcluster(data,distance=clusters.tanimoto)
# clusters.drawdendrogram(clust,wants)

# pearson is not fit for here because the data is 1 or 0
# clust=clusters.hcluster(data,distance=clusters.pearson)
# clusters.drawdendrogram(clust,wants,jpeg='clusters1.jpg')

# coords = clusters.scaledown(data)
# clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')


# avgs=[0.0]*10
# print avgs
import random
print random.random()