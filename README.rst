molo.surveys
=============================

.. image:: https://img.shields.io/travis/praekelt/molo.pwa.svg
        :target: https://travis-ci.org/praekelt/molo.pwa

.. image:: https://img.shields.io/pypi/v/molo.pwa.svg
        :target: https://pypi.python.org/pypi/molo.pwa

.. image:: https://coveralls.io/repos/praekelt/molo.pwa/badge.png?branch=develop
    :target: https://coveralls.io/r/praekelt/molo.pwa?branch=develop
    :alt: Code Coverage

An implementation of pwa as a Molo plugin

Installation::

   pip install molo.pwa


Django setup::

   INSTALLED_APPS = (
      'wagtailsurveys',
      'wagtail_personalisation',
      'wagtailfontawesome',

   )


In your urls.py::

    url(
        r"^(?P<slug>[\w-]+)/success/$",
        SurveySuccess.as_view(),
        name="success"
    ),


In your main.html::

   {% load molo_survey_tags %}

   {% block content %}
      {% surveys_list %}
   {% endblock %}

In your section page or article page::

   {% load molo_survey_tags %}

   {% block content %}
    {{% surveys_list_for_pages page=self %}
   {% endblock %}
