# %%
# Report generation for medicine information
import csv
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table as Richtable
from medicin import Generic
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import datetime
from reportlab.platypus import Table as Pdftable, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Improved the spcaing in code using AI

def generate_terminal_report(med_info: list) -> None:
    # generating terminal report
    for med in med_info:
        TABLE_DATA = [
            [
                f"[b #ffa500]{med.branded_name}[/]",
                f"[b blue]{med.generic_name}[/]",
                f"[b yellow]{med.composition}[/]",
            ],
            [
                f"[b yellow]{med.dosage}[/]",
                f"[b red]{med.req_doctor_prescription}[/]",
            ],
            [
                f"[b #ffa500]{med.branded_med_price}Rs[/]",
                f"[b blue]{med.generic_med_price}Rs[/]",
                f"[b green]{med.savings}Rs[/]",
            ],
        ]

    headings = [
        "Brand name",
        "Generic name",
        "Composition",
        "Dosage",
        "Doctor prescription req?",
        "Branded med price",
        "Generic med price",
        "Savings",
    ]

    for i in range(3):
        console = Console()

        if i == 0:
            table = Richtable(
                title="-----------------MedSaver Report----------------------",
                show_footer=False,
            )
        else:
            table = Richtable(show_footer=False)

        # aligning table to centre
        table_centered = Align.center(table)
        console.clear()

        if i != 1:
            if i == 2:
                i = 5

            with Live(table_centered, console=console, screen=False):
                table.add_column(headings[i], no_wrap=True)
                table.add_column(headings[i + 1], no_wrap=True)
                table.add_column(headings[i + 2], no_wrap=True)
                table.add_row(*TABLE_DATA[0 if i == 0 else 2])
                # table_width = console.measure(table).maximum
                # print("first table width:", table_width)
        else:
            i = 3
            with Live(table_centered, console=console, screen=False):
                table.add_column(headings[i], no_wrap=True)
                table.add_column(headings[i + 1], no_wrap=True)
                table.add_row(*TABLE_DATA[1])


# %%
# def generate_csv_report(med_info: list):
#     with open(
#         "med_report.csv", "w", newline=""
#     ) as csvfile:  # rewriting the file every time
#         writer = csv.writer(csvfile)
#         writer.writerow(
#             [
#                 "Brand name",
#                 "Generic name",
#                 "Composition",
#                 "Dosage",
#                 "Prescription required?",
#                 "Branded med price",
#                 "Generic med price",
#                 "You saved",
#             ]
#         )

#         for med in med_info:
#             writer.writerow(
#                 [
#                     med.branded_name,
#                     med.generic_name,
#                     med.composition,
#                     med.dosage,
#                     med.req_doctor_prescription,
#                     med.branded_med_price,
#                     med.generic_med_price,
#                     med.savings,
#                 ]
#             )


