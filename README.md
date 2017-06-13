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
