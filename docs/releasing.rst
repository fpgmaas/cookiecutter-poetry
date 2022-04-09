===================================
Releasing to Pypi or Artifactory
===================================

.. contents:: :local:
    :depth: 3


when ``include_github_actions`` is set to ``"y"``, a ``.github`` directory is added with the following structure:

::

    .github
    ├── workflows
    ├─── run-checks
    │    └── action.yml    
    ├─── setup-poetry-env
    │    └── action.yml         
    ├── on-merge-to-main.yml
    ├── on-pull-request.yml          
    └── on-release-main.yml
      
``on-merge-to-main.yml`` and ``on-pull-request.tml`` are identical except for their trigger conditions; the first is run whenever a new commit is made to ``main`` 
(which should only happen through merge requests, hence the name), and the latter is run whenever a pull request is opened or updated. They call the ``action.yml`` files
to set-up the environment, run the tests, and check the code formatting.

``on-release-main.yml`` does all of the former whenever a new release is made on the ``main`` branch. A new release can be made by clicking the 
``Draft a new release`` button on your repository's homepage:

.. image:: images/release-1.png
   :width: 500

Or if you fail to find it, by visiting ``https://github.com/<username>/<repository-name>/releases/new``.

Add a new tag in the form ``*.*.*`` where the ``*``'s are alphanumeric.

.. image:: images/release-2.png
   :width: 400

To finish, press ``Publish release``

.. image:: images/release-3.png
   :width: 300


In addition, when ``publish_to`` is set to ``"pypi"`` or ``"artifactory"``, this github action publishes the code to 
`Pypi <https://pypi.org>`_ or `Artifactory <https://jfrog.com/artifactory>`_ respectively. To get these to work, 


:::::::::::::::::::
Pypi
:::::::::::

testmake