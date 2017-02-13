# Run webapps from the desktop

Display any website as web app using the Qt5.
<i>Simple: Just the app and title!</i>

<a href="https://youtu.be/nNzR-OiVSf8" target="_blank"> Watch demo</a>

Run using:
<pre>
qt5webview.py -u https://hckrnews.com/
qt5webview.py -u https://ventusky.com
qt5webview.py -u https://arstechnica.com --nojavascript
qt5webview.py -u https://chat.cloudron.io/home -c  (enable caching)
</pre>

# Add a desktop icon 

Example launcher on XFCE Desktop:
<pre>
[Desktop Entry]
Version=1.0
Type=Application
Name=HN
Exec=qt5webview.py -u https://hckrnews.com/
Icon=/usr/share/icons/webapps/hn.png
Terminal=false
StartupNotify=false
Name[en_US]=HNews
</pre>

# Installation

<pre>
sudo apt install python3-pyqt5
sudo apt-get install libqt5webkit5-dev python3-pyqt5.qtsvg python3-pyqt5.qtwebkit
sudo apt install git
git clone github.com/Maarten08/webapps.git
cd webapps/
sudo apt install python3-setuptools
sudo python3 setup.py install
qt5webview.py -u https://hckrnews.com
qt5webview.py -u https://evernote.com
</pre>
