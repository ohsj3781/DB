#!/usr/bin/env python3
import sys

last_deptno = None
location = None
enames = []

for key_value in sys.stdin:
    key_value = key_value.strip()
    deptno, table_value = key_value.split("\t")
    
    table, value = table_value.split(",") # Gets a table name and a value
 
    if last_deptno == deptno: 
        if table == 'emp':
            enames.append(value)
        else: # table == 'dept'
            location = value
    else:
        if last_deptno and location and enames: # last_deptno and location and enames are not none
            for ename in enames:
                print("%s, %s"%(ename, location))
                
        # Init the location and enames
        location = None
        enames = []
        
        if table == 'emp':
            enames = [value]
        else: # table == 'dept'
            location = value
            
        last_deptno = deptno

if last_deptno and location and enames: # last_deptno and location and enames are not none
    for ename in enames:
        print("%s, %s"%(ename, location))
