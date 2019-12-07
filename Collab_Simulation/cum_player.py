import pandas as pd
player_prob = pd.DataFrame(columns=['batsman','bowler','0', '1', '2', '3', '4',  '6','notout','balls'])
print('batman,bowler,0,1,2,3,4,6,notout,balls')
player = pd.read_csv('player_to_player.csv')
for i in range(len(player)):
	player_prob.at[i] = [None for n in range(10)]
	player_prob.at[i,'0'] = float(player.at[i,'0'])                
	player_prob.at[i,'1'] = float(player.at[i,'1']) + float(player.at[i,'0'])
	player_prob.at[i,'2'] = float(player.at[i,'2']) + float(player_prob.at[i,'1'])
	player_prob.at[i,'3'] = float(player.at[i,'3']) + float(player_prob.at[i,'2'])
	player_prob.at[i,'4'] = float(player.at[i,'4']) + float(player_prob.at[i,'3'])
	player_prob.at[i,'6'] = float(player.at[i,'6']) + float(player_prob.at[i,'4'])   
	player_prob.at[i,'batsman'] = player.at[i,'batsman']	       
	player_prob.at[i,'bowler'] = player.at[i,'bowler']
	player_prob.at[i,'notout'] = 1 - float(player.at[i,'out'])
	player_prob.at[i,'balls'] = player.at[i,'balls']
	print(player_prob.at[i,'batsman'],player_prob.at[i,'bowler'],player_prob.at[i,'0'],player_prob.at[i,'1'],player_prob.at[i,'2'],player_prob.at[i,'3'],player_prob.at[i,'4'],player_prob.at[i,'6'],player_prob.at[i,'notout'],player_prob.at[i,'balls'],sep=",")
