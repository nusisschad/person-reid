from PyQt5.QtCore import Qt, pyqtSlot, QVariant
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QScrollArea, QHBoxLayout, QVBoxLayout, QWidget
import os
import datetime

class ReidentificationPanelWidget(QScrollArea):
    def __init__(self, parent=None):
        super(ReidentificationPanelWidget, self).__init__(parent)
        widget = QWidget()
        self.layout = QVBoxLayout(widget)
        self.layout.setAlignment(Qt.AlignTop)
        
        self.input_dir_path = os.path.join(os.path.dirname(__file__), '../keyframe_output')
        
        self.setWidget(widget)
        self.setWidgetResizable(True)
        
    @pyqtSlot(int, int, str)
    def add_new_person(self, person_id, keyframe_id, matching_image_path):        
        person_layout = QVBoxLayout()
        person_layout.addWidget(QLabel('Person %02d' % person_id))
        
        face_keyframe_path = os.path.join(self.input_dir_path, str(keyframe_id) + '.png')
        
        face_keyframe_match_layout = QHBoxLayout()

        keyframe_pixmap = QPixmap(face_keyframe_path)
        label_image = QLabel()
        label_image.setPixmap(keyframe_pixmap)
        face_keyframe_match_layout.addWidget(label_image)
        
        matched_pixmap = QPixmap(matching_image_path)
        label_image = QLabel()
        label_image.setPixmap(matched_pixmap)
        face_keyframe_match_layout.addWidget(label_image)

        person_layout.addLayout(face_keyframe_match_layout)

        curr_datetime = str(datetime.datetime.now())
        person_layout.addWidget(QLabel('Keyframe ID %02d on %s' % (keyframe_id, curr_datetime)))

        self.layout.addLayout(person_layout)