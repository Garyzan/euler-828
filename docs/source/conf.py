# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#autodoc_mock_imports = ['expression', 'node', 'problem', 'reader', 'solver']

project = 'euler828'
copyright = '2024, Timo van Meegdenburg'
author = 'Timo van Meegdenburg'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc",
              "sphinx.ext.coverage",
              "sphinx.ext.mathjax",
              "sphinx.ext.viewcode",
              "sphinx.ext.githubpages",
              "numpydoc",
              "myst_nb",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

nb_execution_mode = "off"

html_sourcelink_suffix = ""

import os
suppress_warnings = [
    f"autosection_label._examples/{filename.split('.')[0]}"
    for filename in os.listdir("notebooks")
    if os.path.isfile(os.path.join("notebooks", filename))
]

remove_from_toctrees = ["_autosummary/*"]