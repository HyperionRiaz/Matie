#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
import string
import random
import csv
from numpy import genfromtxt


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
	newPath = "http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html" #Redirect to a please upload a file page?
	print "Location: " + newPath + "\n\n"
elif fileitem.filename.split(".")[1] != "csv":
	newPath = "http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html" #Redirect to an incorrect format page
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

	   
	   



	newPath = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/' + 'OptionsPage.html'
	path2 = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/Agram.png'
	pathAgraph = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/Agraph.png'
	pathvisu = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/' + folderID + '_visualize.html'
	
	
	#====== The options page ===== #
	
	open('files/' + folderID + '/' +  'OptionsPage.html', 'wb').write("""<!DOCTYPE html><html>

	<head>

	<title>MAATIE | A new statistical tool</title>

	<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />

	<!-- Stylesheets -->

	<link rel="stylesheet" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/reset.css" />
	<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/styles.css' />
	
	<style>
	#options 
	{
		width:800px;
		height:500px;
		margin:0px auto; /* Right and left margin widths set to "auto" */
		 /* Counteract to IE5/Win Hack */
		padding:15px;
		border:1px dashed #333;
		background-color:#eee;
	}
	
	/* List 1 - variables */
	#list1 { }
	#list1 ul { list-style:none; text-align:center; border-top:1px solid #eee; border-bottom:1px solid #eee; padding:10px 0; }
	#list1 ul li { display:inline; text-transform:uppercase; padding:0 10px; letter-spacing:2px; }
	#list1 ul li a { text-decoration:none; color:#000000; }
	#list1 ul li a:hover { text-decoration:underline; }

	/* LIST #5 */
	#list5 { color:#eee; }
	#list5 ol { font-size:18px; }
	#list5 ol li { }
	#list5 ol li ol { list-style-image: url("../images/nested.png"); padding:5px 0 5px 18px; font-size:15px; }
	#list5 ol li ol li { color:#bfe1f1; height:15px; margin-left:10px; }
		
	.alert 
	{
	  padding: 8px 35px 8px 14px;
	  margin-bottom: 18px;
	  color: #c09853;
	  text-shadow: 0 1px 0 rgba(255, 255, 255, 0.5);
	  background-color: #fcf8e3;
	  border: 1px solid #fbeed5;
	  -webkit-border-radius: 4px;
		 -moz-border-radius: 4px;
			  border-radius: 4px;
	}

	.alert-error {
	  color: #b94a48;
	  background-color: #f2dede;
	  border-color: #eed3d7;
	   border:1px solid #333;
	}

	.alert-success {
	  color: #468847;
	  background-color: #dff0d8;
	  border-color: #d6e9c6;
	  border:1px solid #333;
	}

	.hero-unit {
	  padding: 30px;
	  margin-bottom: 30px;
	  margin-top: 30px;
	  background-color: #eeeeee;
	  -webkit-border-radius: 6px;
		 -moz-border-radius: 6px;
			  border-radius: 6px;
			   border:1px solid #333;
	}

	.hero-unit h1 
	{
	  margin-bottom: 0;
	  font-size: 30px;
	  line-height: 1;
	  letter-spacing: -1px;
	  color: inherit;
	}

	.hero-unit p {
	  font-size: 18px;
	  font-weight: 200;
	  line-height: 27px;
	  color: inherit;
	}
		
	.label,
		.badge {
		  font-size: 10.998px;
		  font-weight: bold;
		  line-height: 14px;
		  color: #ffffff;
		  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
		  white-space: nowrap;
		  vertical-align: baseline;
		  background-color: #999999;
		}

	.label {
	  padding: 1px 4px 2px;
	  -webkit-border-radius: 3px;
		 -moz-border-radius: 3px;
			  border-radius: 3px;
	}

	.badge {
	  padding: 1px 9px 2px;
	  -webkit-border-radius: 9px;
		 -moz-border-radius: 9px;
			  border-radius: 9px;
	}


		
	.label-important,
	.badge-important {
	  background-color: #b94a48;
	}

	.label-success,
	.badge-success {
	  background-color: #468847;
	}


	</style>


	<!-- Scripts -->

	<!-- Add jQuery library -->

	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>


	<!-- Add fancyBox (NOT IN USE AT THE MOMENT) -->

	<link rel="stylesheet" href="js/jquery.fancybox.css" type="text/css" media="screen" />
	<script type="text/javascript" src="js/jquery.fancybox.pack.js"></script>


	<script type="text/javascript">

		$(document).ready(function() {
			$(".fancybox").fancybox();
		});

	</script>
	




	
	
	
	<script type="text/javascript">
		
		function transpose()
		{
	
        $("#transposeClick").click();
		
		}
    
	</script>
	
	<script type="text/javascript">
	
		function report(period) 
		{
		  if (period!="one") 
		  {
		  
		   	  document.getElementById('dropdown').style.display='none';
			  document.getElementById('selector').style.display='none';
		  
		  
		  }
		   else
		   {
		   
		   	  document.getElementById('dropdown').style.display='block';
			  document.getElementById('selector').style.display='block';
		   
		   }


	


		} 
	</script>
	
	<script type="text/javascript">

function showSelected()
{
	
	var selObj = document.getElementById('dropdown');
	var txtIndexObj = document.getElementById('selectedIndex');

	
	var selIndex = selObj.selectedIndex;
	txtIndexObj.value = selIndex+1;
}
</script>





	<!-- D3 scripts) -->

		<script type="text/javascript" src="http://mbostock.github.com/d3/d3.js?2.4.6"></script>
	<link href='http://mbostock.github.com/d3/ex/force.css' rel='stylesheet' type='text/css' /><script src='http://mbostock.github.com/d3/d3.layout.js?2.4.6' type='text/javascript'> </script><script src='http://mbostock.github.com/d3/d3.geom.js?2.4.6' type='text/javascript'></script>

	
	</head>

	<body>
	<script type="text/javascript" src="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/tooltip.js"></script>

	<div id='wrapper' class='container_12 clearfix'>



	

		<a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/indexTWO.html'><img align='left' width='234' height='45' style="padding-top:40px;padding-left:20px;" src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/logo.png' ></a>


		<!-- Navigation Menu -->

		<ul id='navigation' class='grid_8'>

			

			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/contact.html'><span class='meta'>Get in touch</span><br>Contact us</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/news.html'><span class='meta'>Citations</span><br>News</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/help.html'><span class='meta'>Formatting</span><br>Help</a></li>				
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/about.html'><span class='meta'>The method</span><br>About</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html' class='current'><span class='meta'>Analyze data</span><br>Upload</a></li>

			

		</ul>

		

		<div class='hr grid_12'>&nbsp;</div>
		<div class='clear'></div>
		
		

		

	

		<!-- Caption Line -->
		<h4 class='grid_12 caption clearfix' align="left" >Successful file upload. Select your <span>preprocessing</span> options.</h4> 
		
	
		
		
		<br>
		<br>
		<br>
		<h4 class='grid_12 caption clearfix' align='center' style="margin:0px auto;padding-bottom:20px;">Your uploaded <span>data</span> is shown below. Please check it is correct.</h4>
		<br>
		<br>
		<br>
		<br>
		  
	
	
		<div id='table' style="height: 400px; width:700px; overflow: auto; border-style:solid; border-width:1px; padding-left:0px;margin: 0px auto;"></div>
		   
									<script>
									
									 d3.text("uploadDisplay.csv", function(datasetText) {

									var parsedCSV = d3.csv.parseRows(datasetText);
									
									var sampleHTML = d3.select("#table")
	
										.append("table")
										.style("border-collapse", "collapse")
										.style("border", "2px black solid")
												

										.selectAll("tr")
										.data(parsedCSV)
										.enter().append("tr")
										
										.selectAll("td")	
										.data(function(d){return d;})
										.enter().append("td")
										.style("border", "1px black solid")
										.style("padding", "5px")
										.on("mouseover", function(){d3.select(this).style("background-color", "aliceblue")})
										.on("mouseout", function(){d3.select(this).style("background-color", "white")})
										.text(function(d){return d;})
										.style("font-size", "12px");
										
									     
											
										});		
										

										
										</script>

								

							
		
		
		<br>
		""" + tableinfo  + """
		<br>
		<br>
		<h4 class='grid_12 caption clearfix' align='center' style="margin:0px auto;padding-bottom:20px;">Your <span>variables</span> are listed below. Please check they are correct.</h4>
		<br>
		<br>
		<br>
		<br>
		
		<div id="list1">
		   <ul>
		   """ + listVar + """
			  
		   </ul>
		</div>
		
		<span class="meta">These are the variables Maatie will process. Some variables may have had certain characters replaced for safety. <br >If these variables are not correct your data may be the wrong way around. Click <a href='#' onclick="transpose();">here</a> to quickly tranpose your data.</span>
		<br>
		<span class="meta">Uploaded  """ + numcols + """ variables with """ + numrows + """ rows of data.</span>
		
		<br>	
		<br>
		
		<!-- Hidden transpose submit form -->
		<div style="display:none">
		<form enctype='multipart/form-data' action='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/transpose.py'  method='post'>
		
			<input type='text' style="visibility:hidden" class='id' name='id' value='""" +folderID + """'>
			

					<input type='submit'  value='Transpose Data' id='transposeClick'>			

		</form>
		</div>
		
		<br>
		<div """+classComments+""" >
			""" + warnings + """
		</div>
		
		<br>
		<br>
	

		<br> 
		<h4 class='grid_12 caption clearfix' align='center' style="margin:0px auto;padding-bottom:20px;">If your data is incorrect, please correct your data and <a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html'>reupload your file.</a></h4>
		<br> 
		<br> 
		<br> 
		<br> 
		<br> 
		
		
		
	
	
				
		<h4 class='grid_12 caption clearfix' align='center' style="margin:0px auto;padding-bottom:20px;">If your data is correct, choose your processing options.</h4>



		
		<br>
		<br>
		
	<div class='hero-unit'> <!-- old box is id='options' -->
	
			<h5 class='grid_12 caption clearfix'  align='left' style="padding-bottom:5px;text-align:left">Analysis Options</h5>
				
			
			<img align='right' style="margin-right:30px;padding-top:0px;padding-bottom:0px" width='180' height='232' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/processnow.png'>
			<form enctype='multipart/form-data' action='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/process.py'  method='post'>
			
				
				
				Select processing options - last 2 still being implemented, choose first option for full results: <br>
				<select id="method" name="method" onchange="report(this.value)"> 
						<option value="pairs">Find correlation between all pairs of your variables</option>
						<option value="one">One against all (Only table visulization for now, more to be implemented soon)</option>
						<option value="exp">Finding the best set of explanatory variables</option>
						<option value="oneshot">One shot analyses, like testing for significant multivariable associations</option>
				</select>
				
				
				<input type='text' style='display:none' id='selectedIndex'  name='selectedIndex'  value='2'>
				<div id='selector' style='display:none'> Select one variable to be tested against all others:	
					
						
						
				
						<select id='dropdown' style='display:none' name ='dropdown' class='dropdown' onchange='showSelected()'>
						  """ + variables + """
						</select>
				</div>
		
				<br>	
				<br>
				Select output options - to be implemented: <br>
				<select >
				<option>All outputs - .csv output, interactive visulizations and pdf of static images. </option>
				<option>No interactive outputs - only .csv ouput and pdf of static images.</option>
				<option>No interatice outputs or images - only .csv output.</option>
				</select> 
				
				<br>	
				<br>
				Include a statistical significance test - to be implemented: <input type="checkbox" id='longer'>
				<br>	
				<br>
				Save results on server for longer than 3 days - to be implemented: <input type="checkbox" id='longer'>
				<br>	
				<br>
				More options will be added here. 
				
				<input type='text' style="visibility:hidden" class='id' name='id' value='""" +folderID + """'>
				
				
				<br>

				<div class='process' id='process' name='process' onmouseover="Tip('Process your data now with the options specified above.')" onmouseout="UnTip()" >				
					<input type='submit'   >				
				</div>

			</form>
			
		

	</div>	
	

</div> 
	

</body>

</html>
	""")
	
	
	print "Location: " + newPath + "\n\n";
	

else: 
	newPath = "http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html"
	print "Location: " + newPath + "\n\n"
	
