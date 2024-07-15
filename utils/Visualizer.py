import os
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QScrollArea, QApplication

class RealTimeVisualizer(QWidget):
    def __init__(self, perception, control, folder):
        super().__init__()
        self.perception = perception
        self.control = control

        self.folder = folder

        self.self_close = False

        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout()

        self.buttons_layout = QVBoxLayout()
        self.button1 = QPushButton("Show Belief Set")
        self.button2 = QPushButton("Show Perception Functions")
        self.button3 = QPushButton("Show Intentions")
        self.button4 = QPushButton("Show Desires")
        self.button5 = QPushButton("Show Intentions Graph")
        
        self.button1.clicked.connect(lambda: self.show_widget(self.scroll1))
        self.button2.clicked.connect(lambda: self.show_widget(self.scroll2))
        self.button3.clicked.connect(lambda: self.show_widget(self.scroll3))
        self.button4.clicked.connect(lambda: self.show_widget(self.scroll4))
        self.button5.clicked.connect(lambda: self.show_widget(self.scroll5))
        
        self.buttons_layout.addWidget(self.button1)
        self.buttons_layout.addWidget(self.button2)
        self.buttons_layout.addWidget(self.button3)
        self.buttons_layout.addWidget(self.button4)
        self.buttons_layout.addWidget(self.button5)
        
        self.layout.addLayout(self.buttons_layout)

        self.scroll1 = self.create_scrollable_label("Belief Set")
        self.scroll2 = self.create_scrollable_label("Perception Functions")
        self.scroll3 = self.create_scrollable_label("Intentions")
        self.scroll4 = self.create_scrollable_label("Desires")
        self.scroll5 = self.create_scrollable_label("Intentions Graph")

        self.layout.addWidget(self.scroll1)
        self.layout.addWidget(self.scroll2)
        self.layout.addWidget(self.scroll3)
        self.layout.addWidget(self.scroll4)
        self.layout.addWidget(self.scroll5)
        
        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_labels)
        self.timer.start(500)

        self.setWindowTitle('Real-Time Variable Visualizer')
        self.show()
        
        self.show_widget(self.scroll1)  # Show the first widget by default

    def create_scrollable_label(self, text):
        scroll = QScrollArea()
        label = QLabel(text)
        label.setWordWrap(True)
        scroll.setWidget(label)
        scroll.setWidgetResizable(True)
        scroll.setVisible(False)
        return scroll

    def show_widget(self, widget):
        self.scroll1.setVisible(False)
        self.scroll2.setVisible(False)
        self.scroll3.setVisible(False)
        self.scroll4.setVisible(False)
        self.scroll5.setVisible(False)
        widget.setVisible(True)

    def update_labels(self):
        var1_value = self.perception.get_printable_belief_set()
        var2_value = self.perception.manager.get_printable_functions()
        var3_value = self.control.manager.get_printable_intentions()
        var4_value = self.control.manager.get_printable_desires()
        var5_value = self.control.manager.get_printable_intentions_graph()

        self.scroll1.widget().setText(f"Belief Set: {var1_value}")
        self.scroll2.widget().setText(f"Perception Functions: {var2_value}")
        self.scroll3.widget().setText(f"Intentions: {var3_value}")
        self.scroll4.widget().setText(f"Desires: {var4_value}")
        self.scroll5.widget().setText(f"Intentions Graph: {var5_value}")

        if self.self_close:
            os.makedirs(f"{self.folder}/result", exist_ok=True)
            with open(f"{self.folder}/result/belief_set.txt", "w") as f:
                f.write(var1_value)
                f.close()
            with open(f"{self.folder}/result/perception_functions.txt", "w") as f:
                f.write(var2_value)
                f.close()
            with open(f"{self.folder}/result/intentions.txt", "w") as f:
                f.write(var3_value)
                f.close()
            with open(f"{self.folder}/result/desires.txt", "w") as f:
                f.write(var4_value)
                f.close()
            with open(f"{self.folder}/result/intentions_graph.txt", "w") as f:
                f.write(var5_value)
                f.close()
            self.timer.stop()
            self.close()
