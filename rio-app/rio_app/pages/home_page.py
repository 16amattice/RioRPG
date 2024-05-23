from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *  # type: ignore

import rio

from .. import components as comps

class HomePage(rio.Component):
    """
    A sample page, containing a greeting and some testimonials.
    """

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Spacer(),
            rio.Row(
                comps.InformationCard(
                    "material/group",
                    "Jane Doe",
                    "CTO, Synergistic Solutions LLC",
                ),
                comps.InformationCard(
                    "material/group",
                    "Made Up Rick",
                    "CEO, Imaginary Industries",
                ),
                comps.InformationCard(
                    "material/group",
                    "John Doe",
                    "CEO, HyperTech Corp.",
                ),
                spacing=0.5,
                align_x=0.5,
            ),
            rio.Row(
                comps.PlayerCard(),
                rio.Spacer(),
            ),
            spacing=2,
            width=60,
            align_x=0.5,
            align_y=0,
        )

