"""
Tombala Game Driver Code

@file: Driver.py
@author: Uğur Çankaya
@date: June 3, 2020
@brief: Tombala Game with Qt Designer and Python

OBJECT-ORIENTED PROGRAMMING II Project
Eskişehir Osmangazi University Electrical and Electronics Engineering https://eee.ogu.edu.tr/en

"""

from PyQt5 import QtWidgets
from Design import Ui_Form #"Design" making gui design py file
from Player import *
import sys

class mywindow(QtWidgets.QWidget):
	
	def __init__(self):
		
		super(mywindow,self).__init__()
		self.ui=Ui_Form()
		self.ui.setupUi(self)

app=QtWidgets.QApplication([])

application = mywindow()
application.show()

sys.exit(app.exec())
	
