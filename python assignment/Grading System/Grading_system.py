class Grading_system:
    students = []
    subjects = []

    def __init__(self, number_of_students, number_of_subjects)->list:
        self.students = self._generate_students(number_of_students)
        self.subjects = self._generate_subjects(number_of_students)

    def _generate_students(self, number_of_students:int) ->list:
        students = []
        for i in range(number_of_students):
            students.append("student "+str(i+1))

        return students
    
    def _generate_subjects(self, number_of_subjects) ->list:
        subjects = []
        for i in range(number_of_subjects):
            subjects.append("sub "+str(i + 1))
        return subjects
    
    def success_message():
        print("="*30+" \n successfully added...")
    
    def collect_scores(self, number_of_subject, number_of_students) ->list:
        scores = []
        for i in range(number_of_students):
            print(f"enter grades for {self.students[i]} for the following subjects {self.subjects} \nenter grade sepersted with comma\
                  \n>>>>>>> ")
            
            grades = []
            while True:
                grades = input().split(",")
                if self._check_scores(grades):
                    print("invalid score value, score must be between 0-100..")

                else:
                    break
            
            # for j in range(number_of_subject):
            #     scores[i][j] = grade[j]

            for j in grades:
                grades[j] = int(grades[j])
            scores.append(grades)
            self.success_message()
        return scores

            

            
    @staticmethod
    def _check_scores(grades):
        try:
            for grade in grades:
                score = int(grade)
                if score > 100 or score < 0:
                    return True
            return False
        except ValueError:
            return True
        

system = Grading_system(2, 2)
scores = system.collect_scores(2,2)
print(scores)