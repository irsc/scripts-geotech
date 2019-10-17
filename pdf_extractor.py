#import relevant pacakges
# You need to install PyPDf2 package, 
# e.g. go to PowerShell and run 'pip install pypdf2'
import os
import PyPDF2
import xlsxwriter 

#define path where the pdf files are stored
#'path' gets the address of this curent python script
#path = os.path.dirname(os.path.abspath(__file__))+"\PDFs"
path = "C:/Users/ignacio.rivero/python_WIP/PDFs"

#set empty variables for pdfFiles list and text
pdfFiles = []
text = ""

#for-loop to extract the file names stored in 'path'
#the names are saved in pdfFiles
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

#sort the filenmaes within pdfFiles list
pdfFiles.sort(key =  str.lower)

#for-loops to run through the files, read each file 
#and extract the text into 'text'	
for filename in pdfFiles:    
    filepath =str(path)+ "\\" +str(filename)
    pdffile = open(filepath,'rb')
    
#PyPDF2 reader method reading the pdf
    reader = PyPDF2.PdfFileReader(pdffile)

    #number of pages
    num_pages = reader.numPages

#For loop reading each page with method .getPage() 
#and extracting data with method .extractText()
    for sheet in range(0, num_pages):
        page =reader.getPage(sheet)
        text += f"############## Page {sheet+1} of {filename} ##################" +"\n"
        text += page.extractText()

#Create an output txt file to dump the extracted data
txtfile = 'DataExtracted.txt'
output = open (txtfile,'w')
output.write(text)
output.close()

#########################################

#Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('DataExtracted.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,"ID")
worksheet.write(0,1,"Organic content")


#select lookup word to start lookng for relevant information
lookup1 = "Test Results"
lookup2 = "Mean Organic Content (%) ="
reflines = []
counter1 = 1
counter2 = 1

with open(txtfile) as fp:
    linesall = fp.readlines()

# run throught the output to find the linenumber for the keyword
with open(txtfile) as fp:
    for num, line in enumerate(fp,1):
        if lookup1 in line:
            reflines.append(num)            
            worksheet.write(counter1,0,linesall[num])
            counter1 += 1
        elif lookup2 in line:
            reflines.append(num)            
            worksheet.write(counter2,1,linesall[num])
            counter2 += 1

