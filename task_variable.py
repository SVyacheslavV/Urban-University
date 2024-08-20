number_of_jobs_completed = 12
number_of_hours_spent = 1.5
course_name = 'Python'
time_per_task = number_of_hours_spent / number_of_jobs_completed
print('Курс:', course_name, ',',  'всего задач:', number_of_jobs_completed, ',', 'затрачено часов:', number_of_hours_spent, ',', 'среднее время выполнения ', time_per_task, 'часа.') # print в одну строку
print('Курс:', course_name,   end = ', ')
print('всего задач:', number_of_jobs_completed, end = ', ')
print('затрачено часов:', number_of_hours_spent, end = ', ')
print('среднее время выполнения ', time_per_task, 'часа.')