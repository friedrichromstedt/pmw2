# Maintainer: Friedrich Romstedt <friedrichromstedt@gmail.com>
# Copyright 2009 Friedrich Romstedt
#    This file is part of pmw2.
#
#    pmw2 is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    pmw2 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with pmw2.  If not, see <http://www.gnu.org/licenses/>.
# $Last changed: 2009 Sep 23$
# Developed since: Sep 2009
# File version: 0.1.0b

import pmw2.dynload

# Module "import"s ...

about_dialog = pmw2.dynload.Dynload('pmw2.about_dialog')
balloon = pmw2.dynload.Dynload('pmw2.balloon')
base = pmw2.dynload.Dynload('pmw2.base')
blt = pmw2.dynload.Dynload('pmw2.blt')
button_box = pmw2.dynload.Dynload('pmw2.button_box')
color = pmw2.dynload.Dynload('pmw2.color')
combo_box = pmw2.dynload.Dynload('pmw2.combo_box')
combo_box_dialog = pmw2.dynload.Dynload('pmw2.combo_box_dialog')
counter = pmw2.dynload.Dynload('pmw2.counter')
counter_dialog = pmw2.dynload.Dynload('pmw2.counter_dialog')
dialog = pmw2.dynload.Dynload('pmw2.dialog')
entry_field = pmw2.dynload.Dynload('pmw2.entry_field')
group = pmw2.dynload.Dynload('pmw2.group')
history_text = pmw2.dynload.Dynload('pmw2.history_text')
labeled_widget = pmw2.dynload.Dynload('pmw2.labeled_widget')
logical_font = pmw2.dynload.Dynload('pmw2.logical_font')
main_menu_bar = pmw2.dynload.Dynload('pmw2.main_menu_bar')
menu_bar = pmw2.dynload.Dynload('pmw2.menu_bar')
message_bar = pmw2.dynload.Dynload('pmw2.message_bar')
message_dialog = pmw2.dynload.Dynload('pmw2.message_dialog')
note_book = pmw2.dynload.Dynload('pmw2.note_book')
option_menu = pmw2.dynload.Dynload('pmw2.option_menu')
paned_widget = pmw2.dynload.Dynload('pmw2.paned_widget')
prompt_dialog = pmw2.dynload.Dynload('pmw2.prompt_dialog')
radio_select = pmw2.dynload.Dynload('pmw2.radio_select')
scrolled_canvas = pmw2.dynload.Dynload('pmw2.scrolled_canvas')
scrolled_field = pmw2.dynload.Dynload('pmw2.scrolled_field')
scrolled_frame = pmw2.dynload.Dynload('pmw2.scrolled_frame')
scrolled_list_box = pmw2.dynload.Dynload('pmw2.scrolled_list_box')
scrolled_text = pmw2.dynload.Dynload('pmw2.scrolled_text')
selection_dialog = pmw2.dynload.Dynload('pmw2.selection_dialog')
text_dialog = pmw2.dynload.Dynload('pmw2.text_dialog')
time_counter = pmw2.dynload.Dynload('pmw2.time_counter')
time_funcs = pmw2.dynload.Dynload('pmw2.time_funcs')

# "from module import something" ...

AboutDialog = pmw2.dynload.DynloadAttribute('AboutDialog', about_dialog)
aboutversion = pmw2.dynload.DynloadAttribute('aboutversion', about_dialog)
aboutcopyright = pmw2.dynload.DynloadAttribute('aboutcopyright', about_dialog)
aboutcontact = pmw2.dynload.DynloadAttribute('aboutcontact', about_dialog)

Balloon = pmw2.dynload.DynloadAttribute('Balloon', balloon)

END = ['end']
SELECT = ['select']
DEFAULT = ['default']
INITOPT = ['initopt']
forwardmethods = pmw2.dynload.DynloadAttribute('forwardmethods', base)
setgeometryanddeiconify = \
		pmw2.dynload.DynloadAttribute('setgeometryanddeiconify', base)
