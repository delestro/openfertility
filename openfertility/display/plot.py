import numpy as np
import pandas as pd

def hist(data, nbins=None, target=None, **kwargs):

    if isinstance(data, pd.DataFrame):

        if not nbins:
            data.hist(column=target, grid=False, align='left', **kwargs)

        else:
            data.hist(column=target, bins=np.arange(0,nbins+1), grid=False, align='left', **kwargs)

    elif isinstance(data, np.ndarray):
        raise NotImplementedError("Histogram not implemented for numpy arrays")
    
    else:
        raise ValueError(f'Histogram not supported for {type(data)}')