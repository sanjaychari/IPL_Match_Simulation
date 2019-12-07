from __future__ import print_function

from pyspark import SparkContext

# $example on$
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
# $example off$
def isint(par):
   try:
       a=int(par)
   except:
       return False
   return True

def isequal(row,header):
    if(isint(row[0])):
        return False
    return True

if __name__ == "__main__":
    sc = SparkContext(appName="PythonCollaborativeFilteringExample")
    # $example on$
    # Load and parse the data
    data = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/playersid.csv")
    header = data.first()
    data = data.filter(lambda row:isequal(row,header)==False)
    ratings = data.map(lambda l: l.split(','))\
        .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[4])))
    rank = 10
    numIterations = 10
    model = ALS.train(ratings, rank, numIterations)

    # Evaluate the model on training data
    testdata = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/missing.csv")
    #testdata = ratings.map(lambda p: (p[0], p[1]))
    testdata = testdata.map(lambda l: l.split(','))\
        .map(lambda l: (int(l[0]), int(l[1])))
    predictions0 = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    #for (link,rank) in predictions.collect():
        #print("%s,%s,%s" % (link[0],link[1],rank))
    #MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
    #print("Mean Squared Error = " + str(MSE))
    data = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/playersid.csv")
    header = data.first()
    data = data.filter(lambda row:isequal(row,header)==False)
    ratings = data.map(lambda l: l.split(','))\
        .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[5])))
    rank = 10
    numIterations = 10
    model = ALS.train(ratings, rank, numIterations)

    # Evaluate the model on training data
    testdata = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/missing.csv")
    #testdata = ratings.map(lambda p: (p[0], p[1]))
    testdata = testdata.map(lambda l: l.split(','))\
        .map(lambda l: (int(l[0]), int(l[1])))
    predictions1 = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    data = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/playersid.csv")
    header = data.first()
    data = data.filter(lambda row:isequal(row,header)==False)
    ratings = data.map(lambda l: l.split(','))\
        .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[6])))
    rank = 10
    numIterations = 10
    model = ALS.train(ratings, rank, numIterations)

    # Evaluate the model on training data
    testdata = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/missing.csv")
    #testdata = ratings.map(lambda p: (p[0], p[1]))
    testdata = testdata.map(lambda l: l.split(','))\
        .map(lambda l: (int(l[0]), int(l[1])))
    predictions2 = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))

    data = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/playersid.csv")
    header = data.first()
    data = data.filter(lambda row:isequal(row,header)==False)
    ratings = data.map(lambda l: l.split(','))\
        .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[7])))
    rank = 10
    numIterations = 10
    model = ALS.train(ratings, rank, numIterations)

    # Evaluate the model on training data
    testdata = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/missing.csv")
    #testdata = ratings.map(lambda p: (p[0], p[1]))
    testdata = testdata.map(lambda l: l.split(','))\
        .map(lambda l: (int(l[0]), int(l[1])))
    predictions3 = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))

    data = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/playersid.csv")
    header = data.first()
    data = data.filter(lambda row:isequal(row,header)==False)
    ratings = data.map(lambda l: l.split(','))\
        .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[8])))
    rank = 10
    numIterations = 10
    model = ALS.train(ratings, rank, numIterations)

    # Evaluate the model on training data
    testdata = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/missing.csv")
    #testdata = ratings.map(lambda p: (p[0], p[1]))
    testdata = testdata.map(lambda l: l.split(','))\
        .map(lambda l: (int(l[0]), int(l[1])))
    predictions4 = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))

    data = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/playersid.csv")
    header = data.first()
    data = data.filter(lambda row:isequal(row,header)==False)
    ratings = data.map(lambda l: l.split(','))\
        .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[9])))
    rank = 10
    numIterations = 10
    model = ALS.train(ratings, rank, numIterations)

    # Evaluate the model on training data
    testdata = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/missing.csv")
    #testdata = ratings.map(lambda p: (p[0], p[1]))
    testdata = testdata.map(lambda l: l.split(','))\
        .map(lambda l: (int(l[0]), int(l[1])))
    predictions6 = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))

    data = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/playersid.csv")
    header = data.first()
    data = data.filter(lambda row:isequal(row,header)==False)
    ratings = data.map(lambda l: l.split(','))\
        .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[10])))
    rank = 10
    numIterations = 10
    model = ALS.train(ratings, rank, numIterations)

    # Evaluate the model on training data
    testdata = sc.textFile("/home/jnanesh/Main_Project/Collab_Simulation/missing.csv")
    #testdata = ratings.map(lambda p: (p[0], p[1]))
    testdata = testdata.map(lambda l: l.split(','))\
        .map(lambda l: (int(l[0]), int(l[1])))
    predictionsout = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    dic_stats={}
    for (link,rank) in predictions0.collect():
        if (link[0],link[1]) not in dic_stats:
            dic_stats[(link[0],link[1])]=[]
        dic_stats[(link[0],link[1])].append(rank)
    for (link,rank) in predictions1.collect():
        if (link[0],link[1]) not in dic_stats:
            dic_stats[(link[0],link[1])]=[]
        dic_stats[(link[0],link[1])].append(rank)
    for (link,rank) in predictions2.collect():
        if (link[0],link[1]) not in dic_stats:
            dic_stats[(link[0],link[1])]=[]
        dic_stats[(link[0],link[1])].append(rank)
    for (link,rank) in predictions3.collect():
        if (link[0],link[1]) not in dic_stats:
            dic_stats[(link[0],link[1])]=[]
        dic_stats[(link[0],link[1])].append(rank)
    for (link,rank) in predictions4.collect():
        if (link[0],link[1]) not in dic_stats:
            dic_stats[(link[0],link[1])]=[]
        dic_stats[(link[0],link[1])].append(rank)
    for (link,rank) in predictions6.collect():
        if (link[0],link[1]) not in dic_stats:
            dic_stats[(link[0],link[1])]=[]
        dic_stats[(link[0],link[1])].append(rank)
    for (link,rank) in predictionsout.collect():
        if (link[0],link[1]) not in dic_stats:
            dic_stats[(link[0],link[1])]=[]
        dic_stats[(link[0],link[1])].append(rank)
    for i in dic_stats:
        print(str(i[0])+","+str(i[1])+","+str(dic_stats[i][0])+","+str(dic_stats[i][1])+","+str(dic_stats[i][2])+","+str(dic_stats[i][3])+","+str(dic_stats[i][4])+","+str(dic_stats[i][5])+","+str(dic_stats[i][6]))
    # Save and load model
    #model.save(sc, "/home/jnanesh/Main_Project/Collab_Simulation/myCollaborativeFilter")
    #sameModel = MatrixFactorizationModel.load(sc, "/home/jnanesh/Main_Project/Collab_Simulation/myCollaborativeFilter")
