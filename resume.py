import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
)

def build_resume(filename="Aadesh_Shukla_Resume_Matched.pdf"):
    # Page setup: Letter size with precise 0.35 in (25 pt) margins for exact 1-page fit
    margin = 25
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=margin,
        rightMargin=margin,
        topMargin=22,
        bottomMargin=20
    )

    printable_width = 612 - 2 * margin  # 562 pt

    # Palette definition
    PRIMARY = colors.HexColor("#1A365D")    # Deep Slate / Navy
    SECONDARY = colors.HexColor("#2B6CB0")  # Rich Blue accent
    TEXT_DARK = colors.HexColor("#1A202C")  # Near black
    TEXT_MUTED = colors.HexColor("#4A5568") # Neutral slate gray
    TAG_BG = colors.HexColor("#EDF2F7")     # Light pill tag bg
    TAG_TEXT = colors.HexColor("#2D3748")   # Tag text dark
    BORDER_COLOR = colors.HexColor("#CBD5E0")

    styles = getSampleStyleSheet()

    # Base typography styles
    style_name = ParagraphStyle(
        'Name',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=22,
        textColor=PRIMARY,
        alignment=1
    )

    style_tagline = ParagraphStyle(
        'Tagline',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=SECONDARY,
        alignment=1,
        spaceAfter=3
    )

    style_contact = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10,
        textColor=TEXT_MUTED,
        alignment=1
    )

    style_section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=PRIMARY,
        spaceAfter=3
    )

    style_summary = ParagraphStyle(
        'SummaryText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=TEXT_DARK,
        alignment=4  # Justified
    )

    style_proj_title = ParagraphStyle(
        'ProjTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=TEXT_DARK
    )

    style_proj_links = ParagraphStyle(
        'ProjLinks',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=10,
        textColor=SECONDARY,
        alignment=2
    )

    style_bullet = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.4,
        leading=9.4,
        textColor=TEXT_DARK,
        leftIndent=8,
        firstLineIndent=-8,
        spaceAfter=1
    )

    style_pill = ParagraphStyle(
        'TechPill',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=6.4,
        leading=8,
        textColor=TAG_TEXT
    )

    style_subhead = ParagraphStyle(
        'CategorySubhead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=SECONDARY,
        spaceBefore=3,
        spaceAfter=1
    )

    style_skill_pill = ParagraphStyle(
        'SkillPill',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.5,
        textColor=TEXT_DARK
    )

    style_cert_title = ParagraphStyle(
        'CertTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.6,
        leading=9.2,
        textColor=TEXT_DARK
    )

    style_cert_sub = ParagraphStyle(
        'CertSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.5,
        textColor=TEXT_MUTED
    )

    style_edu_degree = ParagraphStyle(
        'EduDegree',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=TEXT_DARK
    )

    style_edu_meta = ParagraphStyle(
        'EduMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.2,
        leading=9,
        textColor=TEXT_MUTED
    )

    style_footer = ParagraphStyle(
        'FooterText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9,
        textColor=SECONDARY,
        alignment=1
    )

    def section_header_table(title, width):
        p = Paragraph(f"<b>{title.upper()}</b>", style_section_heading)
        t = Table([[p]], colWidths=[width])
        t.setStyle(TableStyle([
            ('LINEBELOW', (0, 0), (-1, -1), 0.8, SECONDARY),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ]))
        return t

    def format_badges(items_list, cell_width):
        cells = []
        for it in items_list:
            cells.append(Paragraph(f"• {it}", style_pill))
        # Format into rows of 3
        rows = []
        cur_row = []
        for i, c in enumerate(cells):
            cur_row.append(c)
            if len(cur_row) == 3:
                rows.append(cur_row)
                cur_row = []
        if cur_row:
            while len(cur_row) < 3:
                cur_row.append(Paragraph("", style_pill))
            rows.append(cur_row)
        
        col_w = cell_width / 3.0
        t = Table(rows, colWidths=[col_w, col_w, col_w])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), TAG_BG),
            ('TOPPADDING', (0, 0), (-1, -1), 1.5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
            ('LEFTPADDING', (0, 0), (-1, -1), 4),
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        return t

    story = []

    # 1. HEADER
    story.append(Paragraph("Aadesh Shukla", style_name))
    story.append(Paragraph("FULL-STACK DEVELOPER &bull; AI INTEGRATIONS &bull; MERN STACK", style_tagline))
    contact_html = "Hyderabad, Telangana &nbsp;&bull;&nbsp; +91 9110328513 &nbsp;&bull;&nbsp; aadeshshukla470@gmail.com"
    story.append(Paragraph(contact_html, style_contact))
    links_html = '<font color="#2B6CB0"><u>github.com/aadeshshukla</u></font> &nbsp;&bull;&nbsp; <font color="#2B6CB0"><u>LinkedIn</u></font> &nbsp;&bull;&nbsp; <font color="#2B6CB0"><u>aadeshportfolio.vercel.app</u></font>'
    story.append(Paragraph(links_html, style_contact))
    story.append(Spacer(1, 4))

    # 2. SUMMARY
    story.append(section_header_table("Summary", printable_width))
    story.append(Spacer(1, 2))
    summary_text = (
        "Final-year B.Tech CS student with hands-on experience building full-stack web apps and "
        "integrating browser-based and cloud AI models. Proficient in the MERN stack with a track "
        "record of shipping production-ready projects. Seeking an internship or remote role to "
        "contribute to ambitious engineering teams."
    )
    story.append(Paragraph(summary_text, style_summary))
    story.append(Spacer(1, 5))

    # 3. TWO-COLUMN LAYOUT (Projects & Education vs Skills & Certifications)
    left_w = 346
    gap_w = 14
    right_w = 202

    # --- LEFT COLUMN (Projects + Education) ---
    left_flowables = []
    left_flowables.append(section_header_table("Projects", left_w))
    left_flowables.append(Spacer(1, 3))

    # Project 1: Pathfinder AI
    p1_head = Table([
        [Paragraph("<b>Pathfinder AI</b> &ndash; AI Learning Roadmap Generator", style_proj_title),
         Paragraph("<u>Live</u> | <u>Source</u>", style_proj_links)]
    ], colWidths=[left_w - 75, 75])
    p1_head.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    left_flowables.append(p1_head)
    left_flowables.append(Paragraph("&bull; Architected a full-stack app generating personalized learning paths via Groq Llama 3.1.", style_bullet))
    left_flowables.append(Paragraph("&bull; Implemented JWT-based authentication and encrypted password storage for private user dashboards.", style_bullet))
    left_flowables.append(Paragraph("&bull; Built a high-performance React 18 + Vite frontend with glassmorphism UI & Framer Motion.", style_bullet))
    left_flowables.append(Paragraph("&bull; Secured backend with Express Rate Limit and CORS for reliable API communication.", style_bullet))
    left_flowables.append(Spacer(1, 1.5))
    left_flowables.append(format_badges(["MongoDB", "Express.js", "React 18", "Node.js", "Groq SDK", "Framer Motion"], left_w))
    left_flowables.append(Spacer(1, 4))

    # Project 2: Life Tracker
    p2_head = Table([
        [Paragraph("<b>Life Tracker</b> &ndash; Privacy-First AI Diary", style_proj_title),
         Paragraph("<u>Live</u> | <u>Source</u>", style_proj_links)]
    ], colWidths=[left_w - 75, 75])
    p2_head.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    left_flowables.append(p2_head)
    left_flowables.append(Paragraph("&bull; Built a zero-server diary running semantic search models directly in browser via Transformers.js.", style_bullet))
    left_flowables.append(Paragraph("&bull; Engineered local-first data architecture with IndexedDB (Dexie.js) ensuring 100% offline privacy.", style_bullet))
    left_flowables.append(Paragraph("&bull; Delivered natural language memory queries, mood analytics, and JSON export/import.", style_bullet))
    left_flowables.append(Spacer(1, 1.5))
    left_flowables.append(format_badges(["React 19", "Transformers.js", "Dexie.js", "IndexedDB", "Lucide React", "Responsive UI"], left_w))
    left_flowables.append(Spacer(1, 4))

    # Project 3: Results Analytics
    p3_head = Table([
        [Paragraph("<b>Results Analytics</b> &ndash; JNTUH Academic Dashboard", style_proj_title),
         Paragraph("<u>Source</u>", style_proj_links)]
    ], colWidths=[left_w - 60, 60])
    p3_head.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    left_flowables.append(p3_head)
    left_flowables.append(Paragraph("&bull; Built a React + Vite SPA enabling students to fetch JNTUH results by roll number in real time.", style_bullet))
    left_flowables.append(Paragraph("&bull; Designed an analytics dashboard surfacing semester-wise marks, grades, credits, and SGPA.", style_bullet))
    left_flowables.append(Paragraph("&bull; Rendered interactive charts and summary cards to track academic performance trends.", style_bullet))
    left_flowables.append(Spacer(1, 1.5))
    left_flowables.append(format_badges(["React 18", "Vite", "JavaScript", "CSS3", "REST APIs", "Analytics UI"], left_w))
    left_flowables.append(Spacer(1, 4))

    # Project 4: Mausam.ai
    p4_head = Table([
        [Paragraph("<b>Mausam.ai</b> &ndash; AI-Powered Chatbot", style_proj_title),
         Paragraph("<u>Live</u> | <u>Source</u>", style_proj_links)]
    ], colWidths=[left_w - 75, 75])
    p4_head.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    left_flowables.append(p4_head)
    left_flowables.append(Paragraph("&bull; Integrated Meta Llama API for advanced conversational NLP and streaming dialogue.", style_bullet))
    left_flowables.append(Paragraph("&bull; Developed responsive real-time chat UI with async state management across client and AI engine.", style_bullet))
    left_flowables.append(Spacer(1, 1.5))
    left_flowables.append(format_badges(["React.js", "Llama API", "JavaScript", "HTML5", "CSS3", "Async State"], left_w))
    left_flowables.append(Spacer(1, 5))

    # Education (Bottom Left)
    left_flowables.append(section_header_table("Education", left_w))
    left_flowables.append(Spacer(1, 2))
    left_flowables.append(Paragraph("<b>B.Tech &ndash; Computer Science</b>", style_edu_degree))
    left_flowables.append(Paragraph("St. Mary's Integrated Campus (JNTUH Affiliated), Hyderabad", style_edu_meta))
    left_flowables.append(Paragraph("<i>Expected June 2027</i>", style_edu_meta))

    # --- RIGHT COLUMN (Skills + Certifications) ---
    right_flowables = []
    right_flowables.append(section_header_table("Technical Skills", right_w))
    right_flowables.append(Spacer(1, 2))

    def skill_group(category, skills_text):
        return [
            Paragraph(f"<b>{category.upper()}</b>", style_subhead),
            Paragraph(skills_text, style_skill_pill),
            Spacer(1, 2)
        ]

    right_flowables.extend(skill_group("Languages", "JavaScript (ES6+), Python, HTML5, CSS3, SQL, Java"))
    right_flowables.extend(skill_group("Frontend", "React 18/19, Vite, Framer Motion, Responsive UI"))
    right_flowables.extend(skill_group("Backend", "Node.js, Express.js, REST APIs, JWT Auth"))
    right_flowables.extend(skill_group("Databases", "MongoDB, IndexedDB, MySQL"))
    right_flowables.extend(skill_group("AI & Tools", "Transformers.js, Agentic AI, MCP Servers, GPT-Codex, Claude, Git, Vercel"))
    right_flowables.append(Spacer(1, 3))

    right_flowables.append(section_header_table("Certifications", right_w))
    right_flowables.append(Spacer(1, 2))

    certifications = [
        ("Claude Code In Action", "Anthropic"),
        ("Claude Code 101", "Anthropic &bull; verify.skilljar.com"),
        ("Artificial Intelligence Fundamentals", "IBM SkillsBuild &bull; credly.com verify"),
        ("Front-End Software Engineering Job Sim", "Skyscanner &times; Forage &bull; May 2026"),
        ("Quantitative Research Job Sim", "JPMorgan Chase &times; Forage &bull; May 2026"),
        ("JavaScript Skill Certificate", "TestDome"),
        ("Python Skill Certificate", "TestDome"),
    ]

    for cert_title, cert_sub in certifications:
        right_flowables.append(Paragraph(f"&bull; <b>{cert_title}</b>", style_cert_title))
        right_flowables.append(Paragraph(f"&nbsp;&nbsp;{cert_sub}", style_cert_sub))
        right_flowables.append(Spacer(1, 2))

    # Combine two columns into master layout table
    main_table = Table([[left_flowables, right_flowables]], colWidths=[left_w, right_w])
    main_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (0,0), gap_w / 2),
        ('LEFTPADDING', (1,0), (1,0), gap_w / 2),
    ]))

    story.append(main_table)
    story.append(Spacer(1, 6))

    # 4. FOOTER
    footer_table = Table([
        [Paragraph('<font color="#2B6CB0"><u>aadeshportfolio.vercel.app</u></font> &nbsp;&bull;&nbsp; <font color="#2B6CB0"><u>github.com/aadeshshukla</u></font>', style_footer)]
    ], colWidths=[printable_width])
    footer_table.setStyle(TableStyle([
        ('LINEABOVE', (0, 0), (-1, -1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(footer_table)

    doc.build(story)

if __name__ == "__main__":
    build_resume()