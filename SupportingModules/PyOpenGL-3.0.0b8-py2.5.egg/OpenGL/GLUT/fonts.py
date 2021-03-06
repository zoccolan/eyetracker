"""Load font "constants" (actually void *s) from the GLUT DLL"""
from OpenGL import platform

for name in [
	'GLUT_STROKE_ROMAN',
	'GLUT_STROKE_MONO_ROMAN',
	'GLUT_BITMAP_9_BY_15',
	'GLUT_BITMAP_8_BY_13',
	'GLUT_BITMAP_TIMES_ROMAN_10',
	'GLUT_BITMAP_TIMES_ROMAN_24',
	'GLUT_BITMAP_HELVETICA_10',
	'GLUT_BITMAP_HELVETICA_12',
	'GLUT_BITMAP_HELVETICA_18',
]:
	try:
		# Win32 just has pointers to values 1,2,3,etc
		# GLX has pointers to font structures...
		p = platform.getGLUTFontPointer( name )
	except (ValueError,AttributeError), err:
		print 'GLUT font error', str(err)
	else:
		globals()[name] = p
		del p

del platform, name
