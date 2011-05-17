#!/usr/bin/env python

#AMPY V3

#Standard libraries
import signal

#3rd party
import urwid
import ampylib

class SongWalker(urwid.ListWalker):
    """ Listwalker compatible class for songs """

    focus = None

    def __init__(self):
        self.focus = 0

    def get_focus(self):
        
        return 

    def set_focus(self, focus):
        self.focus = focus
        self._modified()

    def get_next(self, position):
        return

    def get_prev(self, position):
        return

class ampy:
    """ An AMP Python Client. """
    rloop = None

    frame = None
    header = None
    body = None
    footer = None
    listbox = None

    palette = [
            ('banner', '', '', '', '#ffa', '#60a'),
            ('streak', '', '', '', 'g50', '#60a'),
            ('key', 'default', 'default', 'underline'),
            ('footer bg', '', '', '', 'g50', '#60a'),
            ('reveal focus', 'black', 'dark cyan', 'standout'),]

    header_text = [
            ('banner', " AMPy - An Acoustics Client "),
            ]

    footer_text = [
            ('key', "ENTER"), (" for more information, "),
            ('key', "s"), (" to search, "),
            ('key', "l"), (" to login, "),
            ('key', "+"), (" to vote up, "),
            ('key', "-"), (" to vote down, "),
            ('key', "q"), (" to quit, "),]

    content = urwid.SimpleListWalker([
        urwid.AttrMap(w, None, 'reveal focus') for w in [
            urwid.Text("This is a text string that is fairly long"),
            urwid.Divider("-"),
            urwid.Text("Short one"),
            urwid.Text("Another"),
            urwid.Divider("-"),
            urwid.Text("What could be after this?"),
            urwid.Text("The end."),
            ]
        ])

    def sigint_handler(self, signal, frame):
        """ Handle SIGINT """

        raise urwid.ExitMainLoop()

    def key_handler(self, input):
        """ Handle the input keys """

        if input in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def __init__(self):
        """ Constructor. """

        signal.signal(signal.SIGINT, self.sigint_handler)

        self.header = urwid.Pile([
            urwid.AttrMap(urwid.Text(self.header_text, align='center'), 'streak'),
            ])
        self.footer = urwid.AttrMap(urwid.Text(self.footer_text, align='left'), 
                'footer bg')
        self.listbox = urwid.ListBox(self.content)

        self.frame = urwid.Frame(self.listbox, self.header, self.footer)

        self.rloop = urwid.MainLoop(self.frame, self.palette, 
                unhandled_input=self.key_handler)

    def run(self):
        """ Main run loop executor """

        self.rloop.run()

if __name__ == "__main__":
    ampyObj = ampy()
    ampyObj.run()
