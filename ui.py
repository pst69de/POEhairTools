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
    - is the entry library for all UI classes
      (actually external references)

TO-DO:
    - ...

GitHub: https://github.com/pst69de/POEhairTools
Wiki: http://wiki69.pst69.homeip.net/index.php/POErigify#POEhairTools
'''
# <pep8 compliant>

import bpy
from bpy.props import StringProperty
from mathutils import Color

from . import hair_expimp


def register():

    hair_expimp.register()
    # def register() over

def unregister():

    hair_expimp.unregister()
    # def unregister() over
