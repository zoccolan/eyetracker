'''OpenGL extension NV.depth_clamp

This module customises the behaviour of the 
OpenGL.raw.GL.NV.depth_clamp to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.NV.depth_clamp import *
### END AUTOGENERATED SECTION