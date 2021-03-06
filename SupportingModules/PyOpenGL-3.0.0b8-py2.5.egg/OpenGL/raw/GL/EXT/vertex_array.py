'''OpenGL extension EXT.vertex_array

Overview (from the spec)
	
	This extension adds the ability to specify multiple geometric primitives
	with very few subroutine calls.  Instead of calling an OpenGL procedure
	to pass each individual vertex, normal, or color, separate arrays
	of vertexes, normals, and colors are prespecified, and are used to
	define a sequence of primitives (all of the same type) when a single
	call is made to DrawArraysEXT.  A stride mechanism is provided so that
	an application can choose to keep all vertex data staggered in a
	single array, or sparsely in separate arrays.  Single-array storage
	may optimize performance on some implementations.
	
	This extension also supports the rendering of individual array elements,
	each specified as an index into the enabled arrays.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/vertex_array.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_vertex_array'
GL_VERTEX_ARRAY_EXT = constant.Constant( 'GL_VERTEX_ARRAY_EXT', 0x8074 )
GL_NORMAL_ARRAY_EXT = constant.Constant( 'GL_NORMAL_ARRAY_EXT', 0x8075 )
GL_COLOR_ARRAY_EXT = constant.Constant( 'GL_COLOR_ARRAY_EXT', 0x8076 )
GL_INDEX_ARRAY_EXT = constant.Constant( 'GL_INDEX_ARRAY_EXT', 0x8077 )
GL_TEXTURE_COORD_ARRAY_EXT = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_EXT', 0x8078 )
GL_EDGE_FLAG_ARRAY_EXT = constant.Constant( 'GL_EDGE_FLAG_ARRAY_EXT', 0x8079 )
GL_VERTEX_ARRAY_SIZE_EXT = constant.Constant( 'GL_VERTEX_ARRAY_SIZE_EXT', 0x807A )
glget.addGLGetConstant( GL_VERTEX_ARRAY_SIZE_EXT, (1,) )
GL_VERTEX_ARRAY_TYPE_EXT = constant.Constant( 'GL_VERTEX_ARRAY_TYPE_EXT', 0x807B )
glget.addGLGetConstant( GL_VERTEX_ARRAY_TYPE_EXT, (1,) )
GL_VERTEX_ARRAY_STRIDE_EXT = constant.Constant( 'GL_VERTEX_ARRAY_STRIDE_EXT', 0x807C )
glget.addGLGetConstant( GL_VERTEX_ARRAY_STRIDE_EXT, (1,) )
GL_VERTEX_ARRAY_COUNT_EXT = constant.Constant( 'GL_VERTEX_ARRAY_COUNT_EXT', 0x807D )
glget.addGLGetConstant( GL_VERTEX_ARRAY_COUNT_EXT, (1,) )
GL_NORMAL_ARRAY_TYPE_EXT = constant.Constant( 'GL_NORMAL_ARRAY_TYPE_EXT', 0x807E )
glget.addGLGetConstant( GL_NORMAL_ARRAY_TYPE_EXT, (1,) )
GL_NORMAL_ARRAY_STRIDE_EXT = constant.Constant( 'GL_NORMAL_ARRAY_STRIDE_EXT', 0x807F )
glget.addGLGetConstant( GL_NORMAL_ARRAY_STRIDE_EXT, (1,) )
GL_NORMAL_ARRAY_COUNT_EXT = constant.Constant( 'GL_NORMAL_ARRAY_COUNT_EXT', 0x8080 )
glget.addGLGetConstant( GL_NORMAL_ARRAY_COUNT_EXT, (1,) )
GL_COLOR_ARRAY_SIZE_EXT = constant.Constant( 'GL_COLOR_ARRAY_SIZE_EXT', 0x8081 )
glget.addGLGetConstant( GL_COLOR_ARRAY_SIZE_EXT, (1,) )
GL_COLOR_ARRAY_TYPE_EXT = constant.Constant( 'GL_COLOR_ARRAY_TYPE_EXT', 0x8082 )
glget.addGLGetConstant( GL_COLOR_ARRAY_TYPE_EXT, (1,) )
GL_COLOR_ARRAY_STRIDE_EXT = constant.Constant( 'GL_COLOR_ARRAY_STRIDE_EXT', 0x8083 )
glget.addGLGetConstant( GL_COLOR_ARRAY_STRIDE_EXT, (1,) )
GL_COLOR_ARRAY_COUNT_EXT = constant.Constant( 'GL_COLOR_ARRAY_COUNT_EXT', 0x8084 )
glget.addGLGetConstant( GL_COLOR_ARRAY_COUNT_EXT, (1,) )
GL_INDEX_ARRAY_TYPE_EXT = constant.Constant( 'GL_INDEX_ARRAY_TYPE_EXT', 0x8085 )
glget.addGLGetConstant( GL_INDEX_ARRAY_TYPE_EXT, (1,) )
GL_INDEX_ARRAY_STRIDE_EXT = constant.Constant( 'GL_INDEX_ARRAY_STRIDE_EXT', 0x8086 )
glget.addGLGetConstant( GL_INDEX_ARRAY_STRIDE_EXT, (1,) )
GL_INDEX_ARRAY_COUNT_EXT = constant.Constant( 'GL_INDEX_ARRAY_COUNT_EXT', 0x8087 )
glget.addGLGetConstant( GL_INDEX_ARRAY_COUNT_EXT, (1,) )
GL_TEXTURE_COORD_ARRAY_SIZE_EXT = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_SIZE_EXT', 0x8088 )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_SIZE_EXT, (1,) )
GL_TEXTURE_COORD_ARRAY_TYPE_EXT = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_TYPE_EXT', 0x8089 )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_TYPE_EXT, (1,) )
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_STRIDE_EXT', 0x808A )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_STRIDE_EXT, (1,) )
GL_TEXTURE_COORD_ARRAY_COUNT_EXT = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_COUNT_EXT', 0x808B )
glget.addGLGetConstant( GL_TEXTURE_COORD_ARRAY_COUNT_EXT, (1,) )
GL_EDGE_FLAG_ARRAY_STRIDE_EXT = constant.Constant( 'GL_EDGE_FLAG_ARRAY_STRIDE_EXT', 0x808C )
glget.addGLGetConstant( GL_EDGE_FLAG_ARRAY_STRIDE_EXT, (1,) )
GL_EDGE_FLAG_ARRAY_COUNT_EXT = constant.Constant( 'GL_EDGE_FLAG_ARRAY_COUNT_EXT', 0x808D )
glget.addGLGetConstant( GL_EDGE_FLAG_ARRAY_COUNT_EXT, (1,) )
GL_VERTEX_ARRAY_POINTER_EXT = constant.Constant( 'GL_VERTEX_ARRAY_POINTER_EXT', 0x808E )
GL_NORMAL_ARRAY_POINTER_EXT = constant.Constant( 'GL_NORMAL_ARRAY_POINTER_EXT', 0x808F )
GL_COLOR_ARRAY_POINTER_EXT = constant.Constant( 'GL_COLOR_ARRAY_POINTER_EXT', 0x8090 )
GL_INDEX_ARRAY_POINTER_EXT = constant.Constant( 'GL_INDEX_ARRAY_POINTER_EXT', 0x8091 )
GL_TEXTURE_COORD_ARRAY_POINTER_EXT = constant.Constant( 'GL_TEXTURE_COORD_ARRAY_POINTER_EXT', 0x8092 )
GL_EDGE_FLAG_ARRAY_POINTER_EXT = constant.Constant( 'GL_EDGE_FLAG_ARRAY_POINTER_EXT', 0x8093 )
glArrayElementEXT = platform.createExtensionFunction( 
	'glArrayElementEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint,),
	doc = 'glArrayElementEXT( GLint(i) ) -> None',
	argNames = ('i',),
)

glColorPointerEXT = platform.createExtensionFunction( 
	'glColorPointerEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLenum, constants.GLsizei, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glColorPointerEXT( GLint(size), GLenum(type), GLsizei(stride), GLsizei(count), c_void_p(pointer) ) -> None',
	argNames = ('size', 'type', 'stride', 'count', 'pointer',),
)

glDrawArraysEXT = platform.createExtensionFunction( 
	'glDrawArraysEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLint, constants.GLsizei,),
	doc = 'glDrawArraysEXT( GLenum(mode), GLint(first), GLsizei(count) ) -> None',
	argNames = ('mode', 'first', 'count',),
)

glEdgeFlagPointerEXT = platform.createExtensionFunction( 
	'glEdgeFlagPointerEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, constants.GLsizei, ctypes.POINTER(constants.GLboolean),),
	doc = 'glEdgeFlagPointerEXT( GLsizei(stride), GLsizei(count), POINTER(constants.GLboolean)(pointer) ) -> None',
	argNames = ('stride', 'count', 'pointer',),
)

glGetPointervEXT = platform.createExtensionFunction( 
	'glGetPointervEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, ctypes.POINTER(ctypes.c_void_p),),
	doc = 'glGetPointervEXT( GLenum(pname), POINTER(ctypes.c_void_p)(params) ) -> None',
	argNames = ('pname', 'params',),
)

glIndexPointerEXT = platform.createExtensionFunction( 
	'glIndexPointerEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLsizei, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glIndexPointerEXT( GLenum(type), GLsizei(stride), GLsizei(count), c_void_p(pointer) ) -> None',
	argNames = ('type', 'stride', 'count', 'pointer',),
)

glNormalPointerEXT = platform.createExtensionFunction( 
	'glNormalPointerEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLsizei, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glNormalPointerEXT( GLenum(type), GLsizei(stride), GLsizei(count), c_void_p(pointer) ) -> None',
	argNames = ('type', 'stride', 'count', 'pointer',),
)

glTexCoordPointerEXT = platform.createExtensionFunction( 
	'glTexCoordPointerEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLenum, constants.GLsizei, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glTexCoordPointerEXT( GLint(size), GLenum(type), GLsizei(stride), GLsizei(count), c_void_p(pointer) ) -> None',
	argNames = ('size', 'type', 'stride', 'count', 'pointer',),
)

glVertexPointerEXT = platform.createExtensionFunction( 
	'glVertexPointerEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLenum, constants.GLsizei, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glVertexPointerEXT( GLint(size), GLenum(type), GLsizei(stride), GLsizei(count), c_void_p(pointer) ) -> None',
	argNames = ('size', 'type', 'stride', 'count', 'pointer',),
)


def glInitVertexArrayEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
