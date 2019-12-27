from collections import OrderedDict
import numpy as np
import pandas as pd

from tests import generate_random_tickers, generate_random_dates, assert_output, project_test


@project_test
def test_get_high_lows_lookback(fn):
    tickers = generate_random_tickers(3)
    dates = generate_random_dates(4)

    fn_inputs = {
        'high': pd.DataFrame(
            [
                [35.4411, 34.1799, 34.0223],
                [92.1131, 91.0543, 90.9572],
                [57.9708, 57.7814, 58.1982],
                [34.1705, 92.453, 58.5107]],
            dates, tickers),
        'low': pd.DataFrame(
            [
                [15.6718, 75.1392, 34.0527],
                [27.1834, 12.3453, 95.9373],
                [28.2503, 24.2854, 23.2932],
                [86.3725, 32.223, 38.4107]],
            dates, tickers),
        'lookback_days': 2}
    fn_correct_outputs = OrderedDict([
        (
            'lookback_high',
            pd.DataFrame(
                [
                    [np.nan, np.nan, np.nan],
                    [np.nan, np.nan, np.nan],
                    [92.11310000, 91.05430000, 90.95720000],
                    [92.11310000, 91.05430000, 90.95720000]],
                dates, tickers)),
        (
            'lookback_low',
            pd.DataFrame(
                [
                    [np.nan, np.nan, np.nan],
                    [np.nan, np.nan, np.nan],
                    [15.67180000, 12.34530000, 34.05270000],
                    [27.18340000, 12.34530000, 23.29320000]],
                dates, tickers))
    ])

    assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_get_long_short(fn):
    tickers = generate_random_tickers(3)
    dates = generate_random_dates(4)

    fn_inputs = {
        'close': pd.DataFrame(
            [
                [25.6788, 35.1392, 34.0527],
                [25.1884, 14.3453, 39.9373],
                [78.2803, 34.3854, 23.2932],
                [88.8725, 52.223, 34.4107]],
            dates, tickers),
        'lookback_high': pd.DataFrame(
            [
                [np.nan, np.nan, np.nan],
                [92.11310000, 91.05430000, 90.95720000],
                [35.4411, 34.1799, 34.0223],
                [92.11310000, 91.05430000, 90.95720000]],
            dates, tickers),
        'lookback_low': pd.DataFrame(
            [
                [np.nan, np.nan, np.nan],
                [34.1705, 92.453, 58.5107],
                [15.67180000, 12.34530000, 34.05270000],
                [27.18340000, 12.34530000, 23.29320000]],
            dates, tickers)}
    fn_correct_outputs = OrderedDict([
        (
            'long_short',
            pd.DataFrame(
                [
                    [0, 0, 0],
                    [-1, -1, -1],
                    [1, 1, -1],
                    [0, 0, 0]],
                dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_filter_signals(fn):
    tickers = generate_random_tickers(3)
    dates = generate_random_dates(10)

    fn_inputs = {
        'signal': pd.DataFrame(
            [
                [0, 0, 0],
                [-1, -1, -1],
                [1, 0, -1],
                [0, 0, 0],
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [0, -1, 1],
                [-1, 0, 0],
                [0, 0, 0]],
            dates, tickers),
        'lookahead_days': 3}
    fn_correct_outputs = OrderedDict([
        (
            'filtered_signal',
            pd.DataFrame(
                [
                    [0, 0, 0],
                    [-1, -1, -1],
                    [1, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                    [0, -1, 0],
                    [-1, 0, 0],
                    [0, 0, 0]],
                dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_get_lookahead_prices(fn):
    tickers = generate_random_tickers(3)
    dates = generate_random_dates(5)

    fn_inputs = {
        'close': pd.DataFrame(
            [
                [25.6788, 35.1392, 34.0527],
                [25.1884, 14.3453, 39.9373],
                [62.3457, 92.2524, 65.7893],
                [78.2803, 34.3854, 23.2932],
                [88.8725, 52.223, 34.4107]],
            dates, tickers),
        'lookahead_days': 2}
    fn_correct_outputs = OrderedDict([
        (
            'lookahead_prices',
            pd.DataFrame(
                [
                    [62.34570000, 92.25240000, 65.78930000],
                    [78.28030000, 34.38540000, 23.29320000],
                    [88.87250000, 52.22300000, 34.41070000],
                    [np.nan, np.nan, np.nan],
                    [np.nan, np.nan, np.nan]],
                dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_get_return_lookahead(fn):
    tickers = generate_random_tickers(3)
    dates = generate_random_dates(5)

    fn_inputs = {
        'close': pd.DataFrame(
            [
                [25.6788, 35.1392, 34.0527],
                [25.1884, 14.3453, 39.9373],
                [62.3457, 92.2524, 65.7893],
                [78.2803, 34.3854, 23.2932],
                [88.8725, 52.223, 34.4107]],
            dates, tickers),
        'lookahead_prices': pd.DataFrame(
            [
                [62.34570000, 92.25240000, 65.78930000],
                [78.28030000, 34.38540000, 23.29320000],
                [88.87250000, 52.22300000, 34.41070000],
                [np.nan, np.nan, np.nan],
                [np.nan, np.nan, np.nan]],
            dates, tickers)}
    fn_correct_outputs = OrderedDict([
        (
            'lookahead_returns',
            pd.DataFrame(
                [
                    [0.88702896,  0.96521098,  0.65854789],
                    [1.13391240,  0.87420969, -0.53914925],
                    [0.35450805, -0.56900529, -0.64808965],
                    [np.nan, np.nan, np.nan],
                    [np.nan, np.nan, np.nan]],
                dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_get_signal_return(fn):
    tickers = generate_random_tickers(3)
    dates = generate_random_dates(5)

    fn_inputs = {
        'signal': pd.DataFrame(
            [
                [0, 0, 0],
                [-1, -1, -1],
                [1, 0, 0],
                [0, 0, 0],
                [0, 1, 0]],
            dates, tickers),
        'lookahead_returns': pd.DataFrame(
            [
                [0.88702896, 0.96521098, 0.65854789],
                [1.13391240, 0.87420969, -0.53914925],
                [0.35450805, -0.56900529, -0.64808965],
                [0.38572896, -0.94655617, 0.123564379],
                [np.nan, np.nan, np.nan]],
            dates, tickers)}
    fn_correct_outputs = OrderedDict([
        (
            'signal_return',
            pd.DataFrame(
                [
                    [0, 0, 0],
                    [-1.13391240, -0.87420969,  0.53914925],
                    [0.35450805, 0, 0],
                    [0, 0, 0],
                    [np.nan, np.nan, np.nan]],
                dates, tickers))])

    assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_find_outliers(fn):
    tickers = generate_random_tickers(7)
    dates = generate_random_dates(40)
    outlier_values = [{0.0: 1, 0.5: 3, 0.75: 13, 1.0: 12, 1.25: 8, 1.5: 3}]
    norm_values = [
        {-1.0: 6, -0.5: 9, 0.0: 8, 0.5: 11, 1.0: 6},
        {-1.0: 4, -0.5: 13, 0.0: 9, 0.5: 11, 1.0: 3},
        {-1.0: 7, -0.5: 11, 0.0: 7, 0.5: 9, 1.0: 6},
        {-1.0: 5, -0.5: 9, 0.0: 11, 0.5: 10, 1.0: 5},
        {-1.0: 3, -0.5: 12, 0.0: 14, 0.5: 8, 1.0: 3},
        {-1.0: 5, -0.5: 13, 0.0: 7, 0.5: 9, 1.0: 6}]

    # Build the values for the signal_return parameter
    signal_return_values = []
    for values in outlier_values + norm_values:
        current_signal_return_values = []
        for value, value_count in values.items():
            current_signal_return_values.extend([x for x in [value]*value_count])
        signal_return_values.append(current_signal_return_values)
    signal_return_values = np.array(signal_return_values).T

    # Create signals that aren't the same for each date
    tile_value = [1, 1, 1, 0, 1]
    signal_values = np.tile(
        tile_value,
        int(np.product(signal_return_values.shape) / len(tile_value))
    ).reshape(signal_return_values.shape)
    
    fn_inputs = {
        'signal': pd.DataFrame(signal_values, dates, tickers),
        'signal_return': pd.DataFrame(signal_return_values, dates, tickers),
        'ks_threshold': 0.8}
    fn_correct_outputs = OrderedDict([
        (
            'outliers',
            [tickers[0]])])

    assert_output(fn, fn_inputs, fn_correct_outputs)
