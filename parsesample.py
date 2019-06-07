def parsesample(sampletext,parsing):
	'''This function converts the text about the sample in the VCF file into
	data about whether the variant was found in the VCF file and the quality
	score

	Inputs are the sample text and the values for the elements in the colon
	separated text'''
	#Remove "s from text and split into array
	sampletext = sampletext.replace('"','')
	sampledetails = sampletext.split(":")

	#Turn parsing details into an array
	parsing = parsing.split(":")
	#sampletext = "0/0:47,0:47:99:0,117,1751"
	#parseinstructions = "GT:AD:DP:GQ:PL";

	#Turn sample details into a dictionary
	sampledictionary = {}
	sampledetailskey = 0
	for field in parsing:
		sampledictionary[field] = sampledetails[sampledetailskey]
		sampledetailskey = sampledetailskey+1

	#Identify if heterozygous or homozygous for variant
	if sampledictionary['GT'] == '0/1' or sampledictionary['GT'] == '1/0':
		sampledictionary['GT'] = "heterozygous"
	elif sampledictionary['GT'] == '1/1':
		sampledictionary['GT'] = "homozygous variant"
	elif sampledictionary['GT'] == './1' or sampledictionary['GT'] == '1/.':
		sampledictionary['GT'] = "compound heterozygous"
	elif sampledictionary['GT'] == '0/0':
		sampledictionary['GT'] = "homozygous wild-type"

	return sampledictionary
