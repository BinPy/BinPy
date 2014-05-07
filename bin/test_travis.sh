#! /usr/bin/env bash

pep8 --ignore=E501 ./
nosetests
nosetests3
cd BinPy/tests/
nosetests gates_tests.py
nosetests combinational_tests.py
nosetests operations_tests.py
nosetests sequential_tests.py
nosetests counters_tests.py
nosetests series_4000_tests.py
nosetests series_7400_tests.py
nosetests source_tests.py
nosetests sequential_ic_tests.py
nosetests registers_tests.py
nosetests tree_tests.py
nosetests print_tests.py
nosetests expr_tests.py
nosetests analog_devices_tests.py
nosetests analog_source_tests.py
nosetests test_makebooleanfunction.py
nosetests3 gates_tests.py
nosetests3 combinational_tests.py
nosetests3 operations_tests.py
nosetests3 sequential_tests.py
nosetests3 counters_tests.py
nosetests3 series_4000_tests.py
nosetests3 series_7400_tests.py
nosetests3 source_tests.py
nosetests3 sequential_ic_tests.py
nosetests3 registers_tests.py
nosetests3 tree_tests.py
nosetests3 print_tests.py
nosetests3 expr_tests.py
nosetests3 analog_devices_tests.py
nosetests3 analog_source_tests.py
nosetests3 test_makebooleanfunction.py
