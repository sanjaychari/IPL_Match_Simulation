import sys
import csv
import pandas as pd
from collections import defaultdict
dic = defaultdict(list)

def find_bat_clust(batname):
	for index,row in batclust.iterrows():
		if(row[0]==batname):
			print("Cluster",row[1])
			return row[1]
	return 0

def find_bowl_clust(bowlname):
	for index,row in bowlclust.iterrows():
		if(row[0]==bowlname):
			print("Cluster",row[1])
			return row[1]
	return 0

dic_clust={}
for i in range(6):
	for j in range(6):
		dic_clust[i,j]=[0,0,0,0,0,0,0,0]

for line in sys.stdin:
	row = line.split(',')
	if(row[0]=='ball'):
		if(len(row)>=10):
			print(row)
			b = [int(row[7]),row[9]]
		else:
			b = [int(row[7]),'']
		dic[row[4],row[6]].append(b)
		
csvfile = open('player_to_player.csv','w')
fieldnames = ['batsman', 'bowler', '0','1','2','3','4','6','out','batclustno','bowlclustno','balls']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


for key,values in dic.items():
	#print(key,type(key),key[0],key[1])
	dot = 0
	one = 0
	two = 0
	three = 0
	four = 0
	six = 0
	wick = 0
	balls = 0
	for i in values:
		p = i[0]
		#print(i,type(i),i[0],i[1])
		if p == 0:
			dot = dot+1
		elif p == 1:
			one = one+1
		elif p == 2:
			two = two+1
		elif p == 3:
			three = three+1
		elif p == 4:
			four = four+1
		elif p == 6:
			six = six+1
		if i[1] != '':
			wick = wick +1
		balls = balls +1
	#print(key,dot,one,two,three,four,six,wick,balls)
	#print(key,wick)
	batclustno = 0
	bowlclustno = 0
	with open('../Clustering/bat_clusters.csv') as file1:
		read = csv.reader(file1)
		for row in read:
			if row[0] == key[0] or (len(row[0].split())==2 and (row[0].split()[0][0]+" "+row[0].split()[1]==key[0]) or (row[0].split()[-1]==key[0].split()[-1])): 
				batclustno = row[1]
				break
	with open('../Clustering/bowl_clusters.csv') as file2:
		read = csv.reader(file2)
		for row in read:
			if row[0] == key[1] or (len(row[0].split())==2 and (row[0].split()[0][0]+" "+row[0].split()[1]==key[1]) or (row[0].split()[-1]==key[1].split()[-1])):
				bowlclustno = row[1]
				break
	dic_clust[int(batclustno),int(bowlclustno)][0]+=dot
	dic_clust[int(batclustno),int(bowlclustno)][1]+=one
	dic_clust[int(batclustno),int(bowlclustno)][2]+=two
	dic_clust[int(batclustno),int(bowlclustno)][3]+=three
	dic_clust[int(batclustno),int(bowlclustno)][4]+=four
	dic_clust[int(batclustno),int(bowlclustno)][5]+=six
	dic_clust[int(batclustno),int(bowlclustno)][6]+=wick
	dic_clust[int(batclustno),int(bowlclustno)][7]+=balls
	writer.writerow({'batsman':key[0],'bowler':key[1],'0':dot/balls,'1':one/balls,'2':two/balls,'3':three/balls,'4':four/balls,'6':six/balls,'out':wick/balls,'batclustno':batclustno,'bowlclustno':bowlclustno,'balls':balls})

csvfile = open('clust_to_clust.csv','w')
fieldnames = ['batclustno', 'bowlclustno', '0','1','2','3','4','6','out','balls']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()


for i in dic_clust:
	dic_clust[i][0]/=dic_clust[i][7]
	dic_clust[i][1]/=dic_clust[i][7]
	dic_clust[i][2]/=dic_clust[i][7]
	dic_clust[i][3]/=dic_clust[i][7]
	dic_clust[i][4]/=dic_clust[i][7]
	dic_clust[i][5]/=dic_clust[i][7]
	dic_clust[i][6]/=dic_clust[i][7]
	writer.writerow({'batclustno':i[0],'bowlclustno':i[1],'0':dic_clust[i][0],'1':dic_clust[i][1],'2':dic_clust[i][2],'3':dic_clust[i][3],'4':dic_clust[i][4],'6':dic_clust[i][5],'out':dic_clust[i][6],'balls':dic_clust[i][7]})
