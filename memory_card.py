#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup
from random import shuffle, randint

app = QApplication([])
main_win = QWidget()
main_win.resize(500,300)
main_win.setWindowTitle('Memory Card')
main_win.total_question = 0
main_win.score = 0

'''Форма вопроса'''
question = QLabel('Какой национальности не существует?')

answer_button = QPushButton('Ответить')
group_answers = QGroupBox('Варианты ответов')
button_answer_1 = QRadioButton('Энцы')
button_answer_2 = QRadioButton('Смурфы')
button_answer_3 = QRadioButton('Чулымцы')
button_answer_4 = QRadioButton('Алеуты')
v_line_answers_1 = QVBoxLayout()
v_line_answers_2 = QVBoxLayout()
h_line_answers = QHBoxLayout()

button_group = QButtonGroup()
button_group.addButton(button_answer_1)
button_group.addButton(button_answer_2)
button_group.addButton(button_answer_3)
button_group.addButton(button_answer_4)

v_line_answers_1.addWidget(button_answer_1, alignment=Qt.AlignCenter)
v_line_answers_1.addWidget(button_answer_3, alignment=Qt.AlignCenter)
v_line_answers_2.addWidget(button_answer_2, alignment=Qt.AlignCenter)
v_line_answers_2.addWidget(button_answer_4, alignment=Qt.AlignCenter)

h_line_answers.addLayout(v_line_answers_1)
h_line_answers.addLayout(v_line_answers_2)

group_answers.setLayout(h_line_answers)

'''форма ответа'''
group_2_text_1 = QLabel('Правильно/Неправильно')
group_2_text_2 = QLabel('Правильный ответ')
group_result = QGroupBox('Результат теста')
v_layout = QVBoxLayout()

v_layout.addWidget(group_2_text_1, alignment=(Qt.AlignLeft|Qt.AlignTop))
v_layout.addWidget(group_2_text_2, alignment=Qt.AlignCenter, stretch=2)
group_result.setLayout(v_layout)

group_main_line = QHBoxLayout()
group_main_line.addWidget(group_answers)
group_main_line.addWidget(group_result)

text_line = QHBoxLayout()
text_line.addWidget(question, alignment=Qt.AlignCenter)


button_line = QHBoxLayout()
button_line.addStretch(1)
button_line.addWidget(answer_button, stretch = 2)
button_line.addStretch(1)


main_v_line = QVBoxLayout()
main_v_line.addLayout(text_line)
main_v_line.addStretch(1)
main_v_line.addLayout(group_main_line, stretch = 8)
main_v_line.addStretch(1)
main_v_line.addLayout(button_line)

main_win.setLayout(main_v_line)

class Question():
    def __init__(self, question_class, correct_answer, wrong_question_1, wrong_question_2, wrong_question_3):
        self.question = question_class
        self.correct_answer = correct_answer
        self.wrong_question_1 = wrong_question_1
        self.wrong_question_2 = wrong_question_2
        self.wrong_question_3 = wrong_question_3
    


def show_question():
    button_group.setExclusive(False)
    button_answer_1.setChecked(False)
    button_answer_2.setChecked(False)
    button_answer_3.setChecked(False)
    button_answer_4.setChecked(False)
    button_group.setExclusive(True)
    group_result.hide()
    group_answers.show()
    answer_button.setText('Ответить')


def show_result():
    group_answers.hide()
    group_result.show()
    answer_button.setText('Следующий вопрос')


#group_result.hide()

answers = [button_answer_1,button_answer_2,button_answer_3,button_answer_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.correct_answer)
    answers[1].setText(q.wrong_question_1)
    answers[2].setText(q.wrong_question_2)
    answers[3].setText(q.wrong_question_3)
    question.setText(q.question)
    group_2_text_2.setText('Правильный ответ:  ' + q.correct_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика:', '\n', '-Правильных ответов:', main_win.score, '\nВсего вопросов:', main_win.total_question, '\nРейтинг:', (main_win.score/main_win.total_question)*100,'%')
    else:
        show_correct('Неправильно')
        print('Статистика:', '\n', '-Правильных ответов:', main_win.score, '\nВсего вопросов:', main_win.total_question, '\nРейтинг:', (main_win.score/main_win.total_question)*100,'%')

def show_correct(res):
    group_2_text_1.setText(res)
    show_result()


def next_question():
    main_win.total_question +=1
    print('Статистика:', '\n', '-Правильных ответов:', main_win.score, '\nВсего вопросов:', main_win.total_question)
    q_random = randint(0,len(question_list)-1)
    q = question_list[q_random]
    ask(q)



def click_OK():
    if answer_button.text() == 'Ответить':
        check_answer()
    else:
        next_question()


question_list = list()
q1 = Question('Что ставить после функций?', 'Скобки', 'Точка с запятой', 'Решётка', 'слеш')
question_list.append(q1)
q2 = Question('Выберите элементы bool', 'True, False', '1,2,3', '"Привет мир"', '1.00004')
question_list.append(q2)
q3 = Question('Выбрите то, как нельзя называть переменную', '1вопрос', 'question', 'question_2', 'question123')
question_list.append(q3)
q4 = Question('Как назывался особый головной убор, который носили фараоны в Древнем Египте?', 'Немес', 'Картуз', 'Корона', 'Убрус')
question_list.append(q4)
q5 = Question('Какие огурцы сажал на брезентовом поле герой одноименной песни?', 'Алюминиевые', 'Медные', 'Оловянные', 'Железные')
question_list.append(q5)
q6 = Question('У какого животного самые большие глаза относительно тела?', 'У долгопята', 'У лемура', 'У летучей мыши', 'У тупайи')
question_list.append(q6)
q7 = Question('Какое из этих растений — плотоядное?', 'Росянка', 'Володушка', 'Ромашка', 'Тюльпан')
question_list.append(q7)
q8 = Question('Какая пряность по форме напоминает звездочку?', 'Бадьян', 'Кардамон', 'Корица', 'Гвоздика')
question_list.append(q8)
q9 = Question('С какой головой изображается индуистский бог Ганеша?', 'Слона', 'Орла', 'Крокодила', 'Собаки')
question_list.append(q9)

answer_button.clicked.connect(click_OK)
next_question()

main_win.show()
app.exec_()
