import finnhub
import pandas as pd
from airflow.example_dags.example_python_operator import print_context
from airflow.operators.python import PythonOperator
def finnhub_test():
    finnhub_client = finnhub.Client(api_key="c0dopmn48v6sgrj3h0t0")
    # need to get a free key from here: https://finnhub.io/
    # Stock candles
    res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
    print(res)
    import pandas as pd
    print(finnhub_client.symbol_lookup('apple'))
