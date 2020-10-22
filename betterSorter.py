#sorter.py
import csv
import re
import math
import os
from os import walk
import os.path
import processing
returnFiles = []
requests_e = []
requests_m = []
REQUESTFILENAME = "request.txt"
STARTCHAR = "$"
KEYWORDS = "< > <= >= not or .".split()
NONESTR = "none"
FINDLINEM = "FINDLINE_M:"
FINDLINEE = "FINDLINE_E:"
findLineM = ".*"
findLineE = ".*"

def strContainsKeyword (s):
	return False
pass #EOF

def shortcuts():
	pass
	#ADD in shortcuts for cases where: 
	#		Sample id != None,
	#		COSMIC EXPRESSION DATA == NONE
	#       COSMIC MUTATION DATA == NONE
#eof

def checkString(s, pattern):
	if re.search(pattern, s, flags=0) == None:
		return False
	return True

def setRequests(reqListE, reqListM, eLine, mLine):
	global requests_e
	global requests_m
	global findLineM
	global findLineE
	requests_e = reqListE
	requests_m = reqListM
	findLineM = mLine
	findLineE = eLine
pass #EOF

def checkRequestFile():
	request = open(REQUESTFILENAME, "r")
	lines = request.readlines()
	onLine = 0
	rq = []
	global findLineE
	global findLineM
	for line in lines:
		l = line.strip() 
		l = l.strip(" ")
		if FINDLINEE in line:
			for i in range(len(l)):
				if l[i] == ":":
					findLineE = l[i+1:].strip().lower()
					#print(findLineE)
					break
			pass
		elif FINDLINEM in line:
			for i in range(len(l)):
				if l[i] == ":":
					findLineM = l[i+1:].strip().lower()
					#print(findLineM)
					break
			pass
		else:
			for i in range(len(l)):
				if l[i] == STARTCHAR:
					rq.append(l[i+1:].strip().lower())
					break
			pass
			onLine += 1
	print (str(rq))
	requests = []
	for i in range(len(rq)):
		if NONESTR in rq[i].lower():
			pass
		else:
			if i > 40:
				requests_e.append([i%40, rq[i].lower()])
			else:	
				requests_m.append([i, rq[i].lower()])
		pass
	pass
	print (requests)
	print (findLineM)
	print (findLineE)
#eof

def searchFile(fileName):
	lineFound = False
	global findLineE
	global findLineM
	if ".gx" not in fileName:
		file = open(fileName, "r")
		rows = csv.reader(file, delimiter="\t")
		meets = False
		#lineFound = False
		crit = []
		for i in range(len(requests_m)):
			crit.append(False)
		for row in rows:
			for i in range(len(requests_m)):
				#print(row[requests_m[i][0]], requests_m[i][1])
				if checkString(row[requests_m[i][0]].lower(), requests_m[i][1]):
					crit[i] = True
				pass
			pass
			if lineFound == False:
				longS = ""
				#print(longS)
				for r in row:
					longS += " " + r
				#print(longS)
				if checkString(longS.lower(), findLineM):
					#print("MADE IT HERE", longS, findLineM)#GETS HERE
					lineFound = True
			else:
				pass
				#print("yay!")
		pass
		for i in range(len(crit)):
			#print (crit[i], requests_m[i])
			if crit[i] == False:
				return False
		return lineFound
	else:
		file = open(fileName, "r")
		rows = csv.reader(file, delimiter="\t")
		meets = False
		crit = []
		for i in range(len(requests_e)):
			crit.append(False)
		for row in rows:
			for i in range(len(requests_e)):
				if checkString(row[requests_e[i][0]].lower(), requests_e[i][1]):
					crit[i] = True
				pass
			pass
			if lineFound == False:
				longS = ""
				#print(longS)
				for r in row:
					longS += " " + r
				#print(longS)
				if checkString(longS.lower(), findLineE):
					#print(longS, findLineE) 
					#print(findLineE)
					lineFound = True
			else:
				pass
		pass
		for i in range(len(crit)):
			if crit[i] == False:
				return False
		return lineFound
	return lineFound
