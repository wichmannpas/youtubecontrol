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

As well as a selenium webdriver, for example the Geckodriver, which is available from the repositories of most Linux distributions.

How does that work?
-------------------

This script launches a browser instance using Selenium. That enables the script to control the website in it.

The play/pause-command presses the play/pause-button in the youtube tab.
Previous send the '0' key to the video element and goes one step back in the browsers history if it is triggered twice within a few seconds.
Next looks for all linked urls containig '/?watch' and uses the one appearing most often; this is the 'Up next' video in two of the current YouTube appearances. On other pages (i.e. search) it should at least open a somewhat related video.
If this does not find a valid url (which should actually not happen), the browser history is used to go one page forward.
