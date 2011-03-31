#!/usr/bin/env python

#AMPY V3

#Standard libraries
import signal

#3rd party
import urwid
import ampylib

class ampy:
    """ An AMP Python Client. """


    rloop = None

    txt = None
    fill = None

    def sigint_handler(self, signal, frame):

        raise urwid.ExitMainLoop()

    def main(self, input):

        if input in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        self.txt.set_text(repr(input))

    def __init__(self):

        signal.signal(signal.SIGINT, self.sigint_handler)

        self.txt = urwid.Text("Hello World")
        self.fill = urwid.Filler(self.txt, 'top')

        self.rloop = urwid.MainLoop(self.fill, unhandled_input=self.main)

    def run(self):

        self.rloop.run()

if __name__ == "__main__":
    ampyObj = ampy()
    ampyObj.run()
