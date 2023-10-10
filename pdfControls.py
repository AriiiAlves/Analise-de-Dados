from fpdf import FPDF
from datetime import datetime
from PIL import Image

class modelPDF(FPDF):
    def header(self):
        # Colocando fonte: Times new roman em negrito tamanho 12
        self.set_font("Times", "B", 12)
        # Imprimindo número da página
        self.cell(0, 7, f"Relatório {datetime.now().strftime("%d/%m/%Y %H:%M")} -  AlvzDev", align="C")
        self.ln(20)

    def footer(self):
        # Colocando fonte: Times new roman em negrito tamanho 12
        self.set_font("Times", "I", 8)
        # Posição do cursor de 1.5 cm de distância do fundo:
        self.set_y(-15)
        # Imprimindo número da página
        self.multi_cell(0, 7, f"Página {self.page_no()}", align="C")

    def GraphicBox(self, title, description, image_path):
        # Colocando fonte: Times new roman em negrito tamanho 12
        self.set_font("Times", "B", 12)
        self.cell(0, 7, title.upper())
        self.ln(10)
        # Colocando fonte: Times new roman normal tamanho 12
        self.set_font("Times", "", 12)
        self.multi_cell(0, 7, description)
        self.ln(10)

        img_width, img_height = Image.open(image_path).size

        if img_width > self.w // 1.5 or img_height > self.h:
            while(img_width > self.w // 1.5 or img_height > self.h):
                img_width = int(img_width * 0.9)
                img_height = int(img_height * 0.9)

        self.image(image_path, x=(self.w - img_width) // 2, w=img_width, h=img_height)
        self.ln(10)