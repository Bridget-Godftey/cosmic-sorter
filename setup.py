#setup.py
import csv
from os import walk
#This is the big datafile
case_file = open("Cases/CaseData1.tsv")
CFILE_FRONT = "Cases/CaseData"
#Gene expression datafile
tsv_file = open("Expression/CosmicCompleteGeneExpression_1.tsv")
EFILE_FRONT = "Expression/CosmicCompleteGeneExpression_"

FILE_EXT = ".tsv"

expression_data = csv.reader(tsv_file, delimiter="\t")
case_data = csv.reader(case_file, delimiter="\t")

collected_data = []

NUM_EFILES =  3242
NUM_CFILES = 176#176

onFile = 1
onEFile = 1
onCFile = 1
onGene = 0
onRow = 0

GENE_NAMES = []

FIELDNAMES = ["Gene_name", "Accession Number", "Gene_CDS_length", "HGNC_ID", "Sample_name", "ID_sample", "ID_tumour", "Primary_site", "Site_subtype_1", "Site_subtype_2", "Site_subtype_3", "Primary_histology", "Histology_subtype_1", "Histology_subtype_2", "Histology_subtype_3", "Genome-wide_screen", "GENOMIC_MUTATION_ID", "LEGACY_MUTATION_ID", "MUTATION_ID", "Mutation_CDS", "Mutation_AA", "Mutation_Description", "Mutation_zygosity", "LOH", "GRCh", "Mutation_genome_position", "Mutation_strand", "SNP", "Resistance_Mutation", "FATHMM_prediction", "FATHMM_score", "Mutation_somatic_status", "Pubmed_PMID", "ID_STUDY", "Sample_Type", "Tumour_origin", "Age", "HGVSP", "HGVSC", "HGVSG", "SAMPLE_ID2", "SAMPLE_NAME2", "GENE_NAME2", "REGULATION2", "Z_SCORE2", "ID_STUDY2"]

have_genes = []
numGenes = -1
#geneNames = {"NULL": -1}
genes = {}
genesTemp = []
outPath = "allPatients"

patient_data = {}
patients = []
patientFiles = {}


def addToFile (file, row):
	global FIELDNAMES

	writer = csv.DictWriter(file, fieldnames=FIELDNAMES, delimiter='\t')
	
	tempRowDict = {}
	for k in range(len(row)):
		tempRowDict.update({FIELDNAMES[k]: row[k]})
	pass
	writer.writerow(tempRowDict)


while onCFile <= NUM_CFILES:
	print ("***********" + str(onCFile) + "***********")
	case_file = open("Cases/CaseData" + str(onCFile) + ".tsv")
	case_data = csv.reader(case_file, delimiter="\t")
	onCFile += 1
	for c_row in case_data:
	#if "TP53" in c_row[0]:
		#pN = c_row[20]
		#print(c_row[20])
		#tempPat = "p." + pattern
		if c_row[4] in patients:
		 	#print("Pattern Found")
		 	temp = [c_row]
		 	patients.append(c_row[4])
		 	patient_data.update({c_row[4]: temp})
		 	f =  open(outPath + "/" + c_row[4] +".tsv", "w+")
		 	patientFiles.update({c_row[4]: f})
	case_file.close()
	#print(patient_data)
pass





#READ EXPRESSION DATA
while onEFile <= NUM_EFILES:
	print ("~~~~~~~~~~~" + str(onEFile) + "~~~~~~~~~~~")
	for p in patients:
		patientFiles[p] = open(patientFiles[p].name, "a")
	tsv_file = open(EFILE_FRONT + str(onEFile) + ".tsv")
	onEFile += 1
	expression_data = csv.reader(tsv_file, delimiter="\t")
	for e_row in expression_data:
		if e_row[1] in patient_data:
			addToFile(patientFiles[e_row[1]], e_row)
	pass

	for p in patients:
		patientFiles[p].close()
pass


print (patientFiles)

