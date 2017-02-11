#!/usr/bin/python

import PyQt5
from PyQt5.QtCore import QUrl 
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtWebKitWidgets import QWebView , QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *
import sys
from optparse import OptionParser


class MyBrowser(QWebPage):
    ''' Settings for the browser.'''

    def userAgentForUrl(self, url):
        ''' Returns a User Agent that will be seen by the website. '''
        return "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

class Browser(QWebView):
    def __init__(self):
        # QWebView
        self.view = QWebView.__init__(self)
        #self.view.setPage(MyBrowser())
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
        #super(Browser).connect(self.ui.webView,QtCore.SIGNAL("titleChanged (const QString&)"), self.adjustTitle)

    def load(self,url):  
        self.setUrl(QUrl(url)) 

    def adjustTitle(self):
        self.setWindowTitle(self.title())

    def disableJS(self):
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.JavascriptEnabled, False)



nojs = False

parser = OptionParser(usage="usage: %prog [options] filename",
                      version="%prog 1.0")

parser.add_option("-u", "--url",
                  action="store_true",
                  dest="url_flag",
                  default=False,
                  help="Website URL")

parser.add_option("-j", "--nojavascript",
                  action="store_true",
                  dest="no_js_flag",
                  default=False,
                  help="Disable Javascript")

(options, args) = parser.parse_args()
print(args)

url = args[0]

if options.no_js_flag:
    nojs = True

app = QApplication(sys.argv) 
#url = sys.argv[1]

view = Browser()
view.showMaximized()

if nojs:
    view.disableJS()
view.load(url)
app.exec_()