from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *

import rio

from .. import components as comps

class InformationCard(rio.Component):
    
    icon: str
    info_text: str
    label_text: str
    link_text: str
    link_loc: str

    def build(self) -> rio.Component:
        return rio.Card(
            rio.Card(
                rio.Column(
                    rio.Icon(
                        self.icon,
                        align_x=0.5,
                        height=1.7,
                        width=1.7,
                    ),
                    rio.Text(
                        self.info_text,
                        justify="center",
                    ),
                    rio.Text(
                        f"{self.label_text}",
                        style="dim",
                        justify="center",
                    ),
                    rio.Link(
                        rio.Text(
                            f"{self.link_text}",
                            justify="center",
                            style=rio.TextStyle(
                                fill=rio.Color.from_hex("#0000EE"),
                                font_size=0.8
                            ),
                        ),
                        self.link_loc
                    ),
                    spacing=0.4,
                    margin=2,
                    align_y=0.5,
                ),
                margin_bottom=0.2,
            ),
            color="primary",
            width=20,
        )