import os
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QScrollArea, QApplication

class RealTimeVisualizer(QWidget):
    def __init__(self, perception, control, prompting, folder):
        super().__init__()
        self.perception = perception
        self.control = control
        self.prompting = prompting

        self.folder = folder

        self.self_close = False

        self.initUI()
        
    def initUI(self):
        self.layout = QVBoxLayout()

        self.API_calls = QScrollArea()
        self.API_calls_label = QLabel("API Calls:")
        self.API_calls.setWidget(self.API_calls_label)
        self.API_calls.setWidgetResizable(True)
        self.API_calls.setMaximumHeight(30)
        self.API_calls_label.setWordWrap(True)

        self.perception_status = QScrollArea()
        self.control_status = QScrollArea()
        perception_status_label = QLabel("Perception Status:")
        control_status_label = QLabel("Control Status:")
        self.perception_status.setWidget(perception_status_label)
        self.control_status.setWidget(control_status_label)
        self.perception_status.setWidgetResizable(True)
        self.control_status.setWidgetResizable(True)
        self.perception_status.setMaximumHeight(50)
        self.control_status.setMaximumHeight(50)
        self.perception_status.setVisible(True)
        self.control_status.setVisible(True)
        perception_status_label.setWordWrap(True)
        control_status_label.setWordWrap(True)

        self.buttons_layout = QVBoxLayout()
        self.button1 = QPushButton("Show Belief Set")
        self.button2 = QPushButton("Show Perception Functions")
        self.button3 = QPushButton("Show Intentions")
        self.button4 = QPushButton("Show Desires")
        self.button5 = QPushButton("Show Intentions Graph")
        self.button6 = QPushButton("Show Memory")
        
        self.button1.clicked.connect(lambda: self.show_widget(self.scroll1))
        self.button2.clicked.connect(lambda: self.show_widget(self.scroll2))
        self.button3.clicked.connect(lambda: self.show_widget(self.scroll3))
        self.button4.clicked.connect(lambda: self.show_widget(self.scroll4))
        self.button5.clicked.connect(lambda: self.show_widget(self.scroll5))
        self.button6.clicked.connect(lambda: self.show_widget(self.scroll6))
        
        self.buttons_layout.addWidget(self.button1)
        self.buttons_layout.addWidget(self.button2)
        self.buttons_layout.addWidget(self.button3)
        self.buttons_layout.addWidget(self.button4)
        self.buttons_layout.addWidget(self.button5)
        self.buttons_layout.addWidget(self.button6)
        
        self.layout.addLayout(self.buttons_layout)

        self.scroll1 = self.create_scrollable_label("Belief Set")
        self.scroll2 = self.create_scrollable_label("Perception Functions")
        self.scroll3 = self.create_scrollable_label("Intentions")
        self.scroll4 = self.create_scrollable_label("Desires")
        self.scroll5 = self.create_scrollable_label("Intentions Graph")
        self.scroll6 = self.create_scrollable_label("Memory")

        self.layout.addWidget(self.API_calls)
        self.layout.addWidget(self.perception_status)
        self.layout.addWidget(self.control_status)
        self.layout.addWidget(self.scroll1)
        self.layout.addWidget(self.scroll2)
        self.layout.addWidget(self.scroll3)
        self.layout.addWidget(self.scroll4)
        self.layout.addWidget(self.scroll5)
        self.layout.addWidget(self.scroll6)
        
        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_labels)
        self.timer.start(1000)

        self.setWindowTitle(self.folder.split("/")[-1])
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
        self.scroll6.setVisible(False)
        widget.setVisible(True)

    def update_labels(self):
        api_calls = self.prompting.get_printable_estimate()
        perception_status = self.perception.status
        control_status = self.control.status

        self.API_calls_label.setText(f"API Calls: {api_calls}")
        self.perception_status.widget().setText(f"Perception Status: {perception_status}")
        self.control_status.widget().setText(f"Control Status: {control_status}")

        var1_value = self.perception.get_printable_belief_set()
        var2_value = self.perception.manager.get_printable_functions()
        var3_value = self.control.manager.get_printable_intentions()
        var4_value = self.control.manager.get_printable_desires()
        var5_value = self.control.manager.get_printable_intentions_graph()
        var6_value = self.control.get_printable_memory()

        self.scroll1.widget().setText(f"{var1_value}")
        self.scroll2.widget().setText(f"{var2_value}")
        self.scroll3.widget().setText(f"{var3_value}")
        self.scroll4.widget().setText(f"{var4_value}")
        self.scroll5.widget().setText(f"{var5_value}")
        self.scroll6.widget().setText(f"{var6_value}")

        if self.self_close:
            os.makedirs(f"{self.folder}/result", exist_ok=True)
            with open(f"{self.folder}/result/api_calls.txt", "w") as f:
                f.write(str(api_calls))
                f.close()
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
            with open(f"{self.folder}/result/memory.txt", "w") as f:
                f.write(var6_value)
                f.close()
                
            all, all_working, all_not_working, intentions, working_intentions, not_working_intentions = self.control.manager.get_analyzable_intentions_functions()
            with open(f"{self.folder}/result/analyzable_IF.py", "w") as f:
                f.write(all)
                f.close()
            with open(f"{self.folder}/result/analyzable_IF_W.py", "w") as f:
                f.write(all_working)
                f.close()
            with open(f"{self.folder}/result/analyzable_IF_NW.py", "w") as f:
                f.write(all_not_working)
                f.close()
            os.makedirs(f"{self.folder}/result/analyzable_IF_S", exist_ok=True)
            for key, value in intentions.items():
                with open(f"{self.folder}/result/analyzable_IF_S/{key}.py", "w") as f:
                    f.write(value)
                    f.close()
            os.makedirs(f"{self.folder}/result/analyzable_IF_W_S", exist_ok=True)
            for key, value in working_intentions.items():
                with open(f"{self.folder}/result/analyzable_IF_W_S/{key}.py", "w") as f:
                    f.write(value)
                    f.close()
            os.makedirs(f"{self.folder}/result/analyzable_IF_NW_S", exist_ok=True)
            for key, value in not_working_intentions.items():
                with open(f"{self.folder}/result/analyzable_IF_NW_S/{key}.py", "w") as f:
                    f.write(value)
                    f.close()
            
            string, dictionary = self.control.manager.get_analyzable_desires_trigger_functions()
            with open(f"{self.folder}/result/analyzable_DTF.py", "w") as f:
                f.write(string)
                f.close()
            os.makedirs(f"{self.folder}/result/analyzable_DTF_S", exist_ok=True)
            for key, value in dictionary.items():
                with open(f"{self.folder}/result/analyzable_DTF_S/{key}.py", "w") as f:
                    f.write(value)
                    f.close()
            
            string, dictionary = self.perception.manager.get_analyzable_perception_functions()
            with open(f"{self.folder}/result/analyzable_PF.py", "w") as f:
                f.write(string)
                f.close()
            os.makedirs(f"{self.folder}/result/analyzable_PF_S", exist_ok=True)
            for key, value in dictionary.items():
                with open(f"{self.folder}/result/analyzable_PF_S/{key}.py", "w") as f:
                    f.write(value)
                    f.close()
            
            desire_steps = []
            intention_steps = []
            number_api_calls = []
            number_desires_working = []
            number_desires_not_working = []
            number_intentions_working = []
            number_intentions_not_working = []
            number_perception_functions = []

            desire_steps.append(self.control.desire_steps)
            intention_steps.append(self.control.intention_steps)
            number_api_calls.append(self.prompting.get_requests_made())
            working, not_working = self.control.manager.get_number_desires()
            number_desires_working.append(working)
            number_desires_not_working.append(not_working)
            working, not_working = self.control.manager.get_number_intentions()
            number_intentions_working.append(working)
            number_intentions_not_working.append(not_working)
            number_perception_functions.append(self.perception.manager.get_number_perception_functions())

            with open(f"{self.folder}/result/evolution_steps.txt", "w") as f:
                f.write(str(desire_steps) + "\n")
                f.write(str(intention_steps) + "\n")
                f.write(str(number_api_calls) + "\n")
                f.write(str(number_desires_working) + "\n")
                f.write(str(number_desires_not_working) + "\n")
                f.write(str(number_intentions_working) + "\n")
                f.write(str(number_intentions_not_working) + "\n")
                f.write(str(number_perception_functions) + "\n")
                f.close()
            
            self.timer.stop()
            self.close()
