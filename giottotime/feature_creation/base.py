from abc import abstractmethod
from typing import Union

import pandas as pd


class Feature:
    @abstractmethod
    def __init__(self, output_name):
        self.output_name = output_name

    def _rename_columns(self, X: Union[pd.DataFrame, pd.Series]) -> pd.DataFrame:
        """Rename (in place) the column of the DataFrame with the
        ``output_name``. In case the output columns are more than one, a suffix
         is appended to the name, from ``_0`` to ``_n``, where ``n`` is the
         number of output columns.

        Parameters
        ----------
        X : ``Union[pd.DataFrame, pd.Series]``, required.
            The DataFrame or Series to be renamed.

        Returns
        -------
        X_renamed : ``pd.DataFrame``
            The original DataFrame ``X``, with the columns renamed.

        """
        if isinstance(X, pd.Series):
            X = X.to_frame()

        suffix = ""

        X_renamed = X.T.reset_index(drop=True).T
        for index, col in enumerate(X_renamed.columns):
            if len(X.columns) > 1:
                suffix = "_" + str(index)
            X_renamed.rename(
                columns={col: self.output_name + str(suffix)}, inplace=True
            )

        return X_renamed
