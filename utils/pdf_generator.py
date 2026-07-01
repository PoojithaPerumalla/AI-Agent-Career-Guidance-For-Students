from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import streamlit as st
from utils.theme import apply_theme

apply_theme()
def generate_report(filename, skills, career, score, goal):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("CareerPilot AI Report", styles['Title']))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"<b>Skills:</b> {skills}", styles['BodyText']))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"<b>Career Goal:</b> {goal}", styles['BodyText']))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"<b>Career Recommendation:</b><br/>{career}", styles['BodyText']))
    content.append(Spacer(1, 12))

    content.append(Paragraph(f"<b>Career Readiness Score:</b><br/>{score}", styles['BodyText']))

    doc.build(content)