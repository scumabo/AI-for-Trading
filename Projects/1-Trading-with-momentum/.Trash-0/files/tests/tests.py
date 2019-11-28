import numpy as np
import pandas as pd

def test_load_data(load_data):
    """Run unit tests on the load_data() function."""
    passed = False  # set to True when all tests are passed
    try:
        # Define test data / parameters
        filename = "tests/data/test_prices_large.csv"
        tickers = ['AMZN', 'MSFT', 'FB']
        start_date = '2015-01-01'
        end_date = '2015-12-31'
        correct_results = "tests/data/test_prices.csv"
        expected_cols = ['ticker', 'date', 'adj_close']

        # Correct dataframe
        df_ = pd.read_csv(correct_results, parse_dates=['date'], index_col=False)

        # Student dataframe
        df = load_data(filename, start_date, end_date, tickers)

        # Checks
        assert df is not None and df.__class__ == pd.DataFrame, "Must return a valid pandas.DataFrame object"
        for col in expected_cols:
            assert col in df.columns, "Column not found: '{}', expected columns: {}".format(col, expected_cols)
        assert df['date'].min() >= pd.to_datetime(start_date), "Date range constraint not satisfied (start_date)"
        assert df['date'].max() <= pd.to_datetime(end_date), "Date range constraint not satisfied (end_date)"
        assert len(df) == len(df_), "Incorrect number of rows: {}, expected: {}".format(len(df), len(df_))
        assert set(df['ticker']) == set(tickers), "Universe of stocks constraint not satisfied (tickers)"

        passed = True  # all good
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Your code produced an error:")
        print("{}: {}".format(e.__class__.__name__, str(e)))
        raise
    finally:
        print("test_load_data(): Tests", "passed" if passed else "failed")


def test_resample_prices(resample_prices):
    """Run unit tests on the resample_prices() function."""
    passed = False  # set to True when all tests are passed
    try:
        # Define test data / parameters
        df = pd.read_csv("tests/data/test_prices.csv", parse_dates=['date'], index_col=False)
        expected_cols = ['ticker', 'date', 'price']

        # Correct dataframe
        df_resampled_ = pd.read_csv("tests/data/test_prices_resampled.csv", parse_dates=['date'], index_col=False)

        # Student dataframe
        df_resampled = resample_prices(df)

        # Checks
        assert df_resampled is not None and df_resampled.__class__ == pd.DataFrame, "Must return a valid pandas.DataFrame object"
        for col in expected_cols:
            assert col in df_resampled.columns, "Column not found: '{}', expected columns: {}".format(col, expected_cols)
        assert set(df_resampled['date']) == set(df_resampled_['date']), "Incorrect dates sampled.\nEnsure you are picking the price at the *end* of each period."
        assert set(df_resampled['ticker']) == set(df_resampled_['ticker']), "Incorrect tickers (symbols) returned: {}, expected: {}.\nEnsure you are sampling each ticker on each desired date.".format(set(df_resampled['ticker']), set(df_resampled_['ticker']))
        assert len(df_resampled) == len(df_resampled_), "Incorrect number of rows: {}, expected: {}.\nCheck resampling period/frequency.".format(len(df_resampled), len(df_resampled_))

        passed = True  # all good
    except AssertionError as e:
        print(e)
    finally:
        print("test_resample_prices(): Tests", "passed" if passed else "failed")


