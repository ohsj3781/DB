#!/usr/bin/env python3
import sys
from collections import defaultdict

dept_info = dict()
students_gpas = defaultdict(list)

for key_value in sys.stdin:
    key_value = key_value.strip()
    deptno, table_value = key_value.split("\t")

    table_value = table_value.split(",")  # Gets a table name and a value
    table = table_value[0].strip()
    value = table_value[1:]
    if table == 'dept':
        name = value[0].strip()
        campus = value[1].strip()
        dept_info[deptno] = (name, campus)
    else:  # table == 'student'
        gpa = float(value[0].strip())
        students_gpas[deptno].append(gpa)


for deptno, gpas in students_gpas.items():
    avg_gpa = sum(gpas)/len(gpas)
    if avg_gpa <= 2.5 or dept_info.get(deptno) is None:
        continue

    name, campus = dept_info[deptno]
    print('{0}, {1}, {2}'.format(name, max(gpas), campus))
