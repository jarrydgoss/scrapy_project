from html.parser import HTMLParser

class ParseResults(HTMLParser):

    def __init__(self):
        super().__init__()
        self.recording = False
        self.title = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.recording = True
        else:
            self.recording = False
            
    def handle_data(self, data):
        if self.recording:
            self.title.append(data)


p = ParseResults()
with open("html/1992_World_Junior_Championships_in_Athletics_–_Men's_high_jump") as _f:
    p.feed(_f.read())

print(p.title)
import scrapy
import os
current_dir = os.path.abspath('')
url = os.path.join(current_dir, "html/1992_World_Junior_Championships_in_Athletics_–_Men's_high_jump")
with open(url) as _f:
    url_data = _f.read()

response = scrapy.http.TextResponse(url, body=url_data, encoding='utf-8')
import scrapy
import os
current_dir = os.path.abspath('')
url = os.path.join(current_dir, "html/1992_World_Junior_Championships_in_Athletics_–_Men's_high_jump")
with open(url) as _f:
    url_data = _f.read()
​
response = scrapy.http.TextResponse(url, body=url
