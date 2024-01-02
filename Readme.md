# Cucumber—python


# How to run tests 
- `$ behave`

# How to run unit tests 
- `$ python -m unittest tests.test_your_module1`


    project_root/
    │
    ├── features/
    │   ├── step_definitions/
    │   │   ├── __init__.py
    │   │   ├── your_step_definitions.py
    │   │
    │   ├── support/
    │   │   ├── __init__.py
    │   │   ├── env.py
    │   │   └── your_support_code.py
    │   │
    │   ├── your_feature_file.feature
    │   └── another_feature_file.feature
    │
    ├── src/
    │   ├── __init__.py
    │   ├── your_python_module1.py
    │   └── your_python_module2.py
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_your_module1.py
    │   └── test_your_module2.py
    │
    ├── .gitignore
    ├── requirements.txt
    ├── README.md
    └── your_main_script.py