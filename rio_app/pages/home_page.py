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
        return rio.Column(
            rio.Spacer(),
            rio.Image(
                image=self.session.assets / 'home_bg.png',
                fill_mode='zoom',
                height=25,
                corner_radius=0.8
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