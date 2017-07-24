#Josh Richardson
#Group 56
#importing modules
import urllib, xml.etree.ElementTree as ET

#reading in the RSS feed
conn = urllib.urlopen("http://feeds.nytimes.com/nyt/rss/World")
lines = conn.read()
conn.close()

root = ET.XML(lines)

news_items = root.findall("channel/item")

#user input for category
selected_category = raw_input("Please enter a category to search for: ")

#cycles through each news items and prints relevant information
for news in news_items:
    categories = news.findall("category")
    regions = []
    matches = False
    for category in categories:
        if category.attrib["domain"] == "http://www.nytimes.com/namespaces/keywords/nyt_geo":
            regions.append(category.text)
        elif category.attrib["domain"] == "http://www.nytimes.com/namespaces/":
            regions = ["China"]
        if selected_category.lower() in category.text.lower():
            matches = True
    if matches == True:
        if len(regions) > 1:
            print ", ".join(regions) + ":",
        if len(regions) == 1:
            print regions[0],
        print news.find("title").text + "(By " + news.find("{http://purl.org/dc/elements/1.1/}creator").text + ")"
        print "Link:"
        print news.find("link").text
        print

