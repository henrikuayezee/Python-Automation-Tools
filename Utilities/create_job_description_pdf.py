"""
Script: create_job_description_pdf.py
Description: Tool for create job description pdf
Category: Utilities
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch

# Job description content
job_title = "Digital Platform Annotator - Remote/In-House Opportunity"

sections = [
    ("Position Overview", [
        "We are seeking detail-oriented and tech-savvy Digital Platform Annotators to join our dynamic team for an exciting project involving task execution across various digital platforms and applications. This role offers both remote and in-house work options with start opportunities once you have passed training."
    ]),
    ("Key Responsibilities", [
        "Execute assigned tasks across multiple platforms including LinkedIn, Twitter, PowerPoint, AWS App Studio and other digital channels.",
        "Create and manage accounts on various digital platforms as required",
        "Utilize productivity tools including Microsoft Word, PowerPoint, and other office applications",
        "Work with modern platforms such as ChatGPT, AWS App Studio, and similar tools",
        "Role-play scenarios and complete tasks as directed by project managers",
        "Respond promptly to manager instructions and team communications",
        "Maintain high efficiency standards while ensuring quality output"
    ]),
    ("Required Skills & Experience", [
        "Proficiency in everyday applications: Microsoft Word, PowerPoint, Excel.",
        "Strong familiarity with social media platforms: Twitter, Instagram, Facebook, LinkedIn",
        "Experience with modern AI tools like ChatGPT",
        "Basic knowledge of AWS App Studio or similar cloud platforms",
        "Excellent written and verbal communication skills",
        "Strong attention to detail and ability to follow instructions precisely",
        "Reliable internet connection and appropriate hardware for remote work",
        "Ability to adapt quickly to new platforms and tools"
    ]),
    ("What We Offer", [
        "Comprehensive Training Program: 1-week training session starting 14th July – GHS 200 data Incentive at the end of training month.",
        "Competitive Compensation: During training and throughout the project",
        "Flexible Work Arrangement: Remote and in-house options available",
        "Immediate Start: Project begins as early as next month",
        "Professional Development: Gain experience with cutting-edge digital tools and platforms"
    ]),
    ("Training & Selection Process", [
        "Training Week (Starting Monday, 14th July):",
        "Comprehensive orientation on project expectations and procedures",
        "Hands-on training with required platforms and tools",
        "Performance evaluation based on: ",
        "  o Task completion efficiency and speed",
        "  o Responsiveness to Slack communications",
        "  o Quality and diversity of platform interactions",
        "  o Overall adaptability and learning curve",
        "Selection Criteria: Candidates who demonstrate exceptional performance during the training week will be shortlisted for the main project based on their efficiency, communication skills, and platform proficiency."
    ]),
    ("Ideal Candidate Profile", [
        "Self-motivated individuals who thrive in fast-paced environments",
        "Tech enthusiasts comfortable with learning new digital tools",
        "Strong multitaskers who can manage various platforms simultaneously",
        "Excellent time management skills with ability to meet tight deadlines",
        "Professional communicators who can maintain quality interactions across platforms"
    ]),
    ("Next Steps", [
        "1. Submit your application via this FORM",
        "2. Join the training program (1 week)",
        "3. Performance evaluation and shortlisting",
        "4. Project commencement (target: next month)"
    ]),
    ("Ready to join our innovative team?", [
        "Apply now and be part of a project that combines technology, creativity, and digital innovation. We're looking for candidates who can start immediately and are excited about working with the latest digital tools and platforms.",
        "This is an excellent opportunity for individuals looking to expand their digital skill set while contributing to meaningful projects in a collaborative environment."
    ])
]

def build_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=LETTER, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = ParagraphStyle('title', parent=styles['Heading1'], alignment=TA_CENTER, fontSize=18, spaceAfter=18)
    story.append(Paragraph(job_title, title_style))
    story.append(Spacer(1, 0.2 * inch))

    # Sections
    for section, items in sections:
        story.append(Paragraph(section, styles['Heading2']))
        if len(items) == 1:
            story.append(Paragraph(items[0], styles['Normal']))
        else:
            bullet_items = [ListItem(Paragraph(item, styles['Normal'])) for item in items]
            story.append(ListFlowable(bullet_items, bulletType='bullet', leftIndent=18))
        story.append(Spacer(1, 0.15 * inch))

    doc.build(story)

if __name__ == "__main__":
    build_pdf("Digital_Platform_Annotator_Job_Description.pdf") 