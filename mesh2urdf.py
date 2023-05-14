import os
import logging
from shutil import copyfile
urdf_template_path = 'urdf_template.urdf'
scale = 1.0
mesh_path = 'atomic-manipulation-skills/assets/urdf/ycb/025_mug/textured.obj'
col_mesh_path = 'atomic-manipulation-skills/assets/urdf/ycb/025_mug/mug_collision.obj'
urdf_name = 'mug'
visual_origin = [0., 0., 0.]
collision_origin = [0., 0., 0.]
mass = 1.

#TODO: inertia correct?
ixx = 1e-4
iyy = 1e-4
izz = 1e-4
ixy = 0.
iyz = 0.
ixz = 0.
supported_formats = ['obj']
mesh_format = os.path.basename(mesh_path).split('.')[-1]
col_mesh_format = os.path.basename(col_mesh_path).split('.')[-1] if col_mesh_path else mesh_format
visual_mesh_target_path_rel = os.path.join(urdf_name, '{}_visual.{}'.format(urdf_name, mesh_format))
visual_mesh_target_path = os.path.join('./', visual_mesh_target_path_rel)
collision_mesh_target_path_rel = os.path.join(urdf_name, '{}_collision.{}'.format(urdf_name, mesh_format))
collision_mesh_target_path = os.path.join('./', collision_mesh_target_path_rel)
copyfile(mesh_path, visual_mesh_target_path)
if col_mesh_path:
    copyfile(col_mesh_path, collision_mesh_target_path)
with open(urdf_template_path, 'r') as f:
    urdf_template = f.read()
urdf = urdf_template.replace('$name$', urdf_name) \
                    .replace('$visual_origin_xyz$', ' '.join(map(str, visual_origin))) \
                    .replace('$visual_geometry_path$', visual_mesh_target_path_rel) \
                    .replace('$collision_origin_xyz$', ' '.join(map(str, collision_origin))) \
                    .replace('$collision_geometry_path$', collision_mesh_target_path_rel if col_mesh_path else visual_mesh_target_path_rel) \
                    .replace('$mass$', str(mass)) \
                    .replace('$ixx$', str(ixx)) \
                    .replace('$iyy$', str(iyy)) \
                    .replace('$izz$', str(izz)) \
                    .replace('$ixy$', str(ixy)) \
                    .replace('$iyz$', str(iyz)) \
                    .replace('$ixz$', str(ixz)) \
                    .replace('$scale$', ' '.join([str(scale)]*3))
with open(os.path.join('./{}.urdf'.format(urdf_name)), 'w') as f:
    f.write(urdf)