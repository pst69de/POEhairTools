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
    - provides the init interface for the addon POEhairTools

TO-DO:
    - ...

GitHub: https://github.com/pst69de/POEhairTools
Wiki: http://wiki69.pst69.homeip.net/index.php/POErigify#POEhairTools
'''
# <pep8 compliant>

bl_info = {
    "name": "POEhairTools",
    "version": (0, 1),
    "author": "Patrick O.Ehrmann",
    "blender": (2, 79, 0),
    "description": "WIP! Tools to manage hair particle systems, as to transfer them from one to another mesh",
    "warning": "under development (TESTING)",
    "location": "View3d tools panel",
    "wiki_url": "http://wiki69.pst69.homeip.net/index.php/POErigify#POEhairTools"
                "Scripts/Mesh/Hair",
    "tracker_url": "https://github.com/pst69de/POEhairTools",
    "support": "TESTING",
    "category": "Mesh"}


if "bpy" in locals():
    import importlib
    importlib.reload(ui)
else:
    from . import ui

import bpy
import sys
import os
from bpy.types import AddonPreferences
from bpy.props import BoolProperty


class POEhairToolsPreferences(AddonPreferences):
    # this must match the addon name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __name__

    test_mode = BoolProperty()
    show_expanded = BoolProperty()

    def draw(self, context):
        layout = self.layout
        column = layout.column()
        box = column.box()

        # first stage
        expand = getattr(self, 'show_expanded')
        icon = 'TRIA_DOWN' if expand else 'TRIA_RIGHT'
        col = box.column()
        row = col.row()
        sub = row.row()
        sub.context_pointer_set('addon_prefs', self)
        sub.alignment = 'LEFT'
        op = sub.operator('wm.context_toggle', text='', icon=icon,
                          emboss=False)
        op.data_path = 'addon_prefs.show_expanded'
        sub.label('{}: {}'.format('POEhairTools', 'Enable Test Mode'))
        sub = row.row()
        sub.alignment = 'RIGHT'
        sub.prop(self, 'test_mode')

        if expand:
            split = col.row().split(percentage=0.15)
            split.label('Description:')
            split.label(text='When enabled the add-on will run in test mode.')

        row = layout.row()
        row.label("End of POEhairTools Preferences")


class POEhairToolsName(bpy.types.PropertyGroup):
    name = bpy.props.StringProperty()


##### REGISTER #####

def register():
    # ui register routine
    ui.register()
    # register some prefs classes
    bpy.utils.register_class(POEhairToolsName)
    bpy.utils.register_class(POEhairToolsPreferences)
    # register id_store components
    IDStore = bpy.types.WindowManager
    IDStore.POEhairTools_test_mode = bpy.props.BoolProperty(name="Test Mode",
                                                            description="Enables/disables test mode for POEhairTools",
                                                            default=False)
    # over register()


def unregister():
    # unregister id_store components (delete them)
    IDStore = bpy.types.WindowManager
    del IDStore.POEhairTools_test_mode
    # unregister some prefs classes
    bpy.utils.unregister_class(POEhairToolsName)
    bpy.utils.unregister_class(POEhairToolsPreferences)
    # ui unregister routine
    ui.unregister()
    # over unregister()
