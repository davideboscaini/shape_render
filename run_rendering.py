import os
import bpy
import math

# (full) path to the directory 
path_folder      = <string containing the path to the obj files>
flag_texture     = <True,False>
name_texture_img = <string containing the name of the texture image>
flag_shadow      = <True,False>

# [scene]
# remove the default camera and lamp
bpy.data.objects['Camera'].select = True
bpy.ops.object.delete()
bpy.data.objects['Lamp'].select = True
bpy.ops.object.delete()
# to create a new empty scene, uncomment the following line
# bpy.ops.scene.new(type='EMPTY')

# [camera]
# create a camera in the specified position
bpy.ops.object.camera_add(location=(2.5,0.0,0.3),rotation=(math.pi/2.0,0.0,math.pi/2.0))
camera_obj = bpy.context.object
# set the camera name
camera_obj.name = 'camera'
# set the camera properties:
camera_obj.data.type        = 'ORTHO';
camera_obj.data.ortho_scale = 1.25;
camera_obj.data.clip_start  = 0.1;
camera_obj.data.clip_end    = 100.1;
# 
camera_obj.hide        = True
camera_obj.select      = False
camera_obj.hide_render = False
# 
bpy.context.scene.camera = camera_obj

# [hard lamp / front]
# create a sun lamp in the specified position
bpy.ops.object.lamp_add(type='SUN',location=(0.95,-1.0,1.6),rotation=(-18.0*math.pi/180.0,47.0*math.pi/180.0,-70.0*math.pi/180.0))
lamp_front_obj = bpy.context.object
# set the lamp name
lamp_front_obj.name = 'lamp_front'
# set the lamp properties:
# lamp
lamp_front_obj.data.color        = (1.0,1.0,1.0)
lamp_front_obj.data.energy       = 0.7
lamp_front_obj.data.use_specular = True
lamp_front_obj.data.use_diffuse  = True
# shadow
lamp_front_obj.data.shadow_method             = 'RAY_SHADOW'
lamp_front_obj.data.shadow_color              = (0.4,0.4,0.4)
lamp_front_obj.data.shadow_ray_samples        = 1
lamp_front_obj.data.shadow_soft_size          = 1.0
lamp_front_obj.data.shadow_adaptive_threshold = 0.0
# activate the object
lamp_front_obj.hide        = True
lamp_front_obj.select      = False
lamp_front_obj.hide_render = False

# [hard lamp / back]
# create a sun lamp in the specified position
bpy.ops.object.lamp_add(type='SUN',location=(-1.0,-1.0,1.0),rotation=(-20.0*math.pi/180.0,70.0*math.pi/180.0,-155.0*math.pi/180.0))
lamp_back_obj = bpy.context.object
# set the lamp name
lamp_back_obj.name = 'lamp_back'
# set the lamp properties:
# lamp
lamp_back_obj.data.color        = (1.0,1.0,1.0)
lamp_back_obj.data.energy       = 0.5
lamp_back_obj.data.use_specular = True
lamp_back_obj.data.use_diffuse  = True
# shadow
lamp_back_obj.data.shadow_method             = 'RAY_SHADOW'
lamp_back_obj.data.shadow_color              = (0.4,0.4,0.4)
lamp_back_obj.data.shadow_ray_samples        = 1
lamp_back_obj.data.shadow_soft_size          = 1.0
lamp_back_obj.data.shadow_adaptive_threshold = 0.0
# activate the object
lamp_back_obj.hide        = True
lamp_back_obj.select      = False
lamp_back_obj.hide_render = False

# [soft lamp]
# create a soft lamp in the specified position
bpy.ops.object.lamp_add(type='HEMI',location=(0.0,0.0,2.5),rotation=(0.0,0.0,0.0))
lamp_soft_obj = bpy.context.object
# set the lamp name
lamp_soft_obj.name = 'lamp_soft'
# set the lamp properties:
# lamp
lamp_soft_obj.data.color        = (1.0,1.0,1.0)
lamp_soft_obj.data.energy       = 0.7
lamp_soft_obj.data.use_specular = True
lamp_soft_obj.data.use_diffuse  = True
# activate the object
lamp_soft_obj.hide        = True
lamp_soft_obj.select      = False
lamp_soft_obj.hide_render = True

# [plane]
# create a plane in the specified position
bpy.ops.mesh.primitive_plane_add(location=(0.0,0.0,0.0))
plane_shadow_obj = bpy.context.object
# set the plane name
plane_shadow_obj.name = 'plane_shadow'
# scale the plane 'indefinitely'
plane_shadow_obj.scale = (1000.0,1000.0,1000.0)
# create material properties for the plane 
plane_shadow_mat = bpy.data.materials.new('plane_shadow')
# assign material properties to the plane
bpy.ops.object.material_slot_add()
plane_shadow_obj.material_slots[0].material = plane_shadow_mat;
# set the material properties:
# diffuse
plane_shadow_mat.diffuse_color     = (1.0,1.0,1.0)
plane_shadow_mat.diffuse_intensity = 1.0
plane_shadow_mat.diffuse_shader    = 'LAMBERT'
# specular
plane_shadow_mat.specular_color     = (1.0,1.0,1.0)
plane_shadow_mat.specular_intensity = 1.0
plane_shadow_mat.specular_shader    = 'COOKTORR'  
plane_shadow_mat.specular_hardness  = 500
# shading
plane_shadow_mat.emit         = 0.0
plane_shadow_mat.ambient      = 1.0
plane_shadow_mat.translucency = 0.0
# transparency
plane_shadow_mat.use_transparency    = True
plane_shadow_mat.transparency_method = 'Z_TRANSPARENCY'
plane_shadow_mat.alpha               = 0.7
plane_shadow_mat.specular_alpha      = 1.0
plane_shadow_mat.raytrace_transparency.fresnel = 0.0
# options
plane_shadow_mat.use_raytrace = True
plane_shadow_mat.use_mist     = True
# shadow
plane_shadow_mat.use_shadows             = True
plane_shadow_mat.use_only_shadow         = True
plane_shadow_mat.use_ray_shadow_bias     = True
plane_shadow_mat.use_cast_shadows        = True
plane_shadow_mat.use_cast_buffer_shadows = True
plane_shadow_mat.use_cast_approximate    = True
#
plane_shadow_obj.hide        = True
plane_shadow_obj.select      = False
plane_shadow_obj.hide_render = True

