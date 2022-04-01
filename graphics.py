import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

'''def createMenu(toolbar):

    calculators = toolbar.addMenu("Calculators")

    basic = QAction("&Basic")
    calculators.addAction(basic)

    scientific = QAction("&Scientific")
    calculators.addAction(scientific)

    graphing = QAction("&Graphing")
    calculators.addAction(graphing)'''
def createOptions(text):

    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedHeight(20)
    button.setStyleSheet(
        '''

        * {

            background-color: 'white';
            position: absolute;
            border: 2px solid black;
            border-radius: 10px;

        } 

        *:hover{

            background-color: #DBDBDB;

        }

        '''
    )

    return button


def createNumButton(text):
    # create identical buttons with custom left & right margins
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(50)
    button.setFixedHeight(50)
    button.setStyleSheet(
        '''

    	* {

    		background-color: #FFFFFF;
    		position: absolute;
    		border: 4px solid black;
    		border-radius: 20px;

		} 

		*:hover{

			background-color: #DBDBDB;

		}

		'''
    )

    return button


def createOpButton(text):
    # create identical buttons with custom left & right margins
    button = QPushButton(text)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedHeight(50)
    button.setStyleSheet(
        '''

    	* {

    		background-color: #00AFFF;
    		position: absolute;
    		border: 4px solid black;
    		border-radius: 20px;

		} 

		*:hover{

			background-color: #0083FF;

		}

		'''
    )

    return button