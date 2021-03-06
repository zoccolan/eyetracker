'''OpenGL extension EXT.texture_cube_map

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_cube_map.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_texture_cube_map'
GL_NORMAL_MAP_EXT = constant.Constant( 'GL_NORMAL_MAP_EXT', 0x8511 )
GL_REFLECTION_MAP_EXT = constant.Constant( 'GL_REFLECTION_MAP_EXT', 0x8512 )
GL_TEXTURE_CUBE_MAP_EXT = constant.Constant( 'GL_TEXTURE_CUBE_MAP_EXT', 0x8513 )
GL_TEXTURE_BINDING_CUBE_MAP_EXT = constant.Constant( 'GL_TEXTURE_BINDING_CUBE_MAP_EXT', 0x8514 )
GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT = constant.Constant( 'GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT', 0x8515 )
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT = constant.Constant( 'GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT', 0x8516 )
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT = constant.Constant( 'GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT', 0x8517 )
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT = constant.Constant( 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT', 0x8518 )
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT = constant.Constant( 'GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT', 0x8519 )
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT = constant.Constant( 'GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT', 0x851A )
GL_PROXY_TEXTURE_CUBE_MAP_EXT = constant.Constant( 'GL_PROXY_TEXTURE_CUBE_MAP_EXT', 0x851B )
GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT = constant.Constant( 'GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT', 0x851C )


def glInitTextureCubeMapEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
