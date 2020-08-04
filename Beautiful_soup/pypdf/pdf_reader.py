import PyPDF2 as p
file=open('Pragyan.pdf','rb')
pd=p.PdfFileReader(file)
x=pd.getPage(0)

print(x.extractText())

