'''OpenGL extension NV.occlusion_query

Overview (from the spec)
	
	The HP_occlusion_test extension defines a mechanism whereby an
	application can query the visibility of an object, where "visible"
	means that at least one pixel passes the depth and stencil tests.
	
	The HP extension has two major shortcomings.
	
	- It returns the result as a simple GL_TRUE/GL_FALSE result, when in
	  fact it is often useful to know exactly how many pixels passed.
	- It provides only a simple "stop-and-wait" model for using multiple
	  queries.  The application begins an occlusion test and ends it;
	  then, at some later point, it asks for the result, at which point
	  the driver must stop and wait until the result from the previous
	  test is back before the application can even begin the next one.
	  This is a very simple model, but its performance is mediocre when
	  an application wishes to perform many queries, and it eliminates
	  most of the opportunites for parallelism between the CPU and GPU.
	
	This extension solves both of those problems.  It returns as its
	result the number of pixels that pass, and it provides an interface
	conceptually similar to that of NV_fence that allows applications to
	issue many occlusion queries before asking for the result of any one.
	As a result, they can overlap the time it takes for the occlusion
	query results to be returned with other, more useful work, such as
	rendering other parts of the scene or performing other computations
	on the CPU.
	
	There are many situations where a pixel count, rather than a boolean
	result, is useful.
	
	- If the visibility test is an object bounding box being used to
	  decide whether to skip the object, sometimes it can be acceptable,
	  and beneficial to performance, to skip an object if less than some
	  threshold number of pixels could be visible.
	- Knowing the number of pixels visible in the bounding box may also
	  help decide what level of detail a model should be drawn with.  If
	  only a few pixels are visible, a low-detail model may be
	  acceptable.  In general, this allows level-of-detail mechanisms to
	  be slightly less ad hoc.
	- "Depth peeling" techniques, such as order-independent transparency,
	  would typically like to know when to stop rendering more layers; it
	  is difficult to come up with a way to determine a priori how many
	  layers to use.  A boolean count allows applications to stop when
	  more layers will not affect the image at all, but this will likely
	  be unacceptable for performance, with minimal gains to image
	  quality.  Instead, it makes more sense to stop rendering when the
	  number of pixels goes below a threshold; this should provide better
	  results than any of these other algorithms.
	- Occlusion queries can be used as a replacement for glReadPixels of
	  the depth buffer to determine whether, say, a light source is
	  visible for the purposes of a lens flare effect or a halo to
	  simulate glare.  Pixel counts allow you to compute the percentage
	  of the light source that is visible, and the brightness of these
	  effects can be modulated accordingly.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/occlusion_query.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_occlusion_query'
GL_PIXEL_COUNTER_BITS_NV = constant.Constant( 'GL_PIXEL_COUNTER_BITS_NV', 0x8864 )
glget.addGLGetConstant( GL_PIXEL_COUNTER_BITS_NV, (1,) )
GL_CURRENT_OCCLUSION_QUERY_ID_NV = constant.Constant( 'GL_CURRENT_OCCLUSION_QUERY_ID_NV', 0x8865 )
glget.addGLGetConstant( GL_CURRENT_OCCLUSION_QUERY_ID_NV, (1,) )
GL_PIXEL_COUNT_NV = constant.Constant( 'GL_PIXEL_COUNT_NV', 0x8866 )
GL_PIXEL_COUNT_AVAILABLE_NV = constant.Constant( 'GL_PIXEL_COUNT_AVAILABLE_NV', 0x8867 )
glGenOcclusionQueriesNV = platform.createExtensionFunction( 
	'glGenOcclusionQueriesNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, arrays.GLuintArray,),
	doc = 'glGenOcclusionQueriesNV( GLsizei(n), GLuintArray(ids) ) -> None',
	argNames = ('n', 'ids',),
)

glDeleteOcclusionQueriesNV = platform.createExtensionFunction( 
	'glDeleteOcclusionQueriesNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, arrays.GLuintArray,),
	doc = 'glDeleteOcclusionQueriesNV( GLsizei(n), GLuintArray(ids) ) -> None',
	argNames = ('n', 'ids',),
)

glIsOcclusionQueryNV = platform.createExtensionFunction( 
	'glIsOcclusionQueryNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLboolean, 
	argTypes=(constants.GLuint,),
	doc = 'glIsOcclusionQueryNV( GLuint(id) ) -> constants.GLboolean',
	argNames = ('id',),
)

glBeginOcclusionQueryNV = platform.createExtensionFunction( 
	'glBeginOcclusionQueryNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint,),
	doc = 'glBeginOcclusionQueryNV( GLuint(id) ) -> None',
	argNames = ('id',),
)

glEndOcclusionQueryNV = platform.createExtensionFunction( 
	'glEndOcclusionQueryNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(),
	doc = 'glEndOcclusionQueryNV(  ) -> None',
	argNames = (),
)

glGetOcclusionQueryivNV = platform.createExtensionFunction( 
	'glGetOcclusionQueryivNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, arrays.GLintArray,),
	doc = 'glGetOcclusionQueryivNV( GLuint(id), GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('id', 'pname', 'params',),
)

glGetOcclusionQueryuivNV = platform.createExtensionFunction( 
	'glGetOcclusionQueryuivNV', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLuint, constants.GLenum, arrays.GLuintArray,),
	doc = 'glGetOcclusionQueryuivNV( GLuint(id), GLenum(pname), GLuintArray(params) ) -> None',
	argNames = ('id', 'pname', 'params',),
)


def glInitOcclusionQueryNV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
