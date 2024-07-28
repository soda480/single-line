import sys
import cursor
from colorama import Cursor
from colorama import just_fix_windows_console, Fore, Back, Style


class SingleLine(object):

    clear_eol = '\033[K'

    def __init__(self, message_when_done=None, stream=sys.stdout):
        self.message_when_done = '' if not message_when_done else message_when_done
        self.stream = stream
        just_fix_windows_console()

    def __enter__(self):
        if self.stream.isatty():
            cursor.hide()
            # ensure subsequent print replaces our blank line
            print('')
        return self

    def __exit__(self, *args):
        if self.stream.isatty():
            self.write(self.message_when_done)
            cursor.show()

    def write(self, message, color=None):
        _message = message
        if self.stream.isatty():
            print(f'{Cursor.UP(1)}{self.clear_eol}', end='', file=self.stream)
            if not color:
                color = {}
            _color = color.get('fore', Fore.RESET) + color.get('back', Back.RESET) + color.get('style', Style.NORMAL)
            _message = f'{_color}{message}{Style.RESET_ALL}'
        print(_message, file=self.stream, flush=True)
