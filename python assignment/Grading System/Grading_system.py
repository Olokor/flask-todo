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


            for j in range(len(grades)):
                grades[j] = int(grades[j])
            scores.append(grades)
            self.success_message()
        return scores




            
    def get_student_average(self, score:list, number_of_subject:int)->list[float]:
        average = []
        sum = 0
        for i in range(len(score)): #[[45,67], [56,89], [57,90]]
            for j in score[i]:
                sum +=j
            average.append(sum/number_of_subject)
            sum = 0
        return average

    def get_student_total_score(self, score:list)->list[int]:
        total_score = []
        sum = 0
        for i in range(len(score)): #[[45,67], [56,89], [57,90]]
            for j in score[i]:
                sum +=j
            total_score.append(sum)
            sum = 0
        return total_score

    def get_student_position(self, student_average: list, number_of_student: int):
        student_position = []

        for i in range(number_of_student):
            position = 1
            for j in range(number_of_student):
                if student_average[j] > student_average[i]:  # Compare averages
                    position += 1
            student_position.append(position)  # Store position in the list

        return student_position

    def subject_summary(self, scores: list, number_of_subject: int) -> None:
        highest_score = 0
        lowest_score = 100
        number_of_passes = 0
        number_of_failures = 0
        highest_students = ""
        lowest_students = ""
        total_score = 0
        subject_index = 0
        average_score = 0

        for score in scores: #[[89,90], [76,86], [76,50]]
            for i in range(len(score)):
                # Track highest score
                if score[i] > highest_score:
                    highest_score = score[i]
                    highest_students = self.students[i]

                # Track lowest score
                if score[i] < lowest_score:
                    lowest_score = score[i]
                    lowest_students = self.students[i]

                # Count passes and failures correctly
                if score[i] < 39:
                    number_of_failures += 1
                else:
                    number_of_passes += 1

                total_score += score[i]

            if subject_index < number_of_subject:
                print(f"For {self.subjects[subject_index]}")

            average_score = total_score / number_of_subject

            print(f"""
            {"=" * 25}
            Highest scoring student: {highest_students} - {highest_score}
            {"=" * 25}
            Lowest scoring student: {lowest_students} - {lowest_score}
            {"=" * 25}
            Total score: {total_score}
            Average score: {average_score:.2f}
            Number of passes: {number_of_passes}
            Number of failures: {number_of_failures}
            """)

            # Reset values for next subject
            subject_index += 1
            total_score = 0
            highest_score = 0  # Reset highest score
            lowest_score = 100  # Reset lowest score
            highest_students = ""
            lowest_students = ""
            number_of_passes = 0
            number_of_failures = 0

    def sample_output(self, position:list, total_score:list, average_score:list, scores:list):
        print("=" * 70 + "\nstudent\t", end="")

        for subject in self.subjects:
            print(f"\t {subject} ", end="")

        print("\t     TOT      AVG      POS  ")
        print("=" * 70)

        for i in range(len(scores)):
            print(f"{self.students[i]}\t", end="")
            for j in range(len(self.subjects)):
                print(f"{scores[i][j]:.2f}    ", end="")
            print(f"{total_score[i]:.2f}    {average_score[i]:.2f}      {position[i]}   ")

        print("=" * 70 + "\n")
        print("=" * 70)

            
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
total_score = system.get_student_total_score(scores)
posiyion = system.get_student_position(average, 2)
print(scores)
print(average)
print(total_score)
print(posiyion)
system.subject_summary(scores,2)
system.sample_output(posiyion,total_score,average,scores)