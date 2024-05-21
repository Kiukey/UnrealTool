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
        self.create_max_offset_slider()
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
        self.min_offset_label = QLabel("Minimum offset : 10")
        self.min_offset_slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(self.min_offset_label)
        layout.addWidget(self.min_offset_slider)
        self.layout.addWidget(origin)
        self.min_offset_slider.valueChanged.connect(self.min_offset_changed)
        layout.setSpacing(10)
        self.min_offset_slider.setMinimum(10)
        self.min_offset_slider.setMaximum(1000)
    
    def create_max_offset_slider(self):
        origin = QWidget(self)
        layout = QHBoxLayout(origin)
        self.max_offset_label = QLabel("Maximum offset : 10")
        self.max_offset_slider = QSlider(Qt.Orientation.Horizontal)
        layout.addWidget(self.max_offset_label)
        layout.addWidget(self.max_offset_slider)
        self.layout.addWidget(origin)
        self.max_offset_slider.valueChanged.connect(self.max_offset_changed)
        layout.setSpacing(10)
        self.max_offset_slider.setMinimum(10)
        self.max_offset_slider.setMaximum(1000)

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
    
    def min_offset_changed(self):
        self.min_offset_label.setText(str("Minimum offset : {args1}").format(args1 = self.min_offset_slider.value()))

    def max_offset_changed(self):
        self.max_offset_label.setText(str("Maximum offset : {args1}").format(args1 = self.max_offset_slider.value()))

    def treeNumber_changed(self):
        self.treeNumber_label.setText(str("Tree Number : {args1}").format(args1 = self.treeNumber_slider.value()))

    def create_forest(self):
        sqrNbrTrees = int(sqrt(self.treeNumber_slider.value()))
        actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
        for i in range(sqrNbrTrees):
            for j in range(sqrNbrTrees):
                newPos = unreal.Vector(random.randint(self.min_offset_slider.value(),self.max_offset_slider.value()) * i,random.randint(self.min_offset_slider.value(),self.max_offset_slider.value()) * j,0)
                my_class = unreal.EditorAssetLibrary.load_blueprint_class(self.class_LineEdit.text())
                actor = actor_subsystem.spawn_actor_from_class(my_class,newPos)
                actor.set_folder_path(self.folder_LineEdit.text())
                #unreal.SystemLibrary.box_trace_single() //line trace

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