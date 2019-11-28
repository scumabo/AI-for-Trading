from collections import OrderedDict
import pandas as pd
import numpy as np


pd.options.display.float_format = '{:.8f}'.format


def _generate_random_tickers(n_tickers=None):
    min_ticker_len = 3
    max_ticker_len = 5
    tickers = []

    if not n_tickers:
        n_tickers = np.random.randint(8, 14)

    ticker_symbol_random = np.random.randint(ord('A'), ord('Z')+1, (n_tickers, max_ticker_len))
    ticker_symbol_lengths = np.random.randint(min_ticker_len, max_ticker_len, n_tickers)
    for ticker_symbol_rand, ticker_symbol_length in zip(ticker_symbol_random, ticker_symbol_lengths):
        ticker_symbol = ''.join([chr(c_id) for c_id in ticker_symbol_rand[:ticker_symbol_length]])
        tickers.append(ticker_symbol)

    return tickers


def _generate_output_error_msg(fn_name, fn_inputs, fn_outputs, fn_expected_outputs):
    formatted_inputs = []
    formatted_outputs = []
    formatted_expected_outputs = []

    for input_name, input_value in fn_inputs.items():
        formatted_outputs.append('INPUT {}:\n{}\n'.format(
            input_name, str(input_value)))
    for output_name, output_value in fn_outputs.items():
        formatted_outputs.append('OUTPUT {}:\n{}\n'.format(
            output_name, str(output_value)))
    for expected_output_name, expected_output_value in fn_expected_outputs.items():
        formatted_expected_outputs.append('EXPECTED OUTPUT FOR {}:\n{}\n'.format(
            expected_output_name, str(expected_output_value)))

    return 'Wrong value for {}.\n' \
           '{}\n' \
           '{}\n' \
           '{}' \
        .format(
            fn_name,
            '\n'.join(formatted_inputs),
            '\n'.join(formatted_outputs),
            '\n'.join(formatted_expected_outputs))


def _assert_output(fn, fn_inputs, fn_expected_outputs):
    assert type(fn_expected_outputs) == OrderedDict

    fn_outputs = OrderedDict()
    fn_raw_out = fn(**fn_inputs)

    if len(fn_expected_outputs) == 1:
        fn_outputs[list(fn_expected_outputs)[0]] = fn_raw_out
    elif len(fn_expected_outputs) > 1:
        assert type(fn_raw_out) == tuple,\
            'Expecting function to return tuple, got type {}'.format(type(fn_raw_out))
        assert len(fn_raw_out) == len(fn_expected_outputs),\
            'Expected {} outputs in tuple, only found {} outputs'.format(len(fn_expected_outputs), len(fn_raw_out))
        for key_i, output_key in enumerate(fn_expected_outputs.keys()):
            fn_outputs[output_key] = fn_raw_out[key_i]

    err_message = _generate_output_error_msg(
        fn.__name__,
        fn_inputs,
        fn_outputs,
        fn_expected_outputs)

    for fn_out, (out_name, expected_out) in zip(fn_outputs.values(), fn_expected_outputs.items()):
        assert isinstance(fn_out, type(expected_out)),\
            'Wrong type for output {}. Got {}, expected {}'.format(out_name, type(fn_out), type(expected_out))

        if hasattr(expected_out, 'shape'):
            assert fn_out.shape == expected_out.shape, \
                'Wrong shape for output {}. Got {}, expected {}'.format(out_name, fn_out.shape, expected_out.shape)

        if type(expected_out) == pd.DataFrame:
            assert set(fn_out.columns) == set(expected_out.columns), \
                'Incorrect columns for output {}\n' \
                'COLUMNS:          {}\n' \
                'EXPECTED COLUMNS: {}'.format(out_name, sorted(fn_out.columns), sorted(expected_out.columns))

        if type(expected_out) in {pd.DataFrame, pd.Series}:
            assert set(fn_out.index) == set(expected_out.index), \
                'Incorrect indices for output {}\n' \
                'INDICES:          {}\n' \
                'EXPECTED INDICES: {}'.format(out_name, sorted(fn_out.index), sorted(expected_out.index))

        out_is_close = np.isclose(fn_out, expected_out, equal_nan=True)

        if not isinstance(out_is_close, bool):
            out_is_close = out_is_close.all()

        assert out_is_close, err_message


def project_test(func):
    def func_wrapper(*args):
        result = func(*args)
        print('Tests Passed')
        return result

    return func_wrapper


