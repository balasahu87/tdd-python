# tdd-python
source .venv/bin/activate
pip3 install flask

python app.py

curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"numbers": ""}'

{"result": 0}


curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"numbers": "1,5"}'

{"result": 6}

curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"numbers":"1\n2,3"}'

{"result": 3}

curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"numbers":"1,-2,3,-4"}'

{"error": "negative numbers not allowed -2,-4"}


# Test 

pip3 install pytest pytest-flask

pytest -v

(.venv) Balarams-MacBook-Air:tdd-python postgres$ pytest -v
======================================= test session starts =======================================
platform darwin -- Python 3.13.3, pytest-8.4.2, pluggy-1.6.0 -- /Users/postgres/tdd-python/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/postgres/tdd-python
plugins: flask-1.3.0
collected 13 items                                                                                

test_app.py::test_empty_string_returns_zero PASSED                                          [  7%]
test_app.py::test_single_number PASSED                                                      [ 15%]
test_app.py::test_two_numbers PASSED                                                        [ 23%]
test_app.py::test_multiple_numbers PASSED                                                   [ 30%]
test_app.py::test_newline_delimiter PASSED                                                  [ 38%]
test_app.py::test_custom_delimiter PASSED                                                   [ 46%]
test_app.py::test_negative_number_raises_error PASSED                                       [ 53%]
test_app.py::test_multiple_negatives PASSED                                                 [ 61%]
test_app.py::test_api_empty_string PASSED                                                   [ 69%]
test_app.py::test_api_two_numbers PASSED                                                    [ 76%]
test_app.py::test_api_newline PASSED                                                        [ 84%]
test_app.py::test_api_custom_delimiter PASSED                                               [ 92%]
test_app.py::test_api_negative_numbers PASSED                                               [100%]

======================================= 13 passed in 0.41s ========================================

