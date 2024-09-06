courses = {
    "mabani computer": (20, 3),
    "zaban omomi": (17, 2),
    "varzesh": (15, 1),
    "riazi omomi 1": (7, 3),
    "andishe eslami 1": (14, 2)
}


# جمع نمرات با احتساب ضریب تقسیم بر جمع ضرایب
# print((20 * 3 + 17 * 2 + 15 * 1 + 7 * 3 + 14 * 2) / (3 + 2 + 1 + 3 + 2))


def calculate_grade(courses):
    scores = [v[0] * v[1] for v in courses.values()]
    units = [v[1] for v in courses.values()]
    grade = sum(scores) / sum(units)
    print("Your grade is", str(grade)[:5])


calculate_grade(courses)
