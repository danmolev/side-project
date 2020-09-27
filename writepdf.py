import numpy as np
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont




from reportlab.pdfgen import canvas 
import StringIO




packet = StringIO.StringIO()
c = canvas.Canvas(packet, pagesize=A4, bottomup= 0)

from reportlab.lib.units import inch # move the origin up and to the left c.translate(inch,inch)
# define a large font

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

x = 365
y = 158

c.setFont("Vera", 30)
c.setFillColor("white")
c.rect(x-6,y-50,110,70,fill=1,stroke=0)




c.setFillColorRGB(0,0,0)
c.drawString(x, y, "Daniel")

c.save()


packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(file("orginal.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = file("new.pdf", "wb")
output.write(outputStream)
outputStream.close()







