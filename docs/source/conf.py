# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sp lila'
copyright = '2024, ykd'
author = 'ykd'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

#templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_theme_options = {
    'collapse_navbar': True
}

html_logo = "Designer.png"
# Path to the theme configuration file (optional)
html_theme_options = {
    'toc_title': 'Table of Contents',  # Customize Table of Contents title
}


# Welcome message to display on the landing page (optional)
html_title = project + ' Documentation'
html_welcome_msg = f"Welcome to the documentation for {project}!"


# -- Master file ------------------------------------------------------------

master_doc = 'index'

# Here you can configure the location of your main documentation file (index.rst by default).

# This sample `conf.py` file provides a basic configuration for the Sphinx Book Theme. 
# You can customize it further based on your specific needs. 
# Remember to replace placeholders like `Your Book Title`, `Your Name`, 
# and image paths with your actual information.
html_sidebars = {
   '**': ['globaltoc.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
}