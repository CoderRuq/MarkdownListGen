# MarkdownListGen

---

### Overview

From a text input consisting of one item per line (such as a shopping list), 
output with each line being prefixed with the markdown syntax for an empty to-do list item. `- [ ]`

<br>

### Details

To begin, I'm going to build the simple logic that will take in an input file, and output the formatted text
to a output file. From there, I plan on designing and assembling a simple GUI that will take in input in one text
box and format it to another text box, that will enable simple copy/paste usage. Hopefully I can also figure out
exporting the entire program as a simple .apk file so I can make use of it on my Android device.

<br>

---

<br>

### Libraries

* kivy
  * For a simple GUI.

### Objects

* Layout
  * Contains the GUI elements and program logic, inherits kivy's GridLayout
* MarkdownListGen
  * Required for kivy, just builds and allows the app to be run.