students = {
  'Іван Петров': {
    'Пошта': 'Ivan@gmail.com',
    'Вік': 14,
    'Номер телефону': '+380987771221',
    'Середній бал': 95.8
  },
  'Женя Курич': {
    'Пошта': 'Geka@gmail.com',
    'Вік': 16,
    'Номер телефону': None,
    'Середній бал': 64.5
  },
  'Маша Кера': {
    'Пошта': 'Masha@gmail.com',
    'Вік': 18,
    'Номер телефону': '+380986671221',
    'Середній бал': 80
  },
}

new_student = {
        'Пошта': 'Johny@gmail.com',
        'Вік': 21,
        'Номер телефону': '+380986623221',
        'Середній бал': 87
    }
students['John Wick'] = new_student

average_grade = sum(student['Середній бал'] for student in students.values())/4

students['Іван Петров']['bank_account_number'] = None

student2_salary = students['Женя Курич'].get('Salary') or 0.0

print(average_grade)