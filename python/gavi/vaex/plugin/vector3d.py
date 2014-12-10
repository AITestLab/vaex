__author__ = 'maartenbreddels'


import gavi.vaex.plugin
from gavi.vaex.qt import *
import gavi.vaex.plot_windows
from gavi.icons import iconfile
import matplotlib.widgets
import functools
import gavi.logging
import gavi.vaex.undo as undo
import numpy as np

logger = gavi.logging.getLogger("plugin.zoom")


class Vector3dPlugin(gavi.vaex.plugin.PluginLayer):
	name = "vector3"
	def __init__(self, dialog):
		super(Vector3dPlugin, self).__init__(dialog)
		dialog.plug_page(self.plug_page, "Vector field", 2., 2.)

	@staticmethod
	def useon(dialog_class):
		return issubclass(dialog_class, gavi.vaex.plot_windows.VolumeRenderingPlotDialog)

	def plug_page(self, page):
		existing_layout = page.layout()
		if isinstance(existing_layout, QtGui.QGridLayout):
			layout = existing_layout
		else:
			#raise NotImplementedError("expected different layout")
			self.layout = layout = QtGui.QGridLayout()
			existing_layout.addLayout(self.layout)
		page.setLayout(self.layout)
		layout.setSpacing(0)
		layout.setContentsMargins(0,0,0,0)
		layout.setAlignment(QtCore.Qt.AlignTop)

		row = 0



		def setter(value):
			self.dialog.widget_volume.draw_vectors = value
			self.dialog.widget_volume.update()
		self.vector3d_show_checkbox = self.dialog.create_checkbox(page, "show 3d vectors", lambda : self.dialog.widget_volume.draw_vectors, setter)
		layout.addWidget(self.vector3d_show_checkbox, row, 1)
		row += 1

		def setter(value):
			self.dialog.widget_volume.vector3d_auto_scale = value
			self.dialog.widget_volume.update()
		self.vector3d_auto_scale_checkbox = self.dialog.create_checkbox(page, "auto scale 3d vectors", lambda : self.dialog.widget_volume.vector3d_auto_scale, setter)
		layout.addWidget(self.vector3d_auto_scale_checkbox, row, 1)
		row += 1


		def setter(value):
			self.dialog.widget_volume.min_level_vector3d = value
			self.dialog.widget_volume.update()
		self.vector3d_min_level_label, self.vector3d_min_level_slider, self.vector3d_min_level_value_label =\
				self.dialog.create_slider(page, "min level: ", 0., 1., lambda : self.dialog.widget_volume.min_level_vector3d, setter)
		layout.addWidget(self.vector3d_min_level_label, row, 0)
		layout.addWidget(self.vector3d_min_level_slider, row, 1)
		layout.addWidget(self.vector3d_min_level_value_label, row, 2)
		row += 1

		def setter(value):
			self.dialog.widget_volume.max_level_vector3d = value
			self.dialog.widget_volume.update()
		self.vector3d_max_level_label, self.vector3d_max_level_slider, self.vector3d_max_level_value_label =\
				self.dialog.create_slider(page, "max level: ", 0., 1., lambda : self.dialog.widget_volume.max_level_vector3d, setter)
		layout.addWidget(self.vector3d_max_level_label, row, 0)
		layout.addWidget(self.vector3d_max_level_slider, row, 1)
		layout.addWidget(self.vector3d_max_level_value_label, row, 2)
		row += 1

		def setter(value):
			self.dialog.widget_volume.vector3d_scale = value
			self.dialog.widget_volume.update()
		self.vector3d_scale_level_label, self.vector3d_scale_level_slider, self.vector3d_scale_level_value_label =\
				self.dialog.create_slider(page, "scale: ", 1./20, 20., lambda : self.dialog.widget_volume.vector3d_scale, setter, format=" {0:>05.2f}", transform=lambda x: 10**x, inverse=lambda x: np.log10(x))
		layout.addWidget(self.vector3d_scale_level_label, row, 0)
		layout.addWidget(self.vector3d_scale_level_slider, row, 1)
		layout.addWidget(self.vector3d_scale_level_value_label, row, 2)
		row += 1

		layout.setRowMinimumHeight(row, 8)
		row += 1

