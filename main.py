import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from graphics import createNumButton, createOpButton, createOptions
from functionality import doOperation, setOperator, setValue, clear, remove
from PyQt5 import QtCore

def setWindow():
    global cur_operator, grid

    '''tool_bar = QMenuBar()
    grid.addWidget(tool_bar, 0, 0, 1, 4)
    tool_bar.setStyleSheet("width: 100%; background-color: 'white';")
    createMenu(tool_bar)'''
    '''button_scientific = createOptions("Scientific")
    grid.addWidget(button_scientific, 0, 0, 1, 2)

    button_graph = createOptions("Graphing")
    grid.addWidget(button_graph, 0, 2, 1, 2)'''

    result = QLabel("0")
    result.setStyleSheet(
        '''

    	* {

    		background-color: #DBDBDB;
    		border: 4px solid black;
    		border-radius: 20px;

		} 

		'''
    )
    result.setAlignment(Qt.AlignCenter)
    grid.addWidget(result, 1, 0, 1, 3)

    button1 = createNumButton("1")
    grid.addWidget(button1, 2, 0, 1, 1)

    button2 = createNumButton("2")
    grid.addWidget(button2, 2, 1, 1, 1)

    button3 = createNumButton("3")
    grid.addWidget(button3, 2, 2, 1, 1)

    button4 = createNumButton("4")
    grid.addWidget(button4, 3, 0, 1, 1)

    button5 = createNumButton("5")
    grid.addWidget(button5, 3, 1, 1, 1)

    button6 = createNumButton("6")
    grid.addWidget(button6, 3, 2, 1, 1)

    button7 = createNumButton("7")
    grid.addWidget(button7, 4, 0, 1, 1)

    button8 = createNumButton("8")
    grid.addWidget(button8, 4, 1, 1, 1)

    button9 = createNumButton("9")
    grid.addWidget(button9, 4, 2, 1, 1)

    button0 = createNumButton("0")
    grid.addWidget(button0, 5, 0, 1, 1)

    button_clear = createOpButton("C")
    grid.addWidget(button_clear, 5, 1, 1, 2)

    button_rm = createOpButton("<<")
    grid.addWidget(button_rm, 1, 3, 1, 1)

    button_add = createOpButton("+")
    grid.addWidget(button_add, 2, 3, 1, 1)

    button_sub = createOpButton("-")
    grid.addWidget(button_sub, 3, 3, 1, 1)

    button_mult = createOpButton("*")
    grid.addWidget(button_mult, 4, 3, 1, 1)

    button_div = createOpButton("/")
    grid.addWidget(button_div, 5, 3, 1, 1)

    button_equal = createOpButton("=")
    grid.addWidget(button_equal, 6, 0, 1, 4)

    button1.clicked.connect(lambda x: setValue(1, result))
    button2.clicked.connect(lambda x: setValue(2, result))
    button3.clicked.connect(lambda x: setValue(3, result))
    button4.clicked.connect(lambda x: setValue(4, result))
    button5.clicked.connect(lambda x: setValue(5, result))
    button6.clicked.connect(lambda x: setValue(6, result))
    button7.clicked.connect(lambda x: setValue(7, result))
    button8.clicked.connect(lambda x: setValue(8, result))
    button9.clicked.connect(lambda x: setValue(9, result))
    button0.clicked.connect(lambda x: setValue(0, result))
    button_add.clicked.connect(lambda x: setOperator("add"))
    button_sub.clicked.connect(lambda x: setOperator("sub"))
    button_mult.clicked.connect(lambda x: setOperator("mult"))
    button_div.clicked.connect(lambda x: setOperator("div"))
    button_equal.clicked.connect(lambda x: doOperation(result))
    button_clear.clicked.connect(lambda x: clear(result))
    button_rm.clicked.connect(lambda x: remove(result))

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Calculator")
window.setWindowIcon(QIcon("bad.ico"))
window.setFixedWidth(250)
window.setFixedHeight(400)

grid = QGridLayout()

window.setStyleSheet(
    "background: #373737;")

setWindow()

window.setLayout(grid)

window.show()
sys.exit(app.exec())
