#!/usr/bin/env python
import markdown

s = '![Figure 5](someimg.png){: style="width:700px" }'

m = markdown.markdown(s, extensions=['pm_attr_list'])
print(m)

m = markdown.markdown(s, extensions=['attr_list'])
print(m)

m = markdown.markdown(s, extensions=['pm_attr_list', 'markdown_captions'])
print(m)

m = markdown.markdown(s, extensions=['attr_list', 'markdown_captions'])
print(m)