def test_compute_log_returns(compute_log_returns):
    """Run unit tests on the compute_log_returns() function."""
    passed = False  # set to True when all tests are passed
    try:
        # Define test data / parameters
        df_resampled = pd.read_csv("tests/data/test_prices_resampled.csv", parse_dates=['date'], index_col=False)
        expected_cols = ['ticker', 'date', 'price', 'return']

        # Correct dataframe
        df_returns_ = pd.read_csv("tests/data/test_returns.csv", parse_dates=['date'], index_col=False)

        # Student dataframe
        df_returns = compute_log_returns(df_resampled)

        # Checks
        assert df_returns is not None and df_returns.__class__ == pd.DataFrame, "Must return a valid pandas.DataFrame object"
        for col in expected_cols:
            assert col in df_returns.columns, "Column not found: '{}', expected columns: {}".format(col, expected_cols)
        assert set(df_returns['date']) == set(df_returns_['date']), "Incorrect dates returned.\nEnsure you are computing log returns on each date. The first return for each ticker would be undefined (indicated as NaN)."
        assert set(df_returns['ticker']) == set(df_returns_['ticker']), "Incorrect tickers (symbols) returned: {}, expected: {}.\nEnsure you are computing log returns for each ticker (symbol).".format(set(df_returns['ticker']), set(df_returns_['ticker']))
        assert len(df_returns) == len(df_returns_), "Incorrect number of rows: {}, expected: {}.\nYou must return log returns for each ticker on each date.".format(len(df_returns), len(df_returns_))
        pd.testing.assert_series_equal(df_returns['return'], df_returns_['return'], obj="Log returns")

        passed = True  # all good
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Your code produced an error:")
        print("{}: {}".format(e.__class__.__name__, str(e)))
        raise
    finally:
        print("test_compute_log_returns(): Tests", "passed" if passed else "failed")


def test_shift_returns(shift_returns):
    """Run unit tests on the shift_returns() function."""
    passed = False  # set to True when all tests are passed
    try:
        # Define test data / parameters
        df_returns = pd.read_csv("tests/data/test_returns.csv", parse_dates=['date'], index_col=False)
        expected_cols = ['ticker', 'date', 'price', 'return', 'prev_return', 'lookahead_return']

        # Correct dataframe
        df_shifted_  = pd.read_csv("tests/data/test_returns_shifted.csv", parse_dates=['date'], index_col=False)

        # Student dataframe
        df_shifted = shift_returns(df_returns)

        # Checks
        assert df_shifted is not None and df_shifted.__class__ == pd.DataFrame, "Must return a valid pandas.DataFrame object"
        for col in expected_cols:
            assert col in df_shifted.columns, "Column not found: '{}', expected columns: {}".format(col, expected_cols)
        assert set(df_shifted['date']) == set(df_shifted_['date']), "Incorrect dates returned.\nShifted returns should be produced for each date, even if some are undefined (NaNs)."
        assert set(df_shifted['ticker']) == set(df_shifted_['ticker']), "Incorrect tickers (symbols) returned: {}, expected: {}.\nEnsure you are shifting returns for each ticker (symbol).".format(set(df_shifted['ticker']), set(df_shifted_['ticker']))
        assert len(df_shifted) == len(df_shifted_), "Incorrect number of rows: {}, expected: {}.\nYou must produce shifted returns for each ticker on each date.".format(len(df_shifted), len(df_shifted_))
        pd.testing.assert_series_equal(df_shifted['prev_return'], df_shifted_['prev_return'], obj="Previous returns")
        pd.testing.assert_series_equal(df_shifted['lookahead_return'], df_shifted_['lookahead_return'], obj="Lookahead returns")

        passed = True  # all good
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Your code produced an error:")
        print("{}: {}".format(e.__class__.__name__, str(e)))
        raise
    finally:
        print("test_shift_returns(): Tests", "passed" if passed else "failed")


