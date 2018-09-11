#Import neccesary functions from core functions file
from corefunctions import splitinfoeff, gethgvs, parsevcf

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