#Open the VCF file with the given name
vcffilename = "TestVCF_Filtered_Annotated.vcf"
vcffile = open(vcffilename, "r")

#Read each line in the VCF and print to confirm that VCF can be read
for vcfline in vcffile:
	print(vcfline)

vcffile.close()