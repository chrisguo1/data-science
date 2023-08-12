from typing import Optional
from dataclasses import dataclass

import pandas as pd
from bs4 import BeautifulSoup as Soup

@dataclass
class PrettyDataFrameStyle():
    rounding: Optional[int] = None
    

@dataclass
class PrettyDataFrame():
    df: pd.DataFrame
    style: Optional[PrettyDataFrameStyle] = None
    
    def _apply_style(self) -> pd.DataFrame:
        if self.style:
            if self.style.rounding:
                new_df = self.df.round(self.style.rounding)
                return new_df
            
        return self.df

    def _repr_html_(self) -> str:
        """this function is used by Jupyter Notebooks to render the dataframe as html

        Returns:
            str: string representation of html to be rendered in jupyter notebook
        """
        styled_df = self._apply_style()
        html: str = styled_df.to_html()
        soup = Soup(html)
        final_html = str(soup)
        return final_html

