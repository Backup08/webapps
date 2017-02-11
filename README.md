# Run webapps from the desktop

Examples: <br />
<br />
<pre>
qt5webview.py -u https://hckrnews.com/
qt5webview.py -u https://ventusky.com
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
