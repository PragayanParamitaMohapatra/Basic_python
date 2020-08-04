import tabula
df = tabula.read_pdf("table.pdf", output_format="json")
print(df)