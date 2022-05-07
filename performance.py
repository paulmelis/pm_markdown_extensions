#!/usr/bin/env python
import markdown, timeit

# Don't add ^ markers in baseline test, as those would become extra attributes
sb = """
First do these steps:
    
1. Item
{ .myitem .mylist }
2. Item
{ #item2 #list1 }
3. Item

Don't forget to finish with these steps:

4. Item
{ start=4 .important }
5. Especially the last one!
{ style="font-style: bold" }
"""

spm = """
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
"""

R = 100

def baseline():
    markdown.markdown(sb*R, extensions=['attr_list'])
    
def pm():
    markdown.markdown(spm*R, extensions=['pm_attr_list'])

N = 100

tb = timeit.timeit('baseline()', globals=globals(), number=N)
tbpm = timeit.timeit('pm()', globals=globals(), number=N)

print('%.3fs' % tb)
print('%.3fs (+%.1f%%)' % (tbpm, (tbpm-tb)/tb*100.0))
