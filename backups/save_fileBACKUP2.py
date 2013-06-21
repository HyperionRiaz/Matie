#!C:/Python27/python.exe 

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

	#A massive if statement for validation

		
if fileitem.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   os.makedirs('files/' + folderID + '/')
   open('files/' + folderID + '/' + 'upload.csv', 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully to random folder ' + folderID
   s = ''+folderID
   
else:
   message = 'No file was uploaded'
   s = 'derp'
   
   
   


newPath = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/' + folderID + '_Page.html'
path2 = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/Agram.png'
pathAgraph = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/Agraph.png'
pathvisu = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/' + folderID + '_visualize.html'

#======== The first loading page ============

open('files/' + folderID + '/' + folderID + '_Page.html', 'wb').write("""<html>
<head>
	<title>MAATIE| A new statistical tool</title>
	<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
	
	<!-- Stylesheets -->

	<link rel="stylesheet" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/reset.css" />
	<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/d3.css' />
	<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/styles.css' />
	

	<!-- Scripts -->
	<!-- JQUERY LOADING SCREEN SCRIPT -->
	<script type="text/javascript" src="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery-1.7.2.min.js"></script>
	

	<!-- D3 Script -->
	<script type="text/javascript" src="http://mbostock.github.com/d3/d3.js"></script>
	


	<!-- Refresh box script -->
	<script type="text/javascript">
			setInterval(function() {
			$('#output').load('consoleOut.txt');
			}, 50);
	</script>
	
	<!-- Update images/display options script -->
		<script type="text/javascript">
			var refreshImage = setInterval(function() 
			{
				 $.ajax
				 ({
			   
				 url:'adj3.json',
				type:'HEAD',
				error:
				  function()
				  {
						 var imgDest = document.getElementById('ok');
						
						imgDest.setAttribute('src', 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/loader2.gif');
						$("#proceed").fadeOut("slow");
						$("#proceed").fadeOut(2000);
					
						
					
					}, 
				success:
					function()
					{
						
						
						
						//$("#proceed").fadeIn(6000);
						
					
						
						//clearInterval(refreshImage);		
												
		

					}
				}) 

	}, 2000);
	
	</script>
	

	<!-- Fancybox stuff-->
	<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox.css' type='text/css' media='screen' />
	 <!--script type='text/javascript' src='http://jquery-ui.googlecode.com/svn/trunk/jquery-1.4.2.js'></script-->
	 <script type='text/javascript' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox.pack.js'></script>
	 
	 <!-- Add Buttons -->
	<link rel="stylesheet" type="text/css" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox-buttons.css" />
	<script type="text/javascript" src="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox-buttons.js"></script>
		

	
<script type='text/javascript'>
			$(document).ready(function() 
			{	
				$(".results").fancybox({
						
						
							openEffect  : 'fade',
						closeEffect : 'elastic',
					

						prevEffect : 'fade',
						nextEffect : 'fade',

						closeBtn  : true,

						helpers : {
							title : {
								type : 'inside'
							},
							buttons	: {}
						},

						afterLoad : function() {
							this.title = 'Image ' + (this.index + 1) + ' of ' + this.group.length + (this.title ? ' - ' + this.title : '');
						}
					});
					
					$(".help").fancybox({
						
						
						openEffect  : 'fade',
						closeEffect : 'elastic',
						

						prevEffect : 'fade',
						nextEffect : 'fade',

						closeBtn  : true,

						helpers : {
							title : {
								type : 'inside'
							},
							buttons	: {}
						},

						//afterLoad : function() {
						//	this.title = 'Image ' + (this.index + 1) + ' of ' + this.group.length + (this.title ? ' - ' + this.title : '');
						//}
					});
					
					$('.fancybox-thumbs').fancybox({
				prevEffect : 'none',
				nextEffect : 'none',

				closeBtn  : false,
				arrows    : false,
				nextClick : true,

				helpers : {
					thumbs : {
						width  : 50,
						height : 50
					}
				}
			});
			});
		</script>

	
	<!-- Style for D3 Adj graph-->	
	<style>



			.background 
			{
			  fill: #eee;
			}

			line {
			  stroke: #fff;
			}

			text.active {
			  fill: red;
			}
			
			html { height: 100%; margin-bottom: 1px; }
			
			

	</style>


</head>
<body>

		
	

	<!-- Results go here -->
	<div id='wrapper' class='container_12 clearfix'>

	
		<!-- Text Logo -->
		<a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html'><img id='logo' width='250' height='86' align='left' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/logo.jpg' ></a>
		<!-- h1 id='logo' class='grid_4'>Maatie</h1 -->
		
		<!-- Navigation Menu -->
		<ul id='navigation' class='grid_8'>
			
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/contact.html'><span class='meta'>Get in touch</span><br />Contact us</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/news.html'><span class='meta'>Citations</span><br />News</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/help.html'><span class='meta'>Formatting</span><br />Help</a></li>
				
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/about.html'><span class='meta'>The method</span><br />About</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html' class='current'><span class='meta'>Analyze data</span><br />Upload</a></li>
			
		</ul>
		
		<div class='hr grid_12'>&nbsp;</div>
		<div class='clear'></div>
	
	
		
		<div class='head'>
		<h2 class='grid_12 caption clearfix' id='heading' style='margin-left:194px;' align='center'>Current process</h2> 
		</div>
		
		<img id='ok' alt=''  align='left' style='margin-left:120px;padding-top:0px;padding-bottom:0px' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/loader2.gif' height='231' width='231' />
		
		<div class='subtext'>
		<p align='center'>A live stream of current process can be seen below.</p>
		</div>
		
		
		<!-- The textbox display -->
		<p align='center'><textarea id="output" style="resize: none;font-weight:normal;font-family:'Lucida Grande', 'Lucida Sans Unicode', Tahoma, Arial, san-serif; font-size:11px; color:#999999 !important; line-height:16px; text-transform:none; text-shadow:none;" id="output" readonly='true'  rows="10" cols="55" >
		
		
		</textarea></p>
		

		
	
		<!-- The table display -->
	
	   <div style="padding-left:450px;">
		<div id='viz' style="height: 200px; width:500px; overflow: auto; display:none; border-style:solid; border-width:1px; padding-left:0px;"></div>
		</div>
		
		
		<!-- Table display script -->
		<script type="text/javascript">
		
				var table = setInterval(function() 
				{	
				 $.ajax
						 ({	   
							url:'output.csv',
							type:'HEAD',
							success:
							function()
							{
							
									var imgDest = document.getElementById('ok');
									$("#ok").fadeOut('slow');
									imgDest.setAttribute('src', 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/completeA.png');
									
									
									$("#output").fadeOut("slow");													
									$("#head").fadeOut("slow");							
									$("#subtext").fadeOut("slow");					 
									 d3.text("output.csv", function(datasetText) {

									var parsedCSV = d3.csv.parseRows(datasetText);
									
									var sampleHTML = d3.select("#viz")
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
										clearInterval(table);
											$("#viz").fadeIn("slow");
											$("#ok").fadeIn('slow');
											$(".head h2").html("Table of results");
											$(".subtext p").html("This table shows..");
											
											$("#head").fadeIn("slow");
											$("#subtext").fadeIn("slow");
											
										});		

							}
							
							})
	
				},2000);
		</script>
	

		<br />
		<br />
		<br />
		<br />
		
		<div class='hr grid_12'>&nbsp;</div>

		
		<br />
		

	<div id='viz2'  style="display:none;position: relative;font-family: "Helvetica Neue", Helvetica, sans-serif;margin: 1em auto 4em auto;width: 960px;">
	<aside style="margin-top:80px;font-size: small;left: 780px;position: absolute;width: 180px;">

	<p>Order: <select id="order">
	  <option value="name">by Name</option>
	  <option value="count">by Frequency</option>
	  <!--option value="group">by Cluster</option-->
	   <option value="nonlin">by Linearity</option>
	</select>

	<p>The graph to the left is called an Adjacency Matrix. Each cell represents the relationship between two of your variables. The colouring of a cell indicates a linear (blue) or non-linear (red) relationship that Maatie has detected. <br /> <br />The intensity of a cell reflects the strength of the relationship, where a stronger intensity indicates a stronger relationship and vice versa.



	<p>Use the drop-down menu to reorder the matrix and explore the data.</p>
	
	<br />
	<br />


	<!-- The gallery of images for help -->

		<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/a.png" data-fancybox-group="gallery" title="Image 1 of 4 - Adjacency Matrix"><b>Click here for more help with understanding this graph.</b></a>

		<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/b.png" data-fancybox-group="gallery" title="Image 2 of 4 - Diagonals"></a>

		<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/c.png" data-fancybox-group="gallery" title="Image 3 of 4 - Colour"></a>
		
		<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/d.png" data-fancybox-group="gallery" title="Image 4 of 4- Opacity"></a>

		

	</aside>

		
		<script type="text/javascript">
			var refreshImage = setInterval(function() 
			{
				 $.ajax
				 ({
			   
				 url:'adj3.json',
				type:'HEAD',
				error:
							  function()
							  {
									 
									
								
									
								
								}, 
				success:
					function()
					{
					
			
						
								var margin = {top: 120, right: 0, bottom: 10, left: 300},
								width = 720,
								height = 720;

							var x = d3.scale.ordinal().rangeBands([0, width]),
								z = d3.scale.linear().domain([0, 1]).clamp(true),
							   // c = d3.scale.category10().domain(d3.range(10));
							   //words- c = d3.scale.linear().domain(d3.range(2));
								c = d3.scale.linear()
								.domain([0, 1])
								.range(['blue' , 'red' ]);

							var svg = d3.select('#viz2').append('svg')
								.attr('width', width + margin.left + margin.right)
								.attr('height', height + margin.top + margin.bottom)
								.style('margin-left', -margin.left + 'px')
							  .append('g')
								.attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

							d3.json('adj3.json', function(miserables) {
							  var matrix = [],
								  nodes = miserables.nodes,
								  n = nodes.length;

							  // Compute index per node.
							  nodes.forEach(function(node, i) {
								node.index = i;
								node.count = 0;
								matrix[i] = d3.range(n).map(function(j) { return {x: j, y: i, z: 0, nonlin:0}; });
							  });

							  // Convert links to matrix; count character occurrences.
							  miserables.links.forEach(function(link) {
								matrix[link.source][link.target].z += link.value;
								matrix[link.target][link.source].z += link.value;
								//matrix[link.source][link.source].z += link.value;
							   // matrix[link.target][link.target].z += link.value;
								nodes[link.source].count += link.value;
								nodes[link.target].count += link.value;
								
								
								matrix[link.source][link.target].nonlin += link.nonlin;
								matrix[link.target][link.source].nonlin += link.nonlin;
							 
								
								nodes[link.source].countnonlin += link.nonlin*link.value;
								nodes[link.target].countnonlin += link.nonlin*link.value;
								
								
								
							  });

							  // Precompute the orders.
							  var orders = {
								name: d3.range(n).sort(function(a, b) { return d3.ascending(nodes[a].name, nodes[b].name); }),
								count: d3.range(n).sort(function(a, b) { return nodes[b].count - nodes[a].count; }),
								group: d3.range(n).sort(function(a, b) { return nodes[b].group - nodes[a].group; }),
								nonlin: d3.range(n).sort(function(a, b) { return nodes[b].countnonlin - nodes[a].countnonlin; })
							  };

							  // The default sort order.
							  x.domain(orders.name);

							  svg.append('rect')
								  .attr('class', 'background')
								  .attr('width', width)
								  .attr('height', height);

							  var row = svg.selectAll('.row')
								  .data(matrix)
								.enter().append('g')
								  .attr('class', 'row')
								  .attr('transform', function(d, i) { return 'translate(0,' + x(i) + ')'; })
								  .each(row);

							  row.append('line')
								  .attr('x2', width);

							  row.append('text')
								  .attr('x', -6)
								  .attr('y', x.rangeBand() / 2)
								  .attr('dy', '.32em')
								  .attr('text-anchor', 'end')
								  .text(function(d, i) { return nodes[i].name; });

							  var column = svg.selectAll('.column')
								  .data(matrix)
								.enter().append('g')
								  .attr('class', 'column')
								  
								  .attr('transform', function(d, i) { return 'translate(' + x(i) + ')rotate(-90)'; });

							  column.append('line')
								  .attr('x1', -width);

							  column.append('text')
								  .attr('x', 6)
								  .attr('y', x.rangeBand() / 2)
								  .attr('dy', '.32em')
								  .attr('text-anchor', 'start')
								  .text(function(d, i) { return nodes[i].name; });

							  function row(row) {
								var cell = d3.select(this).selectAll('.cell')
									.data(row.filter(function(d) { return d.z; }))
								  .enter().append('rect')
									.attr('class', 'cell')
									.attr('x', function(d) { return x(d.x); })
									.attr('width', x.rangeBand())
									.attr('height', x.rangeBand())
									
								   // the original - .style('fill-opacity', function(d) { return z(d.z); })    
									.style('fill-opacity', function(d) { return d.x == d.y ? 1: z(d.z);  })    //If on a diagonal, 0 opacity
								
									.style('fill', function(d) { return d.x == d.y  ? 'black' : c(d.nonlin); })    
									// the original - .style('fill', function(d) { return nodes[d.x].group == nodes[d.y].group ? c(nodes[d.x].group) : null; })   
									
									//.style('fill', function(d) { return 1==1 ? c(nodes[d.x].group) : null; })    		
									
									.on('mouseover', mouseover)
									.on('mouseout', mouseout);
							  }
							  


							  function mouseover(p) {
								d3.selectAll('.row text').classed('active', function(d, i) { return i == p.y; });
								d3.selectAll('.column text').classed('active', function(d, i) { return i == p.x; });
							  }

							  function mouseout() {
								d3.selectAll('text').classed('active', false);
							  }

							  d3.select('#order').on('change', function() {
								clearTimeout(timeout);
								order(this.value);
							  });

							  function order(value) {
								x.domain(orders[value]);

								var t = svg.transition().duration(2500);

								t.selectAll('.row')
									.delay(function(d, i) { return x(i) * 4; })
									.attr('transform', function(d, i) { return 'translate(0,' + x(i) + ')'; })
								  .selectAll('.cell')
									.delay(function(d) { return x(d.x) * 4; })
									.attr('x', function(d) { return x(d.x); });

								t.selectAll('.column')
									.delay(function(d, i) { return x(i) * 4; })
									.attr('transform', function(d, i) { return 'translate(' + x(i) + ')rotate(-90)'; });
							  }

							  var timeout = setTimeout(function() {
								order('group');
								d3.select('#order').property('selectedIndex', 2).node().focus();
							  }, 5000);
							});
							
							$("#viz2").fadeIn(3000);
							$("#proceed").fadeIn(4000);
							clearInterval(refreshImage);	

							
												
		

					}
				}) 

	}, 5000);
	
	</script>
	
	</div>
	
		<br />
		<br />
		<br />
		<br />
		<br />
			
		<div id='proceed' style="display:none;">
		<!-- Caption Line -->
		<h2   class='grid_12 caption clearfix' align="center">Select one of the options below to proceed.</h2>
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		
		
		<div class='hr grid_12 clearfix quicknavhr'>&nbsp;</div>
		<div id='quicknav' class='grid_12'>
			<a class='quicknavgrid_3 quicknav alpha' href='""" + pathvisu + """'>
					<h4 class='title '>Visualize results</h4>
					<p>This link/bottom only becomes active after file has been processed above. View graphs, trees and different interpretations of data [link to visualize page]. </p>
					<p style='text-align:center;'><img alt='' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/visu.png' /></p>
				
			</a>
			<a class='quicknavgrid_3 quicknav' href='output.csv'>   <!-- Downloads the output.csv stored in the random folder -->
					<h4 class='title '>Download results</h4>
					<p>This link/bottom bar only becomes active after file has been processed above. Download your results in pdf, spreadsheet or have it emailed to yourself [link to download page]. </p>
					<p style='text-align:center;'><img alt='' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/dl.png' /></p>
				
			</a>
			<a class='quicknavgrid_3 quicknav' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html'>
					<h4 class='title '>Another analysis</h4>
					<p>If not downloaded previous results, ask for confirmation and warn. Else dump previous results and refresh main page.</p>
					<br />
					<br />
					<p style='text-align:center;'><img alt='' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/again.png' /></p>
				
			</a>
			<a class='quicknavgrid_3 quicknav' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/help.html'>
					<h4 class='title '>Help</h4>
					<p>Need help understanding the results? [Link to popout page with image] </p>
					<br />
					<br />
					<p style='text-align:center;'><img alt='' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/anahelp.png' /></p>
			</a>
		</div>
		
	
		<div class='hr grid_12 clearfix'>&nbsp;</div>
		<!-- Footer -->
		<p class='grid_12 footer clearfix'>
			<span class='float'><b>&copy; Website design by</b> <a href='http://www.rmoola.com'>Riaz Moola</a>, <b>Images by</b> <a href="http://alexanderblv.tumblr.com/">Alexander Bielovich</a>.</span>
			
		</p>
		
			</div>
		
	</div><!--end wrapper-->
</body>
</html>
""")


#======== The second loading page ============

open('files/' + folderID + '/' + folderID + '_visualize.html', 'wb').write("""
<head>
	<title>Maatie | Visualizations</title>
	<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
	
	<!-- Stylesheets -->
		<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/reset.css' />
		<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/styles.css' />
		
		
		
	<!-- Tabs stuff -->
	<script type='text/javascript' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery-1.7.2.min.js'></script>
	<script type='text/javascript' src='http://jquery-ui.googlecode.com/svn/trunk/ui/jquery.ui.core.js'></script>
	<script type='text/javascript' src='http://jquery-ui.googlecode.com/svn/trunk/ui/jquery.ui.widget.js'></script>
	<script type='text/javascript' src='http://jquery-ui.googlecode.com/svn/trunk/ui/jquery.ui.tabs.js'></script>	
	<link type='text/css' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/tabs.css' rel='stylesheet' />	
	<link type='text/css' href='http://jquery-ui.googlecode.com/svn/trunk/demos/demos.css' />
	
	
	<script type="text/javascript" src="http://mbostock.github.com/d3/d3.js"></script>
	
	<script type='text/javascript'>
	$(function() {
		$('#tabs').tabs().addClass('ui-tabs-vertical ui-helper-clearfix');
		$('#tabs li').removeClass('ui-corner-top').addClass('ui-corner-left');
	});
	</script>
	
	
		
	
	
	<!-- Fancybox stuff-->
	<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox.css' type='text/css' media='screen' />
	 <!--script type='text/javascript' src='http://jquery-ui.googlecode.com/svn/trunk/jquery-1.4.2.js'></script-->
	 <script type='text/javascript' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox.pack.js'></script>
	 
	 <!-- Add Button helper (this is optional) -->
	<link rel="stylesheet" type="text/css" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox-buttons.css" />
	<script type="text/javascript" src="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox-buttons.js"></script>
	
		<link rel="stylesheet" type="text/css" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox-thumbs.css" />
	<script type="text/javascript" src="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery.fancybox-thumbs.js"></script>
		

	
		<script type='text/javascript'>
			$(document).ready(function() 
			{	
				$(".results").fancybox({
						
						
							openEffect  : 'fade',
						closeEffect : 'elastic',
					

						prevEffect : 'fade',
						nextEffect : 'fade',

						closeBtn  : true,

						helpers : {
							title : {
								type : 'inside'
							},
							buttons	: {}
						},

					});
					
					$(".help").fancybox({
						
						
						openEffect  : 'fade',
						closeEffect : 'elastic',
						

						prevEffect : 'fade',
						nextEffect : 'fade',

						closeBtn  : true,

						helpers : {
							title : {
								type : 'inside'
							},
							buttons	: {}
						},

						//afterLoad : function() {
						//	this.title = 'Image ' + (this.index + 1) + ' of ' + this.group.length + (this.title ? ' - ' + this.title : '');
						//}
					});
					
					$('.fancybox-thumbs').fancybox({
				prevEffect : 'none',
				nextEffect : 'none',

				closeBtn  : false,
				arrows    : false,
				nextClick : true,

				helpers : {
					thumbs : {
						width  : 50,
						height : 50
					}
				}
			});
			});
		</script>

	
		<!---style type='text/css'>
				<!--- this makes it horozontal! >
			/* Vertical Tabs
			----------------------------------*/
			.ui-tabs-vertical { width: 55em;}
			.ui-tabs-vertical .ui-tabs-nav { padding: .2em .1em .2em .2em; float: left; width: 12em; }
			.ui-tabs-vertical .ui-tabs-nav li { clear: left; width: 100%; border-bottom-width: 1px !important; border-right-width: 0 !important; margin: 0 -1px .2em 0; }
			.ui-tabs-vertical .ui-tabs-nav li a { display:block; }
			.ui-tabs-vertical .ui-tabs-nav li.ui-tabs-selected { padding-bottom: 0; padding-right: .1em; border-right-width: 1px; border-right-width: 1px; }
			.ui-tabs-vertical .ui-tabs-panel { padding: 1em; float: right; width: 40em;}
		</style-->
		
		<style>



			.background {
			  fill: #eee;
			}

			line {
			  stroke: #fff;
			}

			text.active {
			  fill: red;
			}
			
			a:link { color: #1874CD; }
			a:hover { color: #1874CD; text-decoration:underline;  }
			a:active { color: #1874CD; }
			
			a.help { color: #1874CD; }
			a.help:hover { color: #1874CD; text-decoration:underline; }
			a:help:active  { color: #1874CD; }
			
			#options {
				width:800px;
				margin:0px auto; /* Right and left margin widths set to "auto" */
				 /* Counteract to IE5/Win Hack */
				padding:15px;
				border:1px dashed #333;
				background-color:#eee;
				}
		
			
			

		</style>
		
		<style type="text/css">

		.link { stroke: #ccc; }

		.nodetext { pointer-events: none; font: 10px sans-serif; }

		</style>

		
		<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/d3.css' />

	
	
	
</head>

<body>

	<div id='wrapper' class='container_12 clearfix'>

		<!-- Text Logo -->
	<a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html'><img align='left' width='250' height='86' src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/logo.jpg' ></a>
		
		<!-- Navigation Menu -->
		<ul id='navigation' class='grid_8'>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/contact.html'><span class='meta'>Get in touch</span><br />Contact us</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/news.html'><span class='meta'>Citations</span><br />News</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/help.html'><span class='meta'>Formatting</span><br />Help</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/about.html'><span class='meta'>The method</span><br />About</a></li>
			<li><a href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/index.html'><span class='meta'>Analyze data</span><br />Upload</a></li>
		</ul>
		
		<div class='hr grid_12 clearfix'>&nbsp;</div>
			
		<!-- Caption Line -->
		<h2 class='grid_12 caption'><span>Visualize</span> your analyzed data.</h2>
		
		<div class='hr grid_12 clearfix'>&nbsp;</div>

		<!-- Column 1 / Content -->
		
		<div class='grid_12'>
			<h4 class='page_title'>Select a tab below to view and download different graph types.</h4>
			<div class='hr dotted clearfix'>&nbsp;</div>
			
			<div class='demo' >		
						
			<div id='tabs'>
				<ul>
					<li><a href='#tabs-1'>Force Directed Graph</a></li>
					<li><a href='#tabs-2'>A-Graph</a></li>
					<li><a href='#tabs-3'>Adjacency Matrix</a></li>
					<li><a href='#tabs-4'>A-Gram</a></li>
					<li><a href='#tabs-5'>Table of correlations</a></li>
					<li><a href='#tabs-6'>More coming</a></li>
				</ul>
				
				<div id='tabs-1'>
					<h2 class='caption clearfix' style="padding-left:5px;">Force Directed Graph</h2>
					<p align='left'><b>Use your mousewheel to zoom in and out of the graph. Click and drag to pan.</b>
					<br />
					<br />
							<div id='FDG' style="text-align: center;"> 
							
									
							
										<script type="text/javascript">
										
										//var threshold = (document.getElementsByName('threshold')[0].value);
										
										function updateData() 
										{
										vis.selectAll("line.link")
												.style("stroke-opacity", function(d) { return d.value>document.getElementsByName('linkthresh')[0].value ? d.value : 0; })
												.style("stroke-width", function(d) { return Math.sqrt(d.value)*document.getElementsByName('linewidth')[0].value; });
					
										force.gravity(document.getElementsByName('gravity')[0].value)
											.linkDistance(function(d) {return (document.getElementsByName('distance')[0].value/(d.value+0.05));})
											.charge(-1*document.getElementsByName('charge')[0].value)
											.linkStrength(function(d) {  return d.value>document.getElementsByName('linkthresh')[0].value ? (Math.pow(d.value, document.getElementsByName('cstrength')[0].value))*document.getElementsByName('strengthdiv')[0].value : 0;})
											 .start();
										}
										
										function animate()
										{
											
											document.getElementsByName('linkthresh')[0].value=1;
											document.getElementsByName('charge')[0].value=50;
											document.getElementsByName('gravity')[0].value=0.1;
											updateData();
											force.linkStrength(1)
												.linkDistance(0)
												.start();
											document.getElementsByName('gravity')[0].value=0.1;
											document.getElementsByName('charge')[0].value=200;
											setTimeout(function() {updateData();},2000);
											
											setTimeout(function() {document.getElementsByName('charge')[0].value=200;updateData();},3000);
											setTimeout(function() {
												updateData();
												var t = 0;
												var t1 = 0;
												var last = 0;
												d3.timer(function(elapsed) {
												  t1 = (t1 + (elapsed - last) / 10000);
												  t = t1 % 1.2;
												  last = elapsed;
												  vis.selectAll("line.link")
													.style("stroke-opacity", function(d) { return d.value>(1.1-t) ? d.value : 0; });
												force.linkStrength(function(d) {  return d.value>(1.07-t) ? ( (t>1.1 ? 1 : Math.sqrt(d.value))*document.getElementsByName('strengthdiv')[0].value) : 0; })
													.linkDistance(function(d) {return ((t>1.1 ? 0: 25)/(d.value+0.05));})
													.start();		
												return t1>1.09;
												
												reset();
												});
											},4000);
											
											
										}

										
										var c = d3.scale.linear()
										.domain([0, 1])
										.range(["blue" , "red" ]);   //Scale all links between blue and red using this function that takes number between 0-1 and maps to colour inbetween b/r

										var w = 860,
											h = 500

										var vis = d3.select("#FDG").append("svg:svg")
											.attr("width", w)		 
											.attr("height", h)
											.attr("pointer-events", "all")     //Setup pointer events
											.append('svg:g')  
											.call(d3.behavior.zoom().on("zoom", redraw))
											.append('svg:g');
											
											//Append a rectangle behind the g to recieve the mouse scroll events (otherwise only works over nodes/links
											
											vis.append('svg:rect')
											.attr('width', w)
											.attr('height', h)
											.attr('fill', 'white');

											//function that calls on zoom
										  function redraw() 
										  {
											  console.log("here", d3.event.translate, d3.event.scale);
											  vis.attr("transform",
												  "translate(" + d3.event.translate + ")"
												  + " scale(" + d3.event.scale + ")");
											}
											
							
											
										
										d3.json("adj3.json", function(json) {
											var force = self.force = d3.layout.force()
												.nodes(json.nodes)
												.links(json.links)
												.gravity(document.getElementsByName('gravity')[0].value)												
												.charge(-1*(document.getElementsByName('charge')[0].value))
												.linkDistance(function(d) {return (document.getElementsByName('distance')[0].value/(d.value+0.05));})
												.linkStrength(function(d) {  return d.value>document.getElementsByName('linkthresh')[0].value ? (Math.pow(d.value, document.getElementsByName('cstrength')[0].value))*document.getElementsByName('strengthdiv')[0].value : 0;})
													 
												.size([w, h])
												.start();

											var link = vis.selectAll("line.link")
												.data(json.links)
												.enter().append("svg:line")
												.attr("class", "link")
												.style("stroke", function(d) { return c(d.nonlin); })
												.style("stroke-width", function(d) { return Math.sqrt(d.value)*document.getElementsByName('linewidth')[0].value; })
												.style("stroke-opacity", function(d) { return d.value; })
												
												.attr("x1", function(d) { return d.source.x; })
												.attr("y1", function(d) { return d.source.y; })
												.attr("x2", function(d) { return d.target.x; })
												.attr("y2", function(d) { return d.target.y; });

											var node = vis.selectAll("g.node")
												.data(json.nodes)
												.enter().append("svg:g")
												.attr("class", "node")
												.call(force.drag);
												
												
												 node.append("svg:image")
												.attr("class", "circle")
												.attr("xlink:href", "http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/node.png")
												.attr("x", "-8px")
												.attr("y", "-8px")
												.attr("width", "16px")
												.attr("height", "16px");
												
												/* var node = vis.selectAll("circle.node")
												.data(json.nodes)
												.enter().append("circle")
												.attr("class", "node")
												.attr("r", 5)
												.style("fill", function(d) { return color(d.group); })  
												.call(force.drag); */

										   

												 node.append("svg:text")
												.attr("class", "nodetext")
												
												.attr("dx", 8)
												.attr("dy", ".35em")
												.text(function(d) { return d.name });
												
											

											force.on("tick", function() {
											  link.attr("x1", function(d) { return d.source.x; })
												  .attr("y1", function(d) { return d.source.y; })
												  .attr("x2", function(d) { return d.target.x; })
												  .attr("y2", function(d) { return d.target.y; });

											  node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
											});
										});
										
							

										</script>
										
										
										</div>
										
										<div id='options' style="text-align: center;">
										
										<br />
										<br />
										
											<h2 class='caption clearfix' style="text-align:center;">Settings</h2>
												
												Threshold to filter links:<input type="range" name ="linkthresh" min="0" max="1" value="0.00" step="0.01" onchange="updateData(); showValueP(this.value)" />
												<span id="rangeThresh">0</span>
												<script type="text/javascript">
												function showValueP(newValue)
												{
													document.getElementById("rangeThresh").innerHTML=parseFloat(Math.round(newValue * 100) / 100).toFixed(2);
												}
												</script>
												&nbsp; <a href='AGram.png' title='What does this do?'>[?]</a> &nbsp; &nbsp; &nbsp; &nbsp;
												Cluster strength: <input type="range" name ="cstrength" min="0" max="2" value="0.50" step="0.01" onchange="updateData(); showValueC(this.value)" />
												<span id="rangeCS">0.5</span>
												<script type="text/javascript">
												function showValueC(newValue)
												{
													document.getElementById("rangeCS").innerHTML=parseFloat(Math.round(newValue * 100) / 100).toFixed(2);
												}
												</script>
												&nbsp; <a href='AGram.png' title='What does this do?'>[?]</a> 
												<br />
												<br />
											
												Link Distance: <input type="range" name ="distance" min="5" max="500" value="40" step="1" onchange="updateData(); showValueL(this.value)" />
												<span id="rangeDist">40</span>
												<script type="text/javascript">
												function showValueL(newValue)
												{
													document.getElementById("rangeDist").innerHTML=parseFloat(Math.round(newValue * 100) / 100).toFixed(2);
												}
												</script>
												
												&nbsp;  <a href='AGram.png' title='What does this do?'>[?]</a>  &nbsp; &nbsp; &nbsp; &nbsp;
												 Gravity: <input type="range"  name ="gravity" min="0" max="0.5" value="0.05" step="0.01" onchange="updateData(); showValueG(this.value)" />
												<span id="rangeGrav">0.05</span>
												<script type="text/javascript">
												function showValueG(newValue)
												{
													document.getElementById("rangeGrav").innerHTML=parseFloat(Math.round(newValue * 100) / 100).toFixed(2);
												}
												</script>
												&nbsp; <a href='AGram.png' title='What does this do?'>[?]</a> 
												<br />
												<br />
												
												Rigidity: <input type="range" name ="strengthdiv" min="0" max="1" value="0.3" step="0.01" onchange="updateData(); showValueD(this.value)" />
												<span id="rangeDiv" maxlength="2">0.3</span>
												<script type="text/javascript">
												function showValueD(newValue)
												{
												   
													document.getElementById("rangeDiv").innerHTML=parseFloat(Math.round(newValue * 100) / 100).toFixed(2);
												}
												</script>
												&nbsp;  <a href='AGram.png' title='What does this do?'>[?]</a>  &nbsp; &nbsp; &nbsp; &nbsp;
												  Repulsion Force: <input type="range" name ="charge" min="0" max="1000" value="100" step="1" onchange="updateData(); showValueR(this.value)" />
												<span id="rangeForce">100</span>
												<script type="text/javascript">
												function showValueR(newValue)
												{
													document.getElementById("rangeForce").innerHTML=parseFloat(Math.round(newValue * 100) / 100).toFixed(2);
												}
												</script>
												&nbsp; <a href='AGram.png' title='What does this do?'>[?]</a> 
												<br />
												<br />
												
												  Line Width: <input type="range" name ="linewidth" min="0.01" max="10" value="4" step="0.01" onchange="updateData(); showValueW(this.value)" />
												<span id="rangeWidth">4</span>
												<script type="text/javascript">
												function showValueW(newValue)
												{
													document.getElementById("rangeWidth").innerHTML=parseFloat(Math.round(newValue * 100) / 100).toFixed(2);
												}
												</script>
											
												&nbsp;  <a href='AGram.png' title='What does this do?'>[?]</a>  &nbsp; &nbsp; &nbsp; &nbsp;
												
											 <input type="button" value="Reset to defaults"name ="reset"  onclick="reset()" />
												&nbsp; <a href='AGram.png' title='What does this do?'>[?]</a> 
												<script type="text/javascript">
												function reset() 
												{		
														
														document.getElementsByName('linkthresh')[0].value= '0';
														document.getElementsByName('cstrength')[0].value= '0.5';
														document.getElementsByName('distance')[0].value= '40';
														document.getElementsByName('gravity')[0].value= '0.05';
														document.getElementsByName('strengthdiv')[0].value= '0.3';
														document.getElementsByName('charge')[0].value= '100';
														document.getElementsByName('linewidth')[0].value= '4';
														showValueP(0);
														showValueC(0.5);
														showValueL(40);
														showValueG(0.05);
														showValueD(0.3);
														showValueR(100);
														showValueW(4);
														
														updateData();
														
													
												}
												</script>
												
												<br />
												<br />
												 <input type="button" value="Animate"name ="animate"  onclick="animate()" />
										
												<br />
												<br />
												<br />
												<br />
												<a href='lol.html'>Click here to open the graph in a new window for a bigger sized display. </a>
												<br />
												<br />
												<br />
												<br />
													

										 <h2 class='caption clearfix' style="text-align:center;">Download</h2>
										 <a href='adj3.json'>Click here</a> to download the .json file from which this graph is generated. You can upload this .json file later to recreate this graph later by visiting <a href=''>this page.</a></p>
										 
										 <br />
										 <br />
										 
										  <h2 class='caption clearfix' style="text-align:center;">Help</h2>
										
										<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/forcea.jpg" data-fancybox-group="gallery1" title="Image 1 of 4 - Forde Directed Graph"><b>Click here for help with understanding this graph.</b></a>

										<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/forceb.jpg" data-fancybox-group="gallery1" title="Image 2 of 4 - Edges I"></a>

										<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/forcec.jpg" data-fancybox-group="gallery1" title="Image 3 of 4 - Edges II"></a>
										
										<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/forced.jpg" data-fancybox-group="gallery1" title="Image 4 of 4 - Edges III"></a>
										
										
						
										
										
										<br />
										<br />
										
										
												</div>
												
												<br />
												<br />
  
							
						
							
							
							
				
				
					</div>
	
				<div id='tabs-2' height='400'>
					<h2 class='grid_12 caption clearfix'>A-Graph</h2>
					<br />
					<br />
				
					<div style="text-align: center;">
					<a class='results' data-fancybox-group="button" href='Agraph.png' title="Right click and select 'save image as' to download your image.">
					<img src=' """ + pathAgraph + """ ' style='max-width: 930px; max-height: 400px;'/>
					</a>
					</div>
					<br />
					<br />
					<br />
					<div id='options' style="text-align: center;">
							 <h2 class='caption clearfix' style="text-align:center;">Settings</h2>
							
							<p align='center'>An A-Graph of your data is shown above. Click the image and use the 'toggle size' button to zoom in and out or <a href='Agram.png'> click here to open the image in a new window.</a>
							
							<br />
							
							<h2 class='caption clearfix' style="text-align:center;">Download</h2>
							
							 Click the image above and right click 'save as' to download the image. 
						
							<br />
							<br />
							<br />
							 <h2 class='caption clearfix' style="text-align:center;">Help</h2>
							<a href='help.png'>What is an A-Gram and how do I interpret it?</a></p>
					
					</div>
					
					<br />
					<br />
					<br />
					
				</div>
				<div id='tabs-3'>
					<h2 class='grid_12 caption clearfix'>Adjacency Matrix</h2>
					 <div id='viz2' style="padding-left:230px;"> 
				</div>
					 <script>
					 
							var margin = {top: 130, right: 0, bottom: 10, left: 130},
								width = 600;
								height = 600;

							var x = d3.scale.ordinal().rangeBands([0, width]),
								z = d3.scale.linear().domain([0, 1]).clamp(true),
							   // c = d3.scale.category10().domain(d3.range(10));
							   //words- c = d3.scale.linear().domain(d3.range(2));
								c = d3.scale.linear()
								.domain([0, 1])
								.range(['blue' , 'red' ]);

							var svg = d3.select('#viz2').append('svg')
								.attr('width', width + margin.left + margin.right)
								.attr('height', height + margin.top + margin.bottom)
								.style('margin-left', -margin.left + 'px')
							  .append('g')
								.attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

							d3.json('adj3.json', function(miserables) {
							  var matrix = [],
								  nodes = miserables.nodes,
								  n = nodes.length;

							  // Compute index per node.
							  nodes.forEach(function(node, i) {
								node.index = i;
								node.count = 0;
								matrix[i] = d3.range(n).map(function(j) { return {x: j, y: i, z: 0, nonlin:0}; });
							  });

							  // Convert links to matrix; count character occurrences.
							  miserables.links.forEach(function(link) {
								matrix[link.source][link.target].z += link.value;
								matrix[link.target][link.source].z += link.value;
								//matrix[link.source][link.source].z += link.value;
							   // matrix[link.target][link.target].z += link.value;
								nodes[link.source].count += link.value;
								nodes[link.target].count += link.value;
								
								
								matrix[link.source][link.target].nonlin += link.nonlin;
								matrix[link.target][link.source].nonlin += link.nonlin;
							 
								
								nodes[link.source].countnonlin += link.nonlin*link.value;
								nodes[link.target].countnonlin += link.nonlin*link.value;
								
								
								
							  });

							  // Precompute the orders.
							  var orders = {
								name: d3.range(n).sort(function(a, b) { return d3.ascending(nodes[a].name, nodes[b].name); }),
								count: d3.range(n).sort(function(a, b) { return nodes[b].count - nodes[a].count; }),
								group: d3.range(n).sort(function(a, b) { return nodes[b].group - nodes[a].group; }),
								nonlin: d3.range(n).sort(function(a, b) { return nodes[b].countnonlin - nodes[a].countnonlin; })
							  };

							  // The default sort order.
							  x.domain(orders.name);

							  svg.append('rect')
								  .attr('class', 'background')
								  .attr('width', width)
								  .attr('height', height);

							  var row = svg.selectAll('.row')
								  .data(matrix)
								.enter().append('g')
								  .attr('class', 'row')
								  .attr('transform', function(d, i) { return 'translate(0,' + x(i) + ')'; })
								  .each(row);

							  row.append('line')
								  .attr('x2', width);

							  row.append('text')
								  .attr('x', -6)
								  .attr('y', x.rangeBand() / 2)
								  .attr('dy', '.32em')
								  .attr('text-anchor', 'end')
								  .text(function(d, i) { return nodes[i].name; });

							  var column = svg.selectAll('.column')
								  .data(matrix)
								.enter().append('g')
								  .attr('class', 'column')
								  
								  .attr('transform', function(d, i) { return 'translate(' + x(i) + ')rotate(-90)'; });

							  column.append('line')
								  .attr('x1', -width);

							  column.append('text')
								  .attr('x', 6)
								  .attr('y', x.rangeBand() / 2)
								  .attr('dy', '.32em')
								  .attr('text-anchor', 'start')
								  .text(function(d, i) { return nodes[i].name; });

							  function row(row) {
								var cell = d3.select(this).selectAll('.cell')
									.data(row.filter(function(d) { return d.z; }))
								  .enter().append('rect')
									.attr('class', 'cell')
									.attr('x', function(d) { return x(d.x); })
									.attr('width', x.rangeBand())
									.attr('height', x.rangeBand())
									
								   // the original - .style('fill-opacity', function(d) { return z(d.z); })    
									.style('fill-opacity', function(d) { return d.x == d.y ? 1: z(d.z);  })    //If on a diagonal, 0 opacity
								
									.style('fill', function(d) { return d.x == d.y  ? 'black' : c(d.nonlin); })    
									// the original - .style('fill', function(d) { return nodes[d.x].group == nodes[d.y].group ? c(nodes[d.x].group) : null; })   
									
									//.style('fill', function(d) { return 1==1 ? c(nodes[d.x].group) : null; })    		
									
									.on('mouseover', mouseover)
									.on('mouseout', mouseout);
							  }
							  


							  function mouseover(p) {
								d3.selectAll('.row text').classed('active', function(d, i) { return i == p.y; });
								d3.selectAll('.column text').classed('active', function(d, i) { return i == p.x; });
							  }

							  function mouseout() {
								d3.selectAll('text').classed('active', false);
							  }

							  d3.select('#order').on('change', function() {
								clearTimeout(timeout);
								order(this.value);
							  });

							  function order(value) {
								x.domain(orders[value]);

								var t = svg.transition().duration(2500);

								t.selectAll('.row')
									.delay(function(d, i) { return x(i) * 4; })
									.attr('transform', function(d, i) { return 'translate(0,' + x(i) + ')'; })
								  .selectAll('.cell')
									.delay(function(d) { return x(d.x) * 4; })
									.attr('x', function(d) { return x(d.x); });

								t.selectAll('.column')
									.delay(function(d, i) { return x(i) * 4; })
									.attr('transform', function(d, i) { return 'translate(' + x(i) + ')rotate(-90)'; });
							  }

							  var timeout = setTimeout(function() {
								order('group');
								d3.select('#order').property('selectedIndex', 2).node().focus();
							  }, 5000);
							});
							
							</script>
							<br />
							<br />
							<br />
							
							<div id='options' style="text-align: center;">
							
									 <h2 class='caption clearfix' style="text-align:center;">Settings</h2>
									 
									 <p align='center'>An adjacency matrix for your data has been generated above. 
												
									Order: <select id="order">
									  <option value="name">by Name</option>
									  <option value="count">by Frequency</option>
									  <option value="group">by Cluster</option>
									   <option value="nonlin">by Lin</option>
									</select> </p>

						
									<h2 class='caption clearfix' style="text-align:center;">Download</h2>
									
									<a href='adj3.json'>Click here</a> to download the .json file from which this graph is generated. You can upload this .json file later to recreate this graph later by visiting <a href='Agraph.png'>this page.</a></p>
									
									<br />
									<h2 class='caption clearfix' style="text-align:center;">Help</h2>
									
									
										<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/a.png" data-fancybox-group="gallery" title="Image 1 of 4 - Adjacency Matrix"><b>Click here for more help with understanding this graph.</b></a>

										<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/b.png" data-fancybox-group="gallery" title="Image 2 of 4 - Diagonals"></a>

										<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/c.png" data-fancybox-group="gallery" title="Image 3 of 4 - Colour"></a>
										
										<a class="help" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/d.png" data-fancybox-group="gallery" title="Image 4 of 4- Opacity"></a>
										
											<br />
											<br />
	
							</div>
							<br />
							<br />
							<br />
							
				</div>
				
							<div id='tabs-4'>
					<h2 class='grid_12 caption clearfix'>A-Gram</h2>

					<div style="text-align: center;">
						
						<a class='results' data-fancybox-group="button" href='Agram.png' title="Right click and select 'save image as' to download your image.">
							<img src=' """ + path2 + """ ' style='max-width: 930px; max-height: 400px;'/>
						</a>
					
					</div>
					
					<div id='options' style="text-align: center;">
					
						 <h2 class='caption clearfix' style="text-align:center;">Settings</h2>
						
						<p align='center'>An A-Gram of your data is shown above. Click the image and use the 'toggle size' button to zoom in or <a href='Agram.png'> open in a new window where it can be downloaded</a>. <br />
						
						<h2 class='caption clearfix' style="text-align:center;">Download</h2>
						
						Alternatively, you can download a high resolution pdf of this A-Gram <a href='Agram.pdf'>here.</a>
						<br />
						<br />
						<br />
						<h2 class='caption clearfix' style="text-align:center;">Help</h2>
						
						<a href=''>What is an A-Gram and how do I interpret it?</a></p>
					
					</div>
					
					<br />
					<br />
					<br />
					
				</div>
					
					
					<div id='tabs-5'>
							<h2 class='grid_12 caption clearfix'>Table</h2>
							
							<div id='table' style="text-align:center;margin:0 auto;padding-left:60px; overflow:scroll">
							
									<script>
									 d3.text("output.csv", function(datasetText) {

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
										
										doSomething()
											
											
										});		
										
										</script>
					
								</div>
								
								
								<br />
								<br />
								<br />
								<br />
								
								<div id='options' style="text-align: center;">
											 <h2 class='caption clearfix' style="text-align:center;">Settings</h2>
											
											<p align='center'>A table of correlations for your data has been generated above. <a href=''>What is this table  and how do interpret it?</a> 
											<br />
											 <h2 class='caption clearfix' style="text-align:center;">Download</h2>
											
										<a href='adj3.json'>Click here</a> to download the .csv file of outputs which this table is generated. You can upload this .csv file later to recreate this table later by visiting <a href=''>this page.</a></p>
										<br />
											 <br />
										
							   
								</div>
					</div>
					
					<div id='tabs-6'>
							More coming soon!
					</div>
					
					
			</div> <!-- End tabs div -->

			</div> <!-- End demo div -->
			 
			
		</div>
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		<br />
		
		<!-- Column 2 / Sidebar -->
		<div class='grid_12'>
		
			
			<div class='hr dotted clearfix'>&nbsp;</div>
			<dl class='history'> 
		
				<dd><b>Save link</b> - Click here to have an email sent to yourself with this link for future reference. </dd> 
				
				<dd><b>Download all</b> - Click here to download all graphics in zip file. </dd> 
				
				<dd><b>Run another test</b> - Click here to exit and run another test. </dd> 
				
			</dl>
			
		
			<p align='center'><img src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/visubot.png'></p>
			
		</div>

		
		<div class='hr grid_12 clearfix'>&nbsp;</div>
		<!-- Footer -->
		<p class='grid_12 footer clearfix'>
			<span class='float'><b>&copy; Website design by</b> <a href='http://www.rmoola.com'>Riaz Moola</a>, <b>Images by</b> <a href="http://alexanderblv.tumblr.com/">Alexander Bielovich</a>.</span>
			
		</p>
		
	</div><!--end wrapper-->

</body>
</html>
""")



#print """<html>
#<head>
 #<title>Feature information</title>
#</head>
#<body>

#<a href=""" + newPath + """><img alt='' align='left' src='images/test.jpg' /></a>

#</form>
#</body></html>"""

print "Location: " + newPath + "\n\n";
os.system("nohup R --vanilla --slave --args "+folderID+" < datProc.R > /var/www/files/"+folderID+"/consoleOut.txt &")


	



	#open('files/' + folderID + '/' + 'consoleOut.txt', 'w')
	#print "Location: " + newPath + "\n\n";
	#os.system("R --vanilla --slave --args "+folderID+" < datProc.R > /var/www/files/"+folderID+"/consoleOut.txt")



	#print "Location: http://google.com\n\n";
	#print "\Content-Type: text/html"
	#print 'Location: ' + newPath + ' ' 
