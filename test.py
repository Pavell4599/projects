class Journal:
    
    
    def __init__(self, klass):
        self.klass = klass
        self.stud_list = {}

    
    def add_student(self, students):
        self.students = []
        for i in range(len(students)):
            
            self.stud_list[students[i]] = {}
        
    
    
    def add_subjects(self, subject):
        self.subject = subject
      
        for g in self.stud_list:
            self.stud_list[g][subject] = []


    def rate_students(self, fio, subject, mark):
        self.fio = fio 
        self.subject = subject
        self.mark = mark
        self.stud_list[fio][subject].append(mark)
    

    def print_statistics(self, fio, subject):
        self.fio = fio 
        self.subject = subject
        print(self.stud_list[fio][subject])
    

    def print_middle(self, fio, subject):
        self.fio = fio 
        self.subject = subject
        print(round(sum(self.stud_list[fio][subject]) / len(self.stud_list[fio][subject]), 2))

        
    def test(self):
        print(self.stud_list)
    
    
    
clas1=Journal('10-I')
clas1.add_student(['Пётр Васин', 'Вовочка', 'Антон'])
clas1.add_subjects('Английский язык')
clas1.add_subjects('Программирование')
clas1.rate_students('Вовочка', 'Программирование', 4)
clas1.rate_students('Вовочка', 'Программирование', 5)
clas1.rate_students('Вовочка', 'Программирование', 3)
clas1.rate_students('Вовочка', 'Программирование', 5)
clas1.rate_students('Вовочка', 'Программирование', 5)
clas1.rate_students('Вовочка', 'Программирование', 1)
clas1.print_statistics('Вовочка', 'Программирование')
clas1.print_middle('Вовочка', 'Программирование')
