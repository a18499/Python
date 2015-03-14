import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }
  
pickle.dump( favorite_color, open( "save.p", "wb" ) )
with open('save.p','rb') as myloaddata:
	a_list = pickle.load(myloaddata)
print(a_list)