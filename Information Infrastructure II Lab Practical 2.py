#import modules
import re, urllib, webbrowser

#parsing
try:
    web_page = urllib.urlopen("http://www.soic.indiana.edu/undergraduate/courses/index.html")
    contents = web_page.read()
    web_page.close()
except:
    print "Not A Valid URL!"

#lists of courses
csci_courses = re.findall('CSCI [A-Z][\d][\d][\d] [\w, /+-]+', contents)
info_courses = re.findall('INFO [A-Z][\d][\d][\d] [\w, /+-]+', contents)

#main
print "Parsing: http://www.soic.indiana.edu/undergraduate/courses/index.html"
keyword = raw_input("Please enter a word to search for: ")
print "CSCI Undergraduate Courses that match:"
for course in csci_courses:
    if keyword in course or keyword.title() in course or keyword.lower() in course:
        print course
print
print "INFO Undergraduate Courses that match:"
for course in info_courses:
    if keyword in course or keyword.title() in course or keyword.lower() in course:
        print course
course = raw_input("Enter the name of a course (Ex: I210) to view it, or press ENTER: ")

#INFO base link
base_link_info = 'https://www.soic.indiana.edu/undergraduate/courses/index.html\?number={0}&department=INFO'

#CSCI base link
base_link_csci = 'https://www.soic.indiana.edu/undergraduate/courses/index.html\?number={0}&department=INFO'

#opens requested page
try:
    url = base_link_info.format(course)
    webbrowser.open(url)
except:
    url = base_link_csci.format(course)
    webbrowser.open(url)
    
