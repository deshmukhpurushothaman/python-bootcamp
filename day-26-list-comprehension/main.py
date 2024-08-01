# numbers = [1, 2, 3, 4, 5]
# new_numbers = [n+1 for n in numbers]
# print(numbers)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# square = [num*num for num in numbers]
# print(square)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# passed_students = {student: score for (
#     student, score) in students_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed velocity of an Unladen swallow?"
# result_list = sentence.split()
# print(result_list)
# result = {word: len(word) for word in result_list}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day: (temp * (9/5) + 32) for (day, temp) in weather_c.items()}
# print(weather_f)

import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# for (index, row) in student_data_frame.iterrows():
#     print(row)

data = pandas.read_csv(
    "./day-26-list-comprehension/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
