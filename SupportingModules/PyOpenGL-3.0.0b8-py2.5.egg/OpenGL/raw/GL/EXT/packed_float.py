'''OpenGL extension EXT.packed_float

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/packed_float.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_packed_float'
GL_R11F_G11F_B10F_EXT = constant.Constant( 'GL_R11F_G11F_B10F_EXT', 0x8C3A )
GL_UNSIGNED_INT_10F_11F_11F_REV_EXT = constant.Constant( 'GL_UNSIGNED_INT_10F_11F_11F_REV_EXT', 0x8C3B )
GL_RGBA_SIGNED_COMPONENTS_EXT = constant.Constant( 'GL_RGBA_SIGNED_COMPONENTS_EXT', 0x8C3C )


def glInitPackedFloatEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
