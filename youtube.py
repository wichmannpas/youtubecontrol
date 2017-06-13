#!/usr/bin/env python2
import dbus
import dbus.glib
import dbus.service
from selenium import webdriver
import gobject


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


class MediaPlayer2(dbus.service.Object):
    def __init__(self, bus_name, object_path, loop):
        dbus.service.Object.__init__(self, bus_name, object_path)
        self.loop = loop

    @dbus.service.method('org.mpris.MediaPlayer2.Player')
    def Previous(self):
        global chrome
        print('Received previous signal')
        chrome.back()

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
        chrome.forward()

chrome = None


if __name__ == '__main__':
    main()
