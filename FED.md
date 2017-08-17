Running local HTML Tests

To Get Started

- $ virtualenv ve
- $ source ve/bin/activate
- $ pip install -e .

- molo scaffold testapp --require molo.pwa
- cp molo/surveys/test_templates/*.html testapp/testapp/templates/core/

- pip install -e testapp
- py.test --cov=molo.pwa --cov-report=term
- pip install -r requirements-dev.txt
- py.test

To Run A Specific Test
- py.test -k test_pwa