# [world]
world = bpy.data.worlds.new('World')
bpy.context.scene.world = world
world.use_sky_paper                        = True
world.light_settings.use_ambient_occlusion = False
world.light_settings.ao_factor             = 0.8
world.light_settings.gather_method         = 'RAYTRACE'
world.light_settings.distance              = 1.0
world.light_settings.sample_method         = 'CONSTANT_QMC'
world.light_settings.samples               = 5.0

# [render]
# set the render properties:
# dimensions
bpy.context.scene.render.resolution_percentage = 100
# anti-aliasing
bpy.context.scene.render.use_antialiasing     = True
bpy.context.scene.render.antialiasing_samples = '16'
# shading
bpy.context.scene.render.alpha_mode = 'TRANSPARENT'
# output
bpy.context.scene.render.use_overwrite              = True
bpy.context.scene.render.use_file_extension         = True
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.image_settings.color_mode  = 'RGBA'
bpy.context.scene.render.image_settings.color_depth = '16'
bpy.context.scene.render.image_settings.compression = 50

# [texture]
if flag_texture:
	img_tex = bpy.data.images.load(os.path.join(path_folder,name_texture_img))

# get list of all files in directory
full_path_to_directory = os.path.join(path_folder,'input')
file_list = os.listdir(full_path_to_directory)

# reduce the list to files ending in 'obj' using 'list comprehensions'
obj_list = [item for item in file_list if item[-3:] == 'obj']

# loop through the strings in obj_list.
for item in obj_list:
	full_path_to_file = os.path.join(full_path_to_directory,item)
	bpy.ops.import_scene.obj(filepath=full_path_to_file,axis_forward='Y',axis_up='Z')

	shape_name = item[:-4]
	shape_obj  = bpy.data.objects.get(shape_name)

	# set the shape name
	shape_obj.name = shape_name
	
	shape_obj.hide        = False
	shape_obj.select      = True
	shape_obj.hide_render = False

	# warning: the following code does not work so far
	# bpy.ops.object.mode_set(mode='EDIT')
	# bpy.ops.object.normals_make_consistent(inside=True)
	# bpy.ops.object.mode_set(mode='OBJECT')

	#
	bpy.ops.object.shade_smooth()

	# [shape material]
	# create material properties for the shape 
	shape_mat = bpy.data.materials.new(shape_name)
	# assign material properties to the shape
	shape_obj.data.materials.append(shape_mat)
	# set the material properties:
	# diffuse
	shape_mat.diffuse_color     = (0.871,0.716,0.223)
	shape_mat.diffuse_intensity = 0.8
	shape_mat.diffuse_shader    = 'LAMBERT'
	# specular
	shape_mat.specular_color     = (1.0,1.0,1.0)
	shape_mat.specular_intensity = 0.5
	shape_mat.specular_shader    = 'COOKTORR'  
	shape_mat.specular_hardness  = 500
	# shading
	shape_mat.emit         = 0.0
	shape_mat.ambient      = 1.0
	shape_mat.translucency = 0.0
	# transparency
	shape_mat.use_transparency = False
	# options
	shape_mat.use_raytrace = True
	shape_mat.use_mist     = True
	# shadow
	shape_mat.use_shadows             = True # if True, ambient occlusions are enabled
	shape_mat.use_only_shadow         = False
	shape_mat.use_ray_shadow_bias     = True
	shape_mat.use_cast_shadows        = True
	shape_mat.use_cast_buffer_shadows = True
	shape_mat.use_cast_approximate    = True
	
	if flag_texture:
        	#
		tex       = bpy.data.textures.new('texture',type='IMAGE')
		tex.image = img_tex
		#
		shape_tex = shape_mat.texture_slots.add()
		#
		shape_tex.texture               = tex
		shape_tex.texture_coords        = 'UV'
		shape_tex.mapping               = 'FLAT'
		shape_tex.use_map_color_diffuse = True 
		shape_tex.diffuse_color_factor  = 1.0
		shape_tex.blend_type            = 'MIX'

	#
	bpy.context.scene.render.filepath = os.path.join(path_folder,'output',shape_name)
	bpy.ops.render.render(animation=False,write_still=True)

	if flag_shadow:
		# transparency
		shape_mat.use_transparency    = True
		shape_mat.transparency_method = 'Z_TRANSPARENCY'
		shape_mat.alpha               = 0.0
		shape_mat.specular_alpha      = 0.1
		#
		world.light_settings.use_ambient_occlusion = True
		lamp_front_obj.hide_render   = True
		lamp_back_obj.hide_render    = True
		lamp_soft_obj.hide_render    = False
		plane_shadow_obj.hide_render = False
		#
		bpy.context.scene.render.filepath = os.path.join(path_folder,'output',shape_name+'_shadow')
		bpy.ops.render.render(animation=False,write_still=True)

	#
	shape_obj.hide        = True
	shape_obj.select      = False
	shape_obj.hide_render = True

