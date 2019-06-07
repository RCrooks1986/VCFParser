#info = "AC=1;AF=0.021;AN=48;BaseQRankSum=0.393;ClippingRankSum=0;DB;DP=6194;ExcessHet=3.0103;FS=0.523;InbreedingCoeff=-0.0213;MLEAC=1;MLEAF=0.021;MQ=60;MQRankSum=0;QD=8.18;ReadPosRankSum=1.3;SOR=0.64;set=variant;EFF=synonymous_variant(LOW|SILENT|gaC/gaT|p.Asp157Asp/c.471C>T|351|WNT4|protein_coding|CODING|ENST00000290167|4|A)"

def getvariantdescription(info):
    #Break the info column into its elements
    info = info.split(";")
    variantdescription = False
    for element in info:
        if element.find("EFF=",0,4) is 0:
            #Get the bracketed section of the effect element
            element = element[element.find("(")+1:element.find(")")]

            element = element.split("|")
            change = element[3]
            gene = element[5]

            #Get c. and p. descriptors
            pchange = ""
            cchange = ""
            change = change.split("/")
            for descriptor in change:
                if descriptor.find("p.",0,2) is 0:
                    pchange = descriptor
                elif descriptor.find("c.",0,2) is 0:
                    cchange = descriptor

            if cchange is not "":
                variantdescription = gene + ":" + cchange
            if pchange is not "":
                variantdescription = variantdescription + "(" + pchange + ")"

    if variantdescription is "":
        variantdescription = False
    return variantdescription
