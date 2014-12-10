
order_toolbar_navigate = 1.


class RegisterPlugins(type):
	def __init__(cls, name, bases, nmspc):
		super(RegisterPlugins, cls).__init__(name, bases, nmspc)
		if not hasattr(cls, 'registry'):
			cls.registry = set()
		cls.registry.add(cls)
		cls.registry -= set(bases) # Remove base classes

	def __iter__(cls):
		return iter(cls.registry)

	def __str__(cls):
		if cls in cls.registry:
			return cls.__name__
		return cls.__name__ + ": " + ", ".join([sc.__name__ for sc in cls])


class PluginPlot(object):
	__metaclass__ = RegisterPlugins # trick to keep a list of plugins
	def __init__(self, dialog):
		self.dialog = dialog

	def clean_up(self):
		pass

	def use_layer(self, layer):
		pass

	@staticmethod
	def useon(dialog_class):
		return True

	def syncToolbar(self):
		pass

	def setMode(self, action):
		pass


class PluginLayer(object):
	__metaclass__ = RegisterPlugins # trick to keep a list of plugins
	def __init__(self, dialog):
		self.dialog = dialog
		self.dataset = dialog.dataset

	def clean_up(self):
		pass
		
	@staticmethod
	def useon(layer_class):
		return True
	
	def get_options(self):
		return {}

	def apply_options(self, options):
		pass

	def start_animation(self, widget):
		pass

	def stop_animation(self):
		pass

class PluginDataset(object):
	__metaclass__ = RegisterPlugins # trick to keep a list of plugins
	def __init__(self, dataset, widget):
		self.dataset = dataset
		self.widget = widget

	@staticmethod
	def useon(dataset):
		return True
	
