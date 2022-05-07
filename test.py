#!/usr/bin/env python
import markdown

s="""Let's add another shape key:

11. Add a third shape key, it will be called `Key 2`. 
{ ^ start=11 }
12. Select `Key 2` and apply a second set of mesh changes in edit mode.
13. Once again exit edit mode.
14. Play around with the influence values of both shape keys, as well as the checkboxes next to the influence values.
{ .item ^ .list }

# Nested list

* Item 1
{ ^ .toplist }
    3. Third!
    { ^ .sublist start=3 }
    4. Fourth!
    5. Fifth!
* Item 2
* Item 3

# Table

Name      | Value 
----------|-------
Something | Yes { #yes ^ .table }
Other     | No { #no }

# Definition list

Apple { #apple ^ #fruit }
:   Pomaceous fruit of plants of the genus Malus in
    the family Rosaceae.

Orange { #orange ^ .deflist }
:   The fruit of an evergreen tree of the genus Citrus.
"""

m = markdown.markdown(s, extensions=['pm_attr_list', 'tables', 'def_list'])
print(m)