def splitinfoeff(infoeff):
	"""Splits the effect element in the info column into all of its parameters"""
	
	#Format effect element so that all parameters are separated by | and can be split 
	infoeff = infoeff.replace("EFF=","")
	infoeff = infoeff.replace("(","|")
	infoeff = infoeff.replace(")","")
	
	#Split effect info into its parameters
	infoeff = infoeff.split("|")
	
	return infoeff

def gethgvs(infoeff,lookup):
	"""Gets the HGVS format from the effect element of the info column
	effect element has to be split into an array and formated before using this function"""
	
	#Default the lookup parameters to be for c., p. and n. descriptors if none of these are set
	if ("c" not in lookup) and ("p" not in lookup) and ("n" not in lookup):
		lookup = ['c','p','n']
	
	print(lookup)

def parsevcf(file):
	"""Core function that parses the VCF file and extracts specified data from it
	This function reads the VCF file, extracts the data from the variant table, and returns specified data"""
	
	#Flag to start parsing the data in the VCF
	variantslist = False
	
	#Read each line in the VCF and print to confirm that VCF can be read
	for vcfline in file:
		#Check if the line is where the variant table starts
		if "#CHROM" in vcfline:
			#Get the headers for the columns by splitting the vcfline where where finds #CHROM, which indicates the column headers
			#The last column name will contain a new line if this is not removed
			vcfline = vcfline.replace("\n","")
			columnheaders = vcfline.split("\t")
			
			#Flag to tell the script that the following lines are part of the variant table is set
			variantslist = True
		
		#Get variant table
		if variantslist == True:
			#Convert row to list for analysis
			#The last column name will contain a new line if this is not removed
			vcfline = vcfline.replace("\n","")
			vcfline = vcfline.split("\t")
			
			#Extract the info element from the VCF row and split it into an array
			vcfrowinfo = vcfline[7]
			vcfrowinfo = vcfrowinfo.split(";")
			
			print(vcfrowinfo)