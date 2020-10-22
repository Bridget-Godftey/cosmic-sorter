#main.py
import betterSorter
import csv
from shutil import copyfile
import os
import timeit
from os import walk
import re
gFile = open("Genes.tsv")
rows = csv.reader(gFile, delimiter="\t")
genes = []
stnStrings = {}
gne = ""
for row in rows:
	genes.append(row[0])
	temp = row[19]
	temp = temp[1:-1]
	last = 0
	syn = []
	synStr = "(" + row[0] + ")"
	for i in range(len(temp)):
		if temp[i] == ",":
			syn.append(temp[last:i-1])
			last = i + 1
	pass
	for n in syn:
		synStr = synStr + "|(" + n + ")"
	stnStrings.update({row[0] : synStr})

gFile.close()

def func():
	betterSorter.searchIterative(gne)

if __name__ == '__main__':

	# n = 10000
	# req_m =[ [0, ".*(TP53)|(7157)|(ENSG00000141510.16)|(LFS1)|(P04637)|(TP53)|(p53).*"]]
	# desc =  str(n) + " requests took "
	# betterSorter.setRequests([], req_m, ".*", ".*")
	# time = timeit.timeit(func, number = n)
	# print(" %s : %.3fs"%(desc, time))

	for g in genes:
		if not os.path.isdir(g):
			req_m = [[0, ".*" + stnStrings[g] + ".*"]]
			betterSorter.setRequests([], req_m, ".*", ".*")
			gne = g
			time = timeit.timeit(func, number = 1)
			desc = "search took "
			print(" %s : %.3fs"%(desc, time))
			
		pass
		mutTypes = []
		mutCount = {}
		mfiles = []
		for (dirpath, dirnames, filenames) in walk(g + "/mutation"):
			mfiles.extend(filenames)
			break
		for f in mfiles:
			file = open(f)
			rows = csv.reader(file, delimiter="\t")
			for row in rows:
				if betterSorter.checkString(row[0], ".*" + stnStrings[g] + ".*"):
					if row[19] in mutTypes:
						mutCount[row[19]] = mutCount[row[19]] + 1
						copyfile(g + "/expression/" + f, g + "/" + row[19] + "/" + f )
					else:
						mutTypes.append(row[19])
						mutCount.update({row[19] : 1})
						if not os.path.isdir(g + "/" + row[19]):
							os.mkdir(g + "/" + row[19])
						copyfile(g + "/expression/" + f, g + "/" + row[19] + "/" + f )
					pass
				pass
			pass
		pass

		for m in mutTypes:
			print (m, mutCount[m])
			print("total: " + str(len(mutCount)))
		pass

	pass
pass

