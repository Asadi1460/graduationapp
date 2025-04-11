import pandas as pd

def summarize_units(df: pd.DataFrame) -> dict:
    """محاسبه مجموع واحدهای گذرانده/اخذشده به تفکیک نظری/عملی"""
    # return {
    #     "taken": {"total": 80, "practical": 20, "theory": 60},
    #     "passed": {"total": 65, "practical": 15, "theory": 50}
    # }
    pass

def get_passed_courses(df: pd.DataFrame) -> pd.DataFrame:
    """دروس گذرانده با نمره قبولی"""
    # return df_passed
    pass

def get_remaining_courses(df_passed: pd.DataFrame, courses_db: pd.DataFrame) -> pd.DataFrame:
    """دروس باقی‌مانده برای فارغ‌التحصیلی"""
    # return df_remaining
    pass

def check_prerequisites(df_passed: pd.DataFrame, df_taken: pd.DataFrame, courses_db: pd.DataFrame) -> pd.DataFrame:
    """تحلیل عدم رعایت پیش‌نیازها"""
    # return df_violations
    pass