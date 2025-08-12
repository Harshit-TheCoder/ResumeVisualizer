import streamlit as st

st.title("Resume Builder with Fixed Sections")

# --- Personal Info ---
st.header("Full Name and Contact")
full_name = st.text_input("Full Name", key="full_name")
email = st.text_input("Email", key="email")
phone = st.text_input("Phone Number", key="phone")

st.header("Social Media Accounts (Max 10)")

accounts = []
for i in range(10):
    platform = st.text_input(f"Platform #{i+1}", key=f"account_platform_{i}")
    link = st.text_input(f"Link #{i+1}", key=f"account_link_{i}")
    accounts.append({"platform": platform, "link": link})

# --- Experience (Fixed 10) ---
st.header("Experience (Reverse Chronological Order, 10 Fields)")
if "experiences" not in st.session_state:
    st.session_state.experiences = [
        {"COMPANY": "", "START_DATE": "", "END_DATE": "", "ROLE": "", "LOCATION": "", "DESCRIPTION": "", "LINK": ""}
        for _ in range(10)
    ]

for i in range(10):
    st.markdown(f"### Experience #{i+1}")
    st.session_state.experiences[i]["COMPANY"] = st.text_input(f"Company Name #{i+1}", value=st.session_state.experiences[i]["COMPANY"], key=f"company_{i}")
    st.session_state.experiences[i]["START_DATE"] = st.text_input(f"Start Date #{i+1}", value=st.session_state.experiences[i]["START_DATE"], key=f"start_date_exp_{i}")
    st.session_state.experiences[i]["END_DATE"] = st.text_input(f"End Date #{i+1}", value=st.session_state.experiences[i]["END_DATE"], key=f"end_date_exp_{i}")
    st.session_state.experiences[i]["ROLE"] = st.text_input(f"Role #{i+1}", value=st.session_state.experiences[i]["ROLE"], key=f"role_{i}")
    st.session_state.experiences[i]["LOCATION"] = st.text_input(f"Location #{i+1}", value=st.session_state.experiences[i]["LOCATION"], key=f"location_{i}")
    st.session_state.experiences[i]["DESCRIPTION"] = st.text_area(f"Job Description #{i+1}", value=st.session_state.experiences[i]["DESCRIPTION"], key=f"desc_{i}")
    st.session_state.experiences[i]["LINK"] = st.text_input(f"Work Link #{i+1}", value=st.session_state.experiences[i]["LINK"], key=f"work_link_{i}")

# --- Projects (Fixed 5) ---
st.header("Projects (Reverse Chronological Order, 5 Fields)")
if "projects" not in st.session_state:
    st.session_state.projects = [
        {"PROJECT_NAME": "", "START_DATE": "", "END_DATE": "", "ROLE": "", "LOCATION": "", "DESCRIPTION": "", "LINK": ""}
        for _ in range(5)
    ]

for i in range(5):
    st.markdown(f"### Project #{i+1}")
    st.session_state.projects[i]["PROJECT_NAME"] = st.text_input(f"Project Name #{i+1}", value=st.session_state.projects[i]["PROJECT_NAME"], key=f"project_name_{i}")
    st.session_state.projects[i]["START_DATE"] = st.text_input(f"Start Date #{i+1}", value=st.session_state.projects[i]["START_DATE"], key=f"start_date_proj_{i}")
    st.session_state.projects[i]["END_DATE"] = st.text_input(f"End Date #{i+1}", value=st.session_state.projects[i]["END_DATE"], key=f"end_date_proj_{i}")
    st.session_state.projects[i]["ROLE"] = st.text_input(f"Role #{i+1}", value=st.session_state.projects[i]["ROLE"], key=f"role_proj_{i}")
    st.session_state.projects[i]["LOCATION"] = st.text_input(f"Location #{i+1}", value=st.session_state.projects[i]["LOCATION"], key=f"location_proj_{i}")
    st.session_state.projects[i]["DESCRIPTION"] = st.text_area(f"Project Description #{i+1}", value=st.session_state.projects[i]["DESCRIPTION"], key=f"proj_desc_{i}")
    st.session_state.projects[i]["LINK"] = st.text_input(f"Project Link #{i+1}", value=st.session_state.projects[i]["LINK"], key=f"proj_link_{i}")

st.header("Skills (max 50)")
skills = []
for i in range(50):
    skill = st.text_input(f"Skill #{i+1}", key=f"skill_{i}")
    skills.append(skill)

st.header("Languages (max 10)")
languages = []
for i in range(10):
    lang = st.text_input(f"Language #{i+1}", key=f"language_{i}")
    languages.append(lang)

st.header("Certifications (max 5)")
certifications = []
for i in range(5):
    cert_name = st.text_input(f"Certification Name #{i+1}", key=f"cert_name_{i}")
    cert_link = st.text_input(f"Certification Link #{i+1}", key=f"cert_link_{i}")
    certifications.append({"NAME": cert_name, "LINK": cert_link})

# --- Show Resume JSON ---
if st.button("Show Resume JSON"):
    def is_filled(entry):
        if isinstance(entry, dict):
            return any(str(v).strip() for v in entry.values())
        elif isinstance(entry, list):
            # For lists like DESCRIPTION or just lists of strings, check if any non-empty
            return any(str(item).strip() for item in entry)
        else:
            return bool(entry)

    resume_json = {
        "FULL_NAME": full_name,
        "EMAIL": email,
        "PHONE": phone,
        "ACCOUNTS": [a for a in st.session_state.accounts if is_filled(a)],
        "EDUCATION": [edu for edu in st.session_state.educations if is_filled(edu)],
        "EXPERIENCE": [e for e in st.session_state.experiences if is_filled(e)],
        "SKILLS": [s for s in st.session_state.skills if s.strip() != ""],
        "PROJECTS": [p for p in st.session_state.projects if is_filled(p)],
        "ACHIEVEMENTS": [ach for ach in st.session_state.achievements if ach.strip() != ""],
        "LANGUAGES": [lang for lang in st.session_state.languages if lang.strip() != ""],
        "CERTIFICATIONS": [cert for cert in st.session_state.certifications if is_filled(cert)],
    }
    st.json(resume_json)

