#!C:/Python27/python.exe 

import cgi, os
import cgitb; cgitb.enable()
import string
import random
import csv
from numpy import genfromtxt

##!/usr/bin/env python 


def folderGen (size=20, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

folderID = folderGen() 


try: # Windows needs stdio set for binary mode.
	import msvcrt
	msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
	msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
	pass

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']


#A massive if statement for validation, only accepting csv files for now 
if fileitem.filename=="":
	newPath = "index.html" #Redirect to a please upload a file page?
	print "Location: " + newPath + "\n\n"
elif fileitem.filename.split(".")[1] != "csv":
	newPath = "index.html" #Redirect to an incorrect format page
	print "Location: " + newPath + "\n\n"
elif fileitem.filename.split(".")[1] == "csv": 
	#Only store if it is the correct file type. 
		
	if fileitem.filename:
	
	 
	   
	   #Strip leading path from file name to avoid directory traversal attacks
	   fn = os.path.basename(fileitem.filename)
	   os.makedirs('files/' + folderID + '/')
	   
	   
	   #Input cleanings ======================================================
	   
	   #Replace variable unwated chars
	   firstLine = fileitem.file.readline()
	   firstLine = firstLine.replace(" ","_")
	   firstLine = firstLine.replace(")","")
	   firstLine = firstLine.replace("(","")
	   firstLine = firstLine.replace("[","")
	   firstLine = firstLine.replace("]","")
	   
	   total = firstLine
	   open('files/' + folderID + '/' + 'upload.csv', 'wb').write(firstLine)
	   
	   
	   #Get first 50 and print to seperate display csv TEMPORARY FIX TO DO MORE ELEGANT SOLUTION HERE
	   first50 = firstLine
	   
	   #numcols = len(firstLine.split(','))           #numcols fixed but numrows broken for smalltestdata
	   numrows = 1
	   for line in fileitem.file:
			total = total + line
			if numrows < 50:
				first50 = first50 + line
			
			numrows = numrows + 1
			
	   open('files/' + folderID + '/' + 'upload.csv', 'wb').write(total)
	   open('files/' + folderID + '/' + 'uploadDisplay.csv', 'wb').write(first50)
	   
	  	
		
	   r = csv.reader(open('files/' + folderID + '/' + 'upload.csv', 'U'))		
			
	   line1=r.next() #variables should be in the first row of the csv
	   numcols = 0
	   for item in line1:
			numcols = numcols+1
		
	   
	   
	   

       
	   
	   #Warning string that builds up warnings as found
	   warnings = ""
	   warn = False
	   classComments = ""
	   
	  
	   if numcols > numrows:
				warnings = warnings +"\n<span class='label label-important'>Warning</span> You have more columns than rows in your data. This may be because your data is the wrong way around. <a href='#' onmouseover='Tip('Your data above with be transposed after which this page will refresh and display your new data.')' onmouseout='UnTip()' onclick='transpose();'>Click here to transpose your data and fix this error.<br /></a> "
				warn = True
				
	   tableinfo = ""
	   if (numrows > 50):
			tableinfo ="<div style='margin:0px auto;'> <span class='meta'>Only 50 rows of your " + str(numrows) +" rows of uploaded data are shown here.</span></div>"
	   
 
	   numrows = str(numrows)
	   numcols = str(numcols)
	 
			

	   
	   #Create dropdown box of variables and other HTML for page
	   variables = ""
	   listVar = ""
	   flagLong = False
	   for variable in line1:
			
		
			#variable = variable.replace(" ", "_")
			
			variables = variables  + "\n<option>"  + variable + "</option>"
			listVar = listVar + "\n<li>" + variable + "</li>"
			if (flagLong == False):
				if len(variable) > 30:
					flagLong = True
					warnings = warnings + "\n<span class='label label-important'>Warning</span> One or more of your variable names such as '" + variable+ "'  is longer than 30 characters. Using long variable names will diminish the effect of later visulizations and output. Please consider shortening your variables for cleaner outputs.<br />"
					warn =True
		
	   if warn==True:
			   classComments = 'class="alert alert-error"'
	   else:
			   classComments = 'class="alert alert-success"'
			   warnings ="<span class='label label-success'>Success</span>  Maatie found no problems with your data."
			   
			   
       
		
			
	 
		#TODO additional preprocessing, scan columns find any variable <10 values and warn. Scan for textual and non numerical data and warn. 
			
	
	   
	else:
	   message = 'No file was uploaded' #TODO change and redirect to mainpage with an error

	   
	   



	newPath = 'files/' + folderID + '/' + 'OptionsPage.html'
	path2 = 'files/' + folderID + '/Agram.png'
	pathAgraph = 'files/' + folderID + '/Agraph.png'
	pathvisu = 'files/' + folderID + '/' + folderID + '_visualize.html'
	
	
	#====== The options page ===== #
	
	with open ("optionsPage.html", "r") as myfile:
		data=myfile.read().replace('\n', '')
		
	from string import Template
	
	template = Template(data)
	
	
	final = template.safe_substitute(folderID=folderID, numrows=numrows, numcols=numcols, tableInfo = tableinfo, classComments = classComments, listVar=listVar, warnings=warnings, variables=variables)
	open('files/' + folderID + '/' +  'OptionsPage.html', 'wb').write(final)
	
	
	
	print "Location: " + newPath + "\n\n";
	

else: 
	newPath = "index.html"
	print "Location: " + newPath + "\n\n"
	
