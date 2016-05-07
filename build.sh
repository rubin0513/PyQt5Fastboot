#!/bin/sh

pyinstaller -F --distpath burntool burntool.py
cp -rfv lj burntool
tar cvf burntool.tar.bz2 burntool
