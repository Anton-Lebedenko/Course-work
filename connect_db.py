import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")



connection = create_connection("edebo.db")

status_table = """
CREATE TABLE IF NOT EXISTS status(
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_name VARCHAR(20) );
"""

sex_table = """
CREATE TABLE IF NOT EXISTS sex(
    sex_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sex_name VARCHAR(10) );
"""

nationality_table = """
CREATE TABLE IF NOT EXISTS nationality(
    nation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nation_name VARCHAR(56) );
"""

faculty_table = """
CREATE TABLE IF NOT EXISTS faculty(
    faculty_id INTEGER PRIMARY KEY AUTOINCREMENT,
    faculty_name VARCHAR(75) );
"""

academic_degree_table = """
CREATE TABLE IF NOT EXISTS academic_degree(
    degree_id INTEGER PRIMARY KEY AUTOINCREMENT,
    degree_name VARCHAR(10) );
"""

accession_based_table = """
CREATE TABLE IF NOT EXISTS accession_based(
    access_id INTEGER PRIMARY KEY AUTOINCREMENT,
    accession_based_name VARCHAR(30) );
"""

education_form_table = """
CREATE TABLE IF NOT EXISTS education_form(
    form_id INTEGER PRIMARY KEY AUTOINCREMENT,
    form_name VARCHAR(12) );
"""

financing_table = """
CREATE TABLE IF NOT EXISTS financing(
    financing_id INTEGER PRIMARY KEY AUTOINCREMENT,
    financing_name VARCHAR(9) );
"""

speciality_table = """
CREATE TABLE IF NOT EXISTS speciality(
    speciality_id INTEGER PRIMARY KEY AUTOINCREMENT,
    speciality_number VARCHAR(3),
    speciality_name VARCHAR(50) );
"""

specialization_table = """
CREATE TABLE IF NOT EXISTS specialization(
    specialization_id INTEGER PRIMARY KEY AUTOINCREMENT,
    specialization_number VARCHAR(10),
    specialization_name VARCHAR(50));
"""

edu_program_table = """
CREATE TABLE IF NOT EXISTS edu_program(
    edu_program_id INTEGER PRIMARY KEY AUTOINCREMENT,
    edu_program_name VARCHAR(50));
"""

profession_table = """
CREATE TABLE IF NOT EXISTS profession(
    profession_id INTEGER PRIMARY KEY AUTOINCREMENT,
    profession_name VARCHAR(30));
"""

group_table = """
CREATE TABLE IF NOT EXISTS group_(
    group_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    group_name VARCHAR(2) NOT NULL,
    group_year INT NOT NULL,
    group_number INT NOT NULL,
    group_isboost BOOLEAN NOT NULL CHECK (group_isboost IN (0,1)));
"""

student_table = """
CREATE TABLE IF NOT EXISTS student_table(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    statusID INT, 												/* foreign key */
    student_name VARCHAR(50),
    date_brth DATE, 
    sexID INT,													/* foreign key */
    nationID INT,												/* foreign key */
    rnokpp INTEGER,
    year_lisense DATE,
    start_edu DATE,
    end_edu DATE,
    facultyID INT,												/* foreign key */
    dual_edu VARCHAR(3),
    degreeID INT, 												/* foreign key */
    accession_basedID INT,										/* foreign key */
    formID INT,													/* foreign key */
    financingID INT,											/* foreign key */
    another_spec VARCHAR(3),
    cut_term VARCHAR(3),
    specialityID INT,											/* foreign key */
    specializationID INT,										/* foreign key */
    edu_programID INT,											/* foreign key */
    professionID INT,											/* foreign key */
    course_num INT,
    groupID INT,                                                /* foreign key */
    
    FOREIGN KEY(statusID) REFERENCES status(status_id),
    FOREIGN KEY(sexID) REFERENCES sex(sex_id),
    FOREIGN KEY(nationID) REFERENCES nationality(nation_id),
    FOREIGN KEY(facultyID) REFERENCES faculty(faculty_id),
    FOREIGN KEY(degreeID) REFERENCES academic_degree(degree_id),
    FOREIGN KEY(accession_basedID) REFERENCES accession_based(access_id),
    FOREIGN KEY(formID) REFERENCES education_form(form_id),
    FOREIGN KEY(financingID) REFERENCES financing(financing_id),
    FOREIGN KEY(specialityID) REFERENCES speciality(speciality_id),
    FOREIGN KEY(specializationID) REFERENCES specialization(specialization_id),
    FOREIGN KEY(edu_programID) REFERENCES edu_program(edu_program_id),
    FOREIGN KEY(professionID) REFERENCES profession(profession_id),												
    FOREIGN KEY(groupID) REFERENCES group_(group_id) );												
"""


execute_query(connection, status_table)
execute_query(connection, sex_table)
execute_query(connection, nationality_table)
execute_query(connection, faculty_table)
execute_query(connection, academic_degree_table)
execute_query(connection, accession_based_table)
execute_query(connection, education_form_table)
execute_query(connection, financing_table)
#execute_query(connection, speciality_table)
#execute_query(connection, specialization_table)
#execute_query(connection, edu_program_table)
#execute_query(connection, profession_table)
execute_query(connection, group_table)
execute_query(connection, student_table)

