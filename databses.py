import os

import dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# host = "localhost"
# port = 5432
# password = "Aboba4.0"
# user = "postgres"
# db = "hospital"

# reads .env
dotenv.load_dotenv()

# gets required variables from .env
host = os.getenv("HOST")
port = os.getenv("PORT")
user = os.getenv("DB_USER")
password = os.getenv("PASSWORD")
db = os.getenv("DB")

# path to database

db_url = f"postgresql+pg8000://{user}:{password}@{host}:{port}/{db}"

# creation of connection(engine)


engine = create_engine(db_url)

# create session on a base of engine

Session = sessionmaker(bind=engine)
session = Session()

# metadata = MetaData()
# metadata.reflect(bind=engine)

# tables = metadata.tables
# print(list(tables.keys()))


def show_doctor_specializations(session):
    query = """
        SELECT D.NAME, S.NAME
        FROM DOCTORS D
                JOIN DOCTORSSPECIALIZATIONS DS ON D.id = DS.doctor_id
				JOIN SPECIALIZATIONS S ON S.id = DS.specialization_id

    """

    query = text(query)

    result = session.execute(query)

    for row in result:
        print(row)


def show_active_doctors_salary(session):
    query = """
        SELECT D.SURNAME, D.SALARY + D.PREMIUM
        FROM DOCTORS D
                JOIN VACATIONS V ON D.id = V.doctorid
        WHERE V.STARTDATE < '2025-06-04' AND V.ENDDATE > '2025-06-04'

    """

    query = text(query)

    result = session.execute(query)

    for row in result:
        print(row)


def show_wards_in_department(session):
    query = """
        SELECT W.NAME, DP.NAME
        FROM WARDS W JOIN DEPARTMENTS DP ON W.departmentid = DP.id
        WHERE DP.NAME = 'Кардіологічне відділення'

    """

    query = text(query)

    result = session.execute(query)

    for row in result:
        print(row)


def show_month_donations(session):
    month_number = input("uinput a month ")
    year_number = input("uinput a year ")

    query = f"""
        SELECT DP.NAME,S.NAME,DN.AMOUNT,DN.DONATION_DATE
        FROM SPONSORS S
            JOIN DONATIONS DN ON S.id = DN.sponsor_id
            JOIN DEPARTMENTS DP ON DP.id = DN.department_id
        WHERE EXTRACT(MONTH FROM DN.DONATION_DATE) = '{month_number}'
            AND EXTRACT(YEAR FROM DN.DONATION_DATE) = '{year_number}'

    """

    query = text(query)

    result = session.execute(query)

    for row in result:
        print(row)


show_month_donations(session)
