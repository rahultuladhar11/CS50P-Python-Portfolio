from fpdf import FPDF

def main():
    name = input("Name: ")

    # Create a PDF object
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()

    # Title “CS50 Shirtificate” centered at top
    pdf.set_font("Helvetica", style="B", size=32)
    pdf.cell(w=0, h=20, txt="", border=0, ln=1, align="C")
    pdf.cell(w=190, h=20, txt="CS50 Shirtificate", border=0, ln=1, align="C")

    # Add the shirt image centered horizontally
    pdf.image("shirtificate.png", x=10, y=70, w=190)

    # Add the user’s name in white text, placed over the shirt
    pdf.set_text_color(255, 255, 255)  # white
    pdf.set_font("Helvetica", style="B", size=24)
    # Name centered over shirt area
    pdf.cell(w=0, h=180, txt=f"{name} took CS50", border=0, align="C")

    # Save the PDF
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
