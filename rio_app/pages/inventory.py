from __future__ import annotations

from typing import *

import rio

import requests

def fetch_inventory():
    response = requests.get('http://127.0.0.1:8001/inventory')
    response.raise_for_status()
    return response.json()['items']

class Inventory(rio.Component):
    def build(self) -> rio.Component:
        if not hasattr(self, 'all_checked'):
            self.all_checked = False
            
        if not hasattr(self, 'item_checked'):
            items = fetch_inventory()
            self.item_checked = [self.all_checked] * len(items)
            
        if not hasattr(self, 'sort_column'):
            self.sort_column = 0
            
        if not hasattr(self, 'sort_ascending'):
            self.sort_ascending = True

        async def toggle_all_checkboxes(event: rio.CheckboxChangeEvent):
            value = event.is_on
            self.all_checked = value
            self.item_checked = [value] * len(self.item_checked)
            await self.force_refresh()

        async def toggle_item_checkbox(index: int, event: rio.CheckboxChangeEvent):
            value = event.is_on
            self.item_checked[index] = value
            if not value:
                self.all_checked = False
            await self.force_refresh()
            
        async def sort_items(column_index: int):
            self.sort_column = column_index
            self.sort_ascending = not self.sort_ascending
            await self.force_refresh()
            
        def safe_key(item, column_index):
            value = item[column_index]
            if value is None:
                return ""
            try:
                return float(value)
            except ValueError:
                return value
            
        def get_sorted_items(items):
            sorted_items = sorted(items, key=lambda x: safe_key(x, self.sort_column), reverse=not self.sort_ascending)
            return sorted_items
            
        items = fetch_inventory()
        sorted_items = get_sorted_items(items)

        if not self.item_checked:
            self.item_checked = [self.all_checked] * len(items)
            
        grid = rio.Grid(row_spacing=0.5, column_spacing=1,)
        
        headers = ["Select", "Qty", "Name", "Level", "Value", "Type", "Stats"]
        grid.add(rio.Rectangle(fill=rio.Color.from_hex("#1c1c1c")), row=0, column=0, width=len(headers))

        grid.add(
            rio.Checkbox(is_on=self.all_checked, on_change=toggle_all_checkboxes),
            row=0,
            column=0
        )
        
        header_to_index = {
            "Select": None,
            "Qty": 2,
            "Name": 1,
            "Level": 3,
            "Value": 4,
            "Type": 5,
            "Stats": 6
        }
        
        def create_header_listener(col_index: int) -> rio.Component:
            return rio.MouseEventListener(
                content=rio.Text(
                    headers[col_index] + (" ▲" if self.sort_column == header_to_index[headers[col_index]] and self.sort_ascending else " ▼" if self.sort_column == header_to_index[headers[col_index]] else ""),
                    style=rio.TextStyle(
                        font_weight="bold",
                        fill=rio.Color.from_hex("#4f46e5"),
                    ),
                ),
                on_press=lambda event: sort_items(header_to_index[headers[col_index]]),
            )
        
        for col_index in range(1, len(headers)):
            grid.add(create_header_listener(col_index), row=0, column=col_index,)
        
        grid.add(rio.Separator(align_y=0), row=1, column=0, width=len(headers))

        for row_index, item in enumerate(sorted_items, start=1):
            grid.add(
                rio.Checkbox(
                    is_on=self.item_checked[row_index - 1],
                    on_change=lambda event, idx=row_index-1: toggle_item_checkbox(idx, event)
                ),
                row=row_index * 2,
                column=0
            )
            grid.add(rio.Text(str(item[2])), row=row_index * 2, column=1)
            grid.add(rio.Text(item[1]), row=row_index * 2, column=2)
            grid.add(rio.Text(str(item[3])), row=row_index * 2, column=3)
            grid.add(rio.Text(f"{item[4]:.2f}"), row=row_index * 2, column=4)
            grid.add(rio.Text(item[5]), row=row_index * 2, column=5)
            grid.add(rio.Text(item[6] if item[6] else "N/A"), row=row_index * 2, column=6)
            if row_index < len(sorted_items):
                grid.add(rio.Separator(align_y=0), row=row_index * 2 + 1, column=0, width=len(headers),)

        return rio.Row(
            rio.Spacer(
                width=15,    
            ),
            rio.Column(
                rio.Row(  
                    height="grow",
                ),
                rio.Rectangle(
                    content=rio.Row(
                        rio.Column(
                            rio.Text("Item Name"),
                            rio.TextInput(label="Example: Stick"),
                            margin_x=0.8
                        ),
                        rio.Column(
                            rio.Text("Minimum Level"),
                            rio.TextInput(label="Example: 1"),
                            margin_x=0.8
                        ),
                        rio.Column(
                            rio.Text("Maximum Level"),
                            rio.TextInput(label="Example: 100"),
                            margin_x=0.8
                        ),
                        rio.Column(
                            rio.Text("Rarity"),
                            rio.Button(),
                            margin_x=0.8
                        ),
                        rio.Column(
                            rio.Text("Item Type"),
                            rio.Button(),
                            margin_x=0.8
                        ),
                        margin_y=0.8,
                    ),
                    fill=rio.Color.from_hex("#1c1c1c"),
                    corner_radius=0.6,
                    height=6,
                ),
                rio.Rectangle(
                    content=grid,
                    fill=self.session.theme.background_color,
                    stroke_color=self.session.theme.primary_color,
                    stroke_width=0.1,     
                    corner_radius=0.2,
                    margin_y=3,

                ),
                width="grow",
                height="grow",
            ),
            rio.Spacer(
                width=15,    
            ),
        )

