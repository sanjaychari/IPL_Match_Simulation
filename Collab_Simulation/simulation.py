import csv
import random
import pandas as pd  

team1 = list()
bat_clust = {}
team2 = list()
bowl_clust = {}

files = pd.read_csv('player_to_player.csv') 
for i in range(len(files)):
	bowlname = files.loc[i].bowler.strip()   
	bowl_clust[bowlname] = files.loc[i].bowlclustno
	batname = files.loc[i].batsman.strip()     
	bat_clust[batname] = files.loc[i].batclustno


'''squad = pd.read_csv('squad.csv')
for index, row in squad.iterrows():
	if(row[0]!="Team1"):
		team1.append(row[0])
	if(row[1]!="Team2"):
		team2.append(row[1])
print(team1,team2)'''
'''team1 = ['PA Patel','Mandeep Singh','V Kohli','AB de Villiers','YS Chahal','MP Stoinis','P Negi','Washington Sundar','NM Coulter-Nile','UT Yadav','Mohammed Siraj']
team2 =['SR Watson','F du Plessis','SK Raina','KM Jadhav','MS Dhoni','DM Bravo','RA Jadeja','Harbhajan Singh','DL Chahar','MM Sharma','SN Thakur']'''
team2 = ['PP Shaw','S Dhawan','SS Iyer','RR Pant','CA Ingram','AR Patel','SE Rutherford','CH Morris','J Suchith','A Mishra','TA Boult']
team1 =['SR Watson','F du Plessis','SK Raina','KM Jadhav','MS Dhoni','DM Bravo','RA Jadeja','Harbhajan Singh','DL Chahar','MM Sharma','Imran Tahir']

player_prob = pd.read_csv('player_cumprob.csv')

def playerprob(batsman,bowler):
	row = player_prob.loc[player_prob['batsman'] == batsman].loc[player_prob['bowler'] == bowler]
	rand = random.random()
	#print(rand)
	res = 0 if rand <= float(row['0']) else 1 if rand <= float(row['1']) else 2 if rand <= float(row['2']) else 3 if rand <= float(row['3']) else 4 if rand <= float(row['4']) else 6 if rand <= float(row['6']) else -1
	#print(res)
	return res

clust_prob = pd.read_csv('clust_cumprob.csv')

def clusterprob(bat_clust_no,bowl_clust_no):
	row = clust_prob.loc[clust_prob['batclustno'] == bat_clust_no].loc[clust_prob['bowlclustno'] == bowl_clust_no]
	rand = random.random()
	#print(rand)
	res = 0 if rand <= float(row['0']) else 1 if rand <= float(row['1']) else 2 if rand <= float(row['2']) else 3 if rand <= float(row['3']) else 4 if rand <= float(row['4']) else 6 if rand <= float(row['6']) else -1
	#print(res)
	return res

collab_prob = pd.read_csv('miss_cum.csv')
def collabprob(batsman,bowler):
	#row = collab_prob.loc[collab_prob['batsman'] == batsman].loc[collab_prob['bowler'] == bowler]
	for index,row in collab_prob.iterrows():
		if(row[0]==batsman and row[1]==bowler):
			break
	rand = random.random()
	#print(rand)
	res = 0 if rand <= float(row['0']) else 1 if rand <= float(row['1']) else 2 if rand <= float(row['2']) else 3 if rand <= float(row['3']) else 4 if rand <= float(row['4']) else 6 if rand <= float(row['6']) else -1
	#print(res)
	return res


