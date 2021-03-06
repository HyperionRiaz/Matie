function animate()

										{

											
											document.getElementsByName('linkthresh')[0].value=1;
											document.getElementsByName('charge')[0].value=50;
											document.getElementsByName('gravity')[0].value=0.2;
											updateData();
											force.linkStrength(1)
												.linkDistance(0)
												.start();
											document.getElementsByName('gravity')[0].value=0.2;
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

													.linkDistance(function(d) {return ((t>1.1 ? 0: 10)/(d.value+0.05));})

													.start();		

												return t1>3.49;

												});

											},4000);

  											

 										    

										}

										

										function updateData() 

										{

										

										

										

										vis.selectAll("line.link")

												.style("stroke-opacity", function(d) { return d.value>document.getElementsByName('linkthresh')[0].value ? d.value : 0; });

					

										force.gravity(document.getElementsByName('gravity')[0].value)

											.linkDistance(function(d) {return (document.getElementsByName('distance')[0].value/(d.value+0.05));})

											.charge(-1*document.getElementsByName('charge')[0].value)

											.linkStrength(function(d) {  return d.value>document.getElementsByName('linkthresh')[0].value ? (Math.sqrt(d.value))*document.getElementsByName('strengthdiv')[0].value : 0;})

											 .start();

										}							

										

										var c = d3.scale.linear()

										.domain([0, 1])

										.range(["blue" , "red" ]);   //Scale all links between blue and red using this function that takes number between 0-1 and maps to colour inbetween b/r



										var w = 300,

											h = 300



										var vis = d3.select("#FDG").append("svg:svg")

											.attr("width", w)		 

											.attr("height", h)

											//.attr("pointer-events", "all")     //Setup pointer events

											.append('svg:g')  

											//.call(d3.behavior.zoom().on("zoom", redraw))

											.append('svg:g');

											

											//Append a rectangle behind the g to recieve the mouse scroll events (otherwise only works over nodes/links

											

											//vis.append('svg:rect')

											//.attr('width', w)

											//.attr('height', h)

											//.attr('fill', 'white');



											//function that calls on zoom

										  function redraw() 

										  {

											  console.log("here", d3.event.translate, d3.event.scale);

											  vis.attr("transform",

												  "translate(" + d3.event.translate + ")"

												  + " scale(" + d3.event.scale + ")");

											}

											

									function draw()
									{

											

										//Other: adj3.json or huge.json

										d3.json("http://ec2-175-41-179-225.ap-southeast-1.compute.amazonaws.com/adj3.json", function(json) {

											var force = self.force = d3.layout.force()

												.nodes(json.nodes)

												.links(json.links)

												.gravity(document.getElementsByName('gravity')[0].value)												

												.charge(-1*(document.getElementsByName('charge')[0].value))

												.linkDistance(function(d) {return (document.getElementsByName('distance')[0].value/(d.value+0.05));})

												.linkStrength(function(d) {  return (Math.sqrt(d.value))*document.getElementsByName('strengthdiv')[0].value;})

													 

												.size([w, h])

												.start();



											var link = vis.selectAll("line.link")

												.data(json.links)

												.enter().append("svg:line")

												.attr("class", "link")

												.style("stroke", function(d) { return c(d.nonlin); })

												.style("stroke-width", function(d) { return Math.sqrt(d.value)*4; })

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

												.attr("xlink:href", "http://ec2-175-41-179-225.ap-southeast-1.compute.amazonaws.com/images/node.png")

												.attr("x", "-8px")

												.attr("y", "-8px")

												.attr("width", "16px")

												.attr("height", "16px");

												



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

										animate();	

										});
										
										}