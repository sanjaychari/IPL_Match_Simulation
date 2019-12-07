import pandas as pd     
df = pd.read_csv('batsmen.csv')
df.columns = ["Player","Runs","Average","SR","HS","Innings","Buff"]
df.to_csv('batsmen.csv')
df = pd.read_csv('bowlers.csv')
df.columns = ["Player","Runs","Wickets","Overs","Balls","Average","SR","Economy"]
df.to_csv('bowlers.csv')
