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

        def create_progress_rectangle(icon_name: str, title: str, value: str, color: Optional[rio.Color] = None, **kwargs) -> rio.Rectangle:
            return rio.Rectangle(
                content=rio.Row(
                    rio.Icon(icon_name),
                    rio.Column(
                        rio.ProgressBar(
                            progress=1,
                            width="grow",
                            color=color
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
                    margin_x=1,
                ),
                fill=self.session.theme.neutral_color,
                hover_fill=rio.Color.from_hex("#080808"),
                corner_radius=0.7,
                height=4,
                margin_x=0.5,
                **kwargs
            )

        def create_button(icon_name: str, text: str, url: str = "", **kwargs) -> rio.Link:
            return rio.Rectangle(
                content=rio.Link(
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
                    ),
                    url,
                    align_x=0
                ),
                fill=self.session.theme.neutral_color,
                hover_fill=rio.Color.from_hex("#080808"),
                margin_x=0.5,
                corner_radius=0.7,
                height=3,
                **kwargs
            )

        image_path = self.session.assets / 'player_icon.png'
        bg_path = self.session.assets / 'bg.png'
        circle_size = 6
        
        bg_rectangle = rio.Rectangle(
            width=circle_size,
            height=circle_size,
            fill=rio.ImageFill(image=bg_path, fill_mode='stretch'),
            corner_radius=circle_size,
            stroke_width=0.4,
            stroke_color=rio.Color.BLACK,
        )

        image_rectangle = rio.Rectangle(
            width=circle_size,
            height=circle_size,
            fill=rio.ImageFill(image=image_path, fill_mode='fit'),
            corner_radius=circle_size,
            stroke_width=0.4,
            stroke_color=rio.Color.BLACK,
        )

        circle_with_image = rio.Stack(
            bg_rectangle,
            image_rectangle,
            width=circle_size,
            height=circle_size,
            margin_x=1,
            align_x=0,
            align_y=0
        )
        
        gradient_fill = rio.LinearGradientFill(
            (rio.Color.from_hex("#8A2BE2"), 0.0),
            (rio.Color.from_hex("#FF1493"), 0.33),
            (rio.Color.from_hex("#00EEFF"), 1.0),
            angle_degrees=90.0
        )

        return rio.Card(
            content=rio.Column(
                rio.Row(
                    circle_with_image,
                    rio.Column(
                        rio.Text(
                            "[CD] SlydeMW",
                            align_x=0,
                            style=rio.TextStyle(
                                fill=gradient_fill,  # Use the gradient fill
                            ),
                        ),
                        rio.Text("Level 311", align_x=0,),
                        rio.ProgressBar(1, width="grow", color=rio.Color.from_hex("#006400")),
                        rio.Text("11,945 EXP remaining", align_x=0, style="dim"),
                        width="grow",
                        margin_y=0.5
                    ),
                    rio.Spacer(),
                    margin_y=1,
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
                    create_progress_rectangle("material/ecg-heart", "Health", "1,630 out of 1,630", color=rio.Color.RED),
                    create_progress_rectangle("material/bolt", "Energy", "7 out of 7", color=rio.Color.ORANGE),
                    create_progress_rectangle("material/indeterminate-question-box", "Quest Points", "5 out of 5", color=rio.Color.from_hex("#006400")),
                ),
                rio.Separator(),
                create_button("material/group", "Profile", margin_top=0.2),
                create_button("material/star-rate", "Membership"),
                create_button("material/payments", "Payments and Invoices"),
                create_button("material/settings", "Settings"),
                create_button("material/logout", "Logout", margin_bottom=0.2),
            ),
            corner_radius=1.05,
            width=27
        )
