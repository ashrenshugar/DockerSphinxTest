# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Project-AIRE'
copyright = '2022, Consilium Technology'
author = 'Consilium Technology'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinxcontrib.cairosvgconverter'
]

source_suffix = ['.rst', '.md', '.html']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Myst syntaxes
myst_enable_extensions = [

]

latex_engine = 'xelatex'
latex_elements = {
    'extraclassoptions': 'openany,oneside',
    'preamble': r'''
\makeatletter
   \fancypagestyle{normal}{
% this is the stuff in sphinx.sty
    \fancyhf{}
    \fancyfoot[R]{{\py@HeaderFamily\thepage}}
% add copyright stuff
    \fancyhead[L]{UNOFFICAL}
% again original stuff
    \fancyhead[R]{{\py@HeaderFamily \@title\sphinxheadercomma\py@release}}
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
    }
% this is applied to each opening page of a chapter
   \fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[R]{{\py@HeaderFamily\thepage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0.4pt}
% add Classification stuff for example at left of footer on odd pages,
% which is the case for chapter opening page by default
    \fancyhead[L]{UNOFFICAL}
    }
\makeatother
''',
}


#latex_show_urls = 'footnote'
