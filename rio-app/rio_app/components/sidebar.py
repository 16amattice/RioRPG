from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *

import rio

from .. import components as comps

class Sidebar(rio.Component):
    @rio.event.on_page_change
    async def on_page_change(self) -> None:
        await self.force_refresh()

    def build(self) -> rio.Component:
        active_page = self.session.active_page_instances[0]
        active_page_url_segment = active_page.page_url

        def create_link(label: str, icon: str, page_url: str) -> rio.Component:
            return rio.Link(
                rio.Button(
                    rio.Row(
                        rio.Icon(
                            icon,
                            align_x=0,
                        ),
                        rio.Text(
                            label,
                            style=rio.TextStyle(
                                fill=rio.Color.BLACK,
                            ),
                            align_x=0,
                        ),
                        align_x=0,
                    ),
                    style=(
                        "major"
                        if active_page_url_segment == page_url
                        else "plain"
                    ),
                    align_x=0
                ),
                page_url,
                align_x=0
            )

        return rio.Row(
            rio.Rectangle(
                content=rio.Column(
                    rio.Link(
                        rio.IconButton(
                            "rio/logo",
                            style="plain",
                            size=2.5,
                        ),
                        "/",
                    ),
                    rio.Text(
                        "MAIN",
                        style=rio.TextStyle(
                            fill=rio.Color.GREY,
                        ),
                    ),
                    create_link("Home", "material/home", "/news-page"),
                    create_link("Town", "material/map", "/news-page"),
                    create_link("Inventory", "material/backpack", "/news-page"),
                    create_link("Battle", "material/swords", "/news-page"),
                    create_link("Quests", "material/question-mark", "/news-page"),
                    rio.Separator(
                        width="grow"),
                    rio.Text(
                        "CHARACTER",
                        style=rio.TextStyle(
                            fill=rio.Color.GREY,
                        ),
                    ),
                    create_link("Your Character", "material/person", "/news-page"),
                    create_link("Jobs", "material/cases", "/news-page"),
                    create_link("Crafting", "material/build", "/news-page"),
                    create_link("Tasks", "material/exclamation", "/news-page"),
                    create_link("Collections", "material/collections-bookmark", "/news-page"),
                    create_link("Guilds", "material/group", "/news-page"),
                    align_y=0,
                ),
                fill=self.session.theme.neutral_color,
                corner_radius=self.session.theme.corner_radius_medium,
                shadow_radius=0.8,
                shadow_color=self.session.theme.shadow_color,
                shadow_offset_y=0.2,
            ),
            height="grow",
        )
