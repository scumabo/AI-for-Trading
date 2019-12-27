import numpy as np
import pandas as pd
import string


test_lookback_days = 2
test_lookahead_days = 3
test_df_dict = {
    'ticker': ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
               'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
    'adj_close': [111, 103,  98, 105,  96,  85,  95,  98, 105, 113,  81,
                  100, 110, 80,  82, 102, 100, 105, 105, 106],
    'lookback_low': [np.nan, np.nan, 103.0, 98.0, 98.0, 96.0, 85.0, 85.0, 95.0, 98.0, 105.0,
                     np.nan, np.nan, 100.0, 80.0, 80.0, 82.0, 100.0, 100.0, 105],
    'lookback_high': [np.nan, np.nan, 111.0, 103.0, 105.0, 105.0, 96.0, 95.0, 98.0, 105.0, 113.0,
                      np.nan, np.nan, 110.0, 110.0, 82.0, 102.0, 102.0, 105.0, 105.0],
    'pre_signal': [0, 0, -1, 1, -1, -1, 0, 1, 1, 1, -1, 0, 0, -1, 0, 1, 0, 1, 0, 1],
    'signal': [0.0, 0.0, -1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -1.0, 0.0, 0.0, -1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0],
    'lookahead_prices': [98.0, 105.0, 96.0, 85.0, 95.0, 98.0, 105.0, 113.0, 81.0, np.nan, np.nan,
                         80.0, 82.0, 102.0, 100.0, 105.0, 105.0, 106.0, np.nan, np.nan]}
test_filtered_df_dict = {
    'ticker': ['A', 'A', 'A', 'A', 'B', 'B'],
    'adj_close': [105, 96,  98, 81, 102, 106],
    'lookback_low': [98.0, 98.0, 85.0, 105.0, 80.0, 105.0],
    'lookback_high': [103.0, 105.0, 95.0, 113.0, 82.0, 105.0],
    'signal': [1.0, -1.0, 1.0, -1.0, 1.0, 0.0],
    'lookahead_prices': [85.0, 95.0, 113.0, np.nan, 105.0, np.nan],
    'return_lookahead': [-0.211309093667, -0.0104712998673, 0.142420340042, np.nan, 0.0289875368733, np.nan],
    'signal_return': [-0.211309093667, 0.0104712998673, 0.142420340042, np.nan, 0.0289875368733, np.nan]}


def _no_change_pass_by_reference_df(reference_df, fn, additional_parameters=None):
    if additional_parameters is None:
        additional_parameters = []

    copy_df = reference_df.copy(True)
    output = fn(copy_df, *additional_parameters)

    assert copy_df.equals(reference_df), \
        'Input DataFrame has been changed. DataFrame isn\'t supposed to be modified.'

    return output


def _is_series_equal(series1, series2):
    sorted_series1 = series1.reset_index(drop=True).sort_index()
    sorted_series2 = series2.reset_index(drop=True).sort_index()

    if len(sorted_series1) != len(sorted_series2):
        return False

    same_null_values = (sorted_series1.isnull() == sorted_series2.isnull()).all()
    if sorted_series1.dtype == np.object or sorted_series2.dtype == np.object:
        # Can't compare a np.object with other types
        if sorted_series1.dtype != sorted_series2.dtype:
            return False

        same_values = np.array_equal(sorted_series1, sorted_series2)
    else:
        same_values = np.isclose(
            sorted_series1[sorted_series1.notnull()],
            sorted_series2[sorted_series2.notnull()]).all()

    return same_null_values and same_values


def _perfect_norm(loc, scale, size):
    dist = []
    buckets = [1, 2, 3, 2, 1]
    bucket_factor = int(size/sum(buckets))
    assert size > sum(buckets)

    for bucket, norm_value in zip(buckets, np.linspace(loc-scale, loc+scale, len(buckets))):
        dist.extend([norm_value] * bucket * bucket_factor)

    return np.array(dist)


def project_test(func):
    def func_wrapper(*args):
        result = func(*args)
        print('Tests Passed')
        return result

    return func_wrapper


