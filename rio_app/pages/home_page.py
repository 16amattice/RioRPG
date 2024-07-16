from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *

import rio

from .. import components as comps

class HomePage(rio.Component):
    """
    A sample page, containing a greeting and some testimonials.
    """

    def build(self) -> rio.Component:
        image_path = self.session.assets / 'player_icon.png'
        return rio.Column(
            rio.Spacer(),
            rio.Stack(
                rio.Image(
                    image=self.session.assets / 'home_bg.png',
                    fill_mode='zoom',
                    height=25,
                    corner_radius=0.6
                ),
                rio.Rectangle(
                    content=rio.Column(
                        rio.Image(
                            image_path,
                        ),
                        rio.Text("The start of your journey"),
                        rio.Text("With just a press of a button, you can embark on an adventure of a lifetime."),
                        rio.Spacer(),
                        rio.Button(
                            content=rio.Row(
                                rio.Icon("material/ads-click", fill=rio.Color.WHITE),
                                rio.Text(
                                    "Press here to start",
                                    style=rio.TextStyle(
                                        fill=rio.Color.WHITE,
                                    ),
                                ),
                            ),
                            color=rio.Color.from_hex("#0e9f6e"),
                            shape="rounded",
                            height=3,
                            #width=3,
                            margin_x=13,
                            margin_bottom=2,
                        ),
                    ),
                    fill=rio.FrostedGlassFill(rio.Color.from_rgb(0,0,0,0.6), 0.3),
                    margin_x=15,
                    margin_y=3,
                    corner_radius=0.6     
                ),
            ),
            rio.Spacer(),
            rio.Row(
                comps.InformationCard(
                    "material/group",
                    "374",
                    "Players Online",
                    "View Players",
                    "/players"
                ),
                comps.InformationCard(
                    "material/face",
                    "7%",
                    "Donation Goal",
                    "Make a Donation",
                    "/donation"
                ),
                comps.InformationCard(
                    "material/check-circle",
                    "0",
                    "Tasks Completed",
                    "View Tasks",
                    "/tasks"
                ),
                comps.InformationCard(
                    "material/diamond",
                    "29",
                    "Gems Remaining",
                    "Go To Shop",
                    ""
                ),
                spacing=0.5,
                align_x=0.5,
            ),
            rio.Row(
                #comps.PlayerCard(),
                rio.Spacer(),
            ),
            spacing=2,
            width=20,
            align_x=0.5,
            align_y=0,
        )