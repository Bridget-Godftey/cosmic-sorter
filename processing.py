#processing.py
import os
from shutil import copyfile
filesFound = []
names = []
expression = {}
mutation = {}
gene = "NONE"
fileType = ".tsv"
bDone = False
gene = ""
cpath = os.getcwd()

def processData (files, gene):

	global names
	global expression
	global mutation
	global gene

	if not os.path.isdir(gene):
		os.mkdir(gene)
		os.mkdir(gene + "/" + "expression")
		os.mkdir(gene + "/" + "mutation")
	pass

	for n in names:
		copyfile(expression[n], gene + "/" + "expression/" + n + fileType)
		copyfile(mutation[n], gene + "/" + "mutation/" + n + fileType)
	pass



pass

def setGene (g)
	gene = g

def foundFile (fileName):
	global names
	global expression
	global mutation
	global filesFound
	global gene
	if not bDone and not os.path.isdir(gene):
		os.mkdir(gene)
		os.mkdir(gene + "/" + "expression")
		os.mkdir(gene + "/" + "mutation")
		bDone = True
	pass

	tempName = fileName

	tempName = tempName [2:14]
	if fileName[1] == "e":
		f = open(fileName, "r")
		text = f.read()
		f2 = open (gene + "/" + "mutation/" + n + fileType)
		expression.update({tempName:fileName})
		names.append(tempName)
	else:
		mutation.update({tempName:fileName})

	



	filesFound.append(fileName)

pass #EOF