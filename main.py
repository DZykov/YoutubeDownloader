import replacer, downloader
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit, QListWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Youtube Playlist Downloader") 
        
        # playlist
        self.playlistLabel = QLabel(self)
        self.playlistLabel.setText('Playlist:')
        self.line = QLineEdit(self)

        self.line.move(100, 20)
        self.line.resize(300, 32)
        self.playlistLabel.move(10, 20)

        # directory
        self.directoryLabel = QLabel(self)
        self.directoryLabel.setText('Directory:')
        self.line2 = QLineEdit(self)

        self.line2.move(100, 60)
        self.line2.resize(300, 32)
        self.directoryLabel.move(10, 60)

        # replace
        self.replaceLabel = QLabel(self)
        self.replaceLabel.setText('Replace:')
        self.line1 = QLineEdit(self)

        self.line1.move(100, 100)
        self.line1.resize(300, 32)
        self.replaceLabel.move(10, 100)

        pybutton = QPushButton('Download', self)
        pybutton.clicked.connect(self.clickDownload)
        pybutton.resize(300,32)
        pybutton.move(100, 140)

        # show downloads
        self.downloadedLabel = QLabel(self)
        self.downloadedLabel.setText('Downloads:')
        self.downloadedLabel.move(10, 180)

        self.listDownloads = QListWidget(self)
        self.listDownloads.resize(300, 200)
        self.listDownloads.move(100, 180)


    def clickDownload(self):
        playlist = self.line.text()
        directory = self.line2.text()
        replaces = self.line1.text()
        
        self.listDownloads.addItems(['1','2','3'])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )