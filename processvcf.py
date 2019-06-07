#Required libraries
from getvariantdescription import getvariantdescription
from parsesample import parsesample
from checkvariantsample import checkvariantsample
from maketempdir import maketempdir

path = "VCFParser"
maketempdir(path)

#Ask user to place their
input("Copy your input file into the folder and press Enter to continue...")

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
print(onlyfiles)

#Remove this later as file will be defined by input
vcffilename = "TestVCF_Filtered_Annotated.vcf"
quality = 0

#Open VCF file and set flag to true
vcffile = open(vcffilename,"r")

#Flag to start parsing the data in the VCF
variantslist = False

#List of column headings which are not samples
nonsamplenames = ["#CHROM","POS","ID","REF","ALT","QUAL","FILTER","INFO","FORMAT"]

#Read each line in the VCF and print to confirm that VCF can be read
for vcfline in vcffile:
    #Check if the line is where the variant table starts
    if "#CHROM" in vcfline:
        #Get the headers for the columns by splitting the vcfline where the
        #script finds #CHROM, which indicates the column headers
        #The last column name will contain a new line if this is not removed
        vcfline = vcfline.replace("\n","")
        columnheaders = vcfline.split("\t")
        #Sample names are any column headings that are not in the list
        samplenames = [x for x in columnheaders if x not in nonsamplenames]

        #Flag to tell the script that the following lines are part of the variant table is set
        variantslist = True
    #Get variant table
    elif variantslist == True:
        #Convert row to list for analysisvariantdescription
        #The last column name will contain a new line if this is not removed
        vcfline = vcfline.replace("\n","")
        vcfline = vcfline.split("\t")

        vcfline = dict(zip(columnheaders,vcfline))

        format = vcfline['FORMAT']
        info = vcfline['INFO']
        #info = info.split(";")

        variantdescription = getvariantdescription(info)

        if variantdescription is not False:
            for sampleid in samplenames:
                sampletext = vcfline[sampleid]
                sampledetails = parsesample(sampletext,format)

                accept = checkvariantsample(sampledetails,quality)

                #if accept is True:
                #    print(sampleid + " " + variantdescription + " " + sampledetails['GT'] + " " + sampledetails['GQ'])
