import scipy.stats
from colour import Color
import numpy as np
import pandas as pd
import os
import tempfile
import zipfile
import glob
import quandl
import plotly as py
import plotly.graph_objs as go
import plotly.offline as offline_py
from sklearn.preprocessing import Normalizer
offline_py.init_notebook_mode(connected=True)


_color_scheme = {
    'background_label': '#9dbdd5',
    'low_value': '#B6B2CF',
    'high_value': '#2D3ECF',
    'y_axis_2_text_color': 'grey',
    'shadow': 'rgba(0, 0, 0, 0.75)'}


def _generate_stock_trace(df):
    return go.Candlestick(
        x=df['date'],
        open=df['adj_open'],
        high=df['adj_high'],
        low=df['adj_low'],
        close=df['adj_close'],
        showlegend=False)


def _generate_config():
    return {'showLink': False, 'displayModeBar': False, 'showAxisRangeEntryBoxes': True}


def _generate_buy_annotations(df, signal_column):
    return [{
        'x': row['date'], 'y': row['adj_close'], 'text': 'Long', 'bgcolor': _color_scheme['background_label'],
        'ayref': 'y', 'ax': 0, 'ay': 20}
        for _, row in df[df[signal_column] == 1].iterrows()]


def _generate_sell_annotations(df, signal_column):
    return [{
        'x': row['date'], 'y': row['adj_close'], 'text': 'Short', 'bgcolor': _color_scheme['background_label'],
        'ayref': 'y', 'ax': 0, 'ay': 160}
        for _, row in df[df[signal_column] == -1].iterrows()]


