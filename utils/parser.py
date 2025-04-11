import pandas as pd


def parse_student_info(html: str) -> dict:
    """استخراج اطلاعات دانشجو (نام، شماره دانشجویی، ...)"""
    return {
        "name": "Ali Rezaei",
        "student_id": "123456",
        "field": "مهندسی کامپیوتر",
    }

def parse_courses(html: str) -> pd.DataFrame:
    """
    استخراج دروس اخذ شده به تفکیک ترم (ترم، نام درس، نمره، وضعیت، نوع درس، تعداد واحد)
    """
    # •	passed به صورت Boolean (True/False)
	# •	course_type: “نظری”، “عملی”، “نظری-عملی” (بر اساس courses.csv)
    pass
    # return df  # ستونی شامل: term, course_code, course_name, grade, passed, type, units
    
    
def load_courses_info(csv_path: str) -> pd.DataFrame:
    """خواندن فایل courses.csv و تبدیل به DataFrame با اطلاعات دروس، پیش‌نیاز، نوع و واحد"""
    # •	prerequisites: لیست یا رشته‌ای از course_codeهای لازم

    # return df
    pass    