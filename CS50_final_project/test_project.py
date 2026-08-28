import report
from medicin import Generic
import pytest

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

def test_terminal_report():
    assert report.generate_terminal_report(med_info) == None

def test_pdf_report():
    assert report.generate_pdf_report(med_info, "2026-12-3, 12:03:05") == None

def test_history_saver():
    assert report.history_saver(med_info, "2026-12-3, 12:03:05") == None