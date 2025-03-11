def collect_scores(number_of_students: int, number_of_subjects: int) -> list:
    scores = []
    grades = []
    for i in range(number_of_students):
        for j in range(number_of_subjects):
            while True:
                grade = input(f"enter grade for student {i + 1} subject {j + 1}: ")
                if check_grade(grade):
                    print("invalid grade, grade must be a number and must be between 0-100")
                else:
                    grades.append(grade)
                    break
        scores.append(convert_grade_str_to_float(grades))
        grades = []

    return scores


def check_grade(grade:str)->bool:
    try:
        grade = float(grade)
        if grade > 100 or grade < 0:
            return True
        return False
    except ValueError:
        return True


def convert_grade_str_to_float(grade:list[str])->list[float]:
    grade_float = []
    for i in grade:
        grade_float.append(float(i))
    return grade_float


print(collect_scores(number_of_students=3, number_of_subjects=2))