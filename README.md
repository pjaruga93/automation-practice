In order to run automated tests, follow steps below:

    1. Extract the project in desired place
    2. Set python interpreter / configure venv [python 3.9 recommended]
    3. Install requirements.txt
    4. Set path to your local chromedriver in environment.py file
    5. Use following command to run tests:
        behave --no-capture --tags @test_name