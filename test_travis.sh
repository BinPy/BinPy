#! /usr/bin/env bash
status_code=$?
function chk()
{ 
    let "status_code=$status_code||$?";
}

# To make nosetests run under different python environments.
function nt()
{
    python $(which nosetests) $1;
}

pep8 --exclude="build/*" --ignore=E501 ./; chk;

cd BinPy/tests/;

nt .; chk;
nt gates_tests.py; chk;
nt combinational_tests.py; chk;
nt operations_tests.py; chk;
nt sequential_tests.py; chk;
nt counters_tests.py; chk;
nt series_4000_tests.py; chk;
nt series_7400_tests.py; chk;
nt source_tests.py; chk;
nt sequential_ic_tests.py; chk;
nt registers_tests.py; chk;
nt tree_tests.py; chk;
nt print_tests.py; chk;
nt expr_tests.py; chk;
nt analog_devices_tests.py; chk;
nt analog_source_tests.py; chk;
nt test_makebooleanfunction.py; chk;
nt test_analog_converters_buffers.py; chk;
nt test_signal_generator.py; chk;
nt test_multiplication_algorithms.py; chk;
nosetests --with-coverage --cover-package=BinPy

exit $status_code;
