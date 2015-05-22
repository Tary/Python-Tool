# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

from MainWindowLayout import MainWindowLayout as MWLayout

###########################################################################
## Class MainPanel
###########################################################################

class MyFrame ( MWLayout ):
	def __init__(self, parent):
		MWLayout.__init__(self, parent)
		self.m_LogRichText.Clear()
		#wx.Frame.__init__(self, parent)
		#self.panel = MWLayout(self)
	def onDownloadClicked( self, event ):
		val = self.m_dirPicker2.GetTextCtrlValue()
		self.m_LogRichText.WriteText(val + "\n")
		self.m_LogRichText.Refresh()
		event.Skip()

