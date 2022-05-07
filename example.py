#!/usr/bin/env python
import markdown

def print_html(s):
    m = markdown.markdown(s, extensions=['pm_attr_list', 'tables', 'def_list'])
    print(m)
    print()

print_html("""
First do these steps:
    
1. Item
{ .myitem ^ .mylist }
2. Item
{ #item2 ^ #list1 }
3. Item

Don't forget to finish with these steps:

4. Item
{ ^ start=4 .important }
5. Especially the last one!
{ style="font-style: bold" }
""")

# Nested list

print_html("""
* Item 1
{ ^ .toplist }
    3. Third!
    { ^ .sublist start=3 }
    4. Fourth!
    5. Fifth!
* Item 2
* Item 3
""")

# Table

print_html("""
Name      | Value 
----------|-------
Something | Yes { #yes ^ .table }
Other     | No { #no }
""")

# Definition list

print_html("""
Apple { #apple ^ #fruit }
:   Pomaceous fruit of plants of the genus Malus in
    the family Rosaceae.

Orange { #orange ^ .deflist }
:   The fruit of an evergreen tree of the genus Citrus.
""")

