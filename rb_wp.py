#!/usr/bin/env python3

import dbus
import os
from time import sleep

sb = dbus.SessionBus()
previous_title = "123boyleisimlisarkidaolmasınamk_"
while True:
    try:
        rb_obj = sb.get_object("org.mpris.MediaPlayer2.rhythmbox",
                               "/org/mpris/MediaPlayer2")
    except dbus.exceptions.DBusException:
        sleep(1)
        continue
    props_int = dbus.Interface(rb_obj, "org.freedesktop.DBus.Properties")
    rb_meta_dict = props_int.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    try:
        title = rb_meta_dict["xesam:title"]
    except KeyError:
        sleep(1)
        continue
    if str(title) == previous_title:
        sleep(1)
        continue
    try:
        cover_art_url = rb_meta_dict["mpris:artUrl"]
    except KeyError:
        sleep(1)
        continue
    os.system("convert " + str(cover_art_url) + " \( -clone 0 -resize \
              177%x100% -blur 0x20 \) +swap -gravity center -compose over \
              -composite .wp.jpg")
    os.system("gsettings set org.gnome.desktop.background picture-uri \
              file:////home/umuty/.wp.jpg")
    os.system("gsettings set org.gnome.desktop.screensaver picture-uri \
              file:////home/umuty/.wp.jpg")
    previous_title = title
    sleep(1)

