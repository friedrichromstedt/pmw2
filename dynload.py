# Maintainer: Friedrich Romstedt <friedrichromstedt@gmail.com>
# Copyright 2009 Friedrich Romstedt
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
# $Last changed: 2009 Sep 25$
# Developed since: Sep 2009
# Version: 0.2.0b

class Dynload(object):
	"""The Dynload class emulates a module object, by implementing
	__getattr__(), __setattr__() and __delattr__().  Thus the Dynload
	instance behaves the same way as the emulated module, with the important
	exception, that the underlying module is only imported when its
	attributes are accessed first.
	
	To support some reload() mechanism, .reload() is offered."""

	def __init__(self, name):
		"""NAME is the name of the module to be dynloaded."""

		object.__setattr__(self, 'name', name)
		object.__setattr__(self, 'module', None)

		object.__setattr__(self, 'ready', True)  # value doesn't matter

	
	# Loading and reloading ...

	def load(self):
		"""Ensures that the module name passed to __init__() is loaded, and
		loads the module if it is not loaded.  Loading mechanism is the
		Python ``import'' statement in its full glory, thus importing from
		zip archives works, and dotted names can be imported."""

		if self.module is None:
			# Cause the interpreter to load the module in local namespace ...
			exec "import " + self.name

			# Store the module object ...
			object.__setattr__(self, 'module', eval(self.name))

	def reload(self):
		"""Reloads the underlying module.  The reload is implemented by
		an exec call to reload()."""

		if self.module is None:
			# Do nothing, as the module will be imported on attribute access.
			pass
		else:
			exec "reload(" + self.name + ")"
			# The module object is still identical, only its code has been
			# replaced.  Thus no eval(self.name) is necessary.
	

	# Attribute access ...
	
	def __getattr__(self, name):
		self.load()
		return getattr(self.module, name)

	def __setattr__(self, name, value):
		self.load()
		return setattr(self.module, name, value)

	def __delattr__(self, name):
		self.load()
		return delattr(self.module, name)

class DynloadAttribute(object):
	"""A DynloadAttribute emulates an attribute of a module by implmenting 
	__call__(), __getattr__(), __setattr__() and __delattr__().  Thus the 
	Dynload attribute behaves the same way as the emulated class, with the 
	important exception, that the underlying module is imported only when 
	the attribute is accessed first."""

	def __init__(self, name, dynloadmodule = None):
		"""NAME is the name of the class, DYNLOADMODULE is optional and can be
		an Dynload instance to load the class from.  When DYNLOADMODULE is
		given, the name is interpreted as relative to this module, otherwise
		NAME is interpreted as the absolute class name."""

		if dynloadmodule is not None:
			object.__setattr__(self, 'module', dynloadmodule)
			object.__setattr__(self, 'name', name)
		else:
			index = name.rfind('.')
			if index == -1:
				raise ValueError('Need a module attribut as NAME.')

			modulename = name[:index]
			attributename = name[index+1:]

			dynloadmodule = Dynload(modulename)
			object.__setattr__(self, 'module', dynloadmodule)
			object.__setattr__(self, 'name', attributename)

	# Calling ...

	def __call__(self, *args, **kwargs):
		attribute = getattr(self.module, self.name)
		return attribute(*args, **kwargs)

	def __getattr__(self, name):
		attribute = getattr(self.module, self.name)
		return getattr(attribute, name)

	def __setattr__(self, name, value):
		attribute = getattr(self.module, self.name)
		return setattr(attribute, name, value)

	def __delattr__(self, name):
		attribute = getattr(self.module, self.name)
		return delattr(attribute, name)
