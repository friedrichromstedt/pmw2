# Not Based on iwidgets version.

import pmw2.base
import pmw2.dialog
import pmw2.scrolled_list_box

class SelectionDialog(pmw2.dialog.Dialog):
    # Dialog window with selection list.
    
    # Dialog window displaying a list and requesting the user to
    # select one.

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
            ('listbox', 'scrolledlist_listbox'),
            ('label', 'scrolledlist_label'),
        )
        self._list = self.createcomponent('scrolledlist',
                aliases, None,
                pmw.scrolled_list_box.ScrolledListBox, (interior,),
                dblclickcommand = self.invoke)
        self._list.pack(side='top', expand='true', fill='both',
                padx = self['borderx'], pady = self['bordery'])

        if 'activatecommand' not in kw:
            # Whenever this dialog is activated, set the focus to the
            # ScrolledListBox's listbox widget.
            listbox = self.component('listbox')
            self.configure(activatecommand = listbox.focus_set)

        # Check keywords and initialise options.
        self.initialiseoptions()

    # Need to explicitly forward this to override the stupid
    # (grid_)size method inherited from Tkinter.Toplevel.Grid.
    def size(self):
        return self.component('listbox').size()

    # Need to explicitly forward this to override the stupid
    # (grid_)bbox method inherited from Tkinter.Toplevel.Grid.
    def bbox(self, index):
        return self.component('listbox').size(index)

pmw2.base.forwardmethods(SelectionDialog, Pmw.ScrolledListBox, '_list')
