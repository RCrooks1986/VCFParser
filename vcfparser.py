def splitinfoeff(infoeff):
	"""Splits the effect element in the info column into all of its parameters"""
	#Format effect element so that all parameters are separated by | and can be split 
	infoeff = infoeff.replace("EFF=","")
	infoeff = infoeff.replace("(","|")
	infoeff = infoeff.replace(")","")
	
	#Split effect info into its parameters
	infoeff = infoeff.split("|")
	
	return infoeff

def parsevcf(file):
	"""Core function that parses the VCF file and extracts specified data from it
	This function reads the VCF file, extracts the data from the variant table, and returns specified data"""
	#Flag to start parsing the data in the VCF
	variantslist = False
	
	#Read each line in the VCF and print to confirm that VCF can be read
	for vcfline in vcffile:
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
			vcfrow = vcfline.split("\t")
			
			#Extract VCF info by splitting
			vcfinfo = vcfrow[7].split(";")
			
			for infoelement in vcfinfo:
				#Get the effect of a variant
				if "EFF=" in infoelement:
					infoelement = splitinfoeff(infoelement)
					
					print(infoelement)

#Open the VCF file with the given name, check for presence of file and return error if it is not present
vcffilename = "TestVCF_Filtered_Annotated.vcf"

try:
	#Open VCF file and set flag to true
	vcffile = open(vcffilename,"r")
	
	parsevcf(vcffile)
	
	#Close the file on completion
	vcffile.close()
except IOError:
	#Display error if cannot find file and set flag to true
	print("Error! VCF file does not exist!")	