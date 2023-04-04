# -*- coding: utf-8 -*-
from pathlib import Path
import pandas as pd


class OHLC():
    
    def __init__(self):
        self.df = self.get_df()
        
    def diff(self):
        return self.close() - self.df['收盘'][-2]
    
    def pa(self):
        return self.diff() / self.close()
    
    def close(self):
        return self.df['收盘'][-1]
    
    @staticmethod
    def get_df():
        path = str(Path(__file__).parents[1]) + '/assets/000680.csv'
        return pd.read_csv(path, index_col='时间', nrows=200)
