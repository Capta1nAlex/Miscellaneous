import requests
# Originally I wanted to take some sort of a tournaments resource (either chess or from some computer games from liquipedia.com, but I found their API kind of weird and gave up) 
req = requests.get('https://httpbin.org/get')

print(req.text)