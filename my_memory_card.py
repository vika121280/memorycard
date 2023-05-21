#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QRadioButton, QButtonGroup, QGroupBox, QVBoxLayout, QHBoxLayout, QMessageBox
)
from random import shuffle
app = QApplication([])
window = QWidget()


Lbl_question = QLabel('Сколько месяцев в году имеют 28 дней?')
rbtn_1 = QRadioButton('Ни один')
rbtn_2 = QRadioButton('Два')
rbtn_3 = QRadioButton('Все')
rbtn_4 = QRadioButton('Шесть')
btn_next = QPushButton('Ответить')
grpbox_answers = QGroupBox('Ответы')
lbl_result = QLabel('Вы правильно ответили')
grpbox_result = QGroupBox('Результат')
lbl_right_answer = QLabel('Все')

btn_group = QButtonGroup()
btn_group.addButton(rbtn_1)
btn_group.addButton(rbtn_2)
btn_group.addButton(rbtn_3)
btn_group.addButton(rbtn_4)
v_result = QVBoxLayout()
v_result.addWidget(lbl_result)
v_result.addWidget(lbl_right_answer)

grpbox_result.setLayout(v_result)
grpbox_result.hide()

v_main = QVBoxLayout()
h_main_1 = QHBoxLayout()
h_main_2 = QHBoxLayout()
h_main_3 = QHBoxLayout()

h_grpbox = QHBoxLayout()
v_grpbox_1 = QVBoxLayout()
v_grpbox_2 = QVBoxLayout()

h_main_1.addWidget(Lbl_question)
h_main_2.addWidget(grpbox_answers)
h_main_2.addWidget(grpbox_result)
h_main_3.addWidget(btn_next)

v_grpbox_1.addWidget(rbtn_1)
v_grpbox_1.addWidget(rbtn_2)
v_grpbox_2.addWidget(rbtn_3)
v_grpbox_2.addWidget(rbtn_4)

h_grpbox.addLayout(v_grpbox_1)
h_grpbox.addLayout(v_grpbox_2)

v_main.addLayout(h_main_1)
v_main.addLayout(h_main_2)
v_main.addLayout(h_main_3)

grpbox_answers.setLayout(h_grpbox)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

cur_question = 0
score = 0
buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [
    Question('Сколько месяцев в году имеют 28 дней?', 'Все', 'Два', 'Ни один', 'Шесть'),
    Question('Сколько сегодня градусов?', '10', '-100', '-196', '500'),
    Question('Сколько лет Софье?', '14', '2', '15', '16'),
    Question('Какой рост у Софьи?', '173', '160', '159','170' ),
    Question('Какой у Софьи любимый спорт?', 'баскетбол', 'волейбол', 'каратэ', 'плавание')
]
def get_procent(score):
    procent = score/len(questions)*100
    procent = round(procent, 1)
    result = 'Вы ответили на ' + str(score)
    result += ' вопросов из ' + str(len(questions)) + '\n'
    result += 'Процент верных ответов:' + str(procent) + '%'
    return(result)

def next_question():
    global cur_question
    cur_question += 1
    if cur_question >= len(questions):
        msg = QMessageBox()
        msg.setText(get_procent(score))
        msg.setWindowTitle('Результат')
        msg.exec()
        cur_question = 0
    ask(questions[cur_question])

def ask(q):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)
    Lbl_question.setText(q.question)
    lbl_right_answer.setText('Правильный ответ: '+  q.right_answer)
    show_question()



def show_result():
    if all_checked():    
        if buttons[0].isChecked():
            global score
            score += 1
            lbl_result.setText('Вы ответили правильно')
        else:
            lbl_result.setText('Вы ответили неправильно')
        grpbox_answers.hide()
        grpbox_result.show()
        btn_next.setText('Следующий вопрос')

def show_question():
    grpbox_answers.show()
    grpbox_result.hide()
    btn_next.setText('Ответить')
    btn_group.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    btn_group.setExclusive(True)

def all_checked():
    flag = False
    for btn in buttons:
        if btn.isChecked():
            flag = True
    return flag


def click_next():
    if btn_next.text() == 'Ответить':
        show_result()
    else:
        next_question()
btn_next.clicked.connect(click_next)
window.setLayout(v_main)
shuffle(questions)
print(cur_question)
ask(questions[cur_question]) 
window.show()
app.exec()

