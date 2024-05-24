from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import * 
from pathlib import Path

import rio

from .. import components as comps


class PlayerCard(rio.Component):
    
    def build(self) -> rio.Component:
        
        image_path = self.session.assets / 'player_icon.png'

        image_fill = rio.ImageFill(
            image=image_path,
            fill_mode='fit'
        )

        circle_size = 5

        circle_with_image = rio.Rectangle(
            width=circle_size,
            height=circle_size,
            corner_radius=circle_size / 2,
            fill=image_fill,
            stroke_width=2.0,
            stroke_color=rio.Color.BLACK,
        )
        
        return rio.Card(
            content = rio.Column(
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
                        rio.Card(
                            content= rio.Row(
                                rio.Icon("material/currency-bitcoin"),
                                rio.Column(
                                    rio.Text("Gold"),    
                                    rio.Text("116,291", style="dim",),
                                    align_x=0    
                                ),    
                            ),
                            colorize_on_hover=True,
                            margin_left=0.5,
                            margin_top=0.1,
                            height=4
                        ),
                        rio.Card(
                            content= rio.Row(
                                rio.Icon("material/diamond"),
                                rio.Column(
                                    rio.Text("Diamonds"),    
                                    rio.Text("29", style="dim",),
                                    align_x=0    
                                ),    
                            ),
                            colorize_on_hover=True,   
                            margin_left=0.5,
                            margin_bottom=0.1,
                            height=4     
                        ),
                    ),
                    rio.Column(
                        rio.Card(
                            content= rio.Row(
                                rio.Icon("material/account-balance"),
                                rio.Column(
                                    rio.Text("Bank"),    
                                    rio.Text("2,436,198", style="dim",),    
                                    align_x=0
                                ),    
                            ),    
                            colorize_on_hover=True,  
                            margin_right=0.5,
                            margin_top=0.1,  
                        ),
                        rio.Card(
                            content= rio.Row(
                                rio.Icon("material/steps"),
                                rio.Column(
                                    rio.Text("Total Steps"),    
                                    rio.Text("4,141", style="dim",),   
                                    align_x=0 
                                ),    
                            ),    
                            colorize_on_hover=True,    
                            margin_right=0.5,
                            margin_bottom=0.1,
                        ),
                    ),
                ),
                
                rio.Separator(),
                rio.Column(
                    rio.Card(
                        content = rio.Row(
                            rio.Icon("material/group"),    
                            rio.Column(
                                rio.Text("Progress Bar"),
                                rio.Row(
                                    rio.Text("Health"),
                                    rio.Text("1,630 out of 1,630"),
                                ),
                            ),
                        ),
                        margin_top=0.5,
                        margin_y=0.5   
                    ),
                    rio.Card(
                        content = rio.Row(
                            rio.Icon("material/group"),    
                            rio.Column(
                                rio.Text("Progress Bar"),
                                rio.Row(
                                    rio.Text("Energy"),
                                    rio.Text("7 out of 7"),
                                ),
                            ),
                        ),  
                    ),
                    rio.Card(
                        content = rio.Row(
                            rio.Icon("material/group"),    
                            rio.Column(
                                rio.Text("Progress Bar"),
                                rio.Row(
                                    rio.Text("Quest Points"),
                                    rio.Text("5 out of 5"),
                                ),
                            ),
                        ),  
                    ),
                ),
                rio.Separator(),
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Icon(
                                icon="material/group",
                                align_x=0,
                                height=1.7,
                                width=1.7,
                            ),
                            rio.Text(
                                "Profile",
                                align_x=0,
                            ),
                            align_x=0,
                        ),
                        style=(
                            "plain"
                        ),
                        align_x=0
                    ),
                    "",
                    align_x=0
                ),
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Icon(
                                icon="material/star-rate",
                                align_x=0,
                                height=1.7,
                                width=1.7,
                            ),
                            rio.Text(
                                "Membership",
                                align_x=0,
                            ),
                            align_x=0,
                        ),
                        style=(
                            "plain"
                        ),
                        align_x=0
                    ),
                    "",
                    align_x=0
                ),
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Icon(
                                icon="material/payments",
                                align_x=0,
                                height=1.7,
                                width=1.7,
                            ),
                            rio.Text(
                                "Payments and Invoices",
                                align_x=0,
                            ),
                            align_x=0,
                        ),
                        style=(
                            "plain"
                        ),
                        align_x=0
                    ),
                    "",
                    align_x=0
                ),
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Icon(
                                icon="material/settings",
                                align_x=0,
                                height=1.7,
                                width=1.7,
                            ),
                            rio.Text(
                                "Settings",
                                align_x=0,
                            ),
                            align_x=0,
                        ),
                        style=(
                            "plain"
                        ),
                        align_x=0
                    ),
                    "",
                    align_x=0
                ),
                rio.Link(
                    rio.Button(
                        rio.Row(
                            rio.Icon(
                                icon="material/logout",
                                align_x=0,
                                height=1.7,
                                width=1.7,
                            ),
                            rio.Text(
                                "Logout",
                                align_x=0,
                            ),
                            align_x=0,
                        ),
                        style=(
                            "plain"
                        ),
                        align_x=0
                    ),
                    "",
                    align_x=0
                ),
                
                
            ),
            corner_radius=1.05,
            width=27
        )