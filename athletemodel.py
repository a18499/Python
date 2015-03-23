import pickle
import time_string
import Athete
def get_cocah_data(filename):
	try:
		with open(filename) as jdata:
			"""Read a line to list """
			data = jdata.readline()
			temp = data.strip().split(',')
		return Athete.AtheteList(temp.pop(0),temp.pop(0),temp)
	except IOError:
		return(None)
def put_to_store(files_list):
	all_athletes = {}
	for each_file in files_list:
		ath = get_cocah_data(each_file)
		all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle','wb') as athf:
			pickle.dump(all_athletes,athf)
	except IOError as ioerr:
		print('File error(put_to_store):'+str(ioerr))
	return(all_athletes)
def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle','rb') as athf:
			all_athletes =pickle.load(athf)
	except IOError as ioerr:
		print('File error(get_to_store):'+str(ioerr))
	return(all_athletes)




