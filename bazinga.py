'''
All stuff related to Big Bang Theory property of HBO INC
Spock property of CBS STUDIOS INC

dev = [Percival]
me.dividesbyzero@gmail.com

'''
import imagess
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtGui import QPixmap
from random import choice
import sys
from playsound import playsound

options = ['ROCK', 'SCISSORS', 'PAPER', 'LIZARD', 'SPOCK']

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()        
        uic.loadUi('window.ui', self) 
        self.show()
        self.rules = rules()                     
                
        self.user_choice = 0
        
        self.spock_btn.clicked.connect(self.spock)
        self.paper_btn.clicked.connect(self.paper) 
        self.scissors_btn.clicked.connect(self.scissors) 
        self.rock_btn.clicked.connect(self.rock) 
        self.lizard_btn.clicked.connect(self.lizard)

        self.rules_btn.clicked.connect(self.rules.show)
        self.rules_btn.clicked.connect(self.bazinga)

    def spock(self):
        self.user_choice = 'SPOCK'
        self.gameplay()               

    def paper(self):
        self.user_choice = 'PAPER'
        self.gameplay()  

    def scissors(self):
        self.user_choice = 'SCISSORS'
        self.gameplay()  

    def rock(self):
        self.user_choice = "ROCK"
        self.gameplay()  

    def lizard(self):
        self.user_choice = 'LIZARD'
        self.gameplay()

    def gameplay(self):

        global phrase
        global result
        phrase = result = 0
               
        self.crew()

        computer_choice = choice(options)
        

        # GOD BLESS THIS MESS

        if computer_choice == 'ROCK' and self.user_choice in ['LIZARD', 'SCISSORS']:
            result = 'I WON !!'
            match self.user_choice:
                case 'LIZARD':
                    phrase = 'ROCK CRUSHES LIZARD !'
                case 'SCISSORS':
                    phrase = 'ROCK CRUSHES SCISSORS !'

        elif computer_choice == 'SCISSORS' and self.user_choice in ['PAPER', 'LIZARD']:
            result = 'I WON !!'
            match self.user_choice:
                case 'PAPER':
                    phrase = 'SCISSORS CUTS PAPER !'
                case 'LIZARD':
                    phrase = 'SCISSORS DECAPITATES LIZARD !'

        elif computer_choice == 'PAPER' and self.user_choice in ['ROCK', 'SPOCK']:
            result = 'I WON !!'
            match self.user_choice:
                case 'ROCK':
                    phrase = 'PAPER COVERS ROCK !'
                case 'SPOCK':
                    phrase = 'PAPER DISPROVES SPOCK !'

        elif computer_choice == 'LIZARD' and self.user_choice in ['PAPER', 'SPOCK']:
            result = 'I WON !!'
            match self.user_choice:
                case 'PAPER':
                    phrase = 'LIZARD EATS PAPER !'
                case 'SPOCK':
                    phrase = 'LIZARD POISONS SPOCK !'

        elif computer_choice == 'SPOCK' and self.user_choice in ['ROCK', 'SCISSORS']:
            result = 'I WON !!'
            match self.user_choice:
                case 'ROCK':
                    phrase = 'SPOCK VAPORIZES ROCK !'
                case 'SCISSORS':
                    phrase = 'SPOCK SMASHES SCISSORS !'

        elif computer_choice == self.user_choice:
            result = "IT'S A TIE !!"
            phrase = 'TRY AGAIN !'

        else:
            result = 'YOU WON !!!!!'


        if self.user_choice == 'ROCK' and computer_choice in ['LIZARD', 'SCISSORS']:
            match computer_choice:
                case 'LIZARD':
                    phrase = 'ROCK CRUSHES LIZARD !'
                case 'SCISSORS':
                    phrase = 'ROCK CRUSHES SCISSORS !'

        elif self.user_choice == 'SCISSORS' and computer_choice in ['PAPER', 'LIZARD']:
            match computer_choice:
                case 'PAPER':
                    phrase = 'SCISSORS CUTS PAPER !'
                case 'LIZARD':
                    phrase = 'SCISSORS DECAPITATES LIZARD !'

        elif self.user_choice == 'PAPER' and computer_choice in ['ROCK', 'SPOCK']:
            match computer_choice:
                case 'ROCK':
                    phrase = 'PAPER COVERS ROCK !'
                case 'SPOCK':
                    phrase = 'PAPER DISPROVES SPOCK !'

        elif self.user_choice == 'LIZARD' and computer_choice in ['PAPER', 'SPOCK']:
            match computer_choice:
                case 'PAPER':
                    phrase = 'LIZARD EATS PAPER !'
                case 'SPOCK':
                    phrase = 'LIZARD POISONS SPOCK !'

        elif self.user_choice == 'SPOCK' and computer_choice in ['ROCK', 'SCISSORS']:
            match computer_choice:
                case 'ROCK':
                    phrase = 'SPOCK VAPORIZES ROCK !'
                case 'SCISSORS':
                    phrase = 'SPOCK SMASHES SCISSORS !'

            
        user = self.user_choice
        pixmap = QPixmap(f'{user}' + '.png')
        self.user_pic.setPixmap(pixmap)

        pc = computer_choice
        pixmap = QPixmap(f'{pc}' + '.png')
        self.pc_pic.setPixmap(pixmap)

        self.result_label.setText(result)

        self.phrase_label.setText(f'{phrase}')
    
        

    def bazinga(self):
        playsound('bazinga.mp3')

    def crew(self):
        playsound('gameplay.mp3')


class rules(QtWidgets.QMainWindow):
    def __init__(self):
        super(rules, self).__init__()        
        uic.loadUi('rules.ui', self)


app = QtWidgets.QApplication(sys.argv)     
window = Ui()                              
app.exec_()                                
