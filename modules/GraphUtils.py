# pylint: disable=invalid-name, too-few-public-methods
""" Glaph utility class
"""
import gc
import io
import logging
import threading
import time
import numpy as np
import pandas
import pygame
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import StrMethodFormatter
from matplotlib import font_manager
from matplotlib.dates import DateFormatter, DayLocator, HourLocator


# matplotlib parameters
matplotlib.pyplot.switch_backend("Agg")
#plt.style.use("dark_background")
#colormap = plt.get_cmap("Dark2")

dpi = 100

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
    # plot graph
    df = pandas.read_csv('GraphData.csv', usecols=['xdate', 'temp', 'press', 'rain_1h'], parse_dates=['xdate'])
    #print(df)
    df['xdate'] = pandas.to_datetime(df['xdate'])
    df.set_index('xdate', inplace=True)
    print(df.info())
    # Create subplots sharing x axis
    xaxis = df.index
    x3axis = df.index
    yaxis = df['temp']
    y2axis = df['press']
    y3axis = df['rain_1h']

    f, (ax, ax2, ax3) = plt.subplots(3, figsize=(4.9, 3.0))
    plt.subplots_adjust(hspace=2.0)

    #ax = df.plot(use_index=True, y='temp', kind='line', color='blue', legend=False, linewidth=0.5, figsize=(4.9, 1.5))
    ax.plot(xaxis, yaxis, color='red', linewidth=0.4)
    #ax2 = df.plot(use_index=True, y='press', legend=False, color='coral', linewidth=0.5, secondary_y=True, ax=ax)
    ax2.plot(xaxis, y2axis, color='blue', linewidth=0.4)
    ax3.bar(x3axis, y3axis, color='blue', width=0.4)
    ax.set(xlabel='', ylabel='')
    ax2.set(xlabel='', ylabel='')
    ax3.set(xlabel='', ylabel='')
    ax.tick_params(axis='x', labelsize=8, colors='white', rotation=0)
    ax.tick_params(axis='y', labelsize=8, colors='white')
    ax2.tick_params(axis='x', labelsize=8, colors='white', rotation=0)
    ax2.tick_params(axis='y', labelsize=8, colors='white')
    ax3.tick_params(axis='x', labelsize=8, colors='white', rotation=0)
    ax3.tick_params(axis='y', labelsize=8, colors='white')
    #ax.legend(["Temp"], loc='best', fontsize='x-small')
    ax.grid(which='major', axis='both', color='grey', linestyle='dotted', linewidth=0.4)
    ax2.grid(which='major', axis='both', color='grey', linestyle='dotted', linewidth=0.4)
    ax3.grid(which='major', axis='both', color='grey', linestyle='dotted', linewidth=0.4)
    # set ticks every hour
    ax.xaxis.set_major_locator(plt.LinearLocator(6))
    plt.setp(ax.get_xticklabels(), rotation=0, ha='center')
    ax2.xaxis.set_major_locator(plt.LinearLocator(6))
    plt.setp(ax2.get_xticklabels(), rotation=0, ha='center')
    ax3.xaxis.set_major_locator(plt.LinearLocator(6))
    plt.setp(ax3.get_xticklabels(), rotation=0, ha='center')
    # set major ticks format
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))
    ax.yaxis.set_major_formatter(StrMethodFormatter(u"{x:.1f} °C"))
    ax2.yaxis.set_major_formatter(StrMethodFormatter(u"{x:.0f} pa"))
    ax3.yaxis.set_major_formatter(StrMethodFormatter(u"{x:.1f} mm"))
    #plt.xticks(rotation=0, horizontalalignment='center')
    ##ax.set_xticklabels(df.index, rotation=0, ha='center')

    # plt.axes(frameon=True)


    """
    ======
    fig, ax1 = plt.subplots(figsize=(rect.width / dpi, rect.height / dpi))

    #if title:
    #    plt.title(title)
    if y1 is not None:
        #if ylabel1:
            #ax1.yaxis.label.set_color(colormap(0))
            #ax1.set_ylabel(ylabel1)
        if yscale1:
            ax1.set_yscale(yscale1)
        if sum(x is not np.nan for x in y1) > 0:
            ax1.plot(times, y1, color='blue', linewidth=0.5)
    if y2 is not None:
        ax2 = ax1.twinx()
        #if ylabel2:
         #   ax2.yaxis.label.set_color(colormap(1))
          #  ax2.set_ylabel(ylabel2)
        if yscale2:
            ax2.set_yscale(yscale2)
        if sum(x is not np.nan for x in y2) > 0:
            ax2.plot(times, y2, color='red', linewidth=0.5)
            ax2.xaxis.set_major_locator(plt.LinearLocator(6))
            ax2.tick_params(axis='y2', labelsize=8, colors='white')

    # setting tics
    #ax1.xaxis.set_major_formatter(DateFormatter("%m-%d"))
    #if (max(times) - min(times)).days <= 7:
     #   if (max(times) - min(times)).days > 1:
    #ax1.xaxis.set_major_locator(DayLocator())
    #ax1.xaxis.set_major_locator(HourLocator(24))
    ax1.set(xlabel='', ylabel='')
    ax1.tick_params(axis='x', labelsize=8, colors='white')
    ax1.tick_params(axis='y2', labelsize=8, colors='white')
    ax1.tick_params(axis='y', labelsize=8, colors='white')
    #ax1.legend(["Temp"], loc='best', fontsize='x-small')
    #ax1.legend(["Pres"], loc='best', fontsize='x-small')
    ax1.xaxis.set_major_locator(plt.LinearLocator(6))
    #ax2.xaxis.set_major_locator(plt.LinearLocator(6))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%I %p'))
    ax1.yaxis.set_major_formatter(StrMethodFormatter(u"{x:.1f} °C"))
    ax2.yaxis.set_major_formatter(StrMethodFormatter(u"{x:.1f} pa"))
      #  else:
      #      ax1.xaxis.set_major_locator(HourLocator(interval=24))
      #      ax1.xaxis.set_minor_locator(HourLocator(interval=6))
    """
    # convert to pygame image
    f = io.BytesIO()
    plt.tight_layout()
    plt.savefig(f, format="png", transparent=True, bbox_inches='tight')
    plt.close
    f.seek(0)
    image = pygame.image.load(f)
    print(df.info())
    ###del df
    ###gc.collect()
    ###df = pandas.DataFrame

    # draw image
    surface.blit(image, (0, 0))
    screen.blit(surface, (rect.left, rect.top))


class GraphUtils:
    """Graph Utility class
    """

    @staticmethod
    def set_font(font):
        """set graph text font
        """
        if font not in plt.rcParams["font.family"]:
            font_manager.fontManager.ttflist.extend(
                font_manager.createFontList(font_manager.findSystemFonts()))
            plt.rcParams["font.family"] = font

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
