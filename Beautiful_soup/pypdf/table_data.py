from tabula import read_pdf
import ssl
url="https://www.w3.org/WAI/WCAG20/Techniques/working-examples/PDF20/table.pdf"
try:
    df=read_pdf(url)
    print(df)
except Exception as e:
    print("Error {}".format(e))