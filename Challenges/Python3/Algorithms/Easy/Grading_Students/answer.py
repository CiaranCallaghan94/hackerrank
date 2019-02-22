#!/bin/python3
# https://www.hackerrank.com/challenges/grading/problem

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        new_grade = grade
        if grade > 35:
            remainder = grade % 5
            if remainder >= 3:
                new_grade = grade + (5 - remainder)
        rounded_grades.append(new_grade)
    return rounded_grades


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
