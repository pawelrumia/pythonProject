import matplotlib.pyplot as mpl
import numpy as np

xStart = 0
xStop = 2 * np.pi
increment = 0.1
x = np.arange(xStart, xStop, increment)
y = np.sin(x)
z = np.cos(x)


mpl.subplot(2, 1, 1)
mpl.plot( x , y , 'g' )
mpl.title ( ' sin' )
mpl.xlabel('x')
mpl.ylabel ( ' sin(x)' )
mpl.grid ( )
mpl.show ( )

mpl.subplot( 2 , 1 , 2 )
mpl.plot( x , z , ' r ' )
mpl.title ( ' cos ' )
mpl.xlabel (' x ' )
mpl.ylabel ( ' c o s ( x ) ' )
mpl.grid ( )
mpl. show ( )