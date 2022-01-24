from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject
import os
from direct.task import Task
from panda3d.core import CollisionRay, CollisionNode, CollideMask
from pandac.PandaModules import WindowProperties
class MyApp(ShowBase):
    def __init__(self):
        #camera angle view
        Yaw = 0
        Pitch = 0
        Roll = 40
        #keys
        self.keyMap = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "shoot": False,
            "l": False,
            "p": False,
            "e": False
        }
        ShowBase.__init__(self)
        Yaw = 0
        Pitch = 0
        Roll = 0
        #disable mouse
        self.disableMouse()
        #move camera
        #base.cam.setPos(-10,0,0)
        #load the 3d player
        self.player = self.loader.loadModel("head.bam")
        #reparent it to render so it actually gets rendered
        self.player.reparentTo(self.render)
        self.player.setScale(0.25, 0.25, 0.25)
        self.player.setPos(-8, 42, 0)
        self.scene = self.loader.loadModel("models/environment")
        # reparent it to render so it actually gets rendered
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        self.accept("w", self.updateKeyMap, ["up", True])
        self.accept("w-up", self.updateKeyMap, ["up", False])
        self.accept("s", self.updateKeyMap, ["down", True])
        self.accept("s-up", self.updateKeyMap, ["down", False])
        self.accept("a", self.updateKeyMap, ["left", True])
        self.accept("a-up", self.updateKeyMap, ["left", False])
        self.accept("d", self.updateKeyMap, ["right", True])
        self.accept("d-up", self.updateKeyMap, ["right", False])
        self.accept("mouse1", self.updateKeyMap, ["shoot", True])
        self.accept("mouse1-up", self.updateKeyMap, ["shoot", False])
        self.accept("l", self.updateKeyMap, ["l", True])
        self.accept("l-up", self.updateKeyMap, ["l", False])
        self.accept("p", self.updateKeyMap, ["p", True])
        self.accept("p-up", self.updateKeyMap, ["p", False])
        self.accept("e", self.updateKeyMap, ["e", True])
        self.accept("e-up", self.updateKeyMap, ["e", False])
        self.updateTask = taskMgr.add(self.moveplayer, "update")
        self.eyesTask=taskMgr.add(self.eyes, "eyes", extraArgs=[Yaw,Pitch,Roll], appendTask=True)
    def eyes(self,Yaw,Pitch,Roll,task):
        playerpos=self.player.getPos()
        self.cam.setPos(playerpos.getX(),playerpos.getY()-60,playerpos.getZ()+15)
        mw = self.mouseWatcherNode
        campos=base.cam.getPos()
        if mw.hasMouse():
            x = mw.getMouseX()
            y = mw.getMouseY()
            props = self.win.getProperties()
            self.win.movePointer(0, props.getXSize() // 2, props.getYSize() // 2)
            if(x>0):
                Yaw=Yaw+1
            elif(x==0):
                Yaw=Yaw
            else:
                Yaw=Yaw-1
        print(Yaw, Pitch, Roll)
        self.cam.setHpr(Yaw, Pitch, Roll)
        self.player.setH(self.player,Yaw)
        self.player.setP(self.player, Pitch)
        self.player.setR(self.player, Roll)
        return task.cont
    def updateKeyMap(self, controlName, controlState):
        self.keyMap[controlName] = controlState
        print(controlName,controlState)
    def moveplayer(self,task):
        if(self.keyMap["up"]==True):
            self.goforward(task)
        if(self.keyMap["down"] == True):
            self.goback(task)
        if(self.keyMap["left"] == True):
            self.goleft(task)
        if(self.keyMap["right"] == True):
            self.goright(task)
        if(self.keyMap["l"] == True):
            self.godown(task)
        if (self.keyMap["p"] == True):
            self.goup(task)
        if (self.keyMap["e"] == True):
            self.escape()
        if (self.keyMap["shoot"] == True):
            self.lock()
        return task.cont
    def lock(self):
        props = WindowProperties()
        props.setCursorHidden(True)
        props.setMouseMode(WindowProperties.M_absolute)
        self.win.requestProperties(props)
    def escape(self):
        props = WindowProperties()
        props.setCursorHidden(False)
        props.setMouseMode(WindowProperties.M_absolute)
        self.win.requestProperties(props)
    def goleft(self,task):
        pos=self.player.getPos()
        x=pos.getX()
        y=pos.getY()
        z=pos.getZ()
        self.player.setPos(x-1,y,z)
    def goright(self,task):
        pos=self.player.getPos()
        x=pos.getX()
        y=pos.getY()
        z=pos.getZ()
        self.player.setPos(x+1,y,z)
    def goforward(self,task):
        pos=self.player.getPos()
        x=pos.getX()
        y=pos.getY()
        z=pos.getZ()
        self.player.setPos(x,y+1,z)
    def goback(self,task):
        pos=self.player.getPos()
        x=pos.getX()
        y=pos.getY()
        z=pos.getZ()
        self.player.setPos(x,y-1,z)
    def goup(self,task):
        pos=self.player.getPos()
        x=pos.getX()
        y=pos.getY()
        z=pos.getZ()
        self.player.setPos(x,y,z+1)
    def godown(self,task):
        pos=self.player.getPos()
        x=pos.getX()
        y=pos.getY()
        z=pos.getZ()
        self.player.setPos(x,y,z-1)
app = MyApp()
app.run()