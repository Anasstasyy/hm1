class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задание: {self.grades}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res
    
    def aw_grades(self):
        gr_list = sum(self.grades.values(), start = [])
        return round(sum(gr_list) / len(gr_list), 2)
    
    def __lt__(self, other):
        if isinstance(other, Student):
            result = self.aw_grades() < other.aw_grades()
        else:
            print('ошибка')
            return
        return result
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'ошибка'
        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades}'
        return res
        
    def aw_grades_lec(self):
        gr_list = sum(self.grades.values(), start = [])
        return round(sum(gr_list) / len(gr_list), 2)
         
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            result = self.aw_grades_lec() < other.aw_grades_lec()
        else:
            print('ошибка')
            return
        return result
       
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'  
        return res  
    
    
    def rate_hm(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'ошибка' 
        
        
student1 = Student('Саша', 'Петров', 'male')
student1.courses_in_progress += ['Python', 'Java']
student1.finished_courses +=['C']
student2 = Student('Маша', 'Петрова', 'female')
student2.courses_in_progress += ['Python', 'C+']
student2.finished_courses += ['Java']

print(student1)
print(student2)

Lecturer1 = Lecturer('Игорь', 'Иванов')
Lecturer2 = Lecturer('Марина', 'Иванова')

print(Lecturer1)
print(Lecturer2)

Reviewer1 = Reviewer('Иван', 'Степанов')
Reviewer1.courses_attached += ['Python', 'Java']
Reviewer2 = Reviewer('Елена', 'Антонова')
Reviewer2.courses_attached += ['C+', 'HTML']

print(Reviewer1)
print(Reviewer2)

student1.rate_lecturer(Lecturer1, 'Python', 9)
student1.rate_lecturer(Lecturer2, 'Python', 8)
student2.rate_lecturer(Lecturer1, 'Python', 8)
student2.rate_lecturer(Lecturer2, 'Python', 9)

Reviewer1.rate_hm(student1, 'Python', 7)
Reviewer1.rate_hm(student2, 'Python', 8)
Reviewer2.rate_hm(student1, 'Python', 8)
Reviewer2.rate_hm(student2, 'Python', 7)

print(student1 < student2)
print(Lecturer1 > Lecturer2)

student_list = [student1, student2]
lecturer_list = [Lecturer1, Lecturer2]

def grade_all_st(student_list, course):
    all_sum = 0
    len_all = 0 
    for students in student_list:
        for value in students.grades:
            rate = students._average_st_course(course)
            all_sum += rate
            len_all += 1
    result = round(all_sum / len_all, 2)
    return result

def grade_all_lec(lecturer_list, course):
    all_sum = 0
    len_all = 0 
    for lecturers in lecturer_list:
        for value in Lecturer.grades:
            rate = lecturers._average_st_course(course)
            all_sum += rate
            len_all += 1
    result = round(all_sum / len_all, 2)
    return result

print(student_list)
print(lecturer_list)

        