pass

def searchFile2(fileName):
	f = open(fileName, "r")
	checkString(f.read(), requests_m[0][1])


#eof

def main():
	pass
#eof

def search():
	checkRequestFile()
	print(requests_e)
	print(requests_m)
	print ("The current working directory is %s" % os.getcwd())
	returnFiles = []
	files = []
	for (dirpath, dirnames, filenames) in walk("m"):
		files.extend(filenames)
		break
	count = 0
	for f in files:
		count = count + 1
		if count%300 == 0:
			#print(findLineE)
			#print(checkString("penis", findLineM))
			print(str(math.floor((count/len(files))*100))+ "%  complete", len(returnFiles))
		if searchFile("m/" + f):
			#print("actually...")
			if os.path.exists("e/" + f[:-7] + ".gx.tsv"):
				#print("file found for", f[:12])
				if searchFile("e/" + f[:-7] + ".gx.tsv"):
					returnFiles.append(f[:12])
					processing.foundFile ("m/" + f)
					processing.foundFile ("e/" + f[:-7] + ".gx.tsv")
				pass
			elif os.path.exists("e/" + f[:12] + "-01.gx.tsv"):
				#print("file found for", f[:12])
				if searchFile("e/" + f[:12] + "-01.gx.tsv"):
					returnFiles.append(f[:12])
					processing.foundFile ("m/" + f)
					processing.foundFile ("e/" + f[:12] + "-01.gx.tsv")
				pass
			elif os.path.exists("e/" + f[:12] + "-02.gx.tsv"):
				#print("file found for", f[:12])
				if searchFile("e/" + f[:12] + "-02.gx.tsv"):
					returnFiles.append(f[:12])
					processing.foundFile ("m/" + f)
					processing.foundFile ("e/" + f[:12] + "-02.gx.tsv")
				pass
			else:
				pass
				
			
	print(returnFiles)
	processing.processData (returnFiles, gene)

def searchIterative(gene):
	processing.setGene(gene)
	print(requests_e)
	print(requests_m)
	print ("The current working directory is %s" % os.getcwd())
	returnFiles = []
	files = []
	for (dirpath, dirnames, filenames) in walk("m"):
		files.extend(filenames)
		break
	count = 0
	for f in files:
		count = count + 1
		if count%300 == 0:
			#print(findLineE)
			#print(checkString("penis", findLineM))
			print(str(math.floor((count/len(files))*100))+ "%  complete", len(returnFiles))
		if searchFile("m/" + f):
			#print("actually...")
			if os.path.exists("e/" + f[:-7] + ".gx.tsv"):
				#print("file found for", f[:12])
				if searchFile("e/" + f[:-7] + ".gx.tsv"):
					returnFiles.append(f[:12])
					processing.foundFile ("m/" + f)
					processing.foundFile ("e/" + f[:-7] + ".gx.tsv")
				pass
			elif os.path.exists("e/" + f[:12] + "-01.gx.tsv"):
				#print("file found for", f[:12])
				if searchFile("e/" + f[:12] + "-01.gx.tsv"):
					returnFiles.append(f[:12])
					processing.foundFile ("m/" + f)
					processing.foundFile ("e/" + f[:12] + "-01.gx.tsv")
				pass
			elif os.path.exists("e/" + f[:12] + "-02.gx.tsv"):
				#print("file found for", f[:12])
				if searchFile("e/" + f[:12] + "-02.gx.tsv"):
					returnFiles.append(f[:12])
					processing.foundFile ("m/" + f)
					processing.foundFile ("e/" + f[:12] + "-02.gx.tsv")
				pass
			else:
				pass
				
			
	print(returnFiles)
	processing.processData (returnFiles, gene)




if __name__ == '__main__':
	search()


#eof