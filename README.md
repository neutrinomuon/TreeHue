### TreeHue
email: [antineutrinomuon@gmail.com](mailto:antineutrinomuon@gmail.com), [jean@astro.up.pt](mailto:jean@astro.up.pt)

github repository: <a href='https://github.com/neutrinomuon/TreeHue/'>TreeHue</a>

last stable version: 0.0.5
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
├── README.md
├── LICENSE.txt
├── index.html
├── requirements.txt
├── dist
│   └── TreeHue-0.0.5.tar.gz
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
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── win-arm64
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── README.md
│   ├── osx-arm64
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── win-64
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── linux-s390x
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── linux-aarch64
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── linux-armv6l
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── meta.yaml
│   ├── linux-32
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── linux-ppc64le
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── linux-ppc64
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── win-32
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   ├── linux-64
│   │   ├── treehue-0.0.3-py39_0.tar.bz2
│   │   └── treehue-0.0.4-py39_0.tar.bz2
│   └── linux-armv7l
│       ├── treehue-0.0.3-py39_0.tar.bz2
│       └── treehue-0.0.4-py39_0.tar.bz2
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
    │   ├── 31
    │   │   └── 874ff501dbdf9fbfb69a7185b441a93774b6bc
    │   ├── c5
    │   │   ├── 30d3b504890de341def7f2ccb7c7247b27580b
    │   │   └── 5bc5c1096217c4d85d324fc6c6246b28d15d02
    │   ├── 7a
    │   │   └── 66d2054794646472ee0127bfa1159dd661b24c
    │   ├── c7
    │   │   └── 3af08177e5d998556f7fe54282451a989e5410
    │   ├── f5
    │   │   └── 2f76ca688f4a60eee4f3afa06b0dd2809b5e8b
    │   ├── e6
    │   │   ├── 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
    │   │   └── f9c79cf41b840c0ae67e13614b934a2a789279
    │   ├── 89
    │   │   ├── bf1e584e0fdcb194183cca08f6206f7e448ba5
    │   │   └── 9361eaea332953134f3ddddb16c14717659845
    │   ├── d2
    │   │   └── 98a482db718d0159412485fedab1b752a251d9
    │   ├── 9a
    │   │   └── 666ea0f13a1f7e77fd56ada39a8ec927425618
    │   ├── d5
    │   │   ├── b27190c5d8fe67cfa4913fe9808e13e889fe89
    │   │   └── 62950fdb1072e09dd436b0b00b1424f6ef26fe
    │   ├── 97
    │   │   ├── 64ffd6225da94e8c39683afad348e30470d0a8
    │   │   └── a508cbec0dc2792317983e8f69d211429ed7c7
    │   ├── bb
    │   │   └── deab6222cb8ad8ab423239cbeff9e6163d0d38
    │   ├── b3
    │   │   └── 075f07eed36d2bfd47337fe947948f79c5a658
    │   ├── 8f
    │   │   └── 1797f1185efbc96c5ff82332c8265e75a9516b
    │   ├── 44
    │   │   └── f6f369c624e49362c1f1a8acf3a24dec8bf725
    │   ├── ac
    │   │   └── dbf2179c243a2b888e400e20212a94cb230f07
    │   ├── 17
    │   │   └── 2b7d9918b281939290370ac28875f1299dcd0b
    │   ├── pack
    │   ├── c2
    │   │   ├── b7151cb2e5abc6af8f1f7da6d459c0bcbfa779
    │   │   └── 413881cd066544add12e0d60df723cf8a93b82
    │   ├── 4f
    │   │   └── 069ff5b07946e906e38c4723f3f8126247e7f6
    │   ├── f4
    │   │   └── 0704a286f527ddfa168f2ace3f45f7344c8935
    │   ├── 69
    │   │   ├── 37cfc0969ec53e3e663807c206d0c0e76bc849
    │   │   ├── eec725f8df1d7332d47852a93a036b7d3ae09e
    │   │   └── 10a33a2173e3a6992d9b9e9dd8beb44b6d2ff5
    │   ├── b5
    │   │   └── 23684bf16d8111d5b2b2f51f559ce10ce0d2aa
    │   ├── f1
    │   │   └── 233fe1a082ef10f448ff9d378fb59b2e79b981
    │   ├── 1d
    │   │   └── d1726b5a3024971c55a24f362d84c448784ed6
    │   ├── b0
    │   │   ├── 31bbface1dbdfe8824966e4d4a8663b0280f1c
    │   │   └── 1a14ea53366ade692980ecd3134e82e8b03834
    │   ├── e2
    │   │   └── 5a8e6d9a04cea70b1f7d7c9115163aa160fab5
    │   ├── ee
    │   │   └── ff3d2aa3f9967cc6630fd49f35a5674298b185
    │   ├── c9
    │   │   └── 01b15d5e0b6168d3fec083b5e3e0cc6ceed184
    │   ├── info
    │   ├── ff
    │   │   └── 63db7da7e4e6671dc557120abd671735d8c4f8
    │   ├── 3d
    │   │   └── 42c32985bedb76e894ab0955efb3c5c11db330
    │   ├── 60
    │   │   └── 2f24b0b12eb1b298df02c1c2eadf0d74f8c32a
    │   ├── aa
    │   │   └── 094d9f64a7cc9debc3bc069b28f8398a62508f
    │   ├── 7f
    │   │   └── d3962e0cb670e58766edcbb906e153cf3ad97d
    │   ├── d4
    │   │   └── 7faab4c42d3177ac0531ddfa5f6797ce7f2996
    │   ├── d9
    │   │   └── 20de400aaadba6479f5cde68a03e1ff63a1d99
    │   ├── 08
    │   │   └── c93ab2b22ad17d39326899c95e835e75f7cf5d
    │   ├── 71
    │   │   └── 5dde02a154e818b07a5c7f14604e55dbdd9d93
    │   ├── ea
    │   │   └── 0d5de6beed610ae74388992752f913326edcfe
    │   ├── 91
    │   │   └── 2451ea382770ce89f3b1152663160c476f7f5d
    │   ├── 21
    │   │   ├── 64718931e14f51f63390bd06f2b2a58ffc9e6b
    │   │   └── f27e4554aacede0f83afede078fc23aa15a097
    │   ├── 8b
    │   │   ├── 31f01815380ffc13b0c9e46346f9468071aef2
    │   │   └── 137891791fe96927ad78e64b0aad7bded08bdc
    │   ├── b4
    │   │   └── 69a80b4c105fd028dbba771295a6828eb0ee4c
    │   ├── c1
    │   │   └── 284539918de9e3fe0f9dcd17808463e17e1481
    │   ├── 4a
    │   │   └── 409f730ebcdc71117d0a93dc2728970860403a
    │   ├── fa
    │   │   └── 8361b63848a5f4a68f7782b970c44f53eb5a3c
    │   ├── 0e
    │   │   └── 330900a52a8a8807e8c9160c07c0bfb9b37e42
    │   ├── 80
    │   │   ├── de325dccbfb87a726dd793fdbeaf14a70abb1c
    │   │   └── 4b5031750c3076e27096ca29bf728901d8fe6d
    │   ├── 5a
    │   │   └── 8dbd0652e37cc2d89b4899e307abcac8bda553
    │   ├── fd
    │   │   └── db5a41258a96bd099b7f15881de301a4b70fb8
    │   ├── 56
    │   │   ├── aaad52e4ba7a8b43e2e3aeda86630f8b944bb0
    │   │   └── 92729f0e25fbf8a98c43b2f354b7ecda7d28c7
    │   ├── 54
    │   │   └── 0830e25e08fe35938b61802ab38c36c3c3be49
    │   ├── 65
    │   │   └── bd3a127ddddf91fe6ca7a0c8eadca2b001abd4
    │   ├── a7
    │   │   └── 53958a9a770f18fbfd9dd5600273b37f91c11f
    │   ├── 6b
    │   │   └── 235cfec2aa3378fa28a0c3f0b53bf2799e0a33
    │   ├── 15
    │   │   └── 89d268bc79400f601d884d8d5db7301aecb9f9
    │   ├── e0
    │   │   └── 00c61baf5ad61d36704c14ab4003e7a43a4ec9
    │   ├── 19
    │   │   └── a8926accab36b527617c1f2e63a6fa7de4531f
    │   ├── 4d
    │   │   └── e96b87204d2b88eb50fc5c103a791ed86db43f
    │   ├── 10
    │   │   └── fefcce31bcb548c1ddd5cced81f71da7fef0a3
    │   ├── 01
    │   │   └── 0e1cf9eb185c1edb1ae5d89b81c6c0977c03ab
    │   ├── de
    │   │   ├── 8ce70558c208ffe64dfd2fc6c255c73df0c3ff
    │   │   └── c290c002941e33d5ec6647b1a6dc523d7995ee
    │   ├── 73
    │   │   └── fc3aaf2a8124fbdf1039f26e4fa82df56b2519
    │   ├── 42
    │   │   ├── c190b8c174a9fe306bba55a4cdd0c3af933b05
    │   │   └── 68430b645889d28100a57891f1c0e589b7c1cd
    │   ├── 0f
    │   │   └── 8971bd9942a347ea402b0b5e5979b0405e1e30
    │   ├── 5f
    │   │   ├── 2d0a3bfe8ce7673f298ed20d24e339aa8772a4
    │   │   └── 34a88fb1186ab80279ff6e5933201f21f45aba
    │   ├── d3
    │   │   └── 1637f0e0bef1066586aad6f204d78ad4ad619d
    │   ├── 07
    │   │   └── c3f5f5faa7fdad4bf958ac15c26a570b438adb
    │   ├── d0
    │   │   ├── 3ad4e41ecb4545372e25e6bb667f89bc432346
    │   │   └── 63da3069458d537958d2856c8a9e4c4ad0bc7a
    │   ├── 1f
    │   │   └── acfbac556f8e938d75ba6e53d8be00eb5c2ae6
    │   ├── d1
    │   │   └── d64756be8d0ff3cd25ed45a1177cab6b5f74dd
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

114 directories, 179 files
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
