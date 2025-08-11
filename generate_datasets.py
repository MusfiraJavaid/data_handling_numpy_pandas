"""generate_datasets.py
Create synthetic datasets used in notebooks.
Run: python generate_datasets.py
"""
import numpy as np
import pandas as pd
from pathlib import Path

out = Path('datasets')
out.mkdir(exist_ok=True)

N = 2000
cities = ['Karachi','Lahore','Islamabad','Peshawar','Quetta']
prods = [f'p_{i}' for i in range(100)]
df = pd.DataFrame({
    'id': np.arange(N),
    'city': np.random.choice(cities, size=N),
    'product': np.random.choice(prods, size=N),
    'price': np.round(np.random.lognormal(3.0, 0.9, size=N), 2),
    'qty': np.random.poisson(2.0, size=N),
    'ts': pd.date_range('2023-01-01', periods=N, freq='H')
})
df.to_csv(out/'sample_data.csv', index=False)

T = 24*180
rng = pd.date_range('2024-01-01', periods=T, freq='H')
values = (np.sin(np.linspace(0, 20*np.pi, T)) + np.random.normal(0, 0.5, T)).cumsum()
ts = pd.DataFrame({'timestamp': rng, 'value': values})
ts.to_csv(out/'timeseries.csv', index=False)

print('Datasets written to', out.resolve())
