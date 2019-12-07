import numpy as np
import pandas as pd
import csv
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

filename = "BattingStats.csv"
df = pd.read_csv(filename) 
columns = ["Runs","Avg","SR"]
df = pd.DataFrame(df , columns=columns)
#print(df.to_numpy())


#Use silhouette score
range_n_clusters = list (range(2,11))
print ("Number of clusters from 2 to 10 for Batsmen: \n", range_n_clusters)

for n_clusters in range_n_clusters:
    clusterer = KMeans (n_clusters=n_clusters)
    preds = clusterer.fit_predict(df)
    centers = clusterer.cluster_centers_

    score = silhouette_score (df, preds, metric='euclidean')
    print ("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))

filename = "BowlingStats.csv"
df = pd.read_csv(filename) 
columns = ["Avg","Econ","SR"]
df = pd.DataFrame(df , columns=columns)
#print(df.to_numpy())


#Use silhouette score
range_n_clusters = list (range(2,11))
print ("Number of clusters from 2 to 10 for Bowlers: \n", range_n_clusters)

for n_clusters in range_n_clusters:
    clusterer = KMeans (n_clusters=n_clusters)
    preds = clusterer.fit_predict(df)
    centers = clusterer.cluster_centers_

    score = silhouette_score (df, preds, metric='euclidean')
    print ("For n_clusters = {}, silhouette score is {})".format(n_clusters, score))


