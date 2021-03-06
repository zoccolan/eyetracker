'''OpenGL extension ARB.point_parameters

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.point_parameters to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.point_parameters import *
### END AUTOGENERATED SECTION
from OpenGL.GL import glget
glget.addGLGetConstant( GL_POINT_SIZE_MIN_ARB, (1,) )
glget.addGLGetConstant( GL_POINT_SIZE_MAX_ARB , (1,) )
glget.addGLGetConstant( GL_POINT_FADE_THRESHOLD_SIZE_ARB, (1,) )
glget.addGLGetConstant( GL_POINT_DISTANCE_ATTENUATION_ARB, (3,) )

glPointParameterfvARB = arrays.setInputArraySizeType(
	glPointParameterfvARB,
	None, # XXX should be dependant on the pname field!
	arrays.GLfloatArray, 
	'params',
)
