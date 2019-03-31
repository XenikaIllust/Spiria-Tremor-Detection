from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def setup_questionnaire_screen(self):
    questionnaire_layout_widget = QWidget(self.questionnaire_screen)
    questionnaire_layout_widget.setGeometry(self.frame.geometry())

    questionnaire_layout = QVBoxLayout(questionnaire_layout_widget)

    questionnaire_title = QLineEdit(questionnaire_layout_widget)
    questionnaire_title.setObjectName("questionnaire_title")
    questionnaire_title.setText("Questionnaire")
    questionnaire_title.setReadOnly(True)
    questionnaire_layout.addWidget(questionnaire_title)

    question1_layout = QVBoxLayout()
    questionnaire_layout.addLayout(question1_layout)

    question1_text = QLineEdit(questionnaire_layout_widget)
    question1_text.setObjectName("question1")
    question1_text.setText("1. Do you think you have a tremor?")
    question1_text.setReadOnly(True)
    question1_layout.addWidget(question1_text)

    question1_buttonlayout = QHBoxLayout(questionnaire_layout_widget)
    questionnaire_layout.addLayout(question1_buttonlayout)

    question1_button0 = QRadioButton()
    question1_button0.setText("Yes")
    question1_button0.setChecked(False)

    question1_button1 = QRadioButton()
    question1_button1.setText("Unsure")
    question1_button1.setChecked(False)

    question1_button2 = QRadioButton()
    question1_button2.setText("No")
    question1_button2.setChecked(True)

    question1_buttonlayout.addWidget(question1_button0)
    question1_buttonlayout.addWidget(question1_button1)
    question1_buttonlayout.addWidget(question1_button2)

    question2_layout = QVBoxLayout()
    questionnaire_layout.addLayout(question2_layout)

    question2_text = QLineEdit(questionnaire_layout_widget)
    question2_text.setObjectName("question2")
    question2_text.setText("2. If you have a tremor, is it worse when writing or using utensils?")
    question2_text.setReadOnly(True)
    question2_layout.addWidget(question2_text)

    question2_buttonlayout = QHBoxLayout(questionnaire_layout_widget)
    questionnaire_layout.addLayout(question2_buttonlayout)

    question2_button0 = QRadioButton()
    question2_button0.setText("Yes")
    question2_button0.setChecked(False)

    question2_button1 = QRadioButton()
    question2_button1.setText("Unsure")
    question2_button1.setChecked(False)

    question2_button2 = QRadioButton()
    question2_button2.setText("No")
    question2_button2.setChecked(True)

    question2_buttonlayout.addWidget(question2_button0)
    question2_buttonlayout.addWidget(question2_button1)
    question2_buttonlayout.addWidget(question2_button2)

    question3_layout = QVBoxLayout()
    questionnaire_layout.addLayout(question3_layout)

    question3_text = QLineEdit(questionnaire_layout_widget)
    question3_text.setObjectName("question3")
    question3_text.setText("3. Is tremor worse when resting arm?")
    question3_text.setReadOnly(True)
    question3_layout.addWidget(question3_text)

    question3_buttonlayout = QHBoxLayout(questionnaire_layout_widget)
    questionnaire_layout.addLayout(question3_buttonlayout)

    question3_button0 = QRadioButton()
    question3_button0.setText("Yes")
    question3_button0.setChecked(False)

    question3_button1 = QRadioButton()
    question3_button1.setText("Unsure")
    question3_button1.setChecked(False)

    question3_button2 = QRadioButton()
    question3_button2.setText("No")
    question3_button2.setChecked(True)

    question3_buttonlayout.addWidget(question3_button0)
    question3_buttonlayout.addWidget(question3_button1)
    question3_buttonlayout.addWidget(question3_button2)

    question4_layout = QVBoxLayout()
    questionnaire_layout.addLayout(question4_layout)

    question4_text = QLineEdit(questionnaire_layout_widget)
    question4_text.setObjectName("question4")
    question4_text.setText("4. Have you/anyone noticed slowness of movement or walking?")
    question4_text.setReadOnly(True)
    question4_layout.addWidget(question4_text)

    question4_buttonlayout = QHBoxLayout(questionnaire_layout_widget)
    questionnaire_layout.addLayout(question4_buttonlayout)

    question4_button0 = QRadioButton()
    question4_button0.setText("Yes")
    question4_button0.setChecked(False)

    question4_button1 = QRadioButton()
    question4_button1.setText("No")
    question4_button1.setChecked(True)

    question4_buttonlayout.addWidget(question4_button0)
    question4_buttonlayout.addWidget(question4_button1)

    question5_layout = QVBoxLayout()
    questionnaire_layout.addLayout(question5_layout)

    question5_text = QLineEdit(questionnaire_layout_widget)
    question5_text.setObjectName("question5")
    question5_text.setText("5. Has anyone noticed you acting out your dreams in sleep?")
    question5_text.setReadOnly(True)
    question5_layout.addWidget(question5_text)

    question5_buttonlayout = QHBoxLayout(questionnaire_layout_widget)
    questionnaire_layout.addLayout(question5_buttonlayout)

    question5_button0 = QRadioButton()
    question5_button0.setText("Yes")
    question5_button0.setChecked(False)

    question5_button1 = QRadioButton()
    question5_button1.setText("No")
    question5_button1.setChecked(True)

    question5_buttonlayout.addWidget(question5_button0)
    question5_buttonlayout.addWidget(question5_button1)

    question6_layout = QVBoxLayout()
    questionnaire_layout.addLayout(question6_layout)

    question6_text = QLineEdit(questionnaire_layout_widget)
    question6_text.setObjectName("question6")
    question6_text.setText("6. Do you have constipation?")
    question6_text.setReadOnly(True)
    question6_layout.addWidget(question6_text)

    question6_buttonlayout = QHBoxLayout(questionnaire_layout_widget)
    questionnaire_layout.addLayout(question6_buttonlayout)

    question6_button0 = QRadioButton()
    question6_button0.setText("Yes")
    question6_button0.setChecked(False)

    question6_button1 = QRadioButton()
    question6_button1.setText("No")
    question6_button1.setChecked(True)

    question6_buttonlayout.addWidget(question6_button0)
    question6_buttonlayout.addWidget(question6_button1)