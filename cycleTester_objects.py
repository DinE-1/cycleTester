import FreeCAD as app
from FreeCAD import Units as unit

pi=3.1415

class object:
	__init__(density):
		self.volume=None
		self.density=density		
		self.mass=None

class cubeoid(object):
	__init__(length,width,height,density):
		self.length=length
		self.width=width
		self.height=height
		self.density=density

		volume=length*width*height
		mass=density*volume
	
class cylinder(object):
	__init__(radius,height,density):
		super().__init__(density)
		self.radius=radius
		self.height=height

		self.volume=self.radius*self.radius*self.height*pi
		self.mass=self.volume*self.density
		
class tube(cylinder):
	__init__(radiusOuter,radiusInner,height,density):
		super.__init__(radiusOuter,height,density)
		self.radiusInner=radiusInner
		self.radiusOuter=self.radius
		
		self.volume=self.volume-self.radiusInner*self.radiusInner*self.height*pi
		self.mass=self.volume*self.density
