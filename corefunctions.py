def splitinfoeff(infoeff):
	"""Splits the effect element in the info column into all of its parameters"""

	#Format effect element so that all parameters are separated by | and can be split
	infoeff = infoeff.replace("EFF=","")
	infoeff = infoeff.replace("(","|")
	infoeff = infoeff.replace(")","")

	print(sampledictionary)
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
