"""Downloading utilities for running script.

   Utilities are mocked upon Nilearn.
"""
import warnings
from nilearn.datasets.utils import _uncompress_file, _fetch_file


def fetch_abide(data_dir=None):
    """Fetch ABIDE timeseries data from Open Science Framework (OSF)

    Parameters
    ----------
    data_dir : string
        Path where data should be downloaded

    Returns
    -------
    data_dir : string
        Path to the downloaded timeseries directory
    """
    if data_dir is None:
        warnings.warn('Data downloading is requested but data_dir is not '
                      'provided. Downloading to the current directory with '
                      'folder name ABIDE', stacklevel=2)
        data_dir = './ABIDE'

    url = 'https://osf.io/hc4md/download'

    # Download the zip file, first
    dl_file = _fetch_file(url, data_dir=data_dir)

    # Second, uncompress the downloaded zip file
    _uncompress_file(dl_file, verbose=2)

    return data_dir
