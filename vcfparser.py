

#Open the VCF file with the given name
vcffilename = "TestVC_Filtered_Annotated.vcf"
try:
	vcffile = open(vcffilename, "r")
	fileexists = True
except:
	print("Error! VCF file does not exist!")
	fileexists = False

	
if fileexists == True:
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
			
			#Generate HGVS variant description
			##if len(vcfrow[3] < vcfrow[4])
				
			hgvs = "g." + vcfrow[0] + ":" + vcfrow[1] + vcfrow[3] + ">" + vcfrow[4]
			
			print(hgvs)
	
	vcffile.close()