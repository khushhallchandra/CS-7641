import pickle

def mapPicture(javaStrArr):
	out = []
	for row in javaStrArr:
		out.append([])
		for element in row:
			out[-1].append(str(element))
	return out

def dumpPolicyMap(javaStrArr,fname):
	pic = mapPicture(javaStrArr)
	with open(fname,'wb') as f:
		pickle.dump(pic,f)