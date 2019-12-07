#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
The K-means algorithm written from scratch against PySpark. In practice,
one may prefer to use the KMeans algorithm in ML, as shown in
examples/src/main/python/ml/kmeans_example.py.
This example requires NumPy (http://www.numpy.org/).
"""
from __future__ import print_function

import sys

import numpy as np
from pyspark.sql import SparkSession
import pandas as pd

def toFloat(string,newrow):
    try:
        newrow.append(float(string))
        #return True
    except ValueError:
        #return False
        newrow.append(string)


def parseVector(line):
    #return np.array([float(x) for x in line.split(',')])
    row=line.split(',')
    if(row[0]=="Player"):
        return np.array(row)
    newrow=[]
    for x in row:
        toFloat(x,newrow)
    #print(newrow)
    return newrow
	
    

def closestPoint(p, centers):
    bestIndex = 0
    closest = float("+inf")
    for i in range(len(centers)):
        tempDist = np.sum((p - centers[i]) ** 2)
        if tempDist < closest:
            closest = tempDist
            bestIndex = i
    return bestIndex

def isequal(row,header):
    flag=True
    for i in range(len(row)):  
        if(row[i]!=header[i]):
            flag=False
    return flag

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: bin/spark-submit <file> <k> <convergeDist> <batsmen or bowlers>", file=sys.stderr)
        sys.exit(-1)

    '''print("""WARN: This is a naive implementation of KMeans Clustering and is given
       as an example! Please refer to examples/src/main/python/ml/kmeans_example.py for an
       example on how to use ML's KMeans implementation.""", file=sys.stderr)'''

    spark = SparkSession\
        .builder\
        .appName("PythonKMeans")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])
    data = lines.map(parseVector).cache()
    header = data.first()
    data_name = data.filter(lambda row:isequal(row,header)==False)
    #for i in data.collect():
        #print(i[0],i[5],i[7],i[9])
    if(sys.argv[4]=="batsmen"):
        #print(data.first()[2])
        data = data_name.map(lambda line:np.array([line[2],line[3],line[4]]))
    elif(sys.argv[4]=="bowlers"):
        data = data_name.map(lambda line:np.array([line[6],line[7],line[8]]))
    #data = spark.read.format("CSV").option("header","true").load(csvfile
    K = int(sys.argv[2])
    convergeDist = float(sys.argv[3])

    kPoints = data.takeSample(False, K, 1)
    tempDist = 1.0

    while tempDist > convergeDist:
        
        closest = data.map(
            lambda p: (closestPoint(p, kPoints), (p, 1)))
        pointStats = closest.reduceByKey(
            lambda p1_c1, p2_c2: (p1_c1[0] + p2_c2[0], p1_c1[1] + p2_c2[1]))
        newPoints = pointStats.map(
            lambda st: (st[0], st[1][0] / st[1][1])).collect()

        tempDist = sum(np.sum((kPoints[iK] - p) ** 2) for (iK, p) in newPoints)

        for (iK, p) in newPoints:
            #print((iK,p))
            kPoints[iK] = p
    clusters = []
    for i in closest.collect():
        clusters.append(i[0])
    names = []
    for i in data_name.collect():
        names.append(i[1])
    for i in range(len(clusters)):
        print(names[i],clusters[i],sep=",")
    #print("Final centers: " + str(kPoints))
    spark.stop()
