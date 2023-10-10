from fpdf import FPDF

class PDF(FPDF):
    def TitlePage(self, title, subtitle = ""):
        # Colocando fonte: Times new roman em negrito tamanho 16
        self.set_font = ("Times", "B", 16)
        # Imprimindo título
        self.multi_cell(0, 9, title, align="C", border=1)
        # Quebra de linha
        self.ln(10)

        # Colocando fonte: Times new roman normal tamanho 14
        self.set_font = ("Times", "", 14)
        # Imprimindo subtítulo
        self.multi_cell(0, 7, subtitle, align="C", border=1)
        # Quebra de linha
        self.ln(10)

    def Title():
        return()
    def Subtitle():
        return()
    def Summary():
        return()
    def l1Title():
        return()
    def l2Title():
        return()
    def l3Title():
        return()

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque libero velit, ultrices eget suscipit non, sagittis vitae orci. Cras quis nisl nunc. Vestibulum venenatis tellus at pellentesque luctus. Phasellus ullamcorper condimentum tellus fringilla euismod. Donec mi enim, ultrices feugiat tincidunt id, tristique tincidunt nibh. Fusce consequat dapibus elit, a commodo velit. Maecenas posuere augue nec suscipit lacinia. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean mollis elementum nisl imperdiet ornare. Fusce a maximus elit. Curabitur et lorem ac nisl ultricies feugiat."

pdf = PDF()
pdf.add_page()
pdf.TitlePage(title="PDF archive test", subtitle="Nothing")
pdf.output("Relatório.pdf")