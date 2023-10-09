from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image

def mm2p(milimetros):
    return milimetros / 0.352777

def redimensioneImage(image_path):
    width, height = img.wrapOn()
    proportion = 

cnv = canvas.Canvas("Relatório.pdf", pagesize=A4)
cnv.drawCentredString(mm2p(105), mm2p(280), "Análise de dados de um conjunto de pessoas")
cnv.drawImage("temp/genreNumber.png", mm2p(50), mm2p(200), width=mm2p(110), height=mm2p(110))
cnv.save()