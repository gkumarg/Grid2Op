# Copyright (c) 2019-2020, RTE (https://www.rte-france.com)
# See AUTHORS.txt
# This Source Code Form is subject to the terms of the Mozilla Public License, version 2.0.
# If a copy of the Mozilla Public License, version 2.0 was not distributed with this file,
# you can obtain one at http://mozilla.org/MPL/2.0/.
# SPDX-License-Identifier: MPL-2.0
# This file is part of Grid2Op, Grid2Op a testbed platform to model sequential decision making in power systems.

import subprocess
import sys
import setuptools
from setuptools import setup

pkgs = {
    "required": [
        "numpy>=1.18.2",
        "scipy>=1.4.1",
        "pandas>=1.0.3",
        "pandapower>=2.2.2",
        "tqdm>=4.43.0",
        "pathlib>=1.0.1",
        "networkx>=2.4"
    ],
    "extras": {
        "test": [
            "nbformat>=5.0.4",
            "jupyter-client>=6.1.0",
            "jyquickhelper>=0.3.128"
        ],
        "optional": [
            "numba==0.48.0",
            "matplotlib==3.2.1",
            "plotly==4.5.4",
            "seaborn==0.10.0",
            "pygame==1.9.6"
        ],
        "challenge": [
            "tensorflow==2.1.0",
            "Keras==2.3.1",
            "torch==1.4.0",
            "statsmodels==0.11.1",
            "scikit-learn==0.22.2.post1",
            "numpy==1.18.2",
            "scipy==1.4.1",
            "pandas==1.0.3",
            "pandapower==2.2.2",
            "tqdm==4.43.0",
            "pathlib==1.0.1",
            "networkx==2.4"
        ],
        "docs": [
            "numpydoc>=0.9.2",
            "sphinx>=2.4.4",
            "sphinx-rtd-theme>=0.4.3",
            "sphinxcontrib-trio>=1.1.0"
        ]
    }
}

# try to install numba, not compatible on every platform
try:
    import numba
except (ImportError, ModuleNotFoundError):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "numba"])
    except subprocess.CalledProcessError:
        import warnings
        warnings.warn("Numba is not available for your platform. You could gain massive speed up if you could install it.")
    except Exception as e:
        import warnings
        warnings.warn("Numba is not available for your platform. You could gain massive speed up if you could install it.")
except Exception as e:
    import warnings
    warnings.warn("Numba is not available for your platform. You could gain massive speed up if you could install it.")

setup(name='Grid2Op',
      version='0.6.1',
      description='An environment that allows to perform powergrid optimization.',
      long_description='Built with modularity in mind, this package allows to perform the same operations '
                       'independently of the software used to compute powerflow or method to generate grid '
                       'states or forecasts.',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: Science/Research",
          "Natural Language :: English"
      ],
      keywords='ML powergrid optmization RL power-systems',
      author='Benjamin DONNOT',
      author_email='benjamin.donnot@rte-france.com',
      url="https://github.com/rte-france/Grid2Op",
      license='MPL',
      packages=setuptools.find_packages(),
      include_package_data=True,
      install_requires=pkgs["required"],
      extras_require=pkgs["extras"],
      zip_safe=False,
      entry_points= {
          'console_scripts': [
              'grid2op.main=grid2op.command_line:main',
              'grid2op.download=grid2op.command_line:download'
          ]
     }
)
