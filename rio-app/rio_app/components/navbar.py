from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *

import rio

from .. import components as comps

class Navbar(rio.Component):
    toggle_sidebar: Callable[[], None]

    @rio.event.on_page_change
    async def on_page_change(self) -> None:
        await self.force_refresh()

    example_state: str = "For demonstration purposes"
    def build(self) -> rio.Component:
        return rio.Rectangle(
            content=rio.Row(
                rio.IconButton(
                    icon="material/menu",
                    align_x=0,
                    margin_x=1,
                    style="plain",
                    on_press=self.toggle_sidebar
                ),
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Text(
                                "Travel",
                                margin_right=0.5
                            ),
                            rio.Icon(
                                icon="material/arrow-circle-right",
                            ),
                        ),
                        style=(
                            "major"
                        ),
                        shape="rounded",
                        color=rio.Color.from_hex("#4f46e5"),
                    ),
                    "about/",
                    margin_x=1,
                    margin_y=0.5,
                ),                
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Text(
                                "Diamond Store",
                            ),
                        ),
                        style=(
                            "plain"
                        ),
                        shape="rectangle"
                    ),
                    "about/",
                    margin_x=1,
                    margin_y=0.5,
                ),  
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Text(
                                "Support",
                            ),
                        ),
                        style=(
                            "plain"
                        ),
                        shape="rectangle"
                    ),
                    "about/",
                    margin_x=1,
                    margin_y=0.5,
                ),  
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Text(
                                "Community",
                            ),
                        ),
                        style=(
                            "plain"
                        ),
                        shape="rectangle"
                    ),
                    "about/",
                    margin_x=1,
                    margin_y=0.5,
                ),  
                rio.TextInput(
                    margin_x=1,
                    margin_y=0.5,
                    width=20,
                    label="Search",
                    suffix_text="⌕"   
                ),
                rio.Spacer(),
                rio.IconButton(
                    icon="material/group",
                    style="plain",
                    align_x=1,
                ),
                rio.IconButton(
                    icon="material/chat",
                    style="plain",
                    align_x=1,
                ),
                rio.IconButton(
                    icon="material/notifications",
                    style="plain",
                    align_x=1,
                ),
                rio.IconButton(
                    icon="material/menu",
                    style="plain",
                    align_x=1
                ),
            ),
            fill=self.session.theme.primary_color,
        )