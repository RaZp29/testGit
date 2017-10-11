#Used to make requests
# python 3.x:
import urllib.request
#import urllib

# python 3.x:

x = urllib.request.urlopen('https://www.google.com/')
#x = urllib.urlopen('https://www.google.com/')
#print(x.read())



# used to parse values into the url
import urllib.parse
'''
#from urllib2 import urlopen
url = 'https://www.google.com/search'
values = {'q' : 'python programming tutorials'}

data = urllib.parse.urlencode(values)
#data = urllib.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
#req = urllib.urlopen(url, data)
resp = urllib.request.urlopen(req)
#resp = urlopen(req)
respData = resp.read()

print(respData)
'''

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    #print(x.read())

    saveFile = open('noheaders.txt','w')
    saveFile.write(str(x.read()))
    saveFile.close()
except Exception as e:
    print(str(e))


try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))


# RegEx

'''
Identifiers:

\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.
Modifiers:

{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance"
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code
White Space Charts:

\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return
Characters to REMEMBER TO ESCAPE IF USED!

. + * ? [ ] $ ^ ( ) { } | \
Brackets:

[] = quant[ia]tative = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z
'''

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, anD hiS grandfather, Oscar, is 102. 
'''

ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)
upper = re.findall(r'[a-z]+[A-Z]',exampleString)

print(ages)
print(names)
print(upper)