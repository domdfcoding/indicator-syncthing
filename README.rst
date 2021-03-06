==========================
indicator-syncthing
==========================

.. start short_desc

**A Syncthing status menu for Unity and other desktops that support AppIndicator.**

.. end short_desc

Syncthing_ v0.11.0 and higher are supported.

This is a fork of Stuart Langridge's syncthing-ubuntu-indicator_.


.. _Syncthing: https://github.com/syncthing/syncthing

.. _syncthing-ubuntu-indicator: https://github.com/stuartlangridge/syncthing-ubuntu-indicator

.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Tests
	  - |actions_linux|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy| |pre_commit_ci|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/domdfcoding/indicator-syncthing/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/indicator-syncthing/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/indicator-syncthing/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/indicator-syncthing/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/indicator-syncthing/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/indicator-syncthing/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://requires.io/github/domdfcoding/indicator-syncthing/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/indicator-syncthing/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/indicator-syncthing?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/indicator-syncthing
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/indicator-syncthing
	:target: https://pypi.org/project/indicator-syncthing/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/indicator-syncthing?logo=python&logoColor=white
	:target: https://pypi.org/project/indicator-syncthing/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/indicator-syncthing
	:target: https://pypi.org/project/indicator-syncthing/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/indicator-syncthing
	:target: https://pypi.org/project/indicator-syncthing/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/indicator-syncthing
	:target: https://github.com/domdfcoding/indicator-syncthing/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/indicator-syncthing
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/indicator-syncthing/v0.1.0
	:target: https://github.com/domdfcoding/indicator-syncthing/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/indicator-syncthing
	:target: https://github.com/domdfcoding/indicator-syncthing/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/indicator-syncthing
	:target: https://pypi.org/project/indicator-syncthing/
	:alt: PyPI - Downloads

.. |pre_commit_ci| image:: https://results.pre-commit.ci/badge/github/domdfcoding/indicator-syncthing/master.svg
	:target: https://results.pre-commit.ci/latest/github/domdfcoding/indicator-syncthing/master
	:alt: pre-commit.ci status

.. end shields

Dependencies
==========================

.. code-block:: bash

	python3_dateutil>=2.8.1
	requests_futures>=1.0.0
	requests>=2.18.4
	PyGObject>=3.34.0


Installation
==========================

.. start installation

``indicator-syncthing`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install indicator-syncthing

.. end installation
