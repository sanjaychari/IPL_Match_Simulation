import pandas as pd
import sys
#clust_prob = pd.DataFrame(columns=['batsman','bowler','0', '1', '2', '3', '4',  '6','notout'])
print('batsman,bowler,0,1,2,3,4,6,notout')
#miss = pd.read_csv('final_miss_probs.csv')
#dic_prob = {}
#header = sys.stdin
count=0
for line in sys.stdin:
	if(count!=0):
		row=line.split(",")
		print(row[0],row[1],end=",",sep=",")
		li=[]
		for i in range(2,8):
			li.append(float(row[i]))
		for i in range(1,6):
			li[i]+=li[i-1]
		for j in li:
			print(j,end=",")
		print(row[8])
	count+=1
	#print()
	'''if((row[0],row[1]) not in dic_prob):
		dic_prob[(row[0],row[1])]=[]
		print(row[0],row[1],sep=",",end=",")
		for i in range(2,9):
			dic_prob[(row[0],row[1])].append(float(row[i]))
		for i in range(1,6):
			dic_prob[(row[0],row[1])][i]+=dic_prob[(row[0],row[1])][i-1]
		for i in dic_prob[(row[0],row[1])]:
			print(i,end=",")
		print()'''
