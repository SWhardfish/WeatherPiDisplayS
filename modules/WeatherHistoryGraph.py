# pylint: disable=invalid-name
"""Weather History Graph module
"""
import pandas as pd
from modules.WeatherModule import WeatherModule
from modules.GraphUtils import GraphUtils


class WeatherHistoryGraph(WeatherModule):
    """
    This module records stats historically for display.

    example config:
    {
      "module": "WeatherHistoryGraph",
      "config": {
        "rect": [x, y, width, height],
        "days_ago": 2
      }
     }
    """

    def __init__(self, fonts, location, language, units, config):
        super().__init__(fonts, location, language, units, config)
        #self.days_ago = config["days_ago"] if "days_ago" in config else 0

    def draw(self, screen, weather, updated):
        if weather is None or not updated:
            return

        # Retrieve the data from CSV file
        df = pd.read_csv('GraphData.csv')
        df['xdate'] = pd.to_datetime(df['xdate'])
        new_cases = df

        # Plot
        self.clear_surface()
        #GraphUtils.set_font(self.fonts["name"])
        GraphUtils.draw_2axis_graph(
            screen,
            self.surface,
            self.rect,
            list(new_cases.xdate),
            new_cases.temp,
            "Temp",
            new_cases.press,
            "Press",
            title="Press",
            yscale2="log")
