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
			
			for info in vcfinfo:
				#Get the effect of a variant
				if "EFF=" in info:
					#Split variants by what type of effects it has
					effects = info.split("|")
					
					#Split the variant description types
					variant = effects[3]
					variant = variant.split("/")
					
					for varianttype in variant:
						if "c." in varianttype:
							cvariant = varianttype
					
					#Format as HGVS
					gene = effects[5]
					hgvs = gene + " " + cvariant
					print(hgvs)

#Open the VCF file with the given name, check for presence of file and return error if it is not present
vcffilename = "TestVCF_Filtered_Annotated.vcf"

vcffile = open(vcffilename,"r")
parsevcf(vcffile)

#try:
#	#Open VCF file
#	vcffile = open(vcffilename,"r")
#	
#	#Call function to parse VCF file
#	parsevcf(vcffile)
#	
#	#Close the file on completion
#	vcffile.close()
#except:
#	#Error if cannot find file
#	print("Error! VCF file does not exist!")
#	fileexists = False