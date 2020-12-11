###############################################################################
#               Button Controller | Template v 1.0 | UPBGE 0.2.5              #
###############################################################################
#                      Created by: Guilherme Teres Nunes                      #
#                       Access: youtube.com/UnidayStudio                      #
#                               github.com/UnidayStudio                       #
###############################################################################
# This component will spawn a minimap based on the camera (which owns the
# component) view. Add this component to a camera and position it on top of
# your character.
# You can read a small doc about this Component here:
# https://github.com/UnidayStudio/UPBGE-UtilsTemplate
###############################################################################
import bge
from mathutils import Vector, Color

class Button(bge.types.KX_PythonComponent):
	args = {
		"Activate"		    : True,
		"Pressed Message"   : "",
		"Released Message"  : "",
		"Normal Color"      : Color([0.7,0.7,0.7,1.0]),
		"Highlighted Color" : Color([1.0,1.0,1.0,1.0]),
		"Pressed Color"     : Color([0.5,0.5,0.5,1.0]),
		"Disabled Color"    : Color([0.2,0.2,0.2,1.0]),
	}

	def start(self, args):
		self.active           = args["Activate"]
		self.pressedFunction  = None
		self.releasedFunction = None

		self.pressedMessage   = args["Pressed Message"]
		self.releasedMessage  = args["Released Message"]

		self.normalColor      = args["Normal Color"]
		self.highlightedColor = args["Highlighted Color"]
		self.pressedColor     = args["Pressed Color"]
		self.disabledColor    = args["Disabled Color"]

		self.materials = []
		for mesh in self.object.meshes:
			for material in mesh.materials:
				self.materials.append(material)

		self.object["Button Component"] = True

	def __mouseOver(self):
		scene = bge.logic.getCurrentScene()
		cam   = scene.active_camera
		mPos  = bge.logic.mouse.position

		obj = cam.getScreenRay(mPos[0], mPos[1], 10000, "Button Component")
		return obj == self.object

	def update(self):
		over = self.__mouseOver()

		if self.active:
			if over:
				if bge.logic.mouse.inputs[bge.events.LEFTMOUSE].values[-1]:
					self.object.color = self.pressedColor
				else:
					self.object.color = self.highlightedColor
			else:
				self.object.color = self.normalColor
		else:
			self.object.color = self.disabledColor

		#for mat in self.materials:
		#	mat.diffuseIntensity = self.test



