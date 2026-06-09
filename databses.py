import os

import dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

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


def show_groups_in_faculties(session):
    """
    Нова функція з JOIN.
    Виводить назви груп та назви факультетів, до яких вони належать.
    """
    query = """
            SELECT g.name AS group_name, f.name AS faculty_name
            FROM groups g
                     JOIN departments d ON g.department_id = d.id
                     JOIN faculties f ON d.faculty_id = f.id \
            """

    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)


def show_high_salary_teachers(session):
    """
    Нова функція з користувацьким введенням (аналог show_month_donations).
    Шукає викладачів, чия ставка перевищує введене користувачем значення.
    """
    min_salary = input("Введіть мінімальну ставку для пошуку: ")

    # Використовуємо іменовані параметри (:min_sal) для захисту від SQL-ін'єкцій
    query = """
            SELECT name, surname, salary
            FROM teachers
            WHERE salary > :min_sal \
            """

    query = text(query)
    result = session.execute(query, {"min_sal": float(min_salary)})

    for row in result:
        print(row)


def show_top_financed_faculties(session):
    """
    Нова проста функція.
    Виводить факультети з фондом фінансування понад 80,000.
    """
    query = """
            SELECT name, financing
            FROM faculties
            WHERE financing > 80000 \
            """

    query = text(query)
    result = session.execute(query)

    for row in result:
        print(row)
