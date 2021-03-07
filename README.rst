Calendar heatmaps from Pandas time series data
==============================================

|build| |lgtm| |sonar| |license| |pypi| |downloads|

.. |build| image:: https://github.com/tomkwok/calplot/workflows/calplot/badge.svg
    :alt: Build status

.. |lgtm| image:: https://img.shields.io/lgtm/grade/python/g/tomkwok/calplot.svg?logo=lgtm&logoWidth=18
    :alt: Code quality
    :target: https://lgtm.com/projects/g/tomkwok/calplot/latest/files/

.. |sonar| image:: https://img.shields.io/sonar/tech_debt/tomkwok_calplot?logo=sonarsource&server=https%3A%2F%2Fsonarcloud.io
    :alt: Maintainability rating
    :target: https://sonarcloud.io/dashboard?id=tomkwok_calplot

.. |license| image:: https://img.shields.io/pypi/l/calplot?color=green
    :alt: License
    :target: LICENSE.rst

.. |pypi| image:: https://img.shields.io/pypi/v/calplot?color=blue
    :alt: PyPI version
    :target: https://pypi.org/project/calplot/

.. |downloads| image:: https://img.shields.io/pypi/dm/calplot?color=blue
    :alt: Downloads
    :target: https://pypi.org/project/calplot/

Calplot creates heatmaps from Pandas time series data.

Plot `Pandas <http://pandas.pydata.org/>`_ time series data sampled by day in
a heatmap per calendar year using
`matplotlib <http://matplotlib.org/>`_.


Installation
------------

To install the `latest release <https://pypi.org/project/calplot/>`_ via PyPI using :code:`pip`::

    pip install calplot

Changelog
---------

Package `calplot <https://pypi.org/project/calplot/>`_ was started as a fork of `calmap <https://github.com/martijnvermaat/calmap>`_ with the addition of new arguments for easier customization.

See `CHANGES.rst <CHANGES.rst>`_ for changelog.

Usage
-----

See `API documentation <https://calplot.readthedocs.io/en/latest/>`_.

Examples
--------

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

    calplot.calplot(events, yearlabel_kws={'color': 'black'}, cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_yearcolor_black.svg
    :alt: Example calendar heatmap with yearcolor set to black

.. code-block:: python

    calplot.calplot(events, textformat='{:.0f}', textfiller='-', cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_textformat.svg
    :alt: Example calendar heatmap with textformat and textfiller set

.. code-block:: python

    calplot.calplot(events, colorbar=False, cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_colorbar_False.svg
    :alt: Example calendar heatmap with colorbar set to False

.. code-block:: python

    calplot.calplot(events, suptitle='Random data from standard normal distribution', cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_suptitle.svg
    :alt: Example calendar heatmap with suptitle set

.. code-block:: python

    calplot.calplot(events, linewidth=0, cmap='YlGn')

.. image:: https://raw.githubusercontent.com/tomkwok/calplot/master/examples/calplot_linewidth_zero.svg
    :alt: Example calendar heatmap with linewidth set to 0
