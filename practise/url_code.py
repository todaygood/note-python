
import urllib.parse

username='"sanqiyanxishe@163.com"'


a = urllib.parse.quote(username)

print(a)

b= urllib.parse.unquote(a)

print(b)

