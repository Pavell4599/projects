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
        
        
        
        
        
    def test(self):
        print(self.stud_list)
    
    
    
    
    



clas1=Journal('10-I')

clas1.add_student(['makan','vova','Лёша Байгашов','Pasha'])

clas1.test()

clas1.add_subjects('химия')

clas1.test()


