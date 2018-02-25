import json
import pandas as pd
import sys

def analysis(file,user_id):

	try:
		data=pd.read_json(file)
	except ValueError:
		return 0,0	
	user_data=data[data['user_id']==user_id].minutes
	times=user_data.count()
	minutes=user_data.sum()

	return times,minutes

if __name__=='__main__':
	print(analysis(sys.argv[1],int(sys.argv[2])))