def test_get_long_short(get_long_short):
    """Run unit tests on the get_long_short() function."""
    passed = False  # set to True when all tests are passed
    try:
        # Define test data / parameters
        df_shifted = pd.read_csv("tests/data/test_returns_shifted_all.csv", parse_dates=['date'], index_col=False)  # larger dataset, so that there are enough stocks and dates
        expected_cols = df_shifted.columns  # all columns should be retained
        
        # Note: We don't have a single "correct" result, as the signal can vary; just need to test for validity

        # Student dataframe
        results = get_long_short(df_shifted)

        # Checks
        assert results is not None and isinstance(results, tuple) and len(results) == 2, "Must return a valid tuple of 2 dataframes: df_long, df_short"
        df_long, df_short = results  # unpack
        assert df_long is not None and df_long.__class__ == pd.DataFrame, "Returned df_long must be a valid pandas.DataFrame object"
        assert df_short is not None and df_short.__class__ == pd.DataFrame, "Returned df_short must be a valid pandas.DataFrame object"
        for col in expected_cols:
            assert col in df_long.columns, "Column not found: '{}' in df_long.\nKeep all columns from supplied dataframe, even if not relevant for generating the signal.".format(col)
            assert col in df_short.columns, "Column not found: '{}' in df_short.\nKeep all columns from supplied dataframe, even if not relevant for generating the signal.".format(col)
        assert set(df_long['date']) <= set(df_shifted['date']), "Returned df_long should only contain dates that are in supplied dataframe."
        assert set(df_short['date']) <= set(df_shifted['date']), "Returned df_short should only contain dates that are in supplied dataframe."
        assert set(df_long['ticker']) <= set(df_shifted['ticker']), "Returned df_long should only contain tickers that are in supplied dataframe."
        assert set(df_short['ticker']) <= set(df_shifted['ticker']), "Returned df_short should only contain tickers that are in supplied dataframe."
        assert len(df_long) + len(df_short) > 0, "You must select at least 1 stock for the long and/or short portfolio."

        passed = True  # all good
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Your code produced an error:")
        print("{}: {}".format(e.__class__.__name__, str(e)))
        raise
    finally:
        print("test_get_long_short(): Tests", "passed" if passed else "failed")


def test_portfolio_returns(portfolio_returns):
    """Run unit tests on the portfolio_returns() function."""
    passed = False  # set to True when all tests are passed
    try:
        # Define test data / parameters
        df_long = pd.read_csv("tests/data/test_long_all.csv", parse_dates=['date'], index_col=False)  # larger dataset
        df_short = pd.read_csv("tests/data/test_short_all.csv", parse_dates=['date'], index_col=False)  # larger dataset
        
        # Correct returns
        net_returns_ = pd.read_csv("tests/data/test_net_returns_all.csv", parse_dates=['date'], index_col='date', squeeze=True)

        # Student returns
        net_returns = portfolio_returns(df_long, df_short)

        # Checks
        assert net_returns is not None and net_returns.__class__ == pd.Series, "Returned net_returns must be a valid pandas.Series object"
        pd.testing.assert_series_equal(net_returns, net_returns_, obj="Net returns")

        passed = True  # all good
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Your code produced an error:")
        print("{}: {}".format(e.__class__.__name__, str(e)))
        raise
    finally:
        print("test_portfolio_returns(): Tests", "passed" if passed else "failed")


def test_analyze_alpha(analyze_alpha):
    """Run unit tests on the portfolio_returns() function."""
    passed = False  # set to True when all tests are passed
    try:
        # Define test data / parameters
        net_returns = pd.read_csv("tests/data/test_net_returns_all.csv", parse_dates=['date'], index_col='date', squeeze=True)
        rtol = 0.01  # relative tolerance, e.g. 0.01 = 1%
        
        # Correct results
        mu_ = 0.006321623373441478
        se_ = 0.00462325179388448
        n_ = 45
        t_ = 1.3673543331132343
        p_ = 0.0892295225667871
        names = ["mu (mean)", "se (standard error)", "n (number of samples)", "t (t-statistic)", "p (p-value)"]

        # Student results
        results = analyze_alpha(net_returns)

        # Checks
        assert results is not None and isinstance(results, tuple) and len(results) == 5, "Must return a tuple with 5 values: {}".format(", ".join(names))
        mu, se, n, t, p = results
        for val, correct_val, name in zip([mu, se, n, t, p], [mu_, se_, n_, t_, p_], names):
            assert np.isclose(val, correct_val, rtol=rtol), "Incorrect {}: {}, expected: {}".format(name, val, correct_val)

        passed = True  # all good
    except AssertionError as e:
        print(e)
    except Exception as e:
        print("Your code produced an error:")
        print("{}: {}".format(e.__class__.__name__, str(e)))
        raise
    finally:
        print("test_analyze_alpha(): Tests", "passed" if passed else "failed")
