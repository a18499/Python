import athletemodel
"""Testing code here """
the_files = ['sarah2.txt','james2.txt','mikey2.txt','julie2.txt']
data = athletemodel.put_to_store(the_files)
print(data)

for each_athlete in data:
	print(data[each_athlete].name+' '+data[each_athlete].dob)
data_copy = athletemodel.get_from_store()
for each_athlete in data_copy:
	print(data_copy[each_athlete].name+' '+data_copy[each_athlete].dob)