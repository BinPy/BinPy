#! /usr/bin/env bash
status_code=$?
function chk()
{ 
    let "status_code=$status_code||$?";
}

pep8 --exclude="build/*" --ignore=E501 ./; chk;

cd BinPy/tests/; chk;
nosetests; chk;
nosetests3; chk;
nosetests gates_tests.py; chk;
nosetests combinational_tests.py; chk;
nosetests operations_tests.py; chk;
nosetests sequential_tests.py; chk;
nosetests counters_tests.py; chk;
nosetests series_4000_tests.py; chk;
nosetests series_7400_tests.py; chk;
nosetests source_tests.py; chk;
nosetests sequential_ic_tests.py; chk;
nosetests registers_tests.py; chk;
nosetests tree_tests.py; chk;
nosetests print_tests.py; chk;
nosetests expr_tests.py; chk;
nosetests analog_devices_tests.py; chk;
nosetests analog_source_tests.py; chk;
nosetests test_makebooleanfunction.py; chk;
nosetests3 gates_tests.py; chk;
nosetests3 combinational_tests.py; chk;
nosetests3 operations_tests.py; chk;
nosetests3 sequential_tests.py; chk;
nosetests3 counters_tests.py; chk;
nosetests3 series_4000_tests.py; chk;
nosetests3 series_7400_tests.py; chk;
nosetests3 source_tests.py; chk;
nosetests3 sequential_ic_tests.py; chk;
nosetests3 registers_tests.py; chk;
nosetests3 tree_tests.py; chk;
nosetests3 print_tests.py; chk;
nosetests3 expr_tests.py; chk;
nosetests3 analog_devices_tests.py; chk;
nosetests3 analog_source_tests.py; chk;
nosetests3 test_makebooleanfunction.py; chk;
nosetests3  --with-coverage --cover-package=BinPy
exit $status_code;

