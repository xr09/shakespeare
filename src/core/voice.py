#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import subprocess, shlex


class Language(object):
    en = "en"
    es = "es"

class Pitch(object):
    slow = 20
    normal = 50
    fast = 80

def talk(text, lang=Language.en, pitch=50, speed=160):
    if os.path.exists("/usr/bin/espeak"):
        args = "/usr/bin/espeak -v %s -p %d -s %d \"%s\"" % (lang, pitch, speed, text)
        return subprocess.Popen(shlex.split(args), stderr=subprocess.PIPE)
    else:
        raise Exception("warning: espeak is not installed on the system")

def main():
    talk("testing text to speak", pitch=40, speed=145)
    #talk("hola mundo", Language.es)

if __name__ == '__main__':
    main()

