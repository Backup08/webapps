#!/usr/bin/python

import PyQt5
from PyQt5.QtCore import QUrl 
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtWebKitWidgets import QWebView , QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtNetwork import *
import sys
from optparse import OptionParser


class WebPage(QWebPage):
    ''' Settings for the browser.'''

    def userAgentForUrl(self, url):
        ''' Returns a User Agent that will be seen by the website. '''
        return "Mozilla/5.0 (X11; CrOS x86_64 5717.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1918.1 Safari/537.36"

    def javaScriptConsoleMessage(self, msg, line, source):
        print('Console: %s line %d: %s' % (source, line, msg))


class Browser(QWebView):
    def __init__(self):
        self.view = QWebView.__init__(self)
        page = WebPage()
        self.setPage(page)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)
    
    def load(self,url):  
        self.setUrl(QUrl(url)) 

    def adjustTitle(self):
        self.setWindowTitle(self.title())

    def disableJS(self):
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.JavascriptEnabled, False)

    def enableCache(self):
        settings = QWebSettings.globalSettings()
        settings.setAttribute(QWebSettings.LocalStorageEnabled, True)
        settings.setAttribute(QWebSettings.OfflineWebApplicationCacheEnabled, True)
        settings.enablePersistentStorage('__your_path__')


####

def main():

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
    
    parser.add_option("-c", "--cache",
                      action="store_true",
                      dest="cache_flag",
                      default=False,
                      help="Enable Caching")
    
    
    (options, args) = parser.parse_args()
    print(args)
    
    if len(args) < 1:
        print('Specify URL with -u ')
        exit()
    
    url = args[0]
    app = QApplication(sys.argv) 
    
    view = Browser()
    view.showMaximized()
    
    
    if options.cache_flag:
        view.enableCache()

    if options.no_js_flag:
        view.disableJS()

    view.load(url)
    app.exec_()

if __name__ == "__main__":
    main()

