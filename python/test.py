import cPickle as pickle
filename = 'shoplist.data'
shoplist = ['apple','mango','carrot']
f = file(filename,'w')
pickle.dump(shoplist,f)
f.close()

f = file(filename)
shoplist = pickle.load(f)
print (shoplist)