from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
class game(Button):
    def __init__(self,position=(0, 0, 0)):
        super().__init__(
            parent= scene,
            position= position,
            model="cube",
            origin_y=.5,
            texture="grass",
            color = color.color(0,0,random.uniform(32,1.0)),
            highlight_color = color.green)
    def input(self, key):
        if self.hovered:
            if key=="left mouse down":
             build =game(position=self.position + mouse.normal)
            if key=="shift":
               destroy(self)
for z in range(8):
   for x in range(8):
      haz = game(position=(x,0,z))
player = FirstPersonController()


app.run()
