import streamlit as st
from jinja2 import Environment, FileSystemLoader
import streamlit.components.v1 as components
import json

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('generated_resume.html')

st.title("Resume Builder with Fixed Sections")
st.header("U DON'T NEED TO FILL ALL THE FIELDS UNDER EACH SECTION, THEY ARE OPTIONAL")
# --- Personal Info ---
st.header("Full Name")
full_name = st.text_input("Full Name", key="full_name")
st.header("Contact")
email = st.text_input("Email", key="email")
phone = st.text_input("Phone Number", key="phone")

# --- Social Media Accounts (Max 5) ---
st.header("Social Media Accounts (Max 5)")
if "accounts" not in st.session_state:
    st.session_state.accounts = [{"platform": "", "link": ""} for _ in range(5)]

for i in range(5):
    st.session_state.accounts[i]["platform"] = st.text_input(
        f"Platform #{i+1}", value=st.session_state.accounts[i]["platform"], key=f"account_platform_{i}"
    )
    st.session_state.accounts[i]["link"] = st.text_input(
        f"Link #{i+1}", value=st.session_state.accounts[i]["link"], key=f"account_link_{i}"
    )

# --- Education (Max 5) ---
st.header("Education (Max 5)")
if "educations" not in st.session_state:
    st.session_state.educations = [
        {"STUDY_PLACE": "", "START_DATE": "", "END_DATE": "", "COURSE": "", "GRADE": ""}
        for _ in range(5)
    ]

for i in range(5):
    st.session_state.educations[i]["STUDY_PLACE"] = st.text_input(
        f"School/College/Institute Name #{i+1}",
        value=st.session_state.educations[i]["STUDY_PLACE"],
        key=f"study_place_{i}",
    )
    st.session_state.educations[i]["START_DATE"] = st.text_input(
        f"Start Date #{i+1}",
        value=st.session_state.educations[i]["START_DATE"],
        key=f"start_date_edu_{i}",
    )
    st.session_state.educations[i]["END_DATE"] = st.text_input(
        f"End Date #{i+1}",
        value=st.session_state.educations[i]["END_DATE"],
        key=f"end_date_edu_{i}",
    )
    st.session_state.educations[i]["COURSE"] = st.text_input(
        f"Course Name #{i+1}",
        value=st.session_state.educations[i]["COURSE"],
        key=f"course_{i}",
    )
    st.session_state.educations[i]["GRADE"] = st.text_input(
        f"Grade #{i+1}",
        value=st.session_state.educations[i]["GRADE"],
        key=f"grade_{i}",
    )

# --- Experience (Max 10) ---
st.header("Experience (Reverse Chronological Order, Max 10)")
if "experiences" not in st.session_state:
    st.session_state.experiences = [
        {
            "COMPANY": "",
            "START_DATE": "",
            "END_DATE": "",
            "ROLE": "",
            "LOCATION": "",
            "DESCRIPTION": "",
            "LINK": "",
        }
        for _ in range(10)
    ]

for i in range(10):
    st.markdown(f"### Experience #{i+1}")
    st.session_state.experiences[i]["COMPANY"] = st.text_input(
        f"Company Name #{i+1}",
        value=st.session_state.experiences[i]["COMPANY"],
        key=f"company_{i}",
    )
    st.session_state.experiences[i]["START_DATE"] = st.text_input(
        f"Start Date #{i+1}",
        value=st.session_state.experiences[i]["START_DATE"],
        key=f"start_date_exp_{i}",
    )
    st.session_state.experiences[i]["END_DATE"] = st.text_input(
        f"End Date #{i+1}",
        value=st.session_state.experiences[i]["END_DATE"],
        key=f"end_date_exp_{i}",
    )
    st.session_state.experiences[i]["ROLE"] = st.text_input(
        f"Role #{i+1}", value=st.session_state.experiences[i]["ROLE"], key=f"role_{i}"
    )
    st.session_state.experiences[i]["LOCATION"] = st.text_input(
        f"Location #{i+1}",
        value=st.session_state.experiences[i]["LOCATION"],
        key=f"location_{i}",
    )
    st.session_state.experiences[i]["DESCRIPTION"] = st.text_area(
        f"Job Description #{i+1}",
        value=st.session_state.experiences[i]["DESCRIPTION"],
        key=f"desc_{i}",
        height=100,
    )
    st.session_state.experiences[i]["LINK"] = st.text_input(
        f"Work Link #{i+1}", value=st.session_state.experiences[i]["LINK"], key=f"work_link_{i}"
    )

