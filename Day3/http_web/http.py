from urllib2 import Request, urlopen, URLError

request = Request('http://placekitten.com/')


try:
	response = urlopen(request)
	value = response.read()
	print value[0:3]
except URLError, e:
    print 'no cats', e
