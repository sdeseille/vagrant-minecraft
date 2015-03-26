outputdir = "/home/notch/mc-overviewer/render"
texturepath = "/home/notch/mc-overviewer/1.8.jar"
rendermode = "smooth_lighting"
world_name = "House Server"
worlds[world_name] = "/home/notch/minecraft/world"
renders["North"] = {
	'world': world_name,
	'title': 'North',
	'dimension': "overworld",
	'rendermode': rendermode,
	'northdirection': 'upper-left'
}
renders["East"] = {
	'world': world_name,
	'title': 'East',
	'dimension': "overworld",
	'rendermode': rendermode,
	'northdirection': 'upper-right'
}
renders["South"] = {
	'world': world_name,
	'title': 'South',
	'dimension': "overworld",
	'rendermode': rendermode,
	'northdirection': 'lower-right'
}
renders["West"] = {
	'world': world_name,
	'title': 'West',
	'dimension': "overworld",
	'rendermode': rendermode,
	'northdirection': 'lower-left'
}
