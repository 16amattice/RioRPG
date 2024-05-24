from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *  # type: ignore

import rio

from .. import components as comps


class InformationCard(rio.Component):
    
        # The quote somebody has definitely said about this company.
    icon: str

    # Who said the quote, probably Mark Twain.
    info_text: str

    # The company the person is from.
    label_text: str

    link_text: str

    link_loc: str

    def build(self) -> rio.Component:
        # Wrap everything in a card to make it stand out from the background.
        return rio.Card(
            # A second card, but this one is offset a bit. This allows the outer
            # card to pop out a bit, displaying a nice colorful border at the
            # bottom.
            rio.Card(
                # Combine the quote, name, and company into a column.
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
                        # Dim text and icons are used for less important
                        # information and make the app more visually appealing.
                        style="dim",
                        justify="center",
                    ),
                    rio.Link(
                        rio.Text(
                            f"{self.link_text}",
                            # Dim text and icons are used for less important
                            # information and make the app more visually appealing.
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
            # Important colors such as primary, secondary, neutral and
            # background are available as string constants for easy access.
            color="primary",
            width=20,
        )