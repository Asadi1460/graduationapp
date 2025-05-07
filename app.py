import streamlit as st
from bs4 import BeautifulSoup
import matplotlib.font_manager as fm
import pandas as pd


# uplaod CSV and HTML

# Cache the data loading function
@st.cache_data
def load_data():
    return pd.read_csv('data/courses.csv')

# Check for remaining courses
courses_df = load_data()

# st.dataframe(courses_df.loc[:,::-1], hide_index=True, use_container_width=True)


st.title("گزارش وضعیت تحصیلی دانشجو")

# Upload Student Report .HTML
# uploaded_html = st.file_uploader("آپلود فایل HTML", type="html")

# Extract Student Info from HTML: Major, Stage, Entrance Year, ...
# Set Major (Ap, Computer, ...)
# Set Stage (Technical, Bachelor, ...)

# Load Major-Stage info from main file .CSV
# Extract info from Major-Stage main file .CSV like theoretical and practical units, ...

# uploaded_csv = st.file_uploader("آپلود فایل دروس", type="csv")


# Display Student Info
# Display Selected lessons
# Display Passed lessons
# Display Remaining lessons
# Display Violations

# Display PDF Report
# Download PDF Report


# if uploaded_html and uploaded_csv:
#     html = uploaded_html.read().decode("utf-8")
#     course_db = load_courses_info(uploaded_csv)
    
#     student_info = parse_student_info(html)
#     df_courses = parse_courses(html)
    
#     df_passed = get_passed_courses(df_courses)
#     df_remaining = get_remaining_courses(df_passed, course_db)
#     df_violations = check_prerequisites(df_courses, df_passed, course_db)
#     summary = summarize_units(df_courses)

