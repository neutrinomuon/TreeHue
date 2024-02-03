### TreeHue
email: [antineutrinomuon@gmail.com](mailto:antineutrinomuon@gmail.com), [jean@astro.up.pt](mailto:jean@astro.up.pt)

github repository: <a href='https://github.com/neutrinomuon/TreeHue/'>TreeHue</a>

last stable version: 0.0.4
<!-- https://zenodo.org/badge/doi/10.5281/zenodo.10433044.svg -->
[![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.10581155.svg)](https://zenodo.org/badge/doi/10.5281/zenodo.10581155.svg)

<hr>

![My Skills](https://skillicons.dev/icons?i=python,numpy&theme=light)<br>
[![python3](https://img.shields.io/pypi/pyversions/TreeHue)](https://img.shields.io/pypi/pyversions/TreeHue)
[![badgetlicense](https://anaconda.org/neutrinomuon/TreeHue/badges/license.svg)](https://anaconda.org/neutrinomuon/TreeHue/badges/license.svg)

© Copyright ®

J.G. - Jean Gomes

<hr>

<img src='https://img.shields.io/pypi/pyversions/TreeHue'>

<hr>

#### <b>RESUME</b>

<img src="https://raw.githubusercontent.com/neutrinomuon/TreeHue/main/figures/TreeHue.png" width=120>

Enhance your directory tree visualization with colorful representations using
TreeHue, a Python package that brings vibrancy to your file system structure.

<img src="https://raw.githubusercontent.com/neutrinomuon/TreeHue/main/figures/Education,_Studying,_University,_Alumni_-_icon.png#gh-light-mode-only" width="70px"><img src="https://raw.githubusercontent.com/neutrinomuon/TreeHue/main/figures/Education_black_background-removebg.png#gh-dark-mode-only" width="70px">This project was also created with a focus on educational purposes.


<img src="https://raw.githubusercontent.com/neutrinomuon/TreeHue/main/figures/PEP8-StyleGuide.jpg" width="70px"> Now, TreeHue has all its scripts in accordance with PEP 8 guidelines.

<br>
--------------------------------------------------------------------
<br>
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

<hr>

#### <b>INSTALLATION</b>

You can easily install <a href='https://pypi.org/project/TreeHue/'>TreeHue</a> by using pip - <a href='https://pypi.org/'>PyPI - The Python Package Index</a>:

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

Example of the TreeHue script in python

<img src="https://github.com/neutrinomuon/TreeHue/blob/main/figures/TreeHue_Screenshot.png?raw=true" width="90%">

<hr>

#### <b>STRUCTURE OF TreeHue (Created with TreeHue)</b>
<pre>
#################################################
workspace
├── tree.out
├── README.md
├── LICENSE.txt
├── index.html
├── dist
│   ├── TreeHue-0.0.4.tar.gz
│   └── TreeHue-0.0.4-py3.9.egg
├── setup.py
├── src
│   └── python
│       ├── treehue.py
│       ├── example.out
│       ├── __pycache__
│       │   ├── tree_colored.cpython-39.pyc
│       │   ├── treehue.cpython-39.pyc
│       │   └── treehue_colored.cpython-39.pyc
│       ├── example1.out
│       ├── __init__.py
│       └── treehue_colored.py
├── build
│   └── lib
│       └── TreeHue
│           ├── treehue.py
│           ├── __init__.py
│           └── treehue_colored.py
├── TreeHue.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── top_level.txt
│   └── requires.txt
├── showdown.min.js
├── version.txt
├── __pycache__
│   ├── tree_colored.cpython-39.pyc
│   └── tree.cpython-39.pyc
├── figures
│   ├── Education,_Studying,_University,_Alumni_-_icon.png
│   ├── Education_black_background.png
│   ├── Education_black_background-removebg.png
│   ├── PEP8-StyleGuide.jpg
│   ├── TreeHue.png
│   ├── Education_white_background.png
│   ├── cc_logo.png
│   └── TreeHue_Screenshot.png
├── TreeHue_conda
│   ├── osx-64
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── win-arm64
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── README.md
│   ├── osx-arm64
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── win-64
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── linux-s390x
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── linux-aarch64
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── linux-armv6l
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── meta.yaml
│   ├── linux-32
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── linux-ppc64le
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── linux-ppc64
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── win-32
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   ├── linux-64
│   │   └── treehue-0.0.3-py39_0.tar.bz2
│   └── linux-armv7l
│       └── treehue-0.0.3-py39_0.tar.bz2
├── .github
│   └── workflows
│       ├── main.yml
│       └── pylint.yml
└── .git
    ├── logs
    │   ├── HEAD
    │   └── refs
    │       ├── heads
    │       │   └── main
    │       └── remotes
    │           └── origin
    │               └── main
    ├── hooks
    │   ├── pre-commit.sample
    │   ├── pre-merge-commit.sample
    │   ├── commit-msg.sample
    │   ├── pre-push.sample
    │   ├── update.sample
    │   ├── sendemail-validate.sample
    │   ├── post-update.sample
    │   ├── fsmonitor-watchman.sample
    │   ├── applypatch-msg.sample
    │   ├── prepare-commit-msg.sample
    │   ├── pre-rebase.sample
    │   ├── pre-receive.sample
    │   ├── pre-applypatch.sample
    │   └── push-to-checkout.sample
    ├── config
    ├── shallow
    ├── info
    │   └── exclude
    ├── index
    ├── FETCH_HEAD
    ├── HEAD
    ├── description
    ├── objects
    │   ├── 41
    │   │   └── 5e27acccc7123d8a1864e12f423b06917717e9
    │   ├── c5
    │   │   ├── 30d3b504890de341def7f2ccb7c7247b27580b
    │   │   └── 5bc5c1096217c4d85d324fc6c6246b28d15d02
    │   ├── 7a
    │   │   ├── 26f38c6a45c060a5c1ffd8e435698c4a4cfeea
    │   │   └── 66d2054794646472ee0127bfa1159dd661b24c
    │   ├── c7
    │   │   └── f45a9b41a6f5fef0434fc1212694826d713bc8
    │   ├── f5
    │   │   ├── 2f76ca688f4a60eee4f3afa06b0dd2809b5e8b
    │   │   └── 6b034a3e2e3820180dc484cf6bea060087c358
    │   ├── bd
    │   │   └── 9d788edc091dcc07074f3c200ece2ca702b134
    │   ├── e6
    │   │   ├── 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
    │   │   └── f9c79cf41b840c0ae67e13614b934a2a789279
    │   ├── 89
    │   │   └── 2f612378d5a27a26e10db67eab2a3552b9949f
    │   ├── d2
    │   │   ├── 8ec90f746317c53ed9301c39f543b415865024
    │   │   └── 98a482db718d0159412485fedab1b752a251d9
    │   ├── 9a
    │   │   └── 666ea0f13a1f7e77fd56ada39a8ec927425618
    │   ├── a5
    │   │   ├── 7693046b0661870c3e9bf1055c6abb0343b3f5
    │   │   └── 3b48eba87b368cd3c2763579e0d1214066cfc9
    │   ├── d5
    │   │   ├── b27190c5d8fe67cfa4913fe9808e13e889fe89
    │   │   └── 62950fdb1072e09dd436b0b00b1424f6ef26fe
    │   ├── 13
    │   │   └── b27e1325431b9874905f2f77c53a5d602a43d8
    │   ├── 97
    │   │   └── a508cbec0dc2792317983e8f69d211429ed7c7
    │   ├── 1b
    │   │   └── 9df24f9acf1991096da996f2604a7795d0548c
    │   ├── 81
    │   │   └── 340c7e72d5c852585d0faea06985a720d4c2df
    │   ├── 44
    │   │   └── f6f369c624e49362c1f1a8acf3a24dec8bf725
    │   ├── pack
    │   ├── 4f
    │   │   └── 069ff5b07946e906e38c4723f3f8126247e7f6
    │   ├── f4
    │   │   └── 8d38249f5c0c8f7b6eff6dfac8043dbbe807f2
    │   ├── 69
    │   │   ├── af46ff8d580519bf80012a774a0421f2700ecc
    │   │   ├── 37cfc0969ec53e3e663807c206d0c0e76bc849
    │   │   └── 10a33a2173e3a6992d9b9e9dd8beb44b6d2ff5
    │   ├── b5
    │   │   └── 2d09afbd1b39082f77dacdf7b005816be2cccf
    │   ├── f1
    │   │   └── 233fe1a082ef10f448ff9d378fb59b2e79b981
    │   ├── 1d
    │   │   └── d1726b5a3024971c55a24f362d84c448784ed6
    │   ├── e2
    │   │   └── 5a8e6d9a04cea70b1f7d7c9115163aa160fab5
    │   ├── ee
    │   │   └── ff3d2aa3f9967cc6630fd49f35a5674298b185
    │   ├── c9
    │   │   └── 01b15d5e0b6168d3fec083b5e3e0cc6ceed184
    │   ├── info
    │   ├── aa
    │   │   ├── faaa6d5085c1804e5e228e3d3f627d2a782e61
    │   │   └── 094d9f64a7cc9debc3bc069b28f8398a62508f
    │   ├── 8e
    │   │   └── 1969aa17e5b94bb2c157aa08f317b4f51aa8ae
    │   ├── 36
    │   │   └── c87f28b7ecb85820302d56fdab8c8fef5f8a37
    │   ├── 5c
    │   │   └── b0a7b71a64caeedc165a9db06d654d6d5e12ec
    │   ├── 71
    │   │   └── 5dde02a154e818b07a5c7f14604e55dbdd9d93
    │   ├── ea
    │   │   └── 0d5de6beed610ae74388992752f913326edcfe
    │   ├── 21
    │   │   └── f27e4554aacede0f83afede078fc23aa15a097
    │   ├── 8b
    │   │   └── 137891791fe96927ad78e64b0aad7bded08bdc
    │   ├── b4
    │   │   └── 69a80b4c105fd028dbba771295a6828eb0ee4c
    │   ├── c1
    │   │   └── 284539918de9e3fe0f9dcd17808463e17e1481
    │   ├── 4a
    │   │   └── 409f730ebcdc71117d0a93dc2728970860403a
    │   ├── 20
    │   │   ├── 2fceb88d0351224bf22d9aecb7a5a308a76347
    │   │   └── fcefe73e574da8258f797e2d3a32659051c3dc
    │   ├── 80
    │   │   └── 4b5031750c3076e27096ca29bf728901d8fe6d
    │   ├── 5a
    │   │   └── 8dbd0652e37cc2d89b4899e307abcac8bda553
    │   ├── 2a
    │   │   └── fe3b3ac75bd1f8694b1bd0de68e9339ab18f74
    │   ├── fd
    │   │   └── db5a41258a96bd099b7f15881de301a4b70fb8
    │   ├── a7
    │   │   └── 53958a9a770f18fbfd9dd5600273b37f91c11f
    │   ├── 6b
    │   │   └── 235cfec2aa3378fa28a0c3f0b53bf2799e0a33
    │   ├── 76
    │   │   └── d50e99fb7cf244bf107536731fb5c56a815ad3
    │   ├── cc
    │   │   └── 13233786d42be7ad805906a84d80095091806b
    │   ├── 6c
    │   │   └── 9eeb8bed13d92dc2860c19656705478d8fc839
    │   ├── 1e
    │   │   └── 57aa55475620ecca7929fe3e54d5597e41c3cc
    │   ├── 4d
    │   │   └── e96b87204d2b88eb50fc5c103a791ed86db43f
    │   ├── 01
    │   │   └── 0e1cf9eb185c1edb1ae5d89b81c6c0977c03ab
    │   ├── 73
    │   │   └── fc3aaf2a8124fbdf1039f26e4fa82df56b2519
    │   ├── 42
    │   │   └── 68430b645889d28100a57891f1c0e589b7c1cd
    │   ├── 11
    │   │   └── 28c1f6627fd028f40cc85bcf2fe51ac3e37a70
    │   ├── e5
    │   │   └── a51a0da3ebf23d221cca2080f543ab4f7c5587
    │   ├── 0f
    │   │   └── 8971bd9942a347ea402b0b5e5979b0405e1e30
    │   ├── cb
    │   │   ├── 8f64e7f137aee9518c3019d7ddb59fe2ad2a67
    │   │   └── 33c4b11b0247e337441a2bcdeb85b59b29be7e
    │   ├── d3
    │   │   └── 1637f0e0bef1066586aad6f204d78ad4ad619d
    │   ├── 07
    │   │   ├── e84a15473342e5417a4a27cf05110adb4b301f
    │   │   └── c3f5f5faa7fdad4bf958ac15c26a570b438adb
    │   ├── 88
    │   │   └── f2578c6337dec2fb8e3301da2239baca2403c5
    │   ├── d0
    │   │   └── 3ad4e41ecb4545372e25e6bb667f89bc432346
    │   ├── 05
    │   │   └── e36c58292b7a104c8d8ab917b0d682638ae6a0
    │   ├── 1f
    │   │   └── acfbac556f8e938d75ba6e53d8be00eb5c2ae6
    │   └── 3b
    │       ├── c9b77a099f53bcba1b21baf0637b3af5eee26d
    │       └── d3b5a80009b500e3e466ba237cbd6b49c60ec5
    ├── branches
    └── refs
        ├── tags
        ├── heads
        │   └── main
        └── remotes
            └── origin
                └── main

106 directories, 155 files
#################################################
Generated with tree_colored @ 2024 - © Jean Gomes
#################################################
</pre>

<hr>

#### <b>ISSUES AND CONTRIBUTIONS</b>

If you encounter any issues with this project, please feel free to submit an
issue on the GitHub repository. We appreciate your feedback and are committed
to improving the quality of our codebase.

If you'd like to contribute to this project, we welcome pull requests from the
community. Before submitting a pull request, please make sure to fork the
repository and create a new branch for your changes. Once your changes are
complete, submit a pull request and we'll review your code as soon as
possible.

For any questions or concerns about contributing, please contact the project
maintainer at antineutrinomuon@gmail.com. Thank you for your interest in
contributing to our project!

<hr>

#### <b>LICENSE</b>

Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0)

<img src="https://github.com/neutrinomuon/TreeHue/blob/main/figures/cc_logo.png?raw=true" width="10%">

<a href='https://creativecommons.org/licenses/by-nc-nd/4.0/'>Creative Commons Attribution-NonCommercial-NoDerivs (CC-BY-NC-ND)</a>
