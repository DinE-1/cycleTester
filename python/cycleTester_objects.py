pi=3.1415

def get_obj(sheet,alias):
	cell=sheet.getCellFromAlias(alias)
	data=sheet.get(cell)
	return data

class object:
	def __init__(self,density):
		self.volume=None
		self.density=density		
		self.mass=None
		self.inertia=None
		self.momentOfInertia=None

class cuboid(object):
	def __init__(self,length,width,height,density):
		super().__init__(density)
		self.length=length
		self.width=width
		self.height=height
		self.density=density

		self.volume=self.length*self.width*self.height
		self.mass=self.density*self.volume
		
		self.inertia=self.mass
class cylinder(object):
	def __init__(self,radius,height,density):
		super().__init__(density)
		self.radius=radius
		self.height=height

		self.volume=self.radius*self.radius * self.height *pi
		self.mass=self.volume * self.density
		
		self.inertia=self.mass
		self.momentOfInertia=self.mass*self.radius*self.radius*0.5
class tube(cylinder):
	def __init__(self,radiusOuter,radiusInner,height,density):
		super().__init__(radiusOuter,height,density)
		self.radiusInner=radiusInner
		self.radiusOuter=self.radius
		
		self.volume=self.volume-self.radiusInner*self.radiusInner*self.height*pi
		self.mass=self.volume*self.density

		self.inertia=self.mass
		self.momentOfInertia=self.mass * (self.radiusOuter*self.radiusOuter - self.radiusInner*self.radiusInner) * 0.5
