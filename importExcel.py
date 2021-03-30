# print whole sheet data
#print(excel_data_df)

#список заголовков
#print(excel_data_df.columns.ravel())

#Можно указать имена столбцов для чтения из файла Excel
#excel_data_df = pandas.read_excel('C://temp/dates.xlsx', sheet_name='Лист1', usecols=['Дата народження'])

import pandas
import datetime

excel_data_df = pandas.read_excel('C://temp/dates.xlsx', sheet_name='Лист1')

#вывод данных столбца
########################################################################################################################
status_name_temp = excel_data_df['Статус навчання'].tolist()
status_name = list(dict.fromkeys(status_name_temp))

#print(status_name)

########################################################################################################################
student_name = excel_data_df['Здобувач'].tolist()

#print(student_name)

########################################################################################################################
date_brth_temp = excel_data_df['Дата народження'].tolist()
date_brth = [str(datetime.datetime.date(x)) for x in date_brth_temp]

#print(date_brth)

########################################################################################################################
sex_temp = excel_data_df['Стать'].tolist()
sex = list(dict.fromkeys(sex_temp))

#print(sex)

########################################################################################################################
nationality_temp = excel_data_df['Громадянство'].tolist()
nationality = list(dict.fromkeys(nationality_temp))
#print(nationality)

########################################################################################################################
rnokpp = excel_data_df['РНОКПП'].tolist()

#print(rnokpp)

########################################################################################################################
year_lisense = excel_data_df['Рік ліцензійних обсягів'].tolist()

#print(year_lisense)

########################################################################################################################
start_edu_temp = excel_data_df['Початок навчання'].tolist()
start_edu = [str(datetime.datetime.date(x)) for x in start_edu_temp]

#print(start_edu)

########################################################################################################################
end_edu_temp = excel_data_df['Завершення навчання'].tolist()
end_edu = [str(datetime.datetime.date(x)) for x in end_edu_temp]

#print(end_edu)

########################################################################################################################
faculty_temp = excel_data_df['Структурний підрозділ'].tolist()
faculty = list(dict.fromkeys(faculty_temp))

#print(faculty)

########################################################################################################################
dual_edu = excel_data_df['Чи здобуває освітній ступінь за дуальною формою навчання'].tolist()

#print(dual_edu)

########################################################################################################################
academic_degree_temp = excel_data_df['Освітній ступінь (рівень)'].tolist()
academic_degree = list(dict.fromkeys(academic_degree_temp))

#print(academic_degree)

########################################################################################################################
accession_based_temp = excel_data_df['Вступ на основі'].tolist()
accession_based = list(dict.fromkeys(accession_based_temp))

#print(accession_based)

########################################################################################################################
education_form_temp = excel_data_df['Форма навчання'].tolist()
education_form = list(dict.fromkeys(education_form_temp))

#print(education_form)

########################################################################################################################
financing_temp = excel_data_df['Джерело фінансування'].tolist()
financing = list(dict.fromkeys(financing_temp))

#print(financing)

########################################################################################################################
another_spec = excel_data_df['Чи здобувався ступень за іншою спеціальністю'].tolist()

#print(another_spec)

########################################################################################################################
cut_term = excel_data_df['Чи скорочений термін навчання'].tolist()

#print(cut_term)

########################################################################################################################
speciality_temp = excel_data_df['Спеціальність'].tolist()
speciality = list(dict.fromkeys(speciality_temp))
speciality = sorted(speciality)

speciality_split = [el.split(' ', 1) for el in speciality]
speciality_number = [el[0] for el in speciality_split]
speciality_name = [el[1] for el in speciality_split]

#print(speciality)
#print(speciality_split)
#print(speciality_number)
#print(speciality_name)

#----------------------------------------------#

speciality_for_check = excel_data_df['Спеціальність'].tolist()
speciality_split_check = [el.split(' ', 1) for el in speciality_for_check]

speciality_number_check = [el[0] for el in speciality_split_check]
speciality_name_check = [el[1] for el in speciality_split_check]

########################################################################################################################
specialization_temp = excel_data_df['Спеціалізація'].tolist()
specialization = list(dict.fromkeys(specialization_temp))

specialization = list(map(str, specialization))
specialization = [x for x in specialization if x != 'nan']
specialization = sorted(specialization)

specialization_split = [el.split(' ', 1) for el in specialization]
specialization_number = [el[0] for el in specialization_split]
specialization_name = [el[1] for el in specialization_split]

#print(specialization)
#print(specialization_split)
#print(specialization_number)
#print(specialization_name)

########################################################################################################################
edu_program_temp = excel_data_df['Освітня програма'].tolist()
edu_program = list(dict.fromkeys(edu_program_temp))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! нужен ли nan?
#print(edu_program)

########################################################################################################################
profession_temp = excel_data_df['Професія'].tolist()
profession = list(dict.fromkeys(profession_temp))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! нужен ли nan?

#print(profession)

########################################################################################################################
course_num = excel_data_df['Курс'].tolist()

#print(course_num)

########################################################################################################################
def split_boost(list_year):
    group_boost = []
    for el in list_year:
        if len(el) > 2:
            group_boost.append(1)
        else:
            group_boost.append(0)

    return group_boost

group_temp = excel_data_df['Група'].tolist()

group_ = list(dict.fromkeys(group_temp))
group_ = sorted(group_)

group_split = [el.split('-', 2) for el in group_]

group_name = [el[0] for el in group_split]
group_year = [el[1] for el in group_split]
group_number = [el[2] for el in group_split]
group_isboost = split_boost(group_year)

group_year = [el[:-1] if len(el) > 2 else el for el in group_year]

#----------------------------------------------#

group_for_check = excel_data_df['Група'].tolist()
group_split_check = [el.split('-', 2) for el in group_for_check]

group_name_check = [el[0] for el in group_split_check]
group_year_check = [el[1] for el in group_split_check]
group_number_check = [el[2] for el in group_split_check]
group_isboost_check = split_boost(group_year_check)

group_year_check = [el[:-1] if len(el) > 2 else el for el in group_year_check]

#print(group_temp)

#print(group_)
#print(group_split)
#print(group_name)
#print(group_year)
#print(group_number)
#print(group_isboost)

########################################################################################################################