@project_test
def test_resample_prices(fn):
    tickers = _generate_random_tickers(5)
    dates = pd.DatetimeIndex(['2008-08-19', '2008-09-08', '2008-09-28', '2008-10-18', '2008-11-07', '2008-11-27'])
    resampled_dates = pd.DatetimeIndex(['2008-08-31', '2008-09-30', '2008-10-31', '2008-11-30'])

    fn_inputs = {
        'prices': pd.DataFrame(
            [
                [21.050810483942833, 17.013843810658827, 10.984503755486879, 11.248093428369392, 12.961712733997235],
                [15.63570258751384, 14.69054309070934, 11.353027688995159, 475.74195118202061, 11.959640427803022],
                [482.34539247360806, 35.202580592515041, 3516.5416782257166, 66.405314327318209, 13.503960481087077],
                [10.918933017418304, 17.9086438675435, 24.801265417692324, 12.488954191854916, 10.52435923388642],
                [10.675971965144655, 12.749401436636365, 11.805257579935713, 21.539039489843024, 19.99766036804861],
                [11.545495378369814, 23.981468434099405, 24.974763062186504, 36.031962102997689, 14.304332320024963]],
            dates, tickers),
        'freq': 'M'}
    fn_correct_outputs = OrderedDict([
        (
            'prices_resampled',
            pd.DataFrame(
                [
                        [21.05081048, 17.01384381, 10.98450376, 11.24809343, 12.96171273],
                        [482.34539247, 35.20258059, 3516.54167823, 66.40531433, 13.50396048],
                        [10.91893302, 17.90864387, 24.80126542, 12.48895419, 10.52435923],
                        [11.54549538, 23.98146843, 24.97476306, 36.03196210, 14.30433232]],
                resampled_dates, tickers))])

    _assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_compute_log_returns(fn):
    tickers = _generate_random_tickers(5)
    dates = pd.DatetimeIndex(['2008-08-31', '2008-09-30', '2008-10-31', '2008-11-30'])

    fn_inputs = {
        'prices': pd.DataFrame(
            [
                    [21.05081048, 17.01384381, 10.98450376, 11.24809343, 12.96171273],
                    [482.34539247, 35.20258059, 3516.54167823, 66.40531433, 13.50396048],
                    [10.91893302, 17.90864387, 24.80126542, 12.48895419, 10.52435923],
                    [11.54549538, 23.98146843, 24.97476306, 36.03196210, 14.30433232]],
            dates, tickers)}
    fn_correct_outputs = OrderedDict([
        (
            'log_returns',
            pd.DataFrame(
                [
                    [np.nan, np.nan, np.nan, np.nan, np.nan],
                    [3.13172138, 0.72709204, 5.76874778, 1.77557845, 0.04098317],
                    [-3.78816218, -0.67583590, -4.95433863, -1.67093250, -0.24929051],
                    [0.05579709, 0.29199789, 0.00697116, 1.05956179, 0.30686995]],
                dates, tickers))])

    _assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_shift_returns(fn):
    tickers = _generate_random_tickers(5)
    dates = pd.DatetimeIndex(['2008-08-31', '2008-09-30', '2008-10-31', '2008-11-30'])

    fn_inputs = {
        'returns': pd.DataFrame(
            [
                [np.nan, np.nan, np.nan, np.nan, np.nan],
                [3.13172138, 0.72709204, 5.76874778, 1.77557845, 0.04098317],
                [-3.78816218, -0.67583590, -4.95433863, -1.67093250, -0.24929051],
                [0.05579709, 0.29199789, 0.00697116, 1.05956179, 0.30686995]],
            dates, tickers),
        'shift_n': 1}
    fn_correct_outputs = OrderedDict([
        (
            'shifted_returns',
            pd.DataFrame(
                [
                    [np.nan, np.nan, np.nan, np.nan, np.nan],
                    [np.nan, np.nan, np.nan, np.nan, np.nan],
                    [3.13172138, 0.72709204, 5.76874778, 1.77557845, 0.04098317],
                    [-3.78816218, -0.67583590, -4.95433863, -1.67093250, -0.24929051]],
                dates, tickers))])

    _assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_get_top_n(fn):
    tickers = _generate_random_tickers(5)
    dates = pd.DatetimeIndex(['2008-08-31', '2008-09-30', '2008-10-31', '2008-11-30'])

    fn_inputs = {
        'prev_returns': pd.DataFrame(
            [
                [np.nan, np.nan, np.nan, np.nan, np.nan],
                [np.nan, np.nan, np.nan, np.nan, np.nan],
                [3.13172138, 0.72709204, 5.76874778, 1.77557845, 0.04098317],
                [-3.78816218, -0.67583590, -4.95433863, -1.67093250, -0.24929051]],
            dates, tickers),
        'top_n': 3}
    fn_correct_outputs = OrderedDict([
        (
            'top_stocks',
            pd.DataFrame(
                [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [1, 0, 1, 1, 0],
                    [0, 1, 0, 1, 1]],
                dates, tickers))])

    _assert_output(fn, fn_inputs, fn_correct_outputs)


