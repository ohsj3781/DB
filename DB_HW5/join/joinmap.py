#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    tuple_list = line.split(",") # Splits a string into a list.
    
    if len(tuple_list) == 8: # emp file
        ename = tuple_list[1]
        deptno = tuple_list[7]
        
        # deptno = key  emp,ename = value
        print('{0}\t{1}'.format(deptno, 'emp,'+ename)) 
        
    else: # dept file
        loc = tuple_list[2]
        deptno = tuple_list[0]
        
        # deptno = key  dept,loc = value
        print('{0}\t{1}'.format(deptno, 'dept,'+loc))
