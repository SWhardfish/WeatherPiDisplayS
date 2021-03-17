# pylint: disable=invalid-name, too-few-public-methods
""" Glaph utility class
"""
import gc
import io
import logging
import threading
import time
import pandas
import pygame
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import StrMethodFormatter
from matplotlib import font_manager

# matplotlib parameters
matplotlib.pyplot.switch_backend("Agg")
matplotlib.rcParams['font.family'] = "arial"

#dpi = 50

# thread lock
lock = threading.Lock()

def synchronized(wrapped):
    """synchronized thread decorator
    """

    def decorator(*args, **kwargs):
        with lock:
            start = time.perf_counter()
            wrapped(*args, **kwargs)
            execution_time = time.perf_counter() - start
            logging.info("%s Execution time: %.2f sec", wrapped.__name__,
                         execution_time)
    return decorator

@synchronized
def _draw_2axis_graph(screen, surface, rect, times, y1, ylabel1, y2, ylabel2,
                      title, yscale1, yscale2):
    # Plot graph
    #df = pandas.read_csv('GraphData.csv', usecols=['xdate', 'temp', 'press', 'rain_1h', 'windspeed'], parse_dates=['xdate'])
    df = pandas.read_csv('GraphData.csv', usecols=['xdate', 'temp'], parse_dates=['xdate'])
    df['xdate'] = pandas.to_datetime(df['xdate'])
    df.set_index('xdate', inplace=True)

    # Create subplots sharing x-axis
    xaxis = df.index
    #x3axis = df.index
    yaxis = df['temp']

    fig, (ax) = plt.subplots(1, 1, sharex=True, figsize=(2.6, 0.18))
    plt.subplots_adjust(hspace=2.0)


    ax.plot(xaxis, yaxis, color='Crimson', linewidth=0.4)

    #ax.set_title('Temperature - °C', loc='center', color='white', size='9')

    #ax.tick_params(axis='x', labelsize=8, colors='white', rotation=0)
    ax.tick_params(axis='y', labelsize=8, colors='white')

    #ax.grid(which='major', axis='both', color='grey', linestyle='dotted', linewidth=0.4)

    # Set ticks every hour
    ax.xaxis.set_major_locator(plt.LinearLocator(6))
    plt.setp(ax.get_xticklabels(), rotation=0, ha='center')

    # Set major ticks format
    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))
    #ax.yaxis.set_major_formatter(StrMethodFormatter(u"{x:.1f} °C"))

    # Convert to pygame image
    f = io.BytesIO()
    #plt.tight_layout()
    plt.savefig(f, format="png", transparent=True, bbox_inches='tight')
    plt.close(fig)
    f.seek(0)
    image = pygame.image.load(f)

    del df
    gc.collect()

    # draw image
    surface.blit(image, (0, 0))
    screen.blit(surface, (rect.left, rect.top))


class GraphUtils:
    """Graph Utility class
    """

    """
    @staticmethod
    def set_font(font):
        """"""set graph text font
        
        if font not in plt.rcParams["font.family"]:
            font_manager.fontManager.ttflist.extend(
                font_manager.createFontList(font_manager.findSystemFonts()))
            plt.rcParams["font.family"] = font
    """

    @staticmethod
    def draw_2axis_graph(screen,
                         surface,
                         rect,
                         times,
                         y1,
                         ylabel1,
                         y2,
                         ylabel2,
                         *,
                         title=None,
                         yscale1=None,
                         yscale2=None):
        """draw 2-axis graph in another thread
        """
        threading.Thread(target=_draw_2axis_graph,
                         args=(screen, surface, rect, times, y1, ylabel1, y2,
                               ylabel2, title, yscale1, yscale2)).start()
