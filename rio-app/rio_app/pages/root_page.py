from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *

import rio

from .. import components as comps

class RootPage(rio.Component):
    expanded: bool = True
    
    def toggle_sidebar(self) -> None:
        self.expanded = not self.expanded
        self.force_refresh()
        
    def build(self) -> rio.Component:
        sidebar_proportion = 1.5 if self.expanded else 0.3
        main_content_proportion = 8.5 if self.expanded else 9.7

        return rio.Row(
            comps.Sidebar(expanded=self.expanded),
            rio.Column(
                comps.Navbar(toggle_sidebar=self.toggle_sidebar),
                rio.PageView(),
                proportions=(0.7, 9.3),
            ),
            proportions=(sidebar_proportion, main_content_proportion)
        )
