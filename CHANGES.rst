Changelog
---------

Package `calplot <https://pypi.org/project/calplot/>`_ is a fork of `calmap <https://github.com/martijnvermaat/calmap>`_ 0.0.7-dev with the following changes and additions.

Todo

- Added argument :code:`weekstart` for function :code:`yearplot` to specify the index representing the `day of week <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DatetimeIndex.dayofweek.html>`_ of the first day in each week in the generated plot. Defaults to `0`, which represents Monday.

Since version 0.1.7 (Mar 3, 2021):

- Added argument :code:`tight_layout` for function :code:`calplot` to specify whether to use tight layout for the figure. Defaults to :code:`True`.
- Added argument :code:`monthlabeloffset` for function :code:`yearplot` to specify day offset for month labels to adjust the horizontal alignment of labels. Defaults to :code:`15`.
- Added argument :code:`suptitle_kws` for function :code:`calplot` to specify arguments to Matplotlib :code:`suptitle` call. Defaults to empty dict.
- Changed argument :code:`colorbar` default to :code:`None`.
- Changed argument :code:`dropzero` default to :code:`None`.

Since version 0.1.6 (Dec 24, 2020):

- Added argument :code:`textformat` for function :code:`yearplot` to specify the text format string for grid cell text. Defaults to :code:`None`.
- Added argument :code:`textfiller` for function :code:`yearplot` to specify the fallback text for grid cell text. Defaults to empty string.
- Added argument :code:`textcolor` for function :code:`yearplot` to specify the text color for grid cell text. Defaults to :code:`black`.

Since version 0.1.5 (Dec 23, 2020):

- Added argument :code:`edgecolor` for function :code:`yearplot` to specify color of seperation lines between months. Defaults to :code:`gray`. Note that lines can be turned off by setting the argument to :code:`None` without quotes.

Since version 0.1.3 (Aug 17, 2020):

- Removed legacy code for compatibility to fix a FutureWarning in :code:`yearplot`. Note that :code:`pandas>=1` is now required to install the package.

Since version 0.1.2 (Jan 15, 2020):

- Added argument :code:`dropzero` for function :code:`yearplot` to specify whether to not fill a cell with a color for days with a zero value. Defaults to :code:`False`.

Since version 0.1.1 (Jan 15, 2020):

- Renamed function :code:`calendarplot` to :code:`calplot`.
- Added argument :code:`colorbar` for function :code:`calplot` to display a colorbar to the right of the heatmap if more than one unique values in plot. Defaults to :code:`True`.
- Added argument :code:`figsize` for function :code:`calplot`. Defaults to a tighter layout automatically adjusted to fit the number of years in plot.
- Added argument :code:`suptitle` for function :code:`calplot`. Defaults to :code:`None`.
- Changed default colormap :code:`cmap` for function :code:`calplot` to :code:`viridis`.
