import json
import urllib
url = "http://python-data.dr-chuck.net/comments_303993.json"
print 'Retriving:', url
content = urllib.urlopen(url).read()
print 'Retriving', len(content),'characters'
info = json.loads(content)
comments = info['comments']
print 'User count:', len(comments)
count_lst = [int(item['count']) for item in comments]
print "Sum", sum(count_lst)

