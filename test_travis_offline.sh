#! /usr/bin/env bash
status_code=$?
function chk()
{ 
    let "status_code=$status_code||$?";
}
if [ "$1" != "nopep8" ] && [ "$2" != "nopep8" ];
    then
    {
        echo "Starting PEP8 Test";
        pep8 --exclude="build/*" --ignore=E501 ./; chk;
        echo "PEP8 Test ended";
    }
else
    echo "PEP8 Test skipped";

fi

cd BinPy/tests/; chk;
nosetests -v; chk;
nosetests3 -v -v; chk;
nosetests -v gates_tests.py; chk;
nosetests -v combinational_tests.py; chk;
nosetests -v operations_tests.py; chk;
nosetests -v sequential_tests.py; chk;
nosetests -v counters_tests.py; chk;
nosetests -v series_4000_tests.py; chk;
nosetests -v series_7400_tests.py; chk;
nosetests -v source_tests.py; chk;
nosetests -v sequential_ic_tests.py; chk;
nosetests -v registers_tests.py; chk;
nosetests -v tree_tests.py; chk;
nosetests -v print_tests.py; chk;
nosetests -v expr_tests.py; chk;
nosetests -v analog_devices_tests.py; chk;
nosetests -v analog_source_tests.py; chk;
nosetests -v test_makebooleanfunction.py; chk;
nosetests -v test_analog_converters_buffers.py; chk;
nosetests -v test_signal_generator.py; chk;
nosetests -v test_multiplication_algorithms.py; chk;
nosetests3 -v gates_tests.py; chk;
nosetests3 -v combinational_tests.py; chk;
nosetests3 -v operations_tests.py; chk;
nosetests3 -v sequential_tests.py; chk;
nosetests3 -v counters_tests.py; chk;
nosetests3 -v series_4000_tests.py; chk;
nosetests3 -v series_7400_tests.py; chk;
nosetests3 -v source_tests.py; chk;
nosetests3 -v sequential_ic_tests.py; chk;
nosetests3 -v registers_tests.py; chk;
nosetests3 -v tree_tests.py; chk;
nosetests3 -v print_tests.py; chk;
nosetests3 -v expr_tests.py; chk;
nosetests3 -v analog_devices_tests.py; chk;
nosetests3 -v analog_source_tests.py; chk;
nosetests3 -v test_makebooleanfunction.py; chk;
nosetests3 -v test_analog_converters_buffers.py; chk;
nosetests3 -v test_signal_generator.py; chk;
nosetests3 -v test_multiplication_algorithms.py; chk;
nosetests3 -v  --with-coverage --cover-package=BinPy
exit $status_code;

