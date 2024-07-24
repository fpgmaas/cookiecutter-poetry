{%- if cookiecutter.database == 'n' %}
::: {{cookiecutter.project_slug}}.foo
{%- else %}
::: {{cookiecutter.project_slug}}
{%- endif %}
