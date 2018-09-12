

class Color(object):
    purple = '\33[95m'
    blue = '\33[94m'
    green ='\33[92m'
    yellow = '\33[93m'
    red = '\33[91m'
    navy = '\33[96m'

def colorize(s, c=Color.green):
    return c + s + '\33[0m'

def _test():
    print(colorize("Hello world in purple", Color.purple))
    print(colorize("Hello world in green", Color.green))
    print(colorize("Hello world in blue", Color.blue))
    print(colorize("Hello world in red", Color.red))
    print(colorize("Hello world in yellow", Color.yellow))
    print(colorize("Hello world in navy", Color.navy))
    
if __name__ == '__main__':
    _test()

