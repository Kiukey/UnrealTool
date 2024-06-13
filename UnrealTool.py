import unreal
import random
from math import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

class ForestGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.create_folder_lineEdit()
        self.create_class_lineEdit()
        self.create_min_offset_slider()
        self.create_half_extent_slider()
        self.create_TreeNumber_slider()
        self.create_button()
    
    def create_folder_lineEdit(self):
        origin = QWidget(self)
        layout = QHBoxLayout(origin)
        self.folder_label = QLabel("Folder name :")
        self.folder_LineEdit = QLineEdit()
        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_LineEdit)
        self.layout.addWidget(origin)
        layout.setSpacing(10)

    def create_class_lineEdit(self):
        origin = QWidget(self)
        layout = QHBoxLayout(origin)
        self.class_label = QLabel("Class name :")
        self.class_LineEdit = QLineEdit()
        layout.addWidget(self.class_label)
        layout.addWidget(self.class_LineEdit)
        self.layout.addWidget(origin)
        layout.setSpacing(10)

    def create_min_offset_slider(self):
        origin = QWidget(self)
        layout = QHBoxLayout(origin)
        self.offset_label = QLabel("Offset : 10")
        self.offset_slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(self.offset_label)
        layout.addWidget(self.offset_slider)
        self.layout.addWidget(origin)
        self.offset_slider.valueChanged.connect(self.offset_changed)
        layout.setSpacing(10)
        self.offset_slider.setMinimum(10)
        self.offset_slider.setMaximum(1000)
    
    def create_half_extent_slider(self):
        origin = QWidget(self)
        layout = QHBoxLayout(origin)
        self.half_extent_label = QLabel("Half extent : 10")
        self.half_extent_slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(self.half_extent_label)
        layout.addWidget(self.half_extent_slider)
        self.layout.addWidget(origin)
        self.half_extent_slider.valueChanged.connect(self.half_extent_changed)
        layout.setSpacing(10)
        self.half_extent_slider.setMinimum(10)
        self.half_extent_slider.setMaximum(1000)
    
    def create_TreeNumber_slider(self):
        origin1 = QWidget(self)
        layout = QHBoxLayout(origin1)
        self.treeNumber_label = QLabel("Tree Number : 1")
        self.treeNumber_slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(self.treeNumber_label)
        layout.addWidget(self.treeNumber_slider)
        self.layout.addWidget(origin1)
        self.treeNumber_slider.valueChanged.connect(self.treeNumber_changed)
        layout.setSpacing(10)
        self.treeNumber_slider.setMinimum(1)
        self.treeNumber_slider.setMaximum(999)

    def create_button(self):
        self.create_forest_button = QPushButton("Create Forest")
        self.layout.addWidget(self.create_forest_button)
        self.create_forest_button.clicked.connect(self.create_forest)
    
    def offset_changed(self):
        self.offset_label.setText(str("Offset : {args1}").format(args1 = self.offset_slider.value()))

    def half_extent_changed(self):
        self.half_extent_label.setText(str("Half Extent : {args1}").format(args1 = self.half_extent_slider.value()))

    def treeNumber_changed(self):
        self.treeNumber_label.setText(str("Tree Number : {args1}").format(args1 = self.treeNumber_slider.value()))

    # def raycast_position(self,world : unreal.World,vectorPos : unreal.Vector):
    #     startingPos = vectorPos + unreal.Vector(0,0,1000)
    #     endPos = vectorPos + unreal.Vector(0,0,-1000)
    #     unreal.log(startingPos)
    #     unreal.log(endPos)
    #     array = unreal.Array(unreal.Actor)
    #     out_hit = unreal.SystemLibrary.line_trace_single(world,startingPos,endPos,,True,array,unreal.DrawDebugTrace.FOR_ONE_FRAME)
    #     if out_hit == None :
    #         unreal.log("Zob")
    #         return vectorPos
    #     else :
    #         pass
    #    ### unreal.log(out_hit.to_tuple()
    #     unreal.log(out_hit.to_tuple().count()) ###ça sort cb ? 
    #     return vectorPos
        # unreal.SystemLibrary.box_trace_single(unreal.World.get_world,startingPos,endPos,unreal.Vector(100,100,10),)

    def create_forest(self):
        sqrNbrTrees = int(sqrt(self.treeNumber_slider.value()))
        actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        
        my_class = unreal.EditorAssetLibrary.load_blueprint_class(self.class_LineEdit.text())
        for i in range(sqrNbrTrees):
            for j in range(sqrNbrTrees):
                offsetPos = unreal.Vector.random_point_in_box_extents(unreal.Vector(self.offset_slider.value()*i ,self.offset_slider.value()*j,0), unreal.Vector(self.half_extent_slider.value(),self.half_extent_slider.value(),0))
                # offsetPos = unreal.Vector(self.min_offset_slider.value()*i ,self.min_offset_slider.value()*j,0), unreal.Vector(self.max_offset_slider.value(),self.max_offset_slider.value(),0)
                # bpPos = self.raycast_position(unreal.UnrealEditorSubsystem().get_game_world(),offsetPos)
                actor = actor_subsystem.spawn_actor_from_class(my_class,offsetPos)
                actor.set_folder_path(self.folder_LineEdit.text())


    # def create_forest(self):
    #     newPos = unreal.Vector(0,0,0)
    #     half_size_value = (self.max_offset_slider.value() - self.min_offset_slider.value()) /2
    #     half_size = unreal.Vector(half_size_value,half_size_value,0)
    #     actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    #     for i in range(self.treeNumber_slider.value()):
    #         my_class = unreal.EditorAssetLibrary.load_blueprint_class(self.class_LineEdit.text())
    #         actor = actor_subsystem.spawn_actor_from_class(my_class,newPos)
    #         actor.set_folder_path(self.folder_LineEdit.text())
    #         newPos = unreal.Vector.random_point_in_box_extents(unreal.Vector(0,0,0),half_size)

##########################
main = None
if not QApplication.instance():
    main=QApplication()
else:
    main = QApplication.instance()
    
w = ForestGenerator()
w.show()