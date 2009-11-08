# -*- coding: utf-8 -*-
# Created By: Virgil Dupras
# Created On: 2009-11-01
# $Id$
# Copyright 2009 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

from .base_view import BaseView
from .networth_sheet import NetWorthSheet
from .networth_graph import NetWorthGraph
from .asset_pie_chart import AssetPieChart
from .liability_pie_chart import LiabilityPieChart
from ui.networth_view_ui import Ui_NetWorthView

class NetWorthView(BaseView, Ui_NetWorthView):
    def __init__(self, doc):
        BaseView.__init__(self)
        self.doc = doc
        self._setupUi()
        self.nwsheet = NetWorthSheet(doc=doc, view=self.treeView)
        self.nwgraph = NetWorthGraph(doc=doc, view=self.graphView)
        self.apiechart = AssetPieChart(doc=doc, view=self.assetPieChart)
        self.lpiechart = LiabilityPieChart(doc=doc, view=self.liabilityPieChart)
        self.children = [self.nwsheet, self.nwgraph, self.apiechart, self.lpiechart]
    
    def _setupUi(self):
        self.setupUi(self)
    
