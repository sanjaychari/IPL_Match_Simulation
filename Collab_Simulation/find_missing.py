import pandas as pd
players = pd.read_csv("player_to_player.csv")
batcluster = pd.read_csv("../Clustering/bat_clusters.csv")
bowlcluster = pd.read_csv("../Clustering/bowl_clusters.csv")
li_players=[]
dic_bat = {}
dic_bowl = {}
for index,row in players.iterrows():
	li_players.append([row[0],row[1]])
li_clust=[]
for index,row in batcluster.iterrows():
	if row[0] not in dic_bat:
		dic_bat[row[0]]=index
	for index1,row1 in bowlcluster.iterrows():
		if row1[0] not in dic_bowl:
			dic_bowl[row1[0]]=index1
		li_clust.append([row[0],row1[0]])
#print(dic_bat)
for i in li_clust:
	if i not in li_players:
		print(dic_bat[i[0]],dic_bowl[i[1]],sep=",")