# %%
def generate_pdf_report(med_info: list, search_time)  -> None:
    c = canvas.Canvas("MedSaver_Report.pdf", pagesize=A4)
    width, height = A4  # width = 595 , height = 841

    # HEADER
    # blue background
    c.setFillColorRGB(0.031, 0.647, 0.78)  # values between 0 and 1
    c.rect(x=0, y=height - 90, width=width, height=90, fill=1, stroke=0)

    # brand name
    c.setFont("Times-Roman", size=50)
    c.setFillColor(colors.whitesmoke)
    c.drawString(x=20, y=height - 50, text="MedSaver")

    # small discription below brand
    c.setFont("Times-Roman", size=20)
    c.drawString(x=20, y=height - 72, text="Generic Medicine Finder & Price Comparison")

    # search time
    c.setFont("Times-Roman", size=20)
    c.setFillColor(colors.black)
    c.drawString(x=20, y=height - 120, text=f"Search Time: {search_time}")

    # MEDICINE INFO HEADER
    c.setFont("Times-Roman", size=24)
    c.drawString(x=20, y=height - 155, text="Medicine Information")
    c.line(20, height - 160, 570, height - 160)

    # Table with medicine details
    if med_info:
        med = med_info[0]
        composition_text = (
            ", ".join(med.composition)
            if isinstance(med.composition, (list, tuple))
            else str(med.composition)
        )
        prescription_text = "Yes" if med.req_doctor_prescription else "No"

        # setting style
        styles = getSampleStyleSheet()
        cell_style = styles["Normal"]
        cell_style.fontName = "Times-Roman"
        cell_style.fontSize = 15

        # table
        # used paragraphs as normal key value methods don't allow wrapping of long text
        table_data1 = [
            [
                Paragraph("Input Brand:", cell_style),
                Paragraph(med.branded_name, cell_style),
                Paragraph("Generic:", cell_style),
                Paragraph(med.generic_name, cell_style),
            ],
            [
                Paragraph("Composition:", cell_style),
                Paragraph(composition_text, cell_style),
                Paragraph("Doctor Prescription required?:", cell_style),
                Paragraph(prescription_text, cell_style),
            ],
            [],
            [
                Paragraph("Dosage", cell_style),
                Paragraph(med.dosage, cell_style),
            ],
            [
                Paragraph("Safety Notes", cell_style),
                Paragraph(med.safety_notes, cell_style),
            ],
        ]

        table = Pdftable(table_data1, colWidths=[100, 175, 100, 175])
        table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (3, 1), 1, colors.black,),  # making grid for upper table
                    ("SPAN", (1, 3), (3, 3)),  # extending columns
                    ("SPAN", (1, 4), (3, 4)),  # extending columns
                    ("GRID", (0, 3), (3, 4), 1, colors.black,),  # making grid for lower table
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ("BACKGROUND", (0, 0), (0, 1), colors.HexColor("#f0f0f0")),  # filling colours of headings
                    ("BACKGROUND", (2, 0), (2, 1), colors.HexColor("#f0f0f0")),
                    ("BACKGROUND", (0, 3), (0, 4), colors.HexColor("#f0f0f0")),
                ]
            )
        )

        # initial 1st table bottome coordinates

        table_btm_x_coord, table_btm_y_coord = table.wrapOn(c, width, height)
        table.drawOn(c, 20, height - 180 - table_btm_y_coord)
        # this will allow the table to move
        # downward instead of upward when gets bigger text

        # final 1st table bottome coordinate

        table_btm_x_coord, table_btm_y_coord = (20, height - 180 - table_btm_y_coord)

        # PRICE COMPARISON
        c.drawString(x=20, y=table_btm_y_coord - 50, text="Price Comparison")
        c.line(20, table_btm_y_coord - 58, 570, table_btm_y_coord - 58)

        table_data2 = [
            [
                Paragraph("Branded Price(Rs)", cell_style),
                Paragraph(str(med.branded_med_price), cell_style),
            ],
            [
                Paragraph("Generic Price(Rs)", cell_style),
                Paragraph(str(med.generic_med_price), cell_style),
            ],
            [
                Paragraph("Savings(Rs)", cell_style),
                Paragraph(str(med.savings), cell_style),
            ],
        ]
        table2 = Pdftable(table_data2, colWidths=[150, 100])
        table2.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 1, colors.black),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#f0f0f0")),
                ]
            )
        )

        table2_width, table2_height = table2.wrapOn(c, width, height)
        table2.drawOn(c, 20, table_btm_y_coord - 80 - table2_height)
        # table_data1 = [
        #     [
        #         Paragraph("Dosage", cell_style),
        #         Paragraph(med.dosage, cell_style),
        #     ],
        #     [
        #         Paragraph("Safety Notes", cell_style),
        #         Paragraph(med.safety_notes, cell_style),
        #     ]
        # ]

    # FOOTER
    # blue background
    c.setFillColorRGB(0.031, 0.647, 0.78)  # values between 0 and 1
    c.rect(x=0, y=0, width=width, height=30, fill=1, stroke=0)

    c.setFont("Times-Roman", size=20)
    c.setFillColor(colors.whitesmoke)
    c.drawString(x=20, y=8, text="Thank You")

    c.showPage()
    c.save()


#%%
def history_saver(med_info: list, search_time) -> None :
    with open(
        "history.csv", "a",newline=""
    ) as csvfile:  
        
        header = [
            "Search time",
            "Brand name",
            "Generic name",
            "Branded med price",
            "Generic med price",
            "You saved",
        ]

        
        writer = csv.DictWriter(csvfile,fieldnames=header)
              
        writer.writerow({
            "Search time": search_time,
            "Brand name": med_info[0].branded_name,
            "Generic name": med_info[0].generic_name,
            "Branded med price": med_info[0].branded_med_price,
            "Generic med price": med_info[0].generic_med_price,
            "You saved": med_info[0].savings,
        })


def main():
    # sample med_info
    med_info = [
        Generic(
            branded_name="Allegra",
            generic_name="Fexofenadine",
            composition=["Fexofenadine Hydrochloride"],
            dosage="120 mg Tablet",
            req_doctor_prescription=True,
            branded_med_price=180.0,
            generic_med_price=75.0,
            savings=105.0,
            safety_notes=(
                "May cause headache, dizziness, nausea. Less likely to cause "
                "drowsiness compared to older antihistamines. Consult doctor if "
                "pregnant, breastfeeding, or have kidney/liver disease. Avoid "
                "alcohol consumption. Do not exceed the prescribed dose."
            ),
        )
    ]
    # history_saver(med_info, "12-4-4, 12:34:4")

if __name__ == "__main__":
    main()



# generate_pdf_report(med_info)
# %%
