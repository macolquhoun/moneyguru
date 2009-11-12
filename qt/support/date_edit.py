# -*- coding: utf-8 -*-
# Created By: Virgil Dupras
# Created On: 2009-11-05
# $Id$
# Copyright 2009 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

from PyQt4.QtCore import Qt, QTimer
from PyQt4.QtGui import QLineEdit

from moneyguru.gui.date_widget import DateWidget

class DateEdit(QLineEdit):
    KEY2METHOD = {
        Qt.Key_Left: 'left',
        Qt.Key_Right: 'right',
        Qt.Key_Up: 'increase',
        Qt.Key_Down: 'decrease',
        Qt.Key_Backspace: 'backspace',
        Qt.Key_Delete: 'backspace',
    }
    
    def __init__(self, parent):
        QLineEdit.__init__(self, parent)
        self.widget = DateWidget('dd/MM/yyyy')
    
    def _refresh(self):
        self.setText(self.widget.text)
        selStart, selEnd = self.widget.selection
        self.setSelection(selStart, selEnd-selStart+1)
    
    def keyPressEvent(self, event):
        key = event.key()
        if key in self.KEY2METHOD:
            getattr(self.widget, self.KEY2METHOD[key])()
            self._refresh()
        else:
            text = unicode(event.text())
            if text in "0123456789/-.":
                self.widget.type(text)
                self._refresh()
            else:
                # We want keypresses like Escape to go through.
                QLineEdit.keyPressEvent(self, event)
    
    def focusInEvent(self, event):
        QLineEdit.focusInEvent(self, event)
        self.widget.text = unicode(self.text())
        # A timer is used here because a mouse event following the focusInEvent messes up the
        # selection (so the refresh *has* to happen after the mouse event).
        QTimer.singleShot(0, self._refresh)
    