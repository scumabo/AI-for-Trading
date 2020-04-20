Project 8: Backtesting

In this project, you will build a fairly realistic backtester that uses the Barra data. The backtester will perform portfolio optimization that includes transaction costs, and you'll implement it with computational efficiency in mind, to allow for a reasonably fast backtest. You'll also use performance attribution to identify the major drivers of your portfolio's profit-and-loss (PnL). You will have the option to modify and customize the backtest as well.

Suggestion to customize your project
Try backtesting on different time periods and interpret the final results.
Try different factors to be their alphas.
Try different weights for each alpha, based on some metric that tells us how confident we are in that alpha, such as a rolling average of the sharpe ratio for each alpha factor.
Try different transaction cost models. Read the paper "Crossover from Linear to Square-Root Market Impact”. It has a good overview of the transaction cost models, and it also references other papers that are useful in studying transaction cost models.
Note about testing previous alphas: To test the alphas that you've created using the QuoteMedia data source, we would need a mapping file that identifies which cusip is associated with which barra ID. We currently aren't able to provide this in the classroom.