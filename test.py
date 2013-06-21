#!C:/Python27/python.exe 
print "Content-Type: text/html\n" 
import urllib2 
response = urllib2.urlopen('http://python.org/') 
html = response.read() 
print html  