import re
import pdftotext

with open("Financial_Report_for_ABC_Labs.pdf", "rb") as fp:
    text = pdftotext.PDF(fp)
    separated_text=re.findall('stream(.*?)endstream', text, string = True)
    print(separated_text)