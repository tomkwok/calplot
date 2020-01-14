Calendar heatmaps from Pandas time series data
==============================================

Calplot creates heatmaps from Pandas time series data.

Plot `Pandas <http://pandas.pydata.org/>`_ time series data sampled by day in
a heatmap per calendar year, similar to GitHub's contributions plot, using
`matplotlib <http://matplotlib.org/>`_.

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/calplot.png
    :alt: Example calendar heatmap


Package `calplot <https://pypi.org/project/calplot/>`_ is a fork of `calmap <https://github.com/martijnvermaat/calmap>`_ with the following changes and additions.

- :code:`pandas>=0.18` is now required to install the package. Legacy code for compatibility removed. Fixed a FutureWarning in :code:`yearplot`.
- Function :code:`calendarplot` renamed to :code:`calplot`.
- Argument :code:`colorbar` added for function :code:`calplot` to display a colorbar to the right of the heatmap if more than one unique values in plot. Defaults to :code:`True`.
- Argument :code:`dropzero` added for function :code:`calplot` and :code:`yearplot` to specify whether to not fill a cell with a color for days with a zero value. Defaults to :code:`True`.
- Argument :code:`figsize` added for function :code:`calplot`. Defaults to a tighter layout automatically adjusted to fit the number of years in plot.
- Argument :code:`suptitle` added for function :code:`calplot`. Defaults to :code:`None`.
- Argument :code:`yearcolor` added for function :code:`calplot`. Defaults to :code:`lightgray` (in contrast to :code:`whitesmoke`, the default value for :code:`fillcolor`).
- Default colormap :code:`cmap` for :code:`yearplot` (and hence :code:`calplot`) changed to :code:`viridis`.

Usage
-----

See the `documentation <https://pythonhosted.org/calplot>`_.


Installation
------------

To install the latest release via PyPI using pip::

    pip install calplot

Todo
----

- Option to add a seperating line between months.
- Option to plot a rounded value for the day or plot the day of month for each mesh grid cell.
- Option to change horizontal alignment (for example, to the left) for month labels.
- Fix :code:`figsize` for :code:`yearplot`.
- Fix colorbar misalignment for plots with different :code:`dpi` values.
