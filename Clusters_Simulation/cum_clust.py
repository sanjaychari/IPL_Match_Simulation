import pandas as pd
clust_prob = pd.DataFrame(columns=['batclustno','bowlclustno','0', '1', '2', '3', '4',  '6','notout'])
print('batclustno,bowlclustno,0,1,2,3,4,6,notout')
clust = pd.read_csv('clust_to_clust.csv')
for i in range(len(clust)):
	clust_prob.at[i] = [None for n in range(9)]
	clust_prob.at[i,'0'] = float(clust.at[i,'0'])                
	clust_prob.at[i,'1'] = float(clust.at[i,'1']) + float(clust.at[i,'0'])
	clust_prob.at[i,'2'] = float(clust.at[i,'2']) + float(clust_prob.at[i,'1'])
	clust_prob.at[i,'3'] = float(clust.at[i,'3']) + float(clust_prob.at[i,'2'])
	clust_prob.at[i,'4'] = float(clust.at[i,'4']) + float(clust_prob.at[i,'3'])
	clust_prob.at[i,'6'] = float(clust.at[i,'6']) + float(clust_prob.at[i,'4'])   
	clust_prob.at[i,'batclustno'] = clust.at[i,'batclustno']	       
	clust_prob.at[i,'bowlclustno'] = clust.at[i,'bowlclustno']
	clust_prob.at[i,'notout'] = 1 - float(clust.at[i,'out'])
	print(clust_prob.at[i,'batclustno'],clust_prob.at[i,'bowlclustno'],clust_prob.at[i,'0'],clust_prob.at[i,'1'],clust_prob.at[i,'2'],clust_prob.at[i,'3'],clust_prob.at[i,'4'],clust_prob.at[i,'6'],clust_prob.at[i,'notout'],sep=",")
