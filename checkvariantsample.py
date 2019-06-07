def checkvariantsample(details,qthreshold):
    """Checks if a variant and its sample column should be included in the
    variant list output file"""

    #Flag that a result should be kept
    keep = True

    #Remove homozygous wild type
    if details['GT'] == "homozygous wild-type":
        keep = False

    #Remove where quality score is less than specified
    if details['GQ'] is ".":
        details['GQ'] = 0
    if int(details['GQ']) < qthreshold:
        keep = False

    return keep
