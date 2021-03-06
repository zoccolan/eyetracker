'''OpenGL extension NV.texture_expand_normal

This module customises the behaviour of the 
OpenGL.raw.GL.NV.texture_expand_normal to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.NV.texture_expand_normal import *
### END AUTOGENERATED SECTION