import importExcel, connect_db
from sqlite3 import Error

########################################################################################################################

#выполняет считывание id статуса таблицы Статус в сравнении со входными данными и возвращает обратно списком
def read_status_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        records = []
        for el in data:
            sql_sel = """SELECT status_id FROM status WHERE status_name = '{}'""".format(el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

#выполняет считывание id пола таблицы Пол в сравнении со входными данными и возвращает обратно списком
def read_sex_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        records = []
        for el in data:
            sql_sel = """SELECT sex_id FROM sex WHERE sex_name = '{}'""".format(el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

#выполняет считывание id национальностей таблицы Национальности в сравнении со входными данными и возвращает обратно списком
def read_nation_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        records = []
        for el in data:
            sql_sel = """SELECT nation_id FROM nationality WHERE nation_name = '{}'""".format(el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

#выполняет считывание id факультетов таблицы Факультеты в сравнении со входными данными и возвращает обратно списком
def read_faculty_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        records = []
        for el in data:
            sql_sel = """SELECT faculty_id FROM faculty WHERE faculty_name = '{}'""".format(el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

#выполняет считывание id образовательных степеней таблицы Образовательные степени в сравнении со входными данными и возвращает обратно списком
def read_academic_degree_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        records = []
        for el in data:
            sql_sel = """SELECT degree_id FROM academic_degree WHERE degree_name = '{}'""".format(el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

#выполняет считывание id вступлений на основе таблицы Вступление на основе в сравнении со входными данными и возвращает обратно списком
def read_accession_based_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        records = []
        for el in data:
            sql_sel = """SELECT access_id FROM accession_based WHERE accession_based_name = '{}'""".format(el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

#выполняет считывание id образовательных форм таблицы Образовательные формы в сравнении со входными данными и возвращает обратно списком
def read_education_form_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        records = []
        for el in data:
            sql_sel = """SELECT form_id FROM education_form WHERE form_name = '{}'""".format(el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

#выполняет считывание id финансирований таблицы Источники финансирования в сравнении со входными данными и возвращает обратно списком
def read_financing_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        records = []
        for el in data:
            sql_sel = """SELECT financing_id FROM financing WHERE financing_name = '{}'""".format(el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

def insert_to_specialities_table(conn, data):
    cursor = conn.cursor()
    try:
        res = to_str_first_els_of_gr_spty_spon(data)
        for el in res:
            add_data = "INSERT INTO speciality ('speciality_number', 'speciality_name') VALUES ({})".format(el)
            cursor.execute(add_data)
            conn.commit()
            # print("Query of data executed successfully")

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

#выполняет считывание id групп таблицы Группы в сравнении со входными данными и возвращает обратно списком
def read_speciality_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        res = to_list_first_els_of_gr_spty_spon(data)
        #print(res)
        records = []
        for el in res:
            sql_sel = """SELECT speciality_id FROM speciality WHERE speciality_number = '{}' AND speciality_name = '{}'""".format(*el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

#из 4 списков для групп -> делает список из строк (первые элементы в строку)
def to_str_first_els_of_gr_spty_spon(data):
    res = []
    for i in range(0, len(data[0])):
        line = ""
        for j in data:
            line += "'" + str(j[i]) + "', "
        # print(res)
        line = "".join(list(line)[0:-2])
        res.append(line)
    return res

#из 4 списков для групп -> делает список списков (первые элементы в подсписок)
def to_list_first_els_of_gr_spty_spon(data):
    res = []
    for i in range(0, len(data[0])):
        temp = []
        for j in data:
            temp.append(str(j[i]))
        # print(res)
        res.append(temp)
    return res

########################################################################################################################

#выполняет заполнение в таблицу Группы
def insert_to_group_table(conn, data):
    cursor = conn.cursor()
    try:
        res = to_str_first_els_of_gr_spty_spon(data)
        for el in res:
            add_data = "INSERT INTO group_ ('group_name', 'group_year', 'group_number', 'group_isboost') VALUES ({})".format(el)
            cursor.execute(add_data)
            conn.commit()
            # print("Query of data executed successfully")

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

#выполняет считывание id групп таблицы Группы в сравнении со входными данными и возвращает обратно списком
def read_group_id_comparing_initial_data(conn, data):
    cursor = conn.cursor()
    try:
        res = to_list_first_els_of_gr_spty_spon(data)
        #print(res)
        records = []
        for el in res:
            sql_sel = """SELECT group_id FROM group_ WHERE group_name = '{}' AND group_year = '{}' AND group_number = '{}' AND group_isboost = '{}'""".format(*el)
            cursor.execute(sql_sel)
            records.append(cursor.fetchone())

        records = clear_id_for_stud_table(records)

        return records

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

########################################################################################################################

#выполняет заполнение допполнительных таблиц (не student_table)
def insert_data_to_secondaries_tables(conn, data, name_table, name_column):
    cursor = conn.cursor()
    try:
        for el in data:
            add_data = "INSERT INTO {} ({}) VALUES ('{}')".format(name_table, name_column, el)
            cursor.execute(add_data)
            conn.commit()
            # print("Query of data executed successfully")

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")

#выполняет заполнение главной таблицы (student_table) из списка data_to_student_table
def insert_data_to_student_table(conn, data):
    cursor = conn.cursor()
    try:
        for el in data:
            add_data = "INSERT INTO student_table ('statusID', 'student_name', 'date_brth', 'sexID', 'nationID', 'rnokpp', 'year_lisense', 'start_edu', 'end_edu', 'facultyID', 'dual_edu', 'degreeID', 'accession_basedID', 'formID', 'financingID', 'another_spec', 'cut_term', 'specialityID', 'groupID') VALUES ({})".format(el)
            cursor.execute(add_data)
            conn.commit()
            # print("Query of data executed successfully")

    except Error as error:
        print(error)

    finally:
        if conn:
            cursor.close()
            print("Соединение с MySQL закрыто")


#чистит id от формы (id,) для таблицы студентов
def clear_id_for_stud_table(data):
    res = []
    for el in data:
        el = str(el)
        el = el[1:-2]
        #print(el)
        res.append(el)
    return res

#преобразует из всех готовых списков в один для заполнения построчно (первые элементы в строку)
def to_list_all_first_els_for_stud_table(data):
    res = []
    for i in range(0, len(data[0])):
        line = ""
        for j in data:
            line += "'" + str(j[i]) + "', "
        # print(res)
        line = "".join(list(line)[0:-2])
        res.append(line)
    return res

########################################################################################################################

conn = connect_db.connection

#список для сбора всех готовых списков в один
data_to_student_table = []

#Статус----------------------------------------------------------------------------------------------------------------#
insert_data_to_secondaries_tables(conn, importExcel.status_name, 'status', 'status_name')
data_to_student_table.append(read_status_id_comparing_initial_data(conn, importExcel.status_name_temp))

#ФИО-------------------------------------------------------------------------------------------------------------------#
data_to_student_table.append(importExcel.student_name)

#Дата рождения---------------------------------------------------------------------------------------------------------#
data_to_student_table.append(importExcel.date_brth)

#Пол-------------------------------------------------------------------------------------------------------------------#
insert_data_to_secondaries_tables(conn, importExcel.sex, 'sex', 'sex_name')
data_to_student_table.append(read_sex_id_comparing_initial_data(conn, importExcel.sex_temp))

#Национальность--------------------------------------------------------------------------------------------------------#
insert_data_to_secondaries_tables(conn, importExcel.nationality, 'nationality', 'nation_name')
data_to_student_table.append(read_nation_id_comparing_initial_data(conn, importExcel.nationality_temp))

#РНОКПП----------------------------------------------------------------------------------------------------------------#
data_to_student_table.append(importExcel.rnokpp)

#Год лиценз. объемов---------------------------------------------------------------------------------------------------#
data_to_student_table.append(importExcel.year_lisense)

#Начало учебы----------------------------------------------------------------------------------------------------------#
data_to_student_table.append(importExcel.start_edu)

#Конец учебы-----------------------------------------------------------------------------------------------------------#
data_to_student_table.append(importExcel.end_edu)

#Факультеты------------------------------------------------------------------------------------------------------------#
insert_data_to_secondaries_tables(conn, importExcel.faculty, 'faculty', 'faculty_name')
data_to_student_table.append(read_faculty_id_comparing_initial_data(conn, importExcel.faculty_temp))

#Дуальное образование--------------------------------------------------------------------------------------------------#
data_to_student_table.append(importExcel.dual_edu)

#Образовательная степень-----------------------------------------------------------------------------------------------#
insert_data_to_secondaries_tables(conn, importExcel.academic_degree, 'academic_degree', 'degree_name')
data_to_student_table.append(read_academic_degree_id_comparing_initial_data(conn, importExcel.academic_degree_temp))

#Вступление на базе----------------------------------------------------------------------------------------------------#
insert_data_to_secondaries_tables(conn, importExcel.accession_based, 'accession_based', 'accession_based_name')
data_to_student_table.append(read_accession_based_id_comparing_initial_data(conn, importExcel.accession_based_temp))

#Форма учебы-----------------------------------------------------------------------------------------------------------#
insert_data_to_secondaries_tables(conn, importExcel.education_form, 'education_form', 'form_name')
data_to_student_table.append(read_education_form_id_comparing_initial_data(conn, importExcel.education_form_temp))

#Источник финансирования-----------------------------------------------------------------------------------------------#
insert_data_to_secondaries_tables(conn, importExcel.financing, 'financing', 'financing_name')
data_to_student_table.append(read_financing_id_comparing_initial_data(conn, importExcel.financing_temp))

#Окончание другой специальности----------------------------------------------------------------------------------------#
data_to_student_table.append(importExcel.another_spec)

#Сокращенный учебный срок----------------------------------------------------------------------------------------------#
data_to_student_table.append(importExcel.cut_term)

#Специальность---------------------------------------------------------------------------------------------------------#
data_for_specialities = [importExcel.speciality_number, importExcel.speciality_name]
insert_to_specialities_table(conn, data_for_specialities)

data_for_specialities_check = [importExcel.speciality_number_check, importExcel.speciality_name_check]
data_to_student_table.append(read_speciality_id_comparing_initial_data(conn, data_for_specialities_check))

#Группа----------------------------------------------------------------------------------------------------------------#
data_for_groups = [importExcel.group_name, importExcel.group_year, importExcel.group_number, importExcel.group_isboost]
insert_to_group_table(conn, data_for_groups)

data_for_groups_check = [importExcel.group_name_check, importExcel.group_year_check, importExcel.group_number_check, importExcel.group_isboost_check]
data_to_student_table.append(read_group_id_comparing_initial_data(conn, data_for_groups_check))

#Запись в student_table------------------------------------------------------------------------------------------------#

data_to_student_table = to_list_all_first_els_for_stud_table(data_to_student_table)

#print(data_to_student_table)

insert_data_to_student_table(conn, data_to_student_table)

#----------------------------------------------------------------------------------------------------------------------#

conn.close()
