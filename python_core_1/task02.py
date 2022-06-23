def get_student_names(dict_names):
    return sorted(dict_names.values())


print(
    get_student_names({"Student 1": "Steve", "Student 2": "Becky", "Student 3": "John"})
)
