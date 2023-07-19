def students():
    return [
        {
            'name': 'João',
            'grade': 6
        },
        {
            'name': 'Maria',
            'grade': 9
        },
        {
            'name': 'José',
            'grade': 4
        }
    ];

def plot_students(students):
    total_spaces = 35;

    print(f"{'NOME':10} | {'NOTA':4} | {'STATUS':14}");
    for student in students:
        print('-' * total_spaces)
        print(f"{student['name']:10} | {student['grade']:4} | {student['status']:14}");

def analyze_students_grades(students):
    for student in students:
        student['status'] = analyze_grade(student['grade']);

    return students;

def analyze_grade(grade):
    if grade < 5:
        return 'Reprovado';

    return 'Aprovado' if grade >= 7 else 'Recuperação';

def main():
    analyzed_students = analyze_students_grades(students());
    plot_students(analyzed_students);

main();