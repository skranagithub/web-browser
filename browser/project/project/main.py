import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('C:/Users/sugam/Desktop/web_browser/index.html'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

#navbaar
        navbar=QToolBar()
        self.addToolBar(navbar)
        
        back_btn=QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        
        forward_btn=QAction('Forword',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        
        refresh_btn=QAction('Refresh',self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)
        
        home_btn=QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        self.url_bar= QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        
        self.browser.urlChanged.connect(self.update_url)
        
    def navigate_home(self):
        self.browser.setUrl(QUrl('C:/Users/sugam/Desktop/web_browser/index.html'))    
     
    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))  
    
    def update_url(self,q):
        self.url_bar.setText(q.toString())
        
app=QApplication(sys.argv)
QApplication.setApplicationName(' WEL-COME TO MY Browser')
window=mainwindow()
app.exec_()





