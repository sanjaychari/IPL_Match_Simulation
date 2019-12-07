import pandas as pd
batcluster = pd.read_csv("../Clustering/bat_clusters.csv",header=None)
bowlcluster = pd.read_csv("../Clustering/bowl_clusters.csv",header=None)
dic_bat={}
dic_bowl={}
for index,row in batcluster.iterrows():
	if(index not in dic_bat):
		dic_bat[index]=row[0]
for index,row in bowlcluster.iterrows():
	if(index not in dic_bowl):
		dic_bowl[index]=row[0]
#print(dic_bat)
print('batsman,bowler,0,1,2,3,4,6,notout')
missing = pd.read_csv("missing_probs.csv")
for index,row in missing.iterrows():
	rowt=row
	print(dic_bat[int(row[0])],dic_bowl[int(row[1])],sep=",",end=",")
	for i in range(2,len(rowt)-1):
		if(float(rowt[i])<0):
			rowt[i]='0.0'
	sump=0
	for i in range(2,len(rowt)-1):
		sump+=float(rowt[i])
	for i in range(2,len(rowt)-1):
		if(sump!=0):
			print(float(rowt[i])/float(sump),end=",")
		else:
			print(float(rowt[i])/1000,end=",")
	if(float(rowt[-1])<0):
		print("1",end=",")
	elif(float(rowt[-1])>1):
		print("0",end=",")
	else:
		print(1-float(rowt[-1]),end=",")
	print()
