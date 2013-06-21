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
   
else:
   message = 'No file was uploaded'
   s = 'derp'
   
   
   


newPath = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/' + folderID + '_Page.html'
path2 = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/Agram.png'
pathAgraph = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/Agraph.png'
pathvisu = 'http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/files/' + folderID + '/' + folderID + '_visualize.html'

open('files/' + folderID + '/' + folderID + '_Page.html', 'wb').write("""<html>
<head>
	<title>MAATIE| A new statistical tool</title>
	<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
	
	<!-- Stylesheets -->
	<link rel="stylesheet" href="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/reset.css" />
	<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/styles.css' />

	
	<!-- Scripts -->
	<!-- JQUERY LOADING SCREEN SCRIPT -->
	<script type="text/javascript" src="http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/js/jquery-1.7.2.min.js"></script>
	<script type="text/javascript">
		$(window).load(function(){
		$("#loading").hide();
		})
	</script>

	
	<script src='http://d3js.org/d3.v2.min.js?2.8.1'></script>
	
	<link rel='stylesheet' href='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/css/d3.css' />


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
			   
				 url:'""" +pathAgraph+"""',
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
						
						
						
						$("#proceed").fadeIn(6000);
						
					
						
						clearInterval(refreshImage);		
												
		

					}
				}) 

	}, 2000);
	
	</script>

		


</head>
<body>

	<!-- THE LOADING PORTION OF CONTENT -->
	<div id="loading">
		Loading content, please wait..
	<img src='http://ec2-122-248-225-29.ap-southeast-1.compute.amazonaws.com/images/loading.gif' alt='loading..' />
		</div>
		
	

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
		
		<div id='proceed' style="display:none;">
		<!-- Caption Line -->
		<h2   class='grid_12 caption clearfix' align="center">Select one of the options below to proceed.</h2>

		<br />
		<br />
		<br />
		<br />
		<br />
		
		<p>Order: <select id='order'>
  <option value='name'>by Name</option>
  <option value='count'>by Frequency</option>
  <option value='group'>by Cluster</option>
   <option value='nonlin'>by Lin</option>
</select></p>
<div id='vid'></div>

		
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
					
			
						
													var margin = {top: 80, right: 0, bottom: 10, left: 80},
								width = 720,
								height = 720;

							var x = d3.scale.ordinal().rangeBands([0, width]),
								z = d3.scale.linear().domain([0, 4]).clamp(true),
							   // c = d3.scale.category10().domain(d3.range(10));
							   //words- c = d3.scale.linear().domain(d3.range(2));
								c = d3.scale.linear()
								.domain([0, 1])
								.range(['blue' , 'red' ]);

							var svg = d3.select('body').append('svg')
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
							
							
							clearInterval(refreshImage);	

							
												
		

					}
				}) 

	}, 5000);
	
	</script>
	
	
	
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
		

	
		<script type='text/javascript'>
			$(document).ready(function() 
			{	
				$(".results").fancybox({
						
						
							openEffect  : 'none',
						closeEffect : 'none',

						prevEffect : 'none',
						nextEffect : 'none',

						closeBtn  : false,

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
			
			<div class='demo'>		
						
						<div id='tabs'>
				<ul>
					<li><a href='#tabs-1'>A-Gram</a></li>
					<li><a href='#tabs-2'>A-Graph</a></li>
					<li><a href='#tabs-3'>More to come</a></li>
				</ul>
				<div id='tabs-1'>
					<h2>A-Gram</h2>

					<div style="text-align: center;">
						<a class='results' data-fancybox-group="button" href='Agram.png' title="Right click and select 'save image as' to download your image.">
							<img src=' """ + path2 + """ ' style='max-width: 930px; max-height: 400px;'/>
						</a>
					
					</div>
					<p align='center'>Click the image above to view it in full size. You can then download this single visualization. <br />
					<br />Click here if you need help interpreting the A-Gram graph. <br /><br />
					Click here to create another A-Gram of your data using your own settings.</p>
				</div>
				<div id='tabs-2'>
					<h2>A-Graph</h2>
				
					<div style="text-align: center;">
					<a class='results' data-fancybox-group="button" href='Agraph.png' title="Right click and select 'save image as' to download your image.">
					<img src=' """ + pathAgraph + """ ' style='max-width: 930px; max-height: 400px;'/>
					</a>
					</div>
					<p align='center'>Click the image above to view it in full size. You can then download this single visualization. <br />
					<br />Click here if you need help interpreting the A-Gram graph. <br /><br />
					Click here to create another A-Gram of your data using your own settings.</p>
				</div>
				<div id='tabs-3'>
					<h2>More to come</h2>
					<p>New formats added every week. Check back later. </p>
				</div>
			</div>

			</div>
			 
			
		</div>
		<br>
		<br>
		
		<!-- Column 2 / Sidebar -->
		<div class='grid_12'>
		
			
			<div class='hr dotted clearfix'>&nbsp;</div>
			<dl class='history'> 
		
				<dd><b>Options</b> - Click here to create a graph of your data with different options. </dd> 
				
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
