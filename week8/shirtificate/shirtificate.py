from fpdf import FPDF

class Shirt:

    def __init__(self,name):
        self.name = name
        self.pdf()

    @classmethod
    def get(cls):
        name = input("Full name: ").strip()
        return cls(name)
    
    def pdf(self):
        pdf = FPDF(orientation="portrait", format="a4")
        pdf.add_page()

        # set header
        pdf.set_font("helvetica","",50)
        pdf.text(40,40,"CS50 Shirtificate")

        # add the image
        pdf.image("shirtificate.png","C",60,pdf.epw)

        # add text to image
        pdf.set_font("helvetica","",28)
        pdf.set_text_color(255,255,255)
        pdf.cell(0,250,f"{self.name} took CS50",align="C")

        # save the image as a PDF
        pdf.output("shirtificate.pdf")

        
def main():
    Shirt.get()

if __name__ == "__main__":
    main()
