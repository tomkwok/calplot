Calendar heatmaps from Pandas time series data
==============================================

Calplot creates heatmaps from Pandas time series data.

Plot `Pandas <http://pandas.pydata.org/>`_ time series data sampled by day in
a heatmap per calendar year, similar to GitHub's contributions plot, using
`matplotlib <http://matplotlib.org/>`_.

With default configuration:

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_edgecolor_default.png
    :alt: Example calendar heatmap with default configuration

With arguments :code:`edgecolor=None`, :code:`cmap='YlGn'`:

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_edgecolor_None.png
    :alt: Example calendar heatmap with edgecolor set to None

With arguments :code:`yearcolor=black`, :code:`cmap='YlGn'`:

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_yearcolor_black.png
    :alt: Example calendar heatmap with yearcolor set to black

With arguments :code:`dropzero=False`, :code:`cmap='YlGn'`:

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_dropzero_False.png
    :alt: Example calendar heatmap with dropzero set to False

With arguments :code:`linewidth=0`, :code:`cmap='YlGn'`:

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_linewidth_zero.png
    :alt: Example calendar heatmap with linewidth set to 0


Usage
-----

See the `documentation <https://calplot.readthedocs.io/en/latest/>`_.

Code to generate the first example:

.. code-block:: python

    import calplot
    import numpy as np; np.random.seed(sum(map(ord, 'calplot')))
    import pandas as pd
    all_days = pd.date_range('1/1/2019', periods=730, freq='D')
    days = np.random.choice(all_days, 500)
    events = pd.Series(np.random.randn(len(days)), index=days)
    calplot.calplot(events)

Installation
------------

To install the latest release via PyPI using pip::

    pip install calplot


Changelog
---------

Package `calplot <https://pypi.org/project/calplot/>`_ is a fork of `calmap <https://github.com/martijnvermaat/calmap>`_ 0.0.7-dev with the following changes and additions.

Since version 0.1.5 (Dec 2020):

- Added argument :code:`edgecolor` for function :code:`calplot` and :code:`yearplot` to specify color of seperation lines between months. Defaults to :code:`gray`. Note that lines can be turned off by setting argument to :code:`None` without quotes.

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

Todo
----

- Option to plot a rounded value for the day, or to plot the day of month for each mesh grid cell.
