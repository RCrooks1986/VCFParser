#Required libraries
from getvariantdescription import getvariantdescription
from parsesample import parsesample
from checkvariantsample import checkvariantsample
from maketempdir import maketempdir
import os

path = "VCFParser"
maketempdir(path)

#Specify the name of your file manager here
filemanager = "nautilus"

#Open folder onto screen
folderopencommand = filemanager + " " + path
os.system(folderopencommand)

#Ask user to place their VCF file in the folder
input("Copy your input file into the folder and press Enter to continue...")

#Get list of VCF files and prompt for user selection
files = os.listdir(path)
listvcfs = []
#vcfindex = 1
for vcf in files:
    if vcf.endswith(".vcf"):
        listvcfs.append(vcf)
for index, item in enumerate(listvcfs,1):
    vcfselection = str(index) + ". " + str(item)
    print(vcfselection)


vcfchoice = input("Which no. VCF file would you like you use? ")
vcfchoice = int(vcfchoice)
vcfchoice = vcfchoice-1
vcffilename = listvcfs[vcfchoice]

#Get quality score
quality = input("What quality score would you like to have as a cut off? ")
quality = int(quality)

#Remove this later as file will be defined by input
vcffilename = path + "/" + vcffilename

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

        variantdescription = getvariantdescription(info)

        outputfile = path + "/Output.txt"
        outputfile = open(outputfile,'a+')

        if variantdescription is not False:
            for sampleid in samplenames:
                sampletext = vcfline[sampleid]
                sampledetails = parsesample(sampletext,format)

                accept = checkvariantsample(sampledetails,quality)

                if accept is True:
                    outputlinetext = sampleid + " " + variantdescription + " " + sampledetails['GT'] + " " + sampledetails['GQ'] + "\n"
                    outputlinetext = f"{sampleid}\t{variantdescription}\t{sampledetails['GT']}\t{sampledetails['GQ']}\n"
                    outputfile.write(outputlinetext)

outputfile.close()