# --- Projects (Max 5) ---
st.header("Projects (Reverse Chronological Order, Max 5)")
if "projects" not in st.session_state:
    st.session_state.projects = [
        {
            "PROJECT_NAME": "",
            "START_DATE": "",
            "END_DATE": "",
            "ROLE": "",
            "LOCATION": "",
            "DESCRIPTION": "",
            "LINK": "",
        }
        for _ in range(5)
    ]

for i in range(5):
    st.markdown(f"### Project #{i+1}")
    st.session_state.projects[i]["PROJECT_NAME"] = st.text_input(
        f"Project Name #{i+1}",
        value=st.session_state.projects[i]["PROJECT_NAME"],
        key=f"project_name_{i}",
    )
    st.session_state.projects[i]["START_DATE"] = st.text_input(
        f"Start Date #{i+1}",
        value=st.session_state.projects[i]["START_DATE"],
        key=f"start_date_proj_{i}",
    )
    st.session_state.projects[i]["END_DATE"] = st.text_input(
        f"End Date #{i+1}",
        value=st.session_state.projects[i]["END_DATE"],
        key=f"end_date_proj_{i}",
    )
    st.session_state.projects[i]["ROLE"] = st.text_input(
        f"Role #{i+1}", value=st.session_state.projects[i]["ROLE"], key=f"role_proj_{i}"
    )
    st.session_state.projects[i]["LOCATION"] = st.text_input(
        f"Location #{i+1}",
        value=st.session_state.projects[i]["LOCATION"],
        key=f"location_proj_{i}",
    )
    st.session_state.projects[i]["DESCRIPTION"] = st.text_area(
        f"Project Description #{i+1}",
        value=st.session_state.projects[i]["DESCRIPTION"],
        key=f"proj_desc_{i}",
        height=100,
    )
    st.session_state.projects[i]["LINK"] = st.text_input(
        f"Project Link #{i+1}",
        value=st.session_state.projects[i]["LINK"],
        key=f"proj_link_{i}",
    )

# --- Skills (Max 50) ---
st.header("Skills (Max 50)")
if "skills" not in st.session_state:
    st.session_state.skills = [""] * 50

for i in range(50):
    st.session_state.skills[i] = st.text_input(
        f"Skill #{i+1}", value=st.session_state.skills[i], key=f"skill_{i}"
    )

# --- Languages (Max 10) ---
st.header("Languages (Max 10)")
if "languages" not in st.session_state:
    st.session_state.languages = [""] * 10

for i in range(10):
    st.session_state.languages[i] = st.text_input(
        f"Language #{i+1}", value=st.session_state.languages[i], key=f"language_{i}"
    )

# --- Certifications (Max 5) ---
st.header("Certifications (Max 5)")
if "certifications" not in st.session_state:
    st.session_state.certifications = [{"NAME": "", "LINK": ""} for _ in range(5)]

for i in range(5):
    st.session_state.certifications[i]["NAME"] = st.text_input(
        f"Certification Name #{i+1}",
        value=st.session_state.certifications[i]["NAME"],
        key=f"cert_name_{i}",
    )
    st.session_state.certifications[i]["LINK"] = st.text_input(
        f"Certification Link #{i+1}",
        value=st.session_state.certifications[i]["LINK"],
        key=f"cert_link_{i}",
    )

# --- Achievements (Max 20) ---
st.header("Achievements (Max 5)")
if "achievements" not in st.session_state:
    st.session_state.achievements = [""] * 5

for i in range(5):
    st.session_state.achievements[i] = st.text_area(
        f"Achievement #{i+1}", value=st.session_state.achievements[i], key=f"achievement_{i}"
    )

# --- Show Resume JSON ---
if st.button("Show Resume JSON"):

    def is_filled(entry):
        if isinstance(entry, dict):
            return any(str(v).strip() for v in entry.values())
        elif isinstance(entry, list):
            return any(str(item).strip() for item in entry)
        else:
            return bool(entry)

    resume_json = {
        "Name": full_name,
        "Contact" : {
            "EMAIL": email,
            "PHONE": phone,
            "ACCOUNTS": [a for a in st.session_state.accounts if is_filled(a)],
        },
        "Education": [edu for edu in st.session_state.educations if is_filled(edu)],
        "Experience": [e for e in st.session_state.experiences if is_filled(e)],
        "Skills": [s for s in st.session_state.skills if s.strip() != ""],
        "Projects": [p for p in st.session_state.projects if is_filled(p)],
        "Achievements": [ach for ach in st.session_state.achievements if ach.strip() != ""],
        "Languages": [lang for lang in st.session_state.languages if lang.strip() != ""],
        "Certifications": [cert for cert in st.session_state.certifications if is_filled(cert)],
    }
    # st.json(resume_json)
    rendered_html = template.render(**resume_json)
    components.html(rendered_html, height=1000,width=650, scrolling=True)