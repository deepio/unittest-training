#!/bin/bash
echo "DocTest Starting..."
python3 ./main_doctest.py
echo "Unittest Starting..."
python3 -m unittest discover
echo "py.test Starting..."
py.test
echo "DocTest with py.test Starting..."
py.test --doctest-module main_doctest.py
