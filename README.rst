Calendar heatmaps from Pandas time series data
==============================================

Calplot creates heatmaps from Pandas time series data.

Plot `Pandas <http://pandas.pydata.org/>`_ time series data sampled by day in
a heatmap per calendar year, similar to GitHub's contributions plot, using
`matplotlib <http://matplotlib.org/>`_.

Installation
------------

To install the latest release via PyPI using :code:`pip`::

    pip install calplot

Usage
-----

For detailed usage of this library, refer to the `documentation <https://calplot.readthedocs.io/en/latest/>`_.

The following examples are run in a `Jupyter notebook <https://jupyter.org/>`_.

.. code-block:: python

    import calplot
    import numpy as np; np.random.seed(sum(map(ord, 'calplot')))
    import pandas as pd
    all_days = pd.date_range('1/1/2019', periods=730, freq='D')
    days = np.random.choice(all_days, 500)
    events = pd.Series(np.random.randn(len(days)), index=days)
    calplot.calplot(events)

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_edgecolor_default.svg
    :alt: Example calendar heatmap with default configuration

.. code-block:: python

    all_days = pd.date_range('1/1/2019', periods=360, freq='D')
    days = np.random.choice(all_days, 500)
    events = pd.Series(np.random.randn(len(days)), index=days)
    calplot.calplot(events, edgecolor=None, cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_edgecolor_None.svg
    :alt: Example calendar heatmap with edgecolor set to None

.. code-block:: python

    calplot.calplot(events, yearcolor=black, cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_yearcolor_black.svg
    :alt: Example calendar heatmap with yearcolor set to black

.. code-block:: python

    calplot.calplot(events, textformat='{:.0f}', textfiller='-', cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_textformat.svg
    :alt: Example calendar heatmap with textformat and textfiller set

.. code-block:: python

    calplot.calplot(events, dropzero=False, cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_dropzero_False.svg
    :alt: Example calendar heatmap with dropzero set to False

.. code-block:: python

    calplot.calplot(events, colorbar=False, suptitle='Random data from standard normal distribution', cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_colorbar_False_suptitle.svg
    :alt: Example calendar heatmap with colorbar set to False and suptitle set

.. code-block:: python

    calplot.calplot(events, linewidth=0, cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_linewidth_zero.svg
    :alt: Example calendar heatmap with linewidth set to 0


Changelog
---------

Package `calplot <https://pypi.org/project/calplot/>`_ is a fork of `calmap <https://github.com/martijnvermaat/calmap>`_ 0.0.7-dev with the following changes and additions.

Todo

- Adding argument :code:`startday` for function :code:`calplot` and :code:`yearplot` to specify the index representing the `day of week <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.dayofweek.html>`_ of the first day in each week in the generated plot. Defaults to `0`, which represents Monday. (Implementation of this require non-trivial change to existing code that is inherited from calmap or taken from other projects, including code for pivoting of by_days DataFrame, and for calculation of polygon coordinates for month borders, in addition to new code to handle the ordering of items in :code:`daylabels` list.)

Since version 0.1.6 (Dec 2020):

- Added argument :code:`textformat` for function :code:`calplot` and :code:`yearplot` to specify the text format string for grid cell text. Defaults to empty string. Note that text plotting is turned off by setting the argument to empty string.
- Added argument :code:`textfiller` for function :code:`calplot` and :code:`yearplot` to specify the fallback text for grid cell text. Defaults to empty string.
- Added argument :code:`textcolor` for function :code:`calplot` and :code:`yearplot` to specify the text color for grid cell text. Defaults to :code:`black`.

Since version 0.1.5 (Dec 2020):

- Added argument :code:`edgecolor` for function :code:`calplot` and :code:`yearplot` to specify color of seperation lines between months. Defaults to :code:`gray`. Note that lines can be turned off by setting the argument to :code:`None` without quotes.

Since version 0.1.3 (Aug 2020):

- Removed legacy code for compatibility to fix a FutureWarning in :code:`yearplot`. Note that :code:`pandas>=1.1` is now required to install the package.

Since version 0.1.2 (Jan 2020):

- Added argument :code:`dropzero` for function :code:`calplot` and :code:`yearplot` to specify whether to not fill a cell with a color for days with a zero value. Defaults to :code:`True`.

Since version 0.1.1 (Jan 2020):

- Renamed function :code:`calendarplot` to :code:`calplot`.
- Added argument :code:`colorbar` for function :code:`calplot` to display a colorbar to the right of the heatmap if more than one unique values in plot. Defaults to :code:`True`.
- Added argument :code:`figsize` for function :code:`calplot`. Defaults to a tighter layout automatically adjusted to fit the number of years in plot.
- Added argument :code:`suptitle` for function :code:`calplot`. Defaults to :code:`None`.
- Added argument :code:`yearcolor` for function :code:`calplot`. Defaults to :code:`lightgray`. Note that the default color is in contrast to :code:`whitesmoke`, which is the default value for :code:`fillcolor`.
- Added argument :code:`monthlabelha` for function :code:`calplot` and :code:`yearplot` to specify horizontal alignment for month labels. Defaults to :code:`center`.
- Changed default colormap :code:`cmap` for function :code:`calplot` to :code:`viridis`.
