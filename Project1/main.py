import time
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from panda3d.core import loadPrcFileData
loadPrcFileData('', 'load-display pandagl')  # Must be first

app = Ursina()
player = FirstPersonController()

Ground = Entity(
    model="plane",
    color=color.green,
    scale=(100,1,100),
    position= Vec4(0,0,0,0),
    collider="mesh"
)
Ground1 = Entity(
    model="plane",
    color=color.black33,
    scale=(100,1,100),
    position= Vec4(1,1,1,1),
    collider="mesh"
)
light = PointLight(parent=scene, position=(2, 2, 2, 2), color=color.white)
Sky()
DirectionalLight()
AmbientLight(color=color.rgba(100, 100, 100, 0.5))

def input(key):
    playerpos = player.position + player.forward * 2
    playerpos.y = 0.75
    
    if key == "left mouse down":
        Entity(model="cube", texture="tb.bmp", scale=(1.5,1.5,1.5), collider="box", position=player.position)
    elif key == "right mouse down":
        Entity(model="cube", texture="db", scale=(1.5,1.5,1.5), collider="box", position=playerpos)
    elif key == "escape":
        Text("Quitting Minecraft")
        time.sleep(1)
        application.quit()
        
if player.position == Vec4(-100):
    application.quit()
     
            



app.run()
