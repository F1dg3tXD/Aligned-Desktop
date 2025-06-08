from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys
import os
os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt6 Browser")
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        self.load_html_file()

        # Create a menu bar
        self.menu_bar = self.menuBar()
        self.create_menu()

    def create_menu(self):
        # Create a toggle fullscreen action
        fullscreen_action = QAction("Toggle Fullscreen", self)
        fullscreen_action.triggered.connect(self.toggle_fullscreen)

        # Create a menu and add the action
        file_menu = self.menu_bar.addMenu("File")
        file_menu.addAction(fullscreen_action)

    def load_html_file(self):
        self.browser.setUrl(QUrl("https://docs.google.com/presentation/d/1DSuljNYH39cajCwWPA4Ky0JV-qh13_mh9ayY41YUT9w/embed?start=true"))

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

def main():
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()