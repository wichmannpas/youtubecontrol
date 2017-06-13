Youtube Control
===============

This is a simple youtube controller which allows you to use your media keys to control youtube.

Usage
-----

Run the script:

    ./youtube.py

Now you can use the opened YouTube tab as you are used to. Your media keys will control the <video> element in the opened tab.


Installation
------------

You need to install the required Python packages:

    pip2 install -r requirements.txt

As well as the selenium chrome webdriver:

    curl https://chromedriver.storage.googleapis.com/$(curl https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip > $HOME/.local/bin

Assuming that $HOME/.local/bin is in your PATH.


How does that work?
-------------------

This script launches a chrome instance using Selenium. That enables the script to control the website in it.

The play/pause-command send a space key to the <video> element in the youtube tab.
Previous goes one step back in the browsers history.
Next looks for all linked urls containig '/?watch' and uses the one appearing most often; this is the 'Up next' video in two of the current YouTube appearances. On other pages (i.e. search) it should at least open a somewhat related video.
If this does not find a valid url (which should actually not happen), the browser history is used to go one page forward.
