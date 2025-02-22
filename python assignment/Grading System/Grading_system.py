class Grading_system:
    def __init__(self, number_of_students, number_of_subjects):
        self.students = self._generate_students(number_of_students) #["student 1", "student 2"]
        self.subjects = self._generate_subjects(number_of_subjects)

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
    
    def success_message(self):
        print("="*30+" \n successfully added...")
    
    def collect_scores(self, number_of_subject, number_of_students) ->list:
        scores = []
        for i in range(number_of_students):
            print(f"enter grades for {self.students[i]} for the following subjects {self.subjects} \nenter grade sepersted with comma\
                  \n>>>>>>> ")

            grades = []
            while True:
                grades = input().split(",") #78,90,90
                if self._check_scores(grades):
                    print("invalid score value, score must be between 0-100 and must be a number....")

                else:
                    break
            
            # for j in range(number_of_subject):
            #     scores[i][j] = grade[j]

            for j in range(len(grades)):
                grades[j] = int(grades[j])
            scores.append(grades)
            self.success_message()
        return scores

            
    def get_student_average(self, score:list, number_of_subject:int):
        average = []
        sum = 0
        for i in range(len(score)): #[[45,67], [56,89], [57,90]]
            for j in score[i]:
                sum +=j
            average.append(sum/number_of_subject)
            sum = 0
        return average

    def get_student_total_score(self, score:list, number_of_subject:int):
        total_score = []
        sum = 0
        for i in range(len(score)): #[[45,67], [56,89], [57,90]]
            for j in score[i]:
                sum +=j
            total_score.append(sum)
            sum = 0
        return total_score

    def get_student_position(student_average: list, number_of_student: int):
        student_position = []

        for i in range(number_of_student):
            position = 1
            for j in range(number_of_student):
                if student_average[j] > student_average[i]:  # Compare averages
                    position += 1
            student_position.append(position)  # Store position in the list

        return student_position
            
    @staticmethod
    def _check_scores(grades):
        try:
            for grade in grades:
                score = float(grade)
                if score > 100 or score < 0:
                    return True
            return False
        except ValueError:
            return True
        

system = Grading_system(2, 2)
scores = system.collect_scores(2,2)
average = system.get_student_average(scores,2)
total_score = system.get_student_total_score(scores,2)
posiyion = system.get_student_position(average, 2)
print(scores)
print(average)
print(total_score)
print(posiyion)