onCFile = 1
while onCFile <= NUM_CFILES:
	print ("***********" + str(onCFile) + "***********")
	case_file = open("Cases/CaseData" + str(onCFile) + ".tsv")
	case_data = csv.reader(case_file, delimiter="\t")
	onCFile += 1
	for p in patients:
		patientFiles[p] = open(patientFiles[p].name, "a")
		if onCFile == 2:
			pass
			#addToFile(patientFiles[p], FIELDNAMES)

	for c_row in case_data:
		if c_row[4] in patients:
			addToFile(patientFiles[c_row[4]], c_row)

	for p in patients:
		patientFiles[p].close()
	#print(patient_data)
pass



#######################################################################
#.....................................................................#
#....................SEPARATE FILES...................................#
#.....................................................................#
#######################################################################

filepath = outPath
out_path = "e/"
out_path_2 = "m/"
original_files = []

FIELDNAMES = ["COSMIC ID", "TCGA ID", "GENE", "EXPRESSION", "Z VALUE", "?"]
FIELDNAMES2 = ["Gene_name", "Accession Number", "Gene_CDS_length", "HGNC_ID", "Sample_name", "ID_sample", "ID_tumour", "Primary_site", "Site_subtype_1", "Site_subtype_2", "Site_subtype_3", "Primary_histology", "Histology_subtype_1", "Histology_subtype_2", "Histology_subtype_3", "Genome-wide_screen", "GENOMIC_MUTATION_ID", "LEGACY_MUTATION_ID", "MUTATION_ID", "Mutation_CDS", "Mutation_AA", "Mutation_Description", "Mutation_zygosity", "LOH", "GRCh", "Mutation_genome_position", "Mutation_strand", "SNP", "Resistance_Mutation", "FATHMM_prediction", "FATHMM_score", "Mutation_somatic_status", "Pubmed_PMID", "ID_STUDY", "Sample_Type", "Tumour_origin", "Age", "HGVSP", "HGVSC", "HGVSG", "SAMPLE_ID2", "SAMPLE_NAME2", "GENE_NAME2", "REGULATION2", "Z_SCORE2", "ID_STUDY2"]

for (dirpath, dirnames, filenames) in walk(filepath):
    original_files.extend(filenames)
    break

for n in original_files:
	#print("opening", n[:len(n)-4] + "...")
	og_file = open(filepath + "/" + n)
	#print ("create", n, "expression file")
	expression_file = open(out_path + n[:len(n)-4] + ".gx.tsv", "w+")

	og_data = csv.reader(og_file, delimiter="\t")
	nonNormalExpression = []
	mutData = []
	for row in og_data:
		if row == [] or row[4] == n[:len(n)-4] or row[4] == "Sample_name":
			mutData.append(row[:])
		elif row[3] != "normal":
			r = row[:]
			if r[3] != "over":
				r[2] = r[2] + "+"
			else:
				r[2] = r[2] + "-"
			nonNormalExpression.append(r[:])
		else:
			nonNormalExpression.append(r[:])
		pass

	#write to GX file
	writer = csv.DictWriter(expression_file, fieldnames=FIELDNAMES, delimiter='\t')
	for r in nonNormalExpression:
		tempRowDict = {}
		for k in range(len(r)):
			if k > 5:
				break
			tempRowDict.update({FIELDNAMES[k]: r[k]})
		pass
		writer.writerow(tempRowDict)
	#
	expression_file.close()
	og_file.close()

	#print ("create", n, "mutation file")
	mutation_file = open(out_path_2 + n[:len(n)-4] + ".mu.tsv", "w+")
	writer = csv.DictWriter(mutation_file, fieldnames=FIELDNAMES2, delimiter='\t')
	for r in mutData:
		tempRowDict = {}
		for k in range(len(r)):
			tempRowDict.update({FIELDNAMES2[k]: r[k]})
		pass
		writer.writerow(tempRowDict)
	#
	mutation_file.close()

	pass
pass


