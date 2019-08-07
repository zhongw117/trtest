# python3-env/bin/python3
# -*- coding:utf-8 -*-
import json
import csv
from pyexcel.cookbook import merge_all_to_a_book
import glob
# poen file for reading
with open('data.json', 'r') as input_file:
    # parse file into  dict
    json_file = json.load(input_file)
# columns to be checked
permissionList = [
                'view_grades',
                'change_grades', 
                'add_grades', 
                'delete_grades', 
                'view_classes', 
                'change_classes', 
                'add_classes', 
                'delete_classes'
                ]
# open output file for writing results
with open('results.csv', 'w') as output_file:
    # create csv file
    csv_writer = csv.writer(output_file)

    # write header
    csv_writer.writerow(['name']+permissionList)

    # write row for each user
    for user in json_file:
        # for each element in columns 
        # if element in the permissionlist
        # return 1
        # else
        # return 0
        csv_writer.writerow([user] + [1 if c in json_file[user] else 0 for c in permissionList])

# convert csv file to xlsx file
merge_all_to_a_book(glob.glob("results.csv"), "output.xlsx")
