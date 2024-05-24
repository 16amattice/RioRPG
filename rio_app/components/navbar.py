from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *

import rio

from .. import components as comps

class Navbar(rio.Component):
    toggle_sidebar: Callable[[], None]
    is_popup_open: bool = False

    @rio.event.on_page_change
    async def on_page_change(self) -> None:
        await self.force_refresh()
        
    async def toggle_popup(self, event: rio.PressEvent) -> None:
        self.is_popup_open = not self.is_popup_open
        await self.force_refresh()
        
    def build(self) -> rio.Component:
        image_path = self.session.assets / 'player_icon.png'
        bg_path = self.session.assets / 'bg.png'
        circle_size = 2.5
        
        bg_rectangle = rio.Rectangle(
            width=circle_size,
            height=circle_size,
            fill=rio.ImageFill(image=bg_path, fill_mode='stretch'),
            corner_radius=circle_size,
        )

        image_rectangle = rio.Rectangle(
            width=circle_size,
            height=circle_size,
            fill=rio.ImageFill(image=image_path, fill_mode='fit'),
            corner_radius=circle_size,
        )

        circle_with_image = rio.MouseEventListener(
            content=rio.Stack(
                bg_rectangle,
                image_rectangle,
                width=circle_size,
                height=circle_size,
                margin_x=0.5,
                margin_y=1
            ),
            on_press=self.toggle_popup,
        )

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
                        style="major",
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
                            rio.Text("Diamond Store"),
                        ),
                        style="plain",
                        shape="rectangle"
                    ),
                    "about/",
                    margin_x=1,
                    margin_y=0.5,
                ),
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Text("Support"),
                        ),
                        style="plain",
                        shape="rectangle"
                    ),
                    "about/",
                    margin_x=1,
                    margin_y=0.5,
                ),
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Text("Community"),
                        ),
                        style="plain",
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
                
                rio.Popup(
                    anchor=circle_with_image,
                    content=comps.PlayerCard(),
                    direction='bottom',
                    is_open=self.is_popup_open,
                ),
            ),
            fill=self.session.theme.primary_color,
        )