@project_test
def test_get_high_lows_lookback(get_high_lows_lookback):
    df = pd.DataFrame({k: test_df_dict[k] for k in ['ticker', 'adj_close']})

    lookback_tuple = _no_change_pass_by_reference_df(df, get_high_lows_lookback, [test_lookback_days])

    assert type(lookback_tuple) == tuple, \
        'Function returned {}. Expected a Tuple.'.format(type(lookback_tuple))

    lookback_high, lookback_low = lookback_tuple

    assert type(lookback_high) == pd.Series,\
        'Lookback High is type {}. Expected a Pandas Series.'.format(type(lookback_high))
    assert type(lookback_low) == pd.Series, \
        'Lookback Low is type {}. Expected a Pandas Series.'.format(type(lookback_low))
    assert _is_series_equal(lookback_high, pd.Series(test_df_dict['lookback_high'])), \
        'Wrong value for High Loockbacks.\n' \
        'INPUT df:\n' \
        '{}\n' \
        'INPUT lookback_days: {}\n\n' \
        'OUTPUT lookback_high:\n' \
        '{}' \
        .format(df.head(len(df)), test_lookback_days, lookback_high)
    assert _is_series_equal(lookback_low, pd.Series(test_df_dict['lookback_low'])), \
        'Wrong value for High Loockbacks.\n' \
        'INPUT df:\n' \
        '{}\n' \
        'INPUT lookback_days: {}\n\n' \
        'OUTPUT lookback_low:\n' \
        '{}' \
        .format(df.head(len(df)), test_lookback_days, lookback_low)


@project_test
def test_get_long_short(get_long_short):
    df = pd.DataFrame({k: test_df_dict[k] for k in ['ticker', 'adj_close', 'lookback_low', 'lookback_high']})

    signal = _no_change_pass_by_reference_df(df, get_long_short)

    assert type(signal) == pd.Series, \
        'Long short signals is type {}. Expected a Pandas Series.'.format(type(signal))
    assert _is_series_equal(signal, pd.Series(test_df_dict['pre_signal'])), \
        'Incorrect signals.\n' \
        'INPUT df:\n' \
        '{}\n\n' \
        'Signals:\n' \
        '{}' \
        .format(df.head(len(df)), signal)


@project_test
def test_filter_signals(filter_signals):
    df = pd.DataFrame({
        k: test_df_dict[k] for k in ['ticker', 'adj_close', 'lookback_low', 'lookback_high', 'pre_signal']})
    signal_column = 'pre_signal'

    signal = _no_change_pass_by_reference_df(df, filter_signals, [signal_column, test_lookahead_days])

    assert type(signal) == pd.Series, \
        'Filtered signals is type {}. Expected a Pandas Series.'.format(type(signal))
    assert _is_series_equal(signal, pd.Series(test_df_dict['signal'])), \
        'Incorrect signals.\n' \
        'INPUT df:\n' \
        '{}\n\n' \
        'Signals:\n' \
        '{}' \
        .format(df.head(len(df)), signal)


@project_test
def test_get_lookahead_prices(get_lookahead_prices):
    df = pd.DataFrame({k: test_df_dict[k] for k in ['ticker', 'adj_close', 'lookback_low', 'lookback_high', 'signal']})
    lookahead_days = 2

    lookahead_prices = _no_change_pass_by_reference_df(df, get_lookahead_prices, [lookahead_days])

    assert type(lookahead_prices) == pd.Series, \
        'Lookahead prices is type {}. Expected a Pandas Series.'.format(type(lookahead_prices))
    assert _is_series_equal(lookahead_prices, pd.Series(test_df_dict['lookahead_prices'])), \
        'Incorrect lookahead prices.\n' \
        'INPUT df:\n' \
        '{}\n' \
        'INPUT lookahead_days: {}\n\n' \
        'OUTPUT lookahead prices:\n' \
        '{}' \
        .format(df, lookahead_days, lookahead_prices)


@project_test
def test_get_return_lookahead(get_return_lookahead):
    df = pd.DataFrame({
        k: test_filtered_df_dict[k]
        for k in ['ticker', 'adj_close', 'lookback_low', 'lookback_high', 'signal', 'lookahead_prices']})
    lookahead_column = 'lookahead_prices'

    return_lookahead = _no_change_pass_by_reference_df(df, get_return_lookahead, [lookahead_column])

    assert type(return_lookahead) == pd.Series, \
        'Lookahead price returns is type {}. Expected a Pandas Series.'.format(type(return_lookahead))
    assert _is_series_equal(return_lookahead, pd.Series(test_filtered_df_dict['return_lookahead'])), \
        'Incorrect Lookahead returns.\n' \
        'INPUT df:\n' \
        '{}\n\n' \
        'OUTPUT lookahead return:\n' \
        '{}' \
        .format(df, return_lookahead)


