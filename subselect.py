import graphlab
import datetime as dt
import numpy as np
import pandas as pd

graphlab.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)

sales = graphlab.SFrame('/Users/rebeccakeable/Downloads/Week 2/home_data.gl')
# Load
