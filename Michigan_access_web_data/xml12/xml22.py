# dont name your file name the same as module name
import urllib

import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_303989.xml'

uh = urllib.urlopen(url)

data = uh.read()

tree = ET.fromstring(data)

counts = tree.findall('.//count')

print "count: ", len(counts)
count_lst = [int(count.text) for count in counts]

print "Sum:" ,sum(count_lst)