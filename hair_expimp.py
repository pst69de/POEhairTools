#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================
'''
POE Hair Tools v0.1

This script:
    - Exports a set of Hair Particles as JSON
    - Imports a Hair Particles from JSON
    - frame taken from POErigify/weights_expimp.py

TO-DO:
    - Exporter
    - Importer
    - ...

GitHub: https://github.com/pst69de/POEhairTools
Wiki: http://wiki69.pst69.homeip.net/index.php/POErigify#POEhairTools
'''


import bpy
from bpy.props import StringProperty, CollectionProperty
import json
import mathutils

class hairporter():

    def export_hair(self, to_file, from_mesh, particlesystem):

        # export export_hair to given to_file
        print('hairporter.export_hair: export to %s' % to_file)
        me = from_mesh
        # filter groups
        return
        # over export_hair()

    def import_hair(self, from_file, to_mesh, particlesystem):

        # import hair to particle system
        print('hairporter.import_hair: import from %s' % from_file)
        me = to_mesh
        return
        # over import_hair()
    # class over
hairPorter = hairporter()

# GUI (Panel)
#
class ToolsPanelHair(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tools"
    bl_label = 'POEhairTools Hair Export/Import'

    @classmethod
    def poll(cls, context):
        return context.mode in ['PARTICLE']

    # draw the gui
    def draw(self, context):
        layout = self.layout
        scn = context.scene
        id_store = context.window_manager
        # ~ toolsettings = context.tool_settings
        col = layout.column(align=True)
        row = col.row(align=True)
        row.prop(id_store, "hair_expimp_particlesystem", text="", icon="PARTICLES")
        row = col.row(align=True)
        row.operator('hair_expimp.export_hair', icon='EXPORT')
        row = col.row(align=True)
        row.operator('hair_expimp.import_hair', icon='IMPORT')


class HAIR_OT_expimp_export(bpy.types.Operator):
    bl_label = 'Export hair of particle system'
    bl_idname = 'hair_expimp.export_hair'
    bl_description = 'Exports hair to JSON'
    bl_options = {'REGISTER', 'UNDO'}

    # https://blender.stackexchange.com/questions/39854/how-can-i-open-a-file-select-dialog-via-python-to-add-an-image-sequence-into-vse
    filename_ext = ".json"
    filter_glob = StringProperty(default="*.json", options={'HIDDEN'})
    #this can be look into the one of the export or import python file.
    #need to set a path so so we can get the file name and path
    filepath = StringProperty(name="File Path", description="Filepath used for exporting json files", maxlen= 256, default= "")
    files = CollectionProperty(
        name="File Path",
        type=bpy.types.OperatorFileListElement,
        )

    @classmethod
    def poll(self, context):
        return (context.active_object.type == 'MESH' and context.mode == 'PARTICLE')

    # on mouse up:
    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        obj = bpy.context.active_object
        mesh = bpy.context.active_object
        id_store = context.window_manager

        #print("*************SELECTED FILES ***********")
        #print("FILEPATH: %s" % self.filepath) # display the file name and current path
        #for file in self.files:
        #    print("FILENAME: %s" % file.name)
        hairPorter.export_hair(self.filepath, mesh, id_store.hair_expimp_particlesystem)

        return {'FINISHED'}


class HAIR_OT_expimp_import(bpy.types.Operator):
    bl_label = 'Import hair from JSON'
    bl_idname = 'hair_expimp.import_hair'
    bl_description = 'Imports hair from JSON'
    bl_options = {'REGISTER', 'UNDO'}

    # https://blender.stackexchange.com/questions/39854/how-can-i-open-a-file-select-dialog-via-python-to-add-an-image-sequence-into-vse
    filename_ext = ".json"
    filter_glob = StringProperty(default="*.json", options={'HIDDEN'})
    #this can be look into the one of the export or import python file.
    #need to set a path so so we can get the file name and path
    filepath = StringProperty(name="File Path", description="Filepath used for importing json files", maxlen= 256, default= "")
    files = CollectionProperty(
        name="File Path",
        type=bpy.types.OperatorFileListElement,
        )

    @classmethod
    def poll(cls, context):
        return (context.active_object.type == 'MESH' and context.mode == 'PARTICLE')

    # on mouse up:
    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        obj = bpy.context.active_object
        mesh = bpy.context.active_object
        id_store = context.window_manager

        hairPorter.import_hair(self.filepath, mesh, id_store.hair_expimp_particlesystem)

        return {'FINISHED'}


def register():
    IDStore = bpy.types.WindowManager
    bpy.utils.register_class(ToolsPanelHair)
    bpy.utils.register_class(HAIR_OT_expimp_export)
    bpy.utils.register_class(HAIR_OT_expimp_import)
    IDStore.hair_expimp_particlesystem = StringProperty(name="hair_expimp_particlesystem", description="Particle System ex/importing hair json", maxlen= 32, default= "")

def unregister():
    IDStore = bpy.types.WindowManager
    bpy.utils.unregister_class(ToolsPanelHair)
    bpy.utils.unregister_class(HAIR_OT_expimp_export)
    bpy.utils.unregister_class(HAIR_OT_expimp_import)
    del IDStore.hair_expimp_particlesystem

# bpy.utils.register_module(__name__)
