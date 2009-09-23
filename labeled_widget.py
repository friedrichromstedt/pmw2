import Tkinter
import pmw2

class LabeledWidget(pmw2.base.MegaWidget):
    def __init__(self, parent = None, **kw):

        # Define the megawidget options.
        INITOPT = pmw2.base.INITOPT
        optiondefs = (
            ('labelmargin',            0,      INITOPT),
            ('labelpos',               None,   INITOPT),
            ('sticky',                 'nsew', INITOPT),
        )
        self.defineoptions(kw, optiondefs)

        # Initialise the base class (after defining the options).
        pmw2.base.MegaWidget.__init__(self, parent)

        # Create the components.
        interior = pmw2.base.MegaWidget.interior(self)
        self._labelChildSite = self.createcomponent('labelchildsite',
                (), None,
                Tkinter.Frame, (interior,))
        self._labelChildSite.grid(column=2, row=2, sticky=self['sticky'])
        interior.grid_columnconfigure(2, weight=1)
        interior.grid_rowconfigure(2, weight=1)

        self.createlabel(interior)

        # Check keywords and initialise options.
        self.initialiseoptions()

    def interior(self):
        return self._labelChildSite