def innings(team1, team2, runs1, inningno):
	dic_stats = {"wickets":0,"runs":0,"nextbatsman":2,"overs":0,"striker":team1[0],"bowler":team2[-1],"non_striker":team1[1],"prob":0,"count":2,"not_out_prob":1}
	dic = {}
	#print(dic_stats["striker"])
	dic[dic_stats["striker"]] = 1
	dic[dic_stats["non_striker"]]=1
	part_age=0
	while(dic_stats["overs"]<20 and  dic_stats["wickets"]< 10):
		use_clusters = 0
		use_collab = 0
		balls = 1
		while(balls<=6 and ((inningno==2 and dic_stats["runs"]<=runs1) or (inningno==1)) and dic_stats["wickets"] <10):
			#print("Ball ",balls)
			try:
				row = player_prob.loc[player_prob['batsman'] == dic_stats["striker"]].loc[player_prob['bowler'] == dic_stats["bowler"]]
				dic_stats["prob"] = float(row['notout'])
				if(int(row['balls'])<10):
					row = clust_prob.loc[clust_prob['batclustno'] == bat_clust[dic_stats["striker"]]].loc[clust_prob['bowlclustno'] == bowl_clust[dic_stats["bowler"]]]
					dic_stats["prob"] = float(row['notout'])
					use_clusters = 1
			except:
				#row = collab_prob.loc[collab_prob['batsman'] == dic_stats["striker"]].loc[collab_prob['bowler'] == dic_stats["bowler"]]	
				for index,row in collab_prob.iterrows():
					if(row[0]==dic_stats["striker"] and row[1]==dic_stats["bowler"]):
						break
				dic_stats["prob"] = float(row[8])
				#print(row['notout'])
				#dic_stats["prob"] = float(row['notout'])
				use_collab = 1
				#use_clusters = 0	
			dic_stats["not_out_prob"] = dic_stats["not_out_prob"]*dic_stats["prob"]
			dic[dic_stats["striker"]] = dic[dic_stats["striker"]]*dic_stats["prob"]
			flag = 0
			score = 0
			if (dic[dic_stats["striker"]] < 0.5 or part_age>70):
				flag = 1
				dic_stats["wickets"] = dic_stats["wickets"]+1
				dic_stats["striker"] = team1[dic_stats["nextbatsman"]]
				dic[dic_stats["striker"]] = 1
				dic_stats["nextbatsman"] = (dic_stats["nextbatsman"]+1)%11
				part_age=0
			elif (dic[dic_stats["striker"]] >= 0.5):
				#print("Notout",dic_stats["striker"],dic[dic_stats["striker"]])
				if use_clusters!=0:
					score = clusterprob(batclustno,bowlclustno)	
				elif use_collab==1:
					score = collabprob(dic_stats["striker"],dic_stats["bowler"])
				else:
					if (int(row['balls'])<10):
						score = clusterprob(batclustno,bowlclustno)
					else:
						score = playerprob(dic_stats["striker"],dic_stats["bowler"])
			if(flag==0):
				dic_stats["runs"] = dic_stats["runs"]+score
				if (score==1 or score == 3):
					dic_stats["striker"],dic_stats["non_striker"] = dic_stats["non_striker"],dic_stats["striker"]
			print("{:20s}|{:20s}|{:20s}|{:20s}|{:20s}".format(str(dic_stats["overs"])+"."+str(balls-1),dic_stats["striker"],dic_stats["bowler"],str(dic_stats["runs"]),str(dic_stats["wickets"])))
			balls = balls+1
			part_age+=1
		dic_stats["overs"] += 1
		dic_stats["count"] = (dic_stats["count"]+1)%5 + 1
		dic_stats["striker"],dic_stats["non_striker"] = dic_stats["non_striker"],dic_stats["striker"]                 
		dic_stats["bowler"] = team2[len(team2)-dic_stats["count"]]                    
		#print(str(dic_stats["overs"])+"\t|\t"+str(dic_stats["runs"])+"    \t|\t"+str(dic_stats["wickets"]))
		if(inningno==2 and runs1<dic_stats["runs"]):
			break
	return dic_stats["runs"],dic_stats["wickets"]	 
print("--------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t SCORECARD")
print("--------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t  INNINGS 1")
print("--------------------------------------------------------------------------------------------------------------------")
print("{:20s}|{:20s}|{:20s}|{:20s}|{:20s}".format("Balls","Striker","Bowler","Score","Wickets"))
runs1 ,wicks1 = innings(team1,team2,0,1)
print("--------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t\t\t  INNINGS 2")
print("--------------------------------------------------------------------------------------------------------------------")
print("{:20s}|{:20s}|{:20s}|{:20s}|{:20s}".format("Balls","Striker","Bowler","Score","Wickets"))
runs2 ,wicks2 = innings(team2,team1,runs1,2)
print("--------------------------------------------------------------------------------------------------------------------")
print("Innings 1 Score : ", runs1, "-", wicks1)
print("Innings 2 Score : ", runs2, "-", wicks2)
print("--------------------------------------------------------------------------------------------------------------------")
print("TEAM 2 WON") if runs1<runs2 else print("TEAM 1 WON") if runs1>runs2 else print("TIE")
