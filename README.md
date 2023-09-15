### TreeHue
email: [antineutrinomuon@gmail.com](mailto:antineutrinomuon@gmail.com), [jean@astro.up.pt](mailto:jean@astro.up.pt)

last stable version: 0.0.1

github repository: <a href='https://github.com/neutrinomuon/TreeHue/'>TreeHue</a>

© Copyright ®

J.G. - Jean Gomes

<hr>

<img src='https://img.shields.io/pypi/pyversions/TreeHue'>

<hr>

#### <b>RESUME</b>

<img src="https://raw.githubusercontent.com/neutrinomuon/PyKinematicalBroadening/main/figures/Kinematics.png" width=120>

Enhance your directory tree visualization with colorful representations using
TreeHue, a Python package that brings vibrancy to your file system structure.

<hr>

#### <b>INSTALLATION</b>

You can easily install <a href='https://pypi.org/project/PyKinematicalBroadening/'>PyKinematicalBroadening</a> by using pip - <a href='https://pypi.org/'>PyPI - The Python Package Index</a>:

<pre>
pip install TreeHue
</pre>

<br>or by using a generated conda repository <a href='https://anaconda.org/neutrinomuon/TreeHue'>https://anaconda.org/neutrinomuon/TreeHue</a>:

<img src='https://anaconda.org/neutrinomuon/TreeHue/badges/version.svg'><img src='https://anaconda.org/neutrinomuon/TreeHue/badges/latest_release_date.svg'><img src='https://anaconda.org/neutrinomuon/TreeHue/badges/platforms.svg'>

<pre>
conda install -c neutrinomuon TreeHue
</pre>

<br>OBS.: Linux, OS-X ad Windows pre-compilations available in conda.

You can also clone the repository and install by yourself in your machine:

<pre>
git clone https://github.com/neutrinomuon/TreeHue
python setup.py install
</pre>

<hr>

#### <b>EXAMPLE</b>

Example of the test spectrum test\_spectrum.spec successively broadened by different velocity dispersions in [km/s]. The code is not optimized for cpu speed, but it shows the principle of how it works.

<img src="https://github.com/neutrinomuon/TreeHue/blob/main/figures/KinematicalBroadening.png?raw=true" width="90%">

<hr>

#### <b>STRUCTURE OF TreeHue (Created with TreeHue</b>

<pre>
TreeHue
├── MANIFEST.in
├── dist
│   ├── PyKinematicalBroadening-0.0.3.tar.gz
│   ├── PyKinematicalBroadening-0.0.5.tar.gz
│   ├── PyKinematicalBroadening-0.0.6.tar.gz
│   └── PyKinematicalBroadening-0.0.4.tar.gz
├── README.md
├── figures
│   ├── KinematicalBroadening.png
│   └── cc_logo.png
├── PyKinematicalBroadening.egg-info
│   ├── PKG-INFO
│   ├── dependency_links.txt
│   ├── SOURCES.txt
│   ├── top_level.txt
│   └── requires.txt
├── LICENSE.txt
├── setup.py
├── tutorials
│   ├── .ipynb_checkpoints
│   │   └── Example 1 - Kinematical Broadening-checkpoint.ipynb
│   └── Example 1 - Kinematical Broadening.ipynb
├── pykinematicalbroadening
│   ├── win-32
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── linux-armv7l
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── linux-armv6l
│   │   ├── .projectignore
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── linux-s390x
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── linux-ppc64
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── linux-aarch64
│   │   ├── .projectignore
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── linux-32
│   │   ├── .projectignore
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── linux-64
│   │   ├── .projectignore
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── osx-64
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── meta.yaml
│   ├── win-64
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   ├── README.txt
│   ├── linux-ppc64le
│   │   └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
│   └── osx-arm64
│       └── pykinematicalbroadening-0.0.5-py39_0.tar.bz2
├── Pykinematicalbroadening.egg-info
│   ├── PKG-INFO
│   ├── dependency_links.txt
│   ├── SOURCES.txt
│   ├── top_level.txt
│   └── requires.txt
├── src
│   └── python
│       ├── __pycache__
│       ├── test_spectrum.spec
│       ├── __init__.py
│       └── PyKinematicalBroadening.py
├── version.txt
└── build
    └── lib
        ├── Pykinematicalbroadening
        └── PyKinematicalBroadening

26 directories, 44 files
</pre>

<hr>

#### <b>LICENSE</b>

Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0)

<img src="https://github.com/neutrinomuon/PyKinematicalBroadening/blob/main/figures/cc_logo.png?raw=true" width="10%">

<a href='https://creativecommons.org/licenses/by-nc-nd/4.0/'>Creative Commons Attribution-NonCommercial-NoDerivs (CC-BY-NC-ND)</a>

