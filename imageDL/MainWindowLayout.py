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

###########################################################################
## Class MainWindowLayout
###########################################################################

class MainWindowLayout ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		rootSizer = wx.BoxSizer( wx.VERTICAL )
		
		srcSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"来源" ), wx.HORIZONTAL )
		
		self._id_label = wx.StaticText( self, wx.ID_ANY, u"ID：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._id_label.Wrap( -1 )
		srcSizer.Add( self._id_label, 0, wx.ALL, 5 )
		
		self.m_inputIDText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		srcSizer.Add( self.m_inputIDText, 1, wx.ALL, 5 )
		
		self.m_downloadButton = wx.Button( self, wx.ID_ANY, u"下载", wx.DefaultPosition, wx.DefaultSize, 0 )
		srcSizer.Add( self.m_downloadButton, 0, wx.ALL, 5 )
		
		
		rootSizer.Add( srcSizer, 0, wx.ALL|wx.EXPAND, 5 )
		
		dstSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"保存路径" ), wx.HORIZONTAL )
		
		self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"选择保存路径", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		dstSizer.Add( self.m_dirPicker2, 1, wx.ALL, 5 )
		
		
		rootSizer.Add( dstSizer, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_LogRichText = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER|wx.VSCROLL|wx.WANTS_CHARS )
		rootSizer.Add( self.m_LogRichText, 1, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( rootSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_downloadButton.Bind( wx.EVT_LEFT_UP, self.onDownloadClicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onDownloadClicked( self, event ):
		event.Skip()
	

###########################################################################
## Class MyPanel7
###########################################################################

class MyPanel7 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

