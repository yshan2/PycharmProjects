import urllib.request
# import

g = urllib.request.urlopen('http://nsdual.boxuegu.com/view/home.html')
s = open('./inner.html','wb')
s.write(g.read())
s.close()
