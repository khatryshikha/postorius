Systers Postorius
------------------

.. image:: https://travis-ci.org/systers/postorius.svg?branch=develop
    :target: https://travis-ci.org/systers/postorius
.. image:: https://coveralls.io/repos/github/systers/posotrius/badge.svg?branch=develop
   :target: https://coveralls.io/github/systers/postorius?branch=develop



Systers Postorius is a Systers version of `mailman3 web interface Postorius <https://gitlab.com/mailman/postorius>`_

This repository is originally a clone of mailman's Postorius, it important to check the `LEGACY README <https://github.com/systers/postorius/blob/develop/LEGACY_README.rst>`_ which contains general setup of Postorius project.

This project is constantly changing on original repo so the live documentation maintained by the mailman3 Postorius may become confusing to use for this repository. Hence we maintain basic setup instructions here although it is advised to read the `LEGACY README <https://github.com/systers/postorius/blob/develop/LEGACY_README.rst>`_ first, We are always trying to keep this repo in synchrony with the latest updates.


Installation Setup
------------------

1. Clone the repository, create virtual environment.


    git clone https://gitlab.com/systers/postorius.git

    cd postorius

    virtualenv -p python3.5 venv

    source venv/bin/activate


2. Prepare database for project.


    cd example_project

    python manage.py migrate



3. Create super user.



    python manage.py createsuperuser



Fill in the details prompted to create a super user.

4. Run the development server.



    python manage.py runserver



**Please note**, the `live documentation <http://postorius.readthedocs.io/en/latest/development.html>`_ contains many other details that are important but may not be required for a successful setup, but you are strongly encouraged to visit the live documentation.


If you face any issues while setting up Postorius locally, post your queries on the `#mailman3 <https://systers-opensource.slack.com/messages/C0QK5PCNS/>`_ slack channel.


Documentation
-------------

A more comprehensive documentation for Postorius is generated using `Sphinx <http://sphinx-doc.org/>`_ and available online at http://postorius.readthedocs.io/en/latest/development.html and the general Mailman suite (which includes Postorius setup) at http://docs.mailman3.org/en/latest/prodsetup.html

To build the documentation locally run:



    cd src/postorius/

    make -C doc html



The HTML files will be available in the `doc/_build/html` directory.

For more information on semantics and builds, please refer to the Sphinx `official documentation <http://sphinx-doc.org/contents.html>`_.
