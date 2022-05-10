import os
from vitrix_engine import *

from lib.entities.floor import Floor
from lib.entities.map import Map
from lib.entities.player import Player
from lib.entities.enemy import Zombie

from lib.items.aid_kit import AidKit
from lib.items.ammo import Ammo

from vitrix_engine.shaders.basic_lighting_shader import basic_lighting_shader

app = Ursina()
# The inventory needs to load after ursina app()
from lib.UI.inventory import *

window.borderless = False
window.exit_button.visible = False

paused = False
window.title = "Vitrix - Singleplayer"
Entity.default_shader = basic_lighting_shader
window.fullscreen = True

floor = Floor()
map = Map()
sky = Entity(
    model=os.path.join("assets", "models", "sphere.obj"),
    texture=os.path.join("assets", "textures", "sky.png"),
    scale=9999,
    double_sided=True
)

def toggle_fullscreen():
    if window.fullscreen:
        window.fullscreen = False
    else:
        window.fullscreen = True

fullscreen_button = Button(
            text="Toggle Fullscreen",
            position=Vec2(.2, 0),
            scale=0.15,
            enabled=False,
            on_click=Func(toggle_fullscreen)
        )
fullscreen_button.fit_to_text()


player = Player(Vec3(0, 1, 0))
aid_kit = AidKit(Vec3(10, 1.6, 3))
ammo = Ammo(Vec3(15, 1, 3))

enemies = []


#controls_dict={
#    "tab":"Pause the Game",
#    "L":"Release a zombie",
#    "left-click":"Fire",
#    "space": "Jump",
#    "alt-f4":"Exit game",
#    "1":"Switch ammo"
#}
#controls_text = Text(
#                text= "".join(f"{key} = {value}\n" for key,value in controls_dict.items() ),
#                origin=Vec2(2.8, -3),
#                scale=1
#                )
#def cycleAmmo(bullet_tag):  # default bullet tag is int 1
#    if bullet_tag == 1:
#        return 2
#    else:
#        return 1


def input(key):
    if key == ("tab" or "escape"):
        if fullscreen_button.enabled:
            fullscreen_button.disable()
        else:
            fullscreen_button.enable()
    
    if key == "l":
        enemies.append(Zombie(Vec3(0, 1.5, 0), player))


sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))


if __name__ == "__main__":
    app.run(info=False)
