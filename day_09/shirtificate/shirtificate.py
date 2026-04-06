from fpdf import FPDF


class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__(orientation="portrait", format="A4")
        self.name = name

    def header(self):
        self.set_font("Times", "B", 36)
        self.set_text_color(0, 0, 0)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        
    def add_shirt(self):
        img_width = 190
        img_x = (210 - img_width) / 2
        self.image("shirtificate.png", x=img_x, y=50, w=img_width)

        self.set_font("Times", "B", 24)
        self.set_text_color(255, 255, 255)
        self.set_y(50 + 189.68)
        self.cell(0, -250, f"{self.name} took CS50", align="C")


def main():
    name = input("Name: ")
    pdf = Shirtificate(name)
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()
    pdf.add_shirt()
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
