import streamlit as st
import pdfplumber
import docx
import os
import google.generativeai as genai
from jinja2 import Environment, FileSystemLoader
import streamlit.components.v1 as components
import json
import re
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("📄 AI Resume Optimiser & Generator")
st.write("Upload your resume and paste a job description to get an ATS-friendly optimised version")

uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
job_description = st.text_area("Paste Job Description", height=200)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('resume_template.html')

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    text = ""
    doc = docx.Document(file)
    for p in doc.paragraphs:
        text += p.text + "\n"
    return text

if st.button("Optimised Resume"):
    if uploaded_file and job_description:
        if uploaded_file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_file)
        else:
            resume_text = extract_text_from_docx(uploaded_file)
        

        prompt = f"""
        You are an expert resume writer.
        Optimise the following resume for this job description:
        Resume:
        {resume_text}
        Job Description:
        {job_description}
        Provide:
        1. The optimised resume (ATS friendly, professional format)
        2. Divide the resume into sections 
            a. Full Name followed by email id (if given), contact number (if given)
            b. Contact Details
                1)Email Id (if available)
                2)Contact Number (if available)
                3)Social Media Accounts eg. LinkedIn/Leetcode/Codeforces/Codolio/Instagram/Facebook etc (if available)
            b. Education
                1)School/College/Institute Name
                2)Start Date and End Date (if available)
                3)Course Name (if available)
                4)Grade (if available)
            c. Experience instruction -> FOLLOW REVERSE CHRONOLOGICAL ORDER
                1)Company Name (if available)
                2)Start Date and End Date (if available)
                3)Role (if available)
                4)Location (if available)
                5)Description of your job/internship (if available)
                6)Work Link (if available)
            d. Skills
                1)Skill name (if available)
            e. Projects (if required) instruction -> FOLLOW REVERSE CHRONOLOGICAL ORDER
                1)Project Name (if available)
                2)Start Date and End Date (if available)
                3)Role (if available)
                4)Location (if available)
                5)Description of your job/internship (if available)
                3)Project Link OR Code link (if available)
            f. Achievements
                1)Description (if available)
            g. Languages
                1) Language Name (if available)
            h. Certifications
                1) Certification Name (if available)
                2) Certificate Link (if available)
        2. A bullet list of key changes made

        Give the details in this format
        Full Name : <Full Name>
        Education : <Education>
        Experience : <Experience>
        Skills : <Skills>
        Projects : <Projects>
        Achievements : <Achievements>
        Languages : <Languages>
        Certifications : <Certifications>
        AS JSON FORMAT WITH KEYS AS Name, Education, Experience, Skills, Projects, Achievements, Languages, Certifications, Key_Changes
        For Values, 
        Name : string
        Education : List of inner jsons with keys as specified in the format
        Experience : List of inner jsons with keys as specified in the format
        Skills : List of different skill names
        Projects : List of inner jsons with keys as specified in the format
        Achievements : List of Achievements
        Languages : List of Languages
        Certifications : List of Certifications
        Key_Changes : List of Key Changes
        USE ATS FRIENDLY KEYWORDS DEPENDING UPON JOB DESCRIPTION
        """

        with st.spinner("Optimising your resume..."):
            response = model.generate_content(prompt)
            raw_text = response.text.strip()

            # If Gemini returns code fences like ```json ... ```
            if raw_text.startswith("```"):
                raw_text = re.sub(r"^```[a-zA-Z]*\n", "", raw_text)  # remove opening fence
                raw_text = re.sub(r"```$", "", raw_text)  # remove closing fence
            
            print(raw_text)
            try:
                resume_json = json.loads(raw_text)
            except json.JSONDecodeError as e:
                st.error(f"❌ JSON decoding failed: {e}")
                st.write("Raw response was:", raw_text)
                st.stop()
            rendered_html = template.render(**resume_json)

            # with open("output_resume.html", "w", encoding="utf-8") as f:
            #     f.write(rendered_html)

            # # Convert HTML to PDF
            # pdf_path = "output_resume.pdf"
            # HTML("output_resume.html").write_pdf("output_resume.pdf")

            # # Display PDF download
            # with open(pdf_path, "rb") as f:
            #     st.download_button(
            #         label="📥 Download Optimised Resume PDF",
            #         data=f,
            #         file_name="Optimised_Resume.pdf",
            #         mime="application/pdf"
            #     )

            # Preview in browser
            components.html(rendered_html, height=1000, scrolling=True)
            # st.markdown(rendered_html, unsafe_allow_html=True)
    else:
        st.warning("Please upload a resume and enter the job description.")



