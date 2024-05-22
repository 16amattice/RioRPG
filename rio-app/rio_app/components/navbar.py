from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *

import rio

from .. import components as comps

class Navbar(rio.Component):
    @rio.event.on_page_change
    async def on_page_change(self) -> None:
        await self.force_refresh()

    example_state: str = "For demonstration purposes"
    def build(self) -> rio.Component:
        return rio.Row(
            rio.IconButton(
                icon="material/menu",
                align_x=0,
                margin_left=1,
                style="plain"
            )
        )

   