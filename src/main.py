from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile
from PyQt6.QtCore import QUrl, Qt
import sys
import os
import webbrowser
os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"
# Set remote debugging port before QApplication is created
os.environ["QTWEBENGINE_REMOTE_DEBUGGING"] = "9222"

app = QApplication(sys.argv)  # Instantiate QApplication first

# Create a QWebEngineProfile and set a larger cache size (e.g., 1 GB)
profile = QWebEngineProfile.defaultProfile()
profile.setHttpCacheMaximumSize(1024 * 1024 * 1024)  # 1 GB
profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.DiskHttpCache)
profile.settings().setAttribute(
    profile.settings().WebAttribute.PluginsEnabled, False
)

class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aligned")
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
        self.browser.setUrl(QUrl(
            "https://docs.google.com/presentation/d/1DSuljNYH39cajCwWPA4Ky0JV-qh13_mh9ayY41YUT9w/embed?rm=minimal"
        ))

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F2:
            # Open Chrome DevTools for the running QWebEngineView
            webbrowser.open("http://localhost:9222")
        super().keyPressEvent(event)

def main():
    window = BrowserWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()