MegaArchetry = pmw2.dynload.DynloadAttribute('MegaArchetype', base)
pushgrab = pmw2.dynload.DynloadAttribute('pushgrab', base)
popgrab = pmw2.dynload.DynloadAttribute('popgrab', base)
grabstacktopwindow = pmw2.dynload.DynloadAttribute('grabstacktopwindow', base)
releasegrab = pmw2.dynload.DynloadAttribute('releasegrab', base)
MegaToplevel = pmw2.dynload.DynloadAttribute('MegaToplevel', base)
MegaWidget = pmw2.dynload.DynloadAttribute('MegaWidget', base)
tracetk = pmw2.dynload.DynloadAttribute('tracetk', base)
showbusycursor = pmw2.dynload.DynloadAttribute('showbusycursor', base)
hidebusycursor = pmw2.dynload.DynloadAttribute('hidebusycursor', base)
clearbusycursor = pmw2.dynload.DynloadAttribute('clearbusycursor', base)
setbusycursorattributes = \
		pmw2.dynload.DynloadAttribute('setbusycursorattributes', base)
busycallback = pmw2.dynload.DynloadAttribute('busycallback', base)
reporterrorstofile = pmw2.dynload.DynloadAttribute('reporterrorstofile', base)
displayerror = pmw2.dynload.DynloadAttribute('displayerror', base)
initialise = pmw2.dynload.DynloadAttribute('initialise', base)
alignlabels = pmw2.dynload.DynloadAttribute('alignlabels', base)
drawarrow = pmw2.dynload.DynloadAttribute('drawarrow', base)

haveblt = pmw2.dynload.DynloadAttribute('haveblt', blt)
havebltbusy = pmw2.dynload.DynloadAttribute('havebltbusy', blt)
busy_hold = pmw2.dynload.DynloadAttribute('busy_hold', blt)
busy_release = pmw2.dynload.DynloadAttribute('busy_release', blt)
busy_forget = pmw2.dynload.DynloadAttribute('busy_forget', blt)
vector_expr = pmw2.dynload.DynloadAttribute('vector_expr', blt)
vector_names = pmw2.dynload.DynloadAttribute('vector_names', blt)
Vector = pmw2.dynload.DynloadAttribute('Vector', blt)
Graph = pmw2.dynload.DynloadAttribute('Graph', blt)
Stripchart = pmw2.dynload.DynloadAttribute('Stripchart', blt)
Tabset = pmw2.dynload.DynloadAttribute('Tabset', blt)

ButtonBox = pmw2.dynload.DynloadAttribute('ButtonBox', button_box)

setscheme = pmw2.dynload.DynloadAttribute('setscheme', color)
getdefaultpalette = \
		pmw2.dynload.DynloadAttribute('getdefaultpalette', color)
changebrightness = \
		pmw2.dynload.DynloadAttribute('changebrightness', color)
hue2name = pmw2.dynload.DynloadAttribute('hue2name', color)
bhi2saturation = pmw2.dynload.DynloadAttribute('bhi2saturation', color)
hsi2rgb = pmw2.dynload.DynloadAttribute('hsi2rgb', color)
average = pmw2.dynload.DynloadAttribute('average', color)
rgb2name = pmw2.dynload.DynloadAttribute('rgb2name', color)
rgb2brightness = \
		pmw2.dynload.DynloadAttribute('rgb2brightness', color)
rgb2hsi = pmw2.dynload.DynloadAttribute('rgb2hsi', color)
name2rgb = pmw2.dynload.DynloadAttribute('name2rgb', color)
spectrum = pmw2.dynload.DynloadAttribute('spectrum', color)
correct = pmw2.dynload.DynloadAttribute('correct', color)
changecolor = pmw2.dynload.DynloadAttribute('changecolor', color)
bordercolors = pmw2.dynload.DynloadAttribute('bordercolors', color)

ComboBox = pmw2.dynload.DynloadAttribute('ComboBox', combo_box)

ComboBoxDialog = \
		pmw2.dynload.DynloadAttribute('ComboBoxDialog', combo_box_dialog)

Counter = pmw2.dynload.DynloadAttribute('Counter', counter)

