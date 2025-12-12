#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import pathlib
import shutil
import sys

# 3rd party
from setuptools import setup

sys.path.append('.')

extras_require = {}

# stdlib
from textwrap import dedent

with open("indicator-syncthing.desktop", 'w', encoding="UTF-8") as desktop:
	desktop.write(
			dedent(
					f"""\
[Desktop Entry]
Version=0.1.0
Name=indicator-syncthing
Comment=A Syncthing status menu for Unity and other desktops that support AppIndicator.
Exec=indicator-syncthing
Icon=syncthing
Terminal=False
Type=Application
Categories=Utility
"""
					)
			)

repo_root = pathlib.Path(__file__).parent
install_requires = (repo_root / "requirements.txt").read_text(encoding="UTF-8").split('\n')

setup(
		data_files=[("share/applications", ["indicator-syncthing.desktop"])],
		description="A Syncthing status menu for Unity and other desktops that support AppIndicator.",
		extras_require=extras_require,
		install_requires=install_requires,
		name="indicator-syncthing",
		py_modules=[],
		)

shutil.rmtree("indicator_syncthing.egg-info", ignore_errors=True)
