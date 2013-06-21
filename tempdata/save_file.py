#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
import string
import random

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

# Test if the file was uploaded
if fileitem.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   os.makedirs('files/' + folderID + '/')
   open('files/' + folderID + '/' + 'upload.csv', 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully to random folder ' + folderID
   s = ''+folderID
   #path =  "/var/www/files/"+folderID+"/consoleOut.txt"
   
else:
   message = 'No file was uploaded'
   s = 'derp'
   
   
   
   
   
print """\
Content-Type: text/html\n
<html>
<head>
	<title>MAATIE| A new statistical tool</title>
	<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
	
	<!-- Stylesheets -->
	<link rel="stylesheet" href="css/reset.css" />
	<link rel='stylesheet' href='css/styles.css' />

	
	<!-- Scripts -->
	<!-- JQUERY LOADING SCREEN SCRIPT -->
	<script type="text/javascript" src="js/jquery-1.7.2.min.js"></script>
	<script type="text/javascript">
		$(window).load(function(){
		$("#loading").hide();
		})
	</script>
	
	
	<script type="text/javascript" >
		$.get("/var/www/files/text.txt", null, function(response){
    $("#output").val(response); // where theTextArea is the ID of the textarea you want to put the data into.
	})
	</script>



</head>
<body>

	<!-- THE LOADING PORTION OF CONTENT -->
	<div id="loading">
		Loading content, please wait..
	<img src='images/loading.gif' alt='loading..' />
		</div>
		
	

	<!-- THE ACTUAL CONTENT - PUT RESULTS HERE?  -->
	<div id='wrapper' class='container_12 clearfix'>

	
		<!-- Text Logo -->
		<img align='left' src='images/logo.jpg' >
		<!-- h1 id='logo' class='grid_4'>Maatie</h1 -->
		
		<!-- Navigation Menu -->
		<ul id='navigation' class='grid_8'>
			
			<li><a href='contact.html'><span class='meta'>Get in touch</span><br />Contact us</a></li>
			<li><a href='blog.html'><span class='meta'>Citations</span><br />News</a></li>
			<li><a href='portfolio.html'><span class='meta'>Formatting</span><br />Help</a></li>
				
			<li><a href='about.html'><span class='meta'>The method</span><br />About</a></li>
			<li><a href='index.html' class='current'><span class='meta'>Analyze data</span><br />Upload</a></li>
			
		</ul>
		
		<div class='hr grid_12'>&nbsp;</div>
		<div class='clear'></div>
		
		<!-- TEST IMAGE FOR LOADING (edited out for now) -->
		
		<!-- p style='text-align:center;'><img alt='' src='images/punk_1280x800.jpg' width='700' height='900'/ --></p>
		<br />
		<br />
		<br />
		
		<h2 class='grid_12 caption clearfix' align="center">Results</h2>
		<p align='center'>File uploaded to a random folder ID %s , here is a live stream of some of the output.</p>
		
		<p align='center'><textarea id="output" readonly='true'  rows="15" cols="45" >
		
		</textarea></p>



		<br />
		<br />
		<br />
	

			<br />
		<br />
		<br />
		<!-- Caption Line -->
		<h2 class='grid_12 caption clearfix' align="center">Basic results are visible above. Select one of the options below to see a more detailed breakdown of analysis.</h2>
		
		
		
		<br />
		<br />
		<br />
		<br />
		
		
		<div class='hr grid_12 clearfix quicknavhr'>&nbsp;</div>
		<div id='quicknav' class='grid_12'>
			<a class='quicknavgrid_3 quicknav alpha' href='visualize.html'>
					<h4 class='title '>Visualize results</h4>
					<p>This link/bottom only becomes active after file has been processed above. View graphs, trees and different interpretations of data [link to visualize page]. </p>
					<p style='text-align:center;'><img alt='' src='images/Art_Artdesigner.lv.png' /></p>
				
			</a>
			<a class='quicknavgrid_3 quicknav' href='files/%s/output.csv'>   <!-- Downloads the output.csv stored in the random folder -->
					<h4 class='title '>Download results</h4>
					<p>This link/bottom bar only becomes active after file has been processed above. Download your results in pdf, spreadsheet or have it emailed to yourself [link to download page]. </p>
					<p style='text-align:center;'><img alt='' src='images/info.png' /></p>
				
			</a>
			<a class='quicknavgrid_3 quicknav' href='index.html'>
					<h4 class='title '>Run another analysis</h4>
					<p>If not downloaded previous results, ask for confirmation and warn. Else dump previous results and refresh main page.</p>
					<p style='text-align:center;'><img alt='' src='images/Blog_Artdesigner.lv.png' /></p>
				
			</a>
			<a class='quicknavgrid_3 quicknav' href='about.html'>
					<h4 class='title '>The method</h4>
					<p>Created by Ben Murrell and other researchers, read the paper that describes the method. [Link to method/paper page] </p>
					<p style='text-align:center;'><img alt='' src='images/hungry_bird.png' /></p>
			</a>
		</div>
		<div class='hr grid_12 clearfix'>&nbsp;</div>
		<!-- Footer -->
		<p class='grid_12 footer clearfix'>
			<span class='float'><b>&copy; Created by</b> <a href='http://www.rmoola.com'>Riaz Moola</a>, <b>Images by</b> <a href="">???</a> - .</span>
			<a class='float right' href='#'>top</a>
		</p>
		
	</div><!--end wrapper-->
</body>
</html>z
""" % (s,s)

os.system("R --vanilla --slave --args "+folderID+" < datProc.R > /var/www/files/"+folderID+"/consoleOut.txt")