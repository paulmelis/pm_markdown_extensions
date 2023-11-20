# pm_attr_list

This is a modified version of Python-Markdown's
`attr_list` extension, to allow list-wide and table-wide attributes to
be set. It specifically aims to lift the [limitation](https://python-markdown.github.io/extensions/attr_list/#limitations)
of `attr_list` that attributes cannot be set on implied elements (i.e.
elements that are not explicitly specified in markdown, such as a table start).

By supporting list- and table-wide attributes several useful things become possible, for example

* Starting a numbered list at a specific number
* Setting a specific class on a single list/table, as an exception to the default class
* Any other custom attributes on output `<ol>`, `<ul>`, `<dl>` or `<table>` HTML tags

This extension only applies minimal code changes to the original `attr_list` extension,
so existing functionality of that extension should still be available.
However, for some more exotic markdown input the code could still be buggy, 
please report here if you find any issues.

As this extension does slightly more work than the original `attr_list` it
is somewhat slower. Using a simple test (`performance.py`) the difference appears
to be fairly small though, around 3% extra time.

## Usage

Add attributes to your markdown as usual (as described [here](https://python-markdown.github.io/extensions/attr_list)).
A new marker `^` is available that you can include in the attribute definition.
Any attributes following the marker are set on the parent list/table in the HTML output.

### Examples

Continuing list numbering, setting list class and ID:

```md
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
```

HTML:

```html
<p>First do these steps:</p>
<ol class="mylist" id="list1">
<li class="myitem">Item</li>
<li id="item2">Item</li>
<li>Item</li>
</ol>
<p>Don't forget to finish with these steps:</p>
<ol class="important" start="4">
<li>Item</li>
<li style="font-style: bold">Especially the last one!</li>
</ol>
```

Works for nestes lists as well, e.g.

```md
* Item 1
{ ^ .toplist }
    3. Third!
    { ^ .sublist start=3 }
    4. Fourth!
    5. Fifth!
* Item 2
* Item 3
```

turns into

```html
<ul class="toplist">
<li>Item 1<ol class="sublist" start="3">
<li>Third!</li>
<li>Fourth!</li>
<li>Fifth!</li>
</ol>
</li>
<li>Item 2</li>
<li>Item 3</li>
</ul>
```

Table:

```md
Name      | Value 
----------|-------
Something | Yes { #yes ^ .table }
Other     | No { #no }
```

becomes

```html
<table class="table">
<thead>
<tr>
<th>Name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Something</td>
<td id="yes">Yes</td>
</tr>
<tr>
<td>Other</td>
<td id="no">No</td>
</tr>
</tbody>
</table>
```

Definition list:

```md
Apple { #apple ^ #fruit }
:   Pomaceous fruit of plants of the genus Malus in
    the family Rosaceae.

Orange { #orange ^ .deflist }
:   The fruit of an evergreen tree of the genus Citrus.
```

becomes

```html
<dl class="deflist" id="fruit">
<dt id="apple">Apple</dt>
<dd>Pomaceous fruit of plants of the genus Malus in
the family Rosaceae.</dd>
<dt id="orange">Orange</dt>
<dd>The fruit of an evergreen tree of the genus Citrus.</dd>
</dl>
```

## Installation

This module is not registered on PyPI, but you can still install
it using pip by using:

```
pip install <path-to-this-repo-checkout>
```

This will also work, for example, when working with MkDocs and you use a virtualenv 
to install all its dependencies. Just as long as the virtualenv is active when calling `pip`
installation should work automatically and you enable the extensions as shown below.

See `example.py` for how to use with Python-Markdown directly.

### MkDocs

Adding `pm_attr_list` and/or `pm_markdown_captions` to `mkdocs.yml` instead of `attr_list` should work out 
of the box, assuming the modules can be found as mentioned above. E.g.

```
# mkdocs.yml
markdown_extensions:
  - pm_attr_list
  - pm_markdown_captions
```

## FAQ

* Can you use this to set attributes on a table row, or similar element?

    No, this is currently not supported. It would be a bit tricky to provide,
    as it would mean requiring syntax to differentiate between "set on parent table"
    and "set on parent row". Perhaps a `<` marker could serve for that, but it's 
    currently not implemented.

* This would make a great addition to include in Python-Markdown's
attr_list extension itself. Can you ask to include it?

    Requests to add a feature to control list-wide or table-wide attributes
have been made at the Python-Markdown project over many years since 2013 
(see [227](https://github.com/Python-Markdown/markdown/issues/227), 
[312](https://github.com/Python-Markdown/markdown/issues/312),
[505](https://github.com/Python-Markdown/markdown/issues/505),
[594](https://github.com/Python-Markdown/markdown/issues/594),
[600](https://github.com/Python-Markdown/markdown/issues/600),
[668](https://github.com/Python-Markdown/markdown/issues/668), 
[1251](https://github.com/Python-Markdown/markdown/pull/1252)),
but developer feedback has always been very negative to add it. Hence this
unofficial extension.

## License

The license for `pm_attr_list.py` is BSD-2, just like the original license
as listed at the top comment in the [original file](https://github.com/Python-Markdown/markdown/raw/2164c4b4752b9061c742326ea0413719333058fc/markdown/extensions/attr_list.py).

The file `pm_markdown_captions.py` is based on `markdown_captions.py`
from https://github.com/Evidlo/markdown_captions, which is license
GNU GPL.