CounterDialog = pmw2.dynload.DynloadAttribute('ConterDialog', counter_dialog)

Dialog = pmw2.dynload.DynloadAttribute('Dialog', dialog)

OK = 1
ERROR = 0
PARTIAL = -1
EntryField = pmw2.dynload.DynloadAttribute('EntryField', entry_field)
numericvalidator = \
		pmw2.dynload.DynloadAttribute('numericvalidator', entry_field)
integervalidator = \
		pmw2.dynload.DynloadAttribute('integervalidator', entry_field)
alphabeticvalidator = \
		pmw2.dynload.DynloadAttribute('alphabeticvalidator', entry_field)
alphanumericvalidator = \
		pmw2.dynload.DynloadAttribute('alphanumericvalidator', entry_field)
hexadecimalvalidator = \
		pmw2.dynload.DynloadAttribute('hexadecimalvalidator', entry_field)
realvalidator = \
		pmw2.dynload.DynloadAttribute('realvalidator', entry_field)
timevalidator = \
		pmw2.dynload.DynloadAttribute('timevalidator', entry_field)
datevalidator = \
		pmw2.dynload.DynloadAttribute('datevalidator', entry_field)


aligngrouptags = \
		pmw2.dynload.DynloadAttribute('aligngrouptags', group)
Group = pmw2.dynload.DynloadAttribute('Group', group)

HistoryText = pmw2.dynload.DynloadAttribute('HistoryText', history_text)

LabeledWidget = pmw2.dynload.DynloadAttribute('LabeledWidget', labeled_widget)

logicalfont = pmw2.dynload.DynloadAttribute('logicalfont', logical_font)
logicalfontnames = \
		pmw2.dynload.DynloadAttribute('logicalfontnames', logical_font)

MainMenuBar = pmw2.dynload.DynloadAttribute('MainMenuBar', main_menu_bar)

MenuBar = pmw2.dynload.DynloadAttribute('MenuBar', menu_bar)

MessageBar = pmw2.dynload.DynloadAttribute('MessageBar', message_bar)

MessageDialog = pmw2.dynload.DynloadAttribute('MessageDialog', message_dialog)

NoteBook = pmw2.dynload.DynloadAttribute('NoteBook', note_book)

OptionMenu = pmw2.dynload.DynloadAttribute('OptionMenu', option_menu)

PanedWidget = pmw2.dynload.DynloadAttribute('PanedWidget', paned_widget)

PromptDialog = pmw2.dynload.DynloadAttribute('PromptDialog', prompt_dialog)

RadioSelect = pmw2.dynload.DynloadAttribute('RadioSelect', radio_select)

ScrolledCanvas = \
		pmw2.dynload.DynloadAttribute('ScrolledCanvas', scrolled_canvas)

ScrolledField = \
		pmw2.dynload.DynloadAttribute('ScrolledField', scrolled_field)

ScrolledFrame = \
		pmw2.dynload.DynloadAttribute('ScrolledFrame', scrolled_frame)

ScrolledListBox = \
		pmw2.dynload.DynloadAttribute('ScrolledListBox', scrolled_list_box)

ScrolledText = pmw2.dynload.DynloadAttribute('ScrolledText', scrolled_text)

SelectionDialog = \
		pmw2.dynload.DynloadAttribute('SelectionDialog', selection_dialog)

TextDialog = pmw2.dynload.DynloadAttribute('TextDialog', text_dialog)

TimeCounter = pmw2.dynload.DynloadAttribute('TimeCounter', time_counter)

timestringtoseconds = \
		pmw2.dynload.DynloadAttribute('timestringtoseconds', time_funcs)
setyearpivot = pmw2.dynload.DynloadAttribute('setyearpivot', time_funcs)
datestringtojdn = \
		pmw2.dynload.DynloadAttribute('datestringtojdn', time_funcs)
ymdtojdn = pmw2.dynload.DynloadAttribute('ymdtojdn', time_funcs)
jdntoymd = pmw2.dynload.DynloadAttribute('jdntoymd', time_funcs)
stringtoreal = pmw2.dynload.DynloadAttribute('stringtoreal', time_funcs)
