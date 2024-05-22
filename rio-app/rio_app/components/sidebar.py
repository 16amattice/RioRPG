from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *  # type: ignore

import rio

from .. import components as comps


class Sidebar(rio.Component):
    expanded: bool

    @rio.event.on_page_change
    async def on_page_change(self) -> None:
        await self.force_refresh()

    def build(self) -> rio.Component:
        active_page = self.session.active_page_instances[0]
        active_page_url_segment = active_page.page_url

        def create_link(label: str, icon: str, page_url: str) -> rio.Component:
            if self.expanded:
                return rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Icon(
                                icon,
                                align_x=0,
                                height=1.7,
                                width=1.7,
                            ),
                            rio.Text(
                                label,
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
            else:
                return rio.Link(
                    rio.IconButton(
                        icon=icon,
                        style=(
                            "major"
                            if active_page_url_segment == page_url
                            else "plain"
                        ),
                        align_x=0,
                        size=3
                    ),
                    page_url,
                    align_x=0
                )

        main_text = rio.Text(
            "MAIN",
            style=rio.TextStyle(
                fill=rio.Color.GREY,
            ),
        ) if self.expanded else rio.Spacer()

        character_text = rio.Text(
            "CHARACTER",
            style=rio.TextStyle(
                fill=rio.Color.GREY,
            ),
        ) if self.expanded else rio.Spacer()
        
        logo_link = rio.Link(
            rio.IconButton(
                "rio/logo",
                style="plain",
                size=2.5,
            ),
        "/",
        ) if self.expanded else rio.Spacer(
            height=3.5
        )

        return rio.Row(
            rio.Rectangle(
                content=rio.Column(
                    logo_link,
                    main_text,
                    create_link("Home", "material/home", "/"),
                    create_link("Town", "material/map", "/news-page"),
                    create_link("Inventory", "material/backpack", "/news-page"),
                    create_link("Battle", "material/swords", "/news-page"),
                    create_link("Quests", "material/question-mark", "/news-page"),
                    rio.Separator(width="grow"),
                    character_text,
                    create_link("Your Character", "material/person", "/news-page"),
                    create_link("Jobs", "material/cases", "/news-page"),
                    create_link("Crafting", "material/build", "/news-page"),
                    create_link("Tasks", "material/exclamation", "/news-page"),
                    create_link("Collections", "material/collections-bookmark", "/news-page"),
                    create_link("Guilds", "material/group", "/news-page"),
                    align_y=0,
                ),
                fill=self.session.theme.primary_color,
            ),
            height="grow",
        )