@project_test
def test_get_signal_return(get_signal_return):
    df = pd.DataFrame({
        k: test_filtered_df_dict[k] for k in
        ['ticker', 'adj_close', 'lookback_low', 'lookback_high', 'signal', 'lookahead_prices', 'return_lookahead']})
    return_column = 'return_lookahead'
    signal_column = 'signal'

    signal_return = _no_change_pass_by_reference_df(df, get_signal_return, [return_column, signal_column])

    assert type(signal_return) == pd.Series, \
        'Signal returns is type {}. Expected a Pandas Series.'.format(type(signal_return))
    assert _is_series_equal(signal_return, pd.Series(test_filtered_df_dict['signal_return'])), \
        'Incorrect Signal returns.\n' \
        'INPUT df:\n' \
        '{}\n\n' \
        'OUTPUT signal returns:\n' \
        '{}' \
        .format(df, signal_return)


@project_test
def test_find_outliers(find_outliers):
    signal_column = 'signal'
    signal_return_column = 'signal_return'
    not_outliers_symbols = list(string.ascii_uppercase[1:])
    correct_outlier_symbols = ['A']
    stock_size = 90

    stock_a_signal_returns = _perfect_norm(0, 1, stock_size * len(not_outliers_symbols))
    stock_b_signal_returns = _perfect_norm(1, 0.5, stock_size)

    tickers = not_outliers_symbols * stock_size + correct_outlier_symbols * stock_size

    df = pd.DataFrame({
        'ticker': tickers,
        signal_column: np.random.randint(0, 2, len(tickers)),
        signal_return_column: np.concatenate((stock_a_signal_returns, stock_b_signal_returns))})

    ks_threshold = 0.7
    pvalue_threshold = 0.05

    outlier_symbols = _no_change_pass_by_reference_df(
        df,
        find_outliers,
        [signal_column, signal_return_column, ks_threshold, pvalue_threshold])

    assert type(outlier_symbols) == list, \
        'Signal returns is type {}. Expected a List.'.format(type(outlier_symbols))

    assert sorted(outlier_symbols) == sorted(correct_outlier_symbols), \
        'Incorrect Filtering.\n' \
        'INPUT:\n' \
        '{}\n\n' \
        'OUTPUT:\n' \
        '{}' \
        .format(df, outlier_symbols)


@project_test
def test_remove_outliers(remove_outliers):
    bad_tickers = np.random.randint(ord('A'), ord('Z'), (10, 5))
    bad_tickers = [''.join(row) for row in bad_tickers.view('U1')]

    good_tickers = np.random.randint(ord('A'), ord('Z'), (10, 5))
    good_tickers = [''.join(row) for row in good_tickers.view('U1')]

    tickers = bad_tickers + good_tickers
    df_dict = {
        k: np.random.rand(len(tickers)) for k in
        ['adj_close', 'lookback_low', 'lookback_high', 'signal', 'lookahead_prices', 'return_lookahead']}
    df_dict['ticker'] = tickers
    df = pd.DataFrame(df_dict)

    filtered_df = _no_change_pass_by_reference_df(df, remove_outliers, [bad_tickers])

    assert type(filtered_df) == pd.DataFrame, \
        'Signal returns is type {}. Expected a Pandas DataFrame.'.format(type(filtered_df))

    assert _is_series_equal(filtered_df['ticker'], pd.Series(good_tickers)), \
        'Incorrect Filtering.\n' \
        'INPUT Tickers:\n' \
        '{}\n\n' \
        'OUTPUT Tickers:\n' \
        '{}' \
        .format(df['ticker'], filtered_df['ticker'])


@project_test
def test_parameters(parameters):
    keys = ['lookback_days', 'lookahead_days']

    assert type(parameters) == dict, 'Incorrect type. Parameters should be dict, found {}'.format(type(parameters))

    missing_keys = set(keys) - set(parameters.keys())
    extra_keys = set(parameters.keys()) - set(keys)
    key_error_messages = []
    if missing_keys:
        key_error_messages.append('Missing keys: {}'.format(missing_keys))
    if extra_keys:
        key_error_messages.append('Extra keys: {}'.format(extra_keys))
    assert not (missing_keys or extra_keys), 'Incorrect keys. {}'.format(' and ')

    unique_lookback_days = set(parameters['lookback_days'])
    unique_lookahead_days = set(parameters['lookahead_days'])
    assert 0 not in unique_lookahead_days and 0 not in unique_lookback_days, 'Can\'t use value 0 for days.'
