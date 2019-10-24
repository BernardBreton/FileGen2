import random
from pathlib import Path

#-----------------------------------------------------
#---------------CONFIGURATION PARAMETERS -------------
#-----------------------------------------------------
numFileToGenerate = 2
# --------specify the random range of rows that will be generated
rowLow = 100
rowHigh =101
# ----------specify the random range of  number of columns that will be generated.
colsLow =4
colsHigh = 9
#---------specify the file extention.  file names created will have format "fileX.<fileSuffix>" where X = 1,2,3,....
fileSuffix = ".dat"
#---------desitnation folder where files will be created
path = Path("C:/Users/bebre/PycharmProjects/FileIntegrity/outputFolder")
#------- specify delimeter for csv file
delimeter =','
#----  ramdomly  peturb length of data every "petrubCont" columns
peturbCount =1 #  generate random lenght every time this number is hit
peturbLow =3   # minimum length of random lenght col
peturbHigh = 7 # maximum length of random length col

#-------------end configuration----------------------------------
#----------------------------------------------------------------
def createString(lenOfString):
    result ='X'
    for x in range (1, lenOfString):
        oneChar =  str(x)
        result = result + oneChar
    return (result)

#------------------------generate 1 file------------------------------------------------------------
def generateOneFile(currentFile, numRows, numCols, delimeter):
    text = "file" + str(currentFile)+fileSuffix, "(", str(numRows) , " X ",str(numCols) +" )"

    filename = "file"+str(currentFile)+fileSuffix
    fullPath=path/filename
    print ("output file:",fullPath)
    file = open(fullPath,'w')
    # -- write header row
    for header in range (1, numCols):
        if (header == numCols - 1):
            file.write("column"+str(header))
        else:
            file.write("column"+str(header)+delimeter)
    file.write("\n")
    #-- write data
    for row in range (1, numRows):
        peturb =0
        for cols in range (1, numCols):
            if peturb == peturbCount:
                myString = createString(random.randrange(peturbLow, peturbHigh))
                peturb =0
            else:
                myString = createString(5)
            if ( cols == numCols-1 ):
                file.write (myString)
            else:
                file.write (myString+delimeter)
            peturb = peturb +1
        file.write ("\n")


    file.close()

#----------------------------------- MAIN ------------------------------------------------------------------------
for currentFile in range (1, numFileToGenerate):
    numRows = random.randrange(rowLow, rowHigh)
    numCols = random.randrange(colsLow, colsHigh)
    generateOneFile(currentFile, numRows, numCols, delimeter)