def download_quandl_dataset(database, dataset, save_path, columns, tickers, start_date, end_date):
    """
    Download a dataset from Quandl and save it to `save_path`.
    Filter by columns, tickers, and date
    :param database: The Quandl database to download from
    :param dataset: The dataset to download
    :param save_path: The path to save the dataset
    :param columns: The columns to save
    :param tickers: The tickers to save
    :param start_date: The rows to save that are older than this date
    :param end_date: The rows to save that are younger than this date
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_wiki_file = tmp_dir + 'tmp.zip'
        quandl.bulkdownload(database, dataset_code=dataset, filename=tmp_wiki_file)

        # Unzip downloaded data
        zip_ref = zipfile.ZipFile(tmp_wiki_file, 'r')
        zip_ref.extractall(tmp_dir)
        zip_ref.close()

        # Check if the zip file only contains one csv file
        #   We're assuming that Quandl will always give us the data in a single csv file.
        #   If it's different, we want to throw an error.
        csv_files = glob.glob(os.path.join(tmp_dir, '*.csv'))
        assert len(csv_files) == 1,\
            'Bulk download of Quandl Wiki data failed. Wrong number of csv files found. Found {} file(s).'\
                .format(len(csv_files))
        tmp_csv_file = csv_files[0]

        names = quandl.get_table('{}/{}'.format(database, dataset), ticker='EMPTY_RESULTS_TICKER').columns.values
        tmp_df = pd.read_csv(tmp_csv_file, names=names)
        tmp_df['date'] = pd.to_datetime(tmp_df['date'])

        # Remove unused data and save
        tmp_df = tmp_df[tmp_df['date'].isin(pd.date_range(start_date, end_date))]  # Filter unused dates
        tmp_df = tmp_df[tmp_df['ticker'].isin(tickers)]  # Filter unused tickers
        tmp_df.to_csv(save_path, columns=columns, index=False)  # Filter unused columns and save


def _generate_second_tetration_stock(stock_symbol, dates):
    """
    Generate stock that follows the second tetration curve
    :param stock_symbol: Stock Symbol
    :param dates: Dates for ticker
    :return: Stock data
    """
    n_stock_columns = 5
    linear_line = np.linspace(1, 5, len(dates))
    all_noise = ((np.random.rand(n_stock_columns, len(dates)) - 0.5) * 0.01)
    sector_stock = pd.DataFrame({
        'ticker': stock_symbol,
        'date': dates,
        'base_line': np.power(linear_line, linear_line)})

    sector_stock['base_line'] = sector_stock['base_line'] + all_noise[0]*sector_stock['base_line']
    sector_stock['adj_open'] = sector_stock['base_line'] + all_noise[1]*sector_stock['base_line']
    sector_stock['adj_close'] = sector_stock['base_line'] + all_noise[2]*sector_stock['base_line']
    sector_stock['adj_high'] = sector_stock['base_line'] + all_noise[3]*sector_stock['base_line']
    sector_stock['adj_low'] = sector_stock['base_line'] + all_noise[4]*sector_stock['base_line']

    sector_stock['adj_high'] = sector_stock[['adj_high', 'adj_open', 'adj_close']].max(axis=1)
    sector_stock['adj_low'] = sector_stock[['adj_low', 'adj_open', 'adj_close']].min(axis=1)

    return sector_stock.drop(columns='base_line')


def generate_tb_sector(dates):
    """
    Generate TB sector of stocks
    :param dates: Dates that stocks should have market data on
    :return: TB sector stocks
    """
    symbol_length = 6
    stock_names = [
        'kaufmanniana', 'clusiana', 'greigii', 'sylvestris', 'turkestanica', 'linifolia', 'gesneriana',
        'humilis', 'tarda', 'saxatilis', 'dasystemon', 'orphanidea', 'kolpakowskiana', 'praestans',
        'sprengeri', 'bakeri', 'pulchella', 'biflora', 'schrenkii', 'armena', 'vvedenskyi', 'agenensis',
        'altaica', 'urumiensis']

    return [
        _generate_second_tetration_stock(stock_name[:symbol_length].upper(), dates)
        for stock_name in stock_names]


def get_signal_return_pval(signal_return):
    """
    Calculate p-value from signal returns
    :param signal_return: Signal returns
    :return: P-value
    """
    signal_return_mean = signal_return.mean()
    s_hat_5 = np.std(signal_return, ddof=1) / np.sqrt(len(signal_return))
    t_5 = signal_return_mean / s_hat_5
    return scipy.stats.t.sf(np.abs(t_5), len(signal_return) - 1)


def plot_stock(df, title):
    config = _generate_config()
    layout = go.Layout(title=title)

    stock_trace = _generate_stock_trace(df)

    offline_py.iplot({'data': [stock_trace], 'layout': layout}, config=config)


def plot_high_low(df, title):
    config = _generate_config()
    layout = go.Layout(title=title)

    stock_trace = _generate_stock_trace(df)
    high_trace = go.Scatter(
        x=df['date'],
        y=df['lookback_high'],
        name='Column lookback_high',
        line={'color': _color_scheme['high_value']})
    low_trace = go.Scatter(
        x=df['date'],
        y=df['lookback_low'],
        name='Column lookback_low',
        line={'color': _color_scheme['low_value']})

    offline_py.iplot({'data': [stock_trace, high_trace, low_trace], 'layout': layout}, config=config)


def plot_signal(df, title, signal_column):
    config = _generate_config()
    buy_annotations = _generate_buy_annotations(df, signal_column)
    sell_annotations = _generate_sell_annotations(df, signal_column)
    layout = go.Layout(
        title=title,
        annotations=buy_annotations + sell_annotations)

    stock_trace = _generate_stock_trace(df)

    offline_py.iplot({'data': [stock_trace], 'layout': layout}, config=config)


def plot_lookahead_prices(df, columns, title):
    config = _generate_config()
    layout = go.Layout(title=title)
    colors = Color(_color_scheme['low_value']).range_to(Color(_color_scheme['high_value']), len(columns))

    traces = [_generate_stock_trace(df)]
    for column, color in zip(columns, colors):
        traces.append(
            go.Scatter(
                x=df['date'],
                y=df[column],
                name='Column {}'.format(column),
                line={'color': str(color)}))

    offline_py.iplot({'data': traces, 'layout': layout}, config=config)


def plot_price_returns(df, columns, title):
    config = _generate_config()
    layout = go.Layout(
        title=title,
        yaxis2={
            'title': 'Returns',
            'titlefont': {'color': _color_scheme['y_axis_2_text_color']},
            'tickfont': {'color': _color_scheme['y_axis_2_text_color']},
            'overlaying': 'y',
            'side': 'right'})
    colors = Color(_color_scheme['low_value']).range_to(Color(_color_scheme['high_value']), len(columns))

    traces = [_generate_stock_trace(df)]
    for column, color in zip(columns, colors):
        traces.append(
            go.Scatter(
                x=df['date'],
                y=df[column],
                name='Column {}'.format(column),
                line={'color': str(color)},
                yaxis='y2'))

    offline_py.iplot({'data': traces, 'layout': layout}, config=config)


def plot_signal_returns(df, signal_return_columns, signal_columns, titles):
    config = _generate_config()
    layout = go.Layout(
        yaxis2={
            'title': 'Signal Returns',
            'titlefont': {'color': _color_scheme['y_axis_2_text_color']},
            'tickfont': {'color': _color_scheme['y_axis_2_text_color']},
            'overlaying': 'y',
            'side': 'right'})
    colors = Color(_color_scheme['low_value']).range_to(Color(_color_scheme['high_value']), len(signal_return_columns))

    stock_trace = _generate_stock_trace(df)
    for signal_return_column, signal_column, color, title in zip(signal_return_columns, signal_columns, colors, titles):
        non_zero_signals = df[df[signal_return_column] != 0]
        signal_return_trace = go.Scatter(
                x=non_zero_signals['date'],
                y=non_zero_signals[signal_return_column],
                name='Column {}'.format(signal_return_column),
                line={'color': str(color)},
                yaxis='y2')

        buy_annotations = _generate_buy_annotations(df, signal_column)
        sell_annotations = _generate_sell_annotations(df, signal_column)
        layout['title'] = title
        layout['annotations'] = buy_annotations + sell_annotations

        offline_py.iplot({'data': [stock_trace, signal_return_trace], 'layout': layout}, config=config)


def plot_series_histograms(series_list, title, subplot_titles):
    assert len(series_list) == len(subplot_titles)

    all_values = pd.concat(series_list)
    x_range = [all_values.min(), all_values.max()]
    y_range = [0, 1500]
    config = _generate_config()
    colors = Color(_color_scheme['low_value']).range_to(Color(_color_scheme['high_value']), len(series_list))

    fig = py.tools.make_subplots(rows=1, cols=len(series_list), subplot_titles=subplot_titles, print_grid=False)
    fig['layout'].update(title=title, showlegend=False)

    for series_i, (series, color) in enumerate(zip(series_list, colors), 1):
        filtered_series = series[series != 0].dropna()
        trace = go.Histogram(x=filtered_series, marker={'color': str(color)})
        fig.append_trace(trace, 1, series_i)
        fig['layout']['xaxis{}'.format(series_i)].update(range=x_range)
        fig['layout']['yaxis{}'.format(series_i)].update(range=y_range)

    offline_py.iplot(fig, config=config)


def plot_series_to_normal_histograms(series_list, title, subplot_titles):
    assert len(series_list) == len(subplot_titles)

    all_values = pd.concat(series_list)
    x_range = [all_values.min(), all_values.max()]
    y_range = [0, 1500]
    config = _generate_config()

    fig = py.tools.make_subplots(rows=1, cols=len(series_list), subplot_titles=subplot_titles, print_grid=False)
    fig['layout'].update(title=title)

    for series_i, series in enumerate(series_list, 1):
        filtered_series = series[series != 0].dropna()
        filtered_series_trace = go.Histogram(
            x=filtered_series,
            marker={'color': _color_scheme['low_value']},
            name='Signal Return Distribution',
            showlegend=False)
        normal_trace = go.Histogram(
            x=np.random.normal(np.mean(filtered_series), np.std(filtered_series), len(filtered_series)),
            marker={'color': _color_scheme['shadow']},
            name='Normal Distribution',
            showlegend=False)
        fig.append_trace(filtered_series_trace, 1, series_i)
        fig.append_trace(normal_trace, 1, series_i)
        fig['layout']['xaxis{}'.format(series_i)].update(range=x_range)
        fig['layout']['yaxis{}'.format(series_i)].update(range=y_range)

    # Show legened
    fig['data'][0]['showlegend'] = True
    fig['data'][1]['showlegend'] = True

    offline_py.iplot(fig, config=config)
