# A Dialog with a ScrolledText widget.

import pmw2

class TextDialog(pmw2.dialog.Dialog):
    def __init__(self, parent = None, **kw):
        # Define the megawidget options.
        INITOPT = pmw2.base.INITOPT
        optiondefs = (
            ('borderx',     10,    INITOPT),
            ('bordery',     10,    INITOPT),
        )
        self.defineoptions(kw, optiondefs)

        # Initialise the base class (after defining the options).
        pmw2.dialog.Dialog.__init__(self, parent)

        # Create the components.
        interior = self.interior()
        aliases = (
            ('text', 'scrolledtext_text'),
            ('label', 'scrolledtext_label'),
        )
        self._text = self.createcomponent('scrolledtext',
                aliases, None,
                pmw2.scrolled_text.ScrolledText, (interior,))
        self._text.pack(side='top', expand=1, fill='both',
                padx = self['borderx'], pady = self['bordery'])

        # Check keywords and initialise options.
        self.initialiseoptions()

    # Need to explicitly forward this to override the stupid
    # (grid_)bbox method inherited from Tkinter.Toplevel.Grid.
    def bbox(self, index):
        return self._text.bbox(index)

pmw2.base.forwardmethods(TextDialog, pmw2.scrolled_text.ScrolledText, '_text')