@project_test
def test_portfolio_returns(fn):
    tickers = _generate_random_tickers(5)
    dates = pd.DatetimeIndex(['2008-08-31', '2008-09-30', '2008-10-31', '2008-11-30'])

    fn_inputs = {
        'df_long': pd.DataFrame(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 1, 0],
                [0, 1, 0, 1, 1]],
            dates, tickers),
        'df_short': pd.DataFrame(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 1, 1],
                [1, 1, 1, 0, 0]],
            dates, tickers),
        'lookahead_returns': pd.DataFrame(
            [
                [3.13172138, 0.72709204, 5.76874778, 1.77557845, 0.04098317],
                [-3.78816218, -0.67583590, -4.95433863, -1.67093250, -0.24929051],
                [0.05579709, 0.29199789, 0.00697116, 1.05956179, 0.30686995],
                [1.25459098, 6.87369275, 2.58265839, 6.92676837, 0.84632677]],
            dates, tickers),
        'n_stocks': 3}
    fn_correct_outputs = OrderedDict([
        (
            'portfolio_returns',
            pd.DataFrame(
                [
                    [0.00000000, 0.00000000, 0.00000000, 0.00000000, 0.00000000],
                    [-0.00000000, -0.00000000, -0.00000000, -0.00000000, -0.00000000],
                    [0.01859903, -0.09733263, 0.00232372, 0.00000000, -0.10228998],
                    [-0.41819699, 0.00000000, -0.86088613, 2.30892279, 0.28210892]],
                dates, tickers))])

    _assert_output(fn, fn_inputs, fn_correct_outputs)


def test_analyze_alpha(analyze_alpha):
    """Run unit tests on the portfolio_returns() function."""
    passed = False  # set to True when all tests are passed
    try:
        # Define test data / parameters
        net_returns = pd.Series(
            [
                -0.003674652593455105, -0.0013509534462004848, -0.016823111594328574,
                0.006711394532438875, -0.01367385423210165, -0.01613256430760212,
                -0.016205381129345976, -0.018938551191161355, -0.012789534006155671,
                0.0025571191687112464, 0.010953105187861412, 0.035062645562843484,
                0.019820157244601875, 0.06685539014909703, 0.024573898713671168,
                0.028706880689786753, -0.038051388986914125, 0.04594311985454379,
                0.018595280034134878, 0.050165910521565105, -0.024820241243787747,
                0.07366327962090834, -0.006800619585194637, 0.07834835101210905,
                -0.023749785275014645, 0.02321499435450592, -0.004721754487226459,
                -0.03674208775119875, 0.020368066608067538, -0.024424318809567414,
                -0.05053141558213965, -0.004840977299631063, -0.0005818530942978614,
                -0.004928953156789123, -0.06599924133254942, 0.0036175614509116067,
                0.021953477781310217, 0.014733112015093176, 0.005383568281736988,
                -0.01956589695746009, 0.02663559853443772, 0.044748419057881184,
                0.02235850210575906, 0.03766146855674265, 0.007188886828269343],
            pd.to_datetime([
                '2013-09-30', '2013-10-31', '2013-11-30', '2013-12-31', '2014-01-31', '2014-02-28',
                '2014-03-31', '2014-04-30', '2014-05-31', '2014-06-30', '2014-07-31', '2014-08-31',
                '2014-09-30', '2014-10-31', '2014-11-30', '2014-12-31', '2015-01-31', '2015-02-28',
                '2015-03-31', '2015-04-30', '2015-05-31', '2015-06-30', '2015-07-31', '2015-08-31',
                '2015-09-30', '2015-10-31', '2015-11-30', '2015-12-31', '2016-01-31', '2016-02-29',
                '2016-03-31', '2016-04-30', '2016-05-31', '2016-06-30', '2016-07-31', '2016-08-31',
                '2016-09-30', '2016-10-31', '2016-11-30', '2016-12-31', '2017-01-31', '2017-02-28',
                '2017-03-31', '2017-04-30', '2017-05-31']))
        rtol = 0.01  # relative tolerance, e.g. 0.01 = 1%

        # Correct results
        mu_ = 0.006321623373441478
        se_ = 0.00462325179388448
        t_ = 1.3673543331132343
        p_ = 0.0892295225667871
        names = ["mu (mean)", "se (standard error)", "n (number of samples)", "t (t-statistic)", "p (p-value)"]

        # Student results
        results = analyze_alpha(net_returns)

        # Checks
        assert results is not None and isinstance(results, tuple) and len(
            results) == 4, "Must return a tuple with 5 values: {}".format(", ".join(names))
        mu, se, t, p = results
        for val, correct_val, name in zip([mu, se, t, p], [mu_, se_, t_, p_], names):
            assert np.isclose(val, correct_val, rtol=rtol), "Incorrect {}: {}, expected: {}".format(name, val,
                                                                                                    correct_val)

        passed = True  # all good
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Your code produced an error:")
        print("{}: {}".format(e.__class__.__name__, str(e)))
        raise
    finally:
        print("test_analyze_alpha(): Tests", "passed" if passed else "failed")
