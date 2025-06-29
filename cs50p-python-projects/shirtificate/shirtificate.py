from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", format="A4")
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.set_font("Helvetica", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", align="C")
        self.ln(10)

    def shirt_img(self):
        self.image("shirtificate.png", x=15, y=60, w=180)

    def shirt_text(self, name):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(255, 255, 255)
        self.set_y(140)
        self.cell(0, 10, f"{name} took CS50", align="C")

def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.shirt_img()
    pdf.shirt_text(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
