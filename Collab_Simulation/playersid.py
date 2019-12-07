import pandas as pd
players = pd.read_csv("player_to_player.csv")
batcluster = pd.read_csv("../Clustering/bat_clusters.csv",header=None)
bowlcluster = pd.read_csv("../Clustering/bowl_clusters.csv",header=None)
dic_bat = {}
dic_bowl = {}
li_players=[]
for index,row in players.iterrows():
	li_players.append([row[0],row[1]])
li_clust=[]
for index,row in batcluster.iterrows():
	if row[0] not in dic_bat:
		dic_bat[row[0]]=index
for index,row in bowlcluster.iterrows():
	if row[0] not in dic_bowl:
		dic_bowl[row[0]]=index
print("batid,bowlid,batsman,bowler,0,1,2,3,4,6,out,batclustno,bowlclustno,balls")
for index,row in players.iterrows():
	print(dic_bat[row[0]],dic_bowl[row[1]],sep=",",end=",")
	for i in row:
		print(str(i),end=",")
	print()
