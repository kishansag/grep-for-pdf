import sys
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 

def search(toBeSearched, searchedIn):
    mylist = []
    mystring= ""

    for letter in searchedIn:
	mystring = mystring + letter
	if letter == '\n':
		#print mystring
		mylist.append(mystring)
		mystring = ""
    for index in range(len(mylist)):
	if toBeSearched in mylist[index]:
		print mylist[index]

	
#search("p", "pofdpfopgod")   
search(sys.argv[1],convert(sys.argv[2]))
#search("p", convert("../Untitleddocument.pdf"))    
#print convert("../Untitleddocument.pdf")
