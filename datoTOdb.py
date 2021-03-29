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

#из 4 списков для групп -> делает список из строк (первые элементы в строку)
def to_str_first_els_of_groups(data):
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
def to_list_first_els_of_groups(data):
    res = []
    for i in range(0, len(data[0])):
        temp = []
        for j in data:
            temp.append(str(j[i]))
        # print(res)
        res.append(temp)
    return res

#выполняет заполнение в таблицу Группы
def insert_to_group_table(conn, data):
    cursor = conn.cursor()
    try:
        res = to_str_first_els_of_groups(data)
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
        res = to_list_first_els_of_groups(data)
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
            add_data = "INSERT INTO student_table ('statusID', 'student_name', 'date_brth', 'groupID') VALUES ({})".format(el)

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



#Группа----------------------------------------------------------------------------------------------------------------#
data_for_groups = [importExcel.group_name, importExcel.group_year, importExcel.group_number, importExcel.group_isboost]
insert_to_group_table(conn, data_for_groups)

data_for_groups_check = [importExcel.group_name_check, importExcel.group_year_check, importExcel.group_number_check, importExcel.group_isboost_check]
data_to_student_table.append(read_group_id_comparing_initial_data(conn, data_for_groups_check))

#Запись в student_table------------------------------------------------------------------------------------------------#

data_to_student_table = to_list_all_first_els_for_stud_table(data_to_student_table)

insert_data_to_student_table(conn, data_to_student_table)

#----------------------------------------------------------------------------------------------------------------------#

conn.close()
