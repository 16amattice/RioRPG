from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *
from pathlib import Path

import rio

from .. import components as comps

class PlayerCard(rio.Component):

    def build(self) -> rio.Component:

        def create_rectangle(icon_name: str, title: str, value: str, value_style: str = "dim", **kwargs) -> rio.Rectangle:
            return rio.Rectangle(
                content=rio.Row(
                    rio.Icon(icon_name),
                    rio.Column(
                        rio.Text(title),
                        rio.Text(value, style=value_style),
                        align_x=0
                    ),
                    margin_left=0.5,
                ),
                margin_top=0.1,
                height=4,
                fill=self.session.theme.neutral_color,
                hover_fill=rio.Color.from_hex("#080808"),
                corner_radius=0.7,
                **kwargs
            )

        def create_progress_rectangle(icon_name: str, title: str, value: str, **kwargs) -> rio.Rectangle:
            return rio.Rectangle(
                content=rio.Row(
                    rio.Icon(icon_name),
                    rio.Column(
                        rio.ProgressBar(
                            progress=1,
                            width="grow"
                        ),
                        rio.Row(
                            rio.Text(title),
                            rio.Spacer(),
                            rio.Text(value, style="dim"),
                        ),
                        margin_left=3,
                        margin_y=1,
                        width="grow",
                    ),
                    rio.Spacer(),
                    margin_left=1,
                ),
                fill=self.session.theme.neutral_color,
                hover_fill=rio.Color.from_hex("#080808"),
                corner_radius=0.7,
                height=4,
                margin_left=0.5,
                **kwargs
            )

        def create_button(icon_name: str, text: str, url: str = "", **kwargs) -> rio.Link:
            return rio.Link(
                rio.Button(
                    rio.Row(
                        rio.Icon(
                            icon=icon_name,
                            align_x=0,
                            height=1.7,
                            width=1.7,
                        ),
                        rio.Text(
                            text,
                            align_x=0,
                        ),
                        align_x=0,
                    ),
                    style=("plain"),
                    align_x=0,
                    **kwargs
                ),
                url,
                align_x=0
            )

        image_path = self.session.assets / 'player_icon.png'

        image_fill = rio.ImageFill(
            image=image_path,
            fill_mode='fit'
        )

        circle_size = 6

        circle_with_image = rio.Rectangle(
            width=0.5,
            height=0.5,
            corner_radius=circle_size / 2,
            fill=image_fill,
            stroke_width=0.4,
            stroke_color=rio.Color.BLACK,
        )

        return rio.Card(
            content=rio.Column(
                rio.Row(
                    circle_with_image,
                    rio.Column(
                        rio.Text("[CD] SlydeMW"),
                        rio.Text("Level 311"),
                        rio.Text("Progress Bar"),
                        rio.Text("11,945 EXP remaining"),
                    ),
                ),
                rio.Separator(),
                rio.Row(
                    rio.Column(
                        create_rectangle("material/currency-bitcoin", "Gold", "116,291"),
                        create_rectangle("material/diamond", "Diamonds", "29", margin_bottom=0.1),
                    ),
                    rio.Column(
                        create_rectangle("material/account-balance", "Bank", "2,436,198"),
                        create_rectangle("material/steps", "Total Steps", "4,141", margin_bottom=0.1),
                    ),
                ),
                rio.Separator(),
                rio.Column(
                    create_progress_rectangle("material/ecg-heart", "Health", "1,630 out of 1,630"),
                    create_progress_rectangle("material/bolt", "Energy", "7 out of 7"),
                    create_progress_rectangle("material/indeterminate-question-box", "Quest Points", "5 out of 5"),
                ),
                rio.Separator(),
                create_button("material/group", "Profile"),
                create_button("material/star-rate", "Membership"),
                create_button("material/payments", "Payments and Invoices"),
                create_button("material/settings", "Settings"),
                create_button("material/logout", "Logout"),
            ),
            corner_radius=1.05,
            width=27
        )