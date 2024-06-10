#!/usr/bin/env python3
import sys


for line in sys.stdin:
    line = line.strip()
    tuple_list = line.split(",")  # Splits a string into a list.

    if len(tuple_list) == 4:  # dept file
        deptno = tuple_list[0]
        dname = tuple_list[1]
        dcampus = tuple_list[2]

        # deptno = key  dept,dname,dcampus = value
        print('{0}\t{1}'.format(deptno, 'dept,' + dname + ',' + dcampus))

    else:  # student file
        deptno = tuple_list[4]
        gpa = tuple_list[5]

        # deptno = key  student,gpa = value
        print('{0}\t{1}'.format(deptno, 'student,' + gpa))



