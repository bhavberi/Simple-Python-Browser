from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):  #constructor
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        #NavBar
        navbar=QToolBar('Navigation')
        self.addToolBar(navbar)

        home=QAction('Home',self)
        home.setStatusTip("Go to home") 
        home.triggered.connect(self.goHome)
        navbar.addAction(home)

        back=QAction('Back',self)
        back.setStatusTip("Back to previous page")
        back.triggered.connect(self.browser.back)
        navbar.addAction(back)

        forward=QAction('Forward',self)
        forward.setStatusTip("Forward to next page")
        forward.triggered.connect(self.browser.forward)
        navbar.addAction(forward)

        reload=QAction('Reload',self)
        reload.setStatusTip("Reload page") 
        reload.triggered.connect(self.browser.reload)
        navbar.addAction(reload)

        navbar.addSeparator() 

        self.urlbar=QLineEdit()
        self.urlbar.setStatusTip("URL Bar")
        self.urlbar.returnPressed.connect(self.goUrl)
        navbar.addWidget(self.urlbar)

        self.browser.urlChanged.connect(self.update)
        self.setStatusBar(QStatusBar(self))

        stop = QAction("Stop", self) 
        stop.setStatusTip("Stop loading current page") 
        stop.triggered.connect(self.browser.stop) 
        navbar.addAction(stop)

        self.show()

    def goHome(self):
        self.browser.setUrl(QUrl('https://google.com'))
        
    def goUrl(self):
        url=self.urlbar.text()
        if q.scheme() == "": 
            q.setScheme("http")
        self.browser.setUrl(QUrl(url))

    def update(self,q):
        self.urlbar.setText(q.toString())

        

app = QApplication(sys.argv)
QApplication.setApplicationName("BB Browser")
window = MainWindow()
app.exec_()
