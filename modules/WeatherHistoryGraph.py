# pylint: disable=invalid-name
"""Weather History Graph module
"""

import datetime
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
        self.days_ago = config["days_ago"] if "days_ago" in config else 0

    def draw(self, screen, weather, updated):
        if weather is None or not updated:
            return

        # Retrieve the data
        df = pd.read_csv('GraphData.csv')
        #print(df)
        #df = df.reset_index(drop=True, inplace=True)
        #df["xdate"] = pd.to_datetime(df["xdate"])
        #df["人数"] = 1
        #new_cases = pd.DataFrame(df.groupby("date"))
        df['xdate'] = pd.to_datetime(df['xdate'])
        new_cases = df
        #print(df)
        #print(new_cases)

        #total_cases = new_cases.cumsum()
        #total_cases = 100

        # Filter the data
        #if self.days_ago > 0 and self.days_ago < len(new_cases):
         #   start = new_cases.tail(1).date - datetime.timedelta(days=self.days_ago)
          #  new_cases = new_cases[new_cases.index >= start]
            #total_cases = total_cases[total_cases.index >= start]

        # Total cases and doubling time of new cases
        #total = total_cases.tail(1)["人数"][0]
        #dt = 70 / (new_cases.tail(5)["人数"].mean() /
        #           total_cases.tail(2)["人数"][0] * 100)
        #total = total_cases

        # Plot
        self.clear_surface()
        GraphUtils.set_font(self.fonts["name"])
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
