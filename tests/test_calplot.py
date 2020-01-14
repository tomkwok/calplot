"""
Tests for calplot.
"""


from __future__ import unicode_literals

import numpy as np; np.random.seed(sum(map(ord, 'calplot')))
import pandas as pd
import pytest

import calplot


@pytest.fixture
def events():
    """
    We create 500 events as random float values assigned to random days over a
    700-day period.
    """
    all_days = pd.date_range('1/1/2019', periods=730, freq='D')
    days = np.random.choice(all_days, 500)
    return pd.Series(np.random.randn(len(days)), index=days)


@pytest.mark.mpl_image_compare(tolerance=20)
def test_yearplot(events):
    """
    By default, `yearplot` plots the first year and sums the values per day.
    """
    ax = calplot.yearplot(events)
    return ax.figure


@pytest.mark.mpl_image_compare(tolerance=20)
def test_yearplot_year(events):
    """
    We can choose which year is plotted with the `year` keyword argment.
    """
    ax = calplot.yearplot(events, year=2019)
    return ax.figure


@pytest.mark.mpl_image_compare(tolerance=20)
def test_yearplot_cmap_fillcolor_linewidth(events):
    """
    The appearance can be changed by using another colormap. Here we also use
    a darker fill color for days without data and remove the lines.
    """
    ax = calplot.yearplot(events, cmap='YlGn', fillcolor='grey', linewidth=0)
    return ax.figure


@pytest.mark.mpl_image_compare(tolerance=20)
def test_yearplot_monthticks_daylabels_dayticks(events):
    """
    We can ask to draw only every nth label, or explicitely supply the label
    indices. The labels themselves can also be customized.
    """
    ax = calplot.yearplot(events, monthticks=3, daylabels='MTWTFSS',
                         dayticks=[0, 2, 4, 6])
    return ax.figure


@pytest.mark.mpl_image_compare(tolerance=50)
def test_calplot(events):
    """
    With `calplot` we can plot several years in one figure.
    """
    fig, axes = calplot.calplot(events)
    return fig
