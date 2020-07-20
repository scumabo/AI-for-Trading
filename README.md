# AI for Trading

This repo contains my work to Udacity nanodegree [AI for Trading](https://www.udacity.com/course/ai-for-trading--nd880).

## Table of Contents

### 1. Trading with Momentum. [Project](Projects/1-Trading-with-momentum/project_1_starter.ipynb)

* Learn basics of [stock markets](Notes/1-Trading-with-momentum/stock-market-data.md). Learn how to calculate [stock returns and design momentum trading strategy](Notes/1-Trading-with-momentum/returns-momentum.md).

* Quiz: [Stock Prices](Quiz/m1_quant_basics/l2_stock_prices/stock_data.ipynb), [Resample Data](Quiz/m1_quant_basics/l3_market_mechanics/resample_data.ipynb), [Calculate Raw Returns](Quiz/m1_quant_basics/l5_stock_returns/calculate_returns.ipynb), [dtype and astype](Quiz/m1_quant_basics/l6_momentum_trading/dtype.ipynb), [top and bottom performer](Quiz/m1_quant_basics/l6_momentum_trading/top_and_bottom_performing.ipynb)

### 2. Breakout Strategy. [Project](Projects/2-Breakout-strategy/project_2_starter.pdf)

* Learn about the overall [quant workflow](Notes/2-Breakout-strategy/quant-workflow.md), including alpha signal generation, alpha combination, portfolio optimization, and trading.

* Learn the [importance of outliers](Notes/2-Breakout-strategy/outliers.md) and how to detect them. Learn about methods designed to handle outliers.

* Learn about [regression](Notes/2-Breakout-strategy/regression.md), and related statistical tools that pre-process data before regression analysis. Learn commonly-used [time series](Notes/2-Breakout-strategy/time_series.md) models.

* Learn about stock [volatility](Notes/2-Breakout-strategy/volatility.md), and how the GARCH model analysis volatility. See how volatility is used in equity trading.

* Learn about [pair trading](Notes/2-Breakout-strategy/pair.md), and study the tools used in identifying stock pairs and making trading decision.

#### Quiz: advanced quant: [test normality](Quiz/m2_advanced_quants/l3_regression/test_normality.ipynb), [rolling windows](Quiz/m2_advanced_quants/l5_volatility/rolling_windows.ipynb), [pairs candidates](Quiz/m2_advanced_quants/l6_pairs_trading_and_mean_reversion/pairs_candidates.ipynb)

### 3. Smart beta and portfolio optimization. [Project](Projects/3-Smart-Beta/project_3_starter.pdf)

* [Overview of stocks, indices, and funds](Notes/3-Porfolio-optimization/Fund.md). Learn about [ETFs](Notes/3-Porfolio-optimization/ETFs.md).
* Learn fundamentals of [portfolio risk and return](Notes/3-Porfolio-optimization/Portfolio.md).
* Learn how to [optimize portfolios](Notes/3-Porfolio-optimization/Optimization.md) to meet certain criteria and constraints. 

#### Quiz: funds_etfs_portfolio_optimization: [cumsum_and_cumprod](Quiz/m3_funds_etfs_portfolio_optimization/l1_stocks_indices_funds/cumsum_and_cumprod.ipynb), [cov](Quiz/m3_funds_etfs_portfolio_optimization/l3_portfolio_risk_and_return/m3l3_covariance.ipynb), [cvxpy_basis](Quiz/m3_funds_etfs_portfolio_optimization/l4_portfolio_optimization/m3l4_cvxpy_basic.ipynb), [cvxpy_adv](Quiz/m3_funds_etfs_portfolio_optimization/l4_portfolio_optimization/m3l4_cvxpy_advanced.ipynb)


### 4. Alpha Research and Factor Modeling. [Project](Projects/4-Multi-factor-Model/project_4_starter.pdf)

* Learn [factors](Notes/4-Alpha-Research-and-Factor-Modeling/Factors.md) and how to convert factor values into portfolio weights in a dollar neutral portfolio with leverage ratio equals to 1 (i.e., standardize factor values).
* Learn [fundamentals of factor models and type of factors](Notes/4-Alpha-Research-and-Factor-Modeling/Factor-Model.md). Learn how to compute [portfolio variance using risk factor models](Notes/4-Alpha-Research-and-Factor-Modeling/Risk-Factor-Model.md). Learn [time series and cross-sectional risk models](Notes/4-Alpha-Research-and-Factor-Modeling/Cross-Sectional.md).
* Learn how to use [PCA](Notes/4-Alpha-Research-and-Factor-Modeling/PCA.md) to build risk factor models. 


#### Quiz: [zipline pipline](Quiz/m4_multifactor_models/Zipline-Pipeline/Zipline-Pipeline.pdf), [zipline execise](Quiz/m4_multifactor_models/m4l1/zipline_coding_exercises.pdf), [historical_variance](Quiz/m4_multifactor_models/m4l2/historical_variance.pdf), [factor_model_asset_return](Quiz/m4_multifactor_models/m4l2/factor_model_asset_return.pdf),[factor_model_portfolio_return](Quiz/m4_multifactor_models/m4l2/factor_model_portfolio_return.pdf), [covariance_matrix_assets](Quiz/m4_multifactor_models/m4l2/covariance_matrix_assets.pdf), [portfolio_variance](Quiz/m4_multifactor_models/m4l2/portfolio_variance.pdf), [pca_factor_model](Quiz/m4_multifactor_models/m4l2/pca_factor_model.pdf), 

### 5. Intro to NLP. [Project](Projects/5-Intro-NLP/project_5_starter.ipynb)
NLP pipeline consists of text processing, feature extraction, and modeling.

* [Text processing](Quiz/m5_financial_statements/text_processing.ipynb): Learn text acquisition (plane text, tabular data, and online resources), simple data cleaning with python regex and BeautifulSoup, using nltk (natural language toolkit) for tokenization, stemming, and lemmatization.

* Financial Statement: Learn how to apply [Regexes](Quiz/m5_financial_statements/regexes.ipynb) to [10Ks](Quiz/m5_financial_statements/applying_regexes_10ks.ipynb), how [BeautifulSoup](Quiz/m5_financial_statements/beautifulSoup.ipynb) can ease the parse of (perfectly formatted) html and xml downloaded using [request library](Quiz/m5_financial_statements/requests_library.ipynb).

* Basic NLP Analysis: Learn quantitatively measure readability of documents using [readability indices](Quiz/m5_financial_statements/Readability_Exercises.ipynb), [how to convert document into vectors using bag of word and TF-IDF weighting, and metrics to compare similarities between documents](Quiz/m5_financial_statements/Bag_of_Word_Exercises.ipynb).

### 6. Sentiment Analysis with Neural Networks. [Project](Projects/6-Sentiment-Analysis/project_6_starter.ipynb)

* [Neural Network Basics](Notes/6-Sentiment-analysis-with-neutral-networks/README.md): Learn maximum likelihood, cross entropy, logistic regression, gradient decent, regularization, and practical heuristics for training neural networks.

* [Deep Learning with PyTorch](https://github.com/scumabo/deep-learning-v2-pytorch/tree/master/intro-to-pytorch).
<!-- 
    1. [Tensors in Pytorch](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/intro-to-pytorch/Part%201%20-%20Tensors%20in%20PyTorch%20(Exercises).ipynb)

    2. [Neutral Networks in Pytorch](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/intro-to-pytorch/Part%202%20-%20Neural%20Networks%20in%20PyTorch%20(Exercises).ipynb)

    3. [Training Neutral Networks](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/intro-to-pytorch/Part%203%20-%20Training%20Neural%20Networks%20(Exercises).ipynb)

    4. [Fashion MNIST](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/intro-to-pytorch/Part%204%20-%20Fashion-MNIST%20(Exercises).ipynb)

    5. [Inference and Validation](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/intro-to-pytorch/Part%205%20-%20Inference%20and%20Validation%20(Exercises).ipynb)

    6. [Saving and loading models](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/intro-to-pytorch/Part%206%20-%20Saving%20and%20Loading%20Models.ipynb)

    7. [Load Image Data](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/intro-to-pytorch/Part%207%20-%20Loading%20Image%20Data%20(Exercises).ipynb)

    8. [Transfer Learning](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/intro-to-pytorch/Part%208%20-%20Transfer%20Learning%20(Exercises).ipynb) -->

* Recurrence Neutral Networks: 
    1. Learn to use RNN to predict simple [Time Series](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/recurrent-neural-networks/time-series/Simple_RNN.ipynb) and train [Character-Level LSTM](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/recurrent-neural-networks/char-rnn/Character_Level_RNN_Exercise.ipynb) to generate new text based on the text from the book. 
    2. Learn Word2Vec algorithm using the [Skip-gram Architecture](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/word2vec-embeddings/Skip_Grams_Exercise.ipynb) and with [Negative Sampling](https://github.com/scumabo/deep-learning-v2-pytorch/blob/master/word2vec-embeddings/Negative_Sampling_Exercise.ipynb).
    3. [Sentiment Analysis RNN](https://github.com/udacity/deep-learning-v2-pytorch/tree/master/sentiment-rnn): Implement a recurrent neural network that can predict if the text of a movie review is positive or negative.

### 7. Combining Signals for Enhanced Alpha. [Project](Projects/7-Combining-alphas/project_7_starter.ipynb)

* [Decision Tree](Notes/7-Combining-signals-for-enhanced-alpha/README.md): Learn how to branching decision tree using entropy and information gain. Implement decision tree using sklearn for [Titanic Survival Exploration](Quiz/m7/titanic_survival_exploration.ipynb) and [visualize the decision tree](Quiz/m7/VisualizeTree.pdf) using graphviz.

* [Model Testing and Evaluation](Notes/7-Combining-signals-for-enhanced-alpha/Evaluation.md): Learn Type 1 and Type 2 errors, Precision vs. Recall, Cross validation for time series, and using learning curve to determine underfitting and overfitting.

* [Random Forest](Notes/7-Combining-signals-for-enhanced-alpha/Random_forest.md): Learn the ensemble random forest method and [implement it in sklearn](Quiz/m7/spam_rf.ipynb).

* [Feature Engineering](Quiz/m7/m7l3/feature_engineering.ipynb): Certain alphas perform better or worse depending on market conditions. Feature engineering creates additional inputs to give models more contexts about the current market condition so that the model can adjust its prediction accordingly.

* [Overlapping Labels](Quiz/m7/dependent_labels_solution.ipynb): Mitigate the problem when features are dependent on each other (non-IID).

* [Feature Importance](): Company would prefer simple interpretable models to black-box complex models. interpretability opens the door for complex models to be readily acceptable. One way to interpret a model is to measure how much each feature contributed to the model prediction called feature importance. Learn how [sklearn computes features importance](Quiz/m7/m7l6/sklearn_feature_importance.ipynb) for tree-based method. Learn how to [calculate shap](Quiz/m7/m7l6/calculate_shap.ipynb) for feature importance of a single sample.

### 8. Backtesting. [Project](Projects/8-Backtesting/project_8_starter.ipynb)

* Basics: [Learn best practices of backtesting](Notes/8-Backtesting/Intro.md) and see what [overfitting can "look like"](Quiz/m8/overfitting_exercise) in practice.

* [Learn how to optimization a portfolio with transaction cost](Notes/8-Backtesting/optimization.md). Learn some [additional ways to design your optimization with efficiency in mind](Quiz/m8/optimization_with_tcosts.ipynb). This is really helpful when backtesting, because having reasonably shorter runtimes allows you to test and iterate on your alphas more quickly.

## Additions
[1D Kalman filter](Side-projects/1D-Kalman-filter.ipynb)

[Dataframe indexing and selection](Side-projects/Dataframe-indexing-selecting.ipynb)

[Hypothesis testing](Side-projects/Hypthesis-testing.ipynb)
