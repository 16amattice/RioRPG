from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *

import rio

from .. import components as comps

class Navbar(rio.Component):

    example_state: str = "For demonstration purposes"
    def build(self) -> rio.Component:
        return rio.Text(self.example_state)

   