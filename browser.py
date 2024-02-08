import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import os

# Get the script's directory
script_directory = os.path.dirname(os.path.realpath(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)

# Read width and height from files
with open('./html/settings/width', 'r') as w:
    width = int(w.read())

with open('./html/settings/height', 'r') as h:
    height = int(h.read())

with open('./html/settings/name', 'r') as n:
    name = n.read()

def build(width=200, height=200):
    class Browser(QMainWindow):
        def __init__(self, initial_url, initial_size=None):
            super().__init__()
            self.browser = QWebEngineView()
            self.setCentralWidget(self.browser)

            # Set the size of the window (width, height) or use a default size
            self.setFixedSize(*initial_size)

            # Center the window on the screen
            self.center_on_screen()

            # Open the specific HTML file
            self.open_html_file()

        def center_on_screen(self):
            # Get the desktop geometry
            desktop_rect = QDesktopWidget().availableGeometry(self)

            # Calculate the center position of the window
            center_x = round(desktop_rect.center().x() - self.frameGeometry().width() / 2)
            center_y = round(desktop_rect.center().y() - self.frameGeometry().height() / 2)

            # Set the window position
            self.move(center_x, center_y)

        def open_html_file(self):
            # Specify the HTML file name
            html_file_name = "./html/code/index.html"

            # Get the absolute path to the HTML file using the script's directory
            html_file_path = os.path.join(script_directory, html_file_name)

            # Check if the file exists
            if os.path.exists(html_file_path):
                # Load and display the HTML content from the specified file
                self.browser.setUrl(QUrl.fromLocalFile(html_file_path))
            else:
                print(f"Error: {html_file_name} not found in the script's directory.")

    nname = name
    app = QApplication(sys.argv)
    QApplication.setApplicationName(nname)

    # Specify the initial URL here
    initial_url = "http://www.example.com"

    # Specify the initial size as a tuple (width, height)
    initial_size = (width, height)

    window = Browser(initial_url, initial_size)
    window.show()
    app.exec_()

# Call the build function with the width and height read from files
build(width, height)