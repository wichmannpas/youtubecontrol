#!/usr/bin/env python2
from collections import Counter
from datetime import datetime, timedelta
import atexit
import signal
import sys

import dbus
import dbus.glib
import dbus.service
import gobject
from selenium import webdriver


def main():
    """Open youtube and start dbus listener."""
    global chrome

    loop = gobject.MainLoop()

    bus = dbus.SessionBus()
    bus_name = dbus.service.BusName('org.mpris.MediaPlayer2.youtube', bus=bus)

    MediaPlayer2(bus_name, '/org/mpris/MediaPlayer2', loop)

    chrome = webdriver.Chrome()
    chrome.get('https://youtube.com')

    loop.run()


def quit(*args, **kwargs):
    chrome.quit()
    sys.exit(0)
atexit.register(quit)
signal.signal(signal.SIGTERM, quit)


class MediaPlayer2(dbus.service.Object):
    def __init__(self, bus_name, object_path, loop):
        dbus.service.Object.__init__(self, bus_name, object_path)
        self.loop = loop

    @dbus.service.method('org.mpris.MediaPlayer2.Player')
    def Previous(self):
        global chrome, last_previous
        print('Received previous signal')
        now = datetime.now()
        if now - last_previous < timedelta(seconds=5):
            chrome.back()
        else:
            elem = chrome.find_element_by_tag_name('video')
            elem.send_keys('0')
        last_previous = now

    @dbus.service.method('org.mpris.MediaPlayer2.Player')
    def PlayPause(self):
        global chrome
        print('Received PlayPause signal')
        elem = chrome.find_element_by_tag_name('video')
        elem.send_keys(' ')

    @dbus.service.method('org.mpris.MediaPlayer2.Player')
    def Next(self):
        global chrome
        print('Received next signal')
        next_video_url = _find_next_video_url(chrome)
        if next_video_url:
            chrome.get(next_video_url)
        else:
            chrome.forward()


def _find_next_video_url(c):
    """Try different ways to determine the url of the next video."""
    try:
        next_video_url = sorted(Counter(
            a.get_property('href')
            for a in c.find_elements_by_tag_name('a')
            if a.get_property('href').find('/watch?') >= 0
        ).items(), key=lambda k: k[1], reverse=True)[0][0]
    except Exception:
        pass
    if next_video_url:
        return next_video_url
    next_video_url = chrome.find_element_by_class_name('watch-sidebar-body') \
        .find_element_by_tag_name('a').get_property('href')
    if next_video_url:
        return next_video_url

chrome = None
last_previous = datetime.now()


if __name__ == '__main__':
    main()
