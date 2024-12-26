import pathlib
import sys

from pallets_sphinx_themes import ProjectLink

# `sys.path` has to be extended as
# we want to use `autodoc` in `conf.py`.
_DIRECTORY_REPO = pathlib.Path(__file__).parent.parent
assert (_DIRECTORY_REPO / ".git").is_dir(), _DIRECTORY_REPO
sys.path.insert(0, str(_DIRECTORY_REPO))
sys.path.insert(0, str(_DIRECTORY_REPO / "src"))

release, version = "0.0.1", "0.0.1.dev0"

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Octoprobe: Octoprobe"
copyright = "2024 Hans Märki"
author = "Hans Märki"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

default_role = "code"
extensions = [
    "myst_parser",
    "pallets_sphinx_themes",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxmermaid",
]

todo_include_todos = True
templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "sandbox",
]


intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "micropython": ("https://docs.micropython.org/en/latest/", None),
    "octoprobe": ("http://docs.octoprobe.org/octoprobe/", None),
    "tentacle": ("http://docs.octoprobe.org/tentacle/", None),
    "testbed_showcase": ("http://docs.octoprobe.org/testbed_showcase/", None),
    "testbed_micropython": ("http://docs.octoprobe.org/testbed_micropython/", None),
    # "usbhubctl": ("http://docs.octoprobe.org/usbhubctl/", None),
}
sphinxmermaid_mermaid_init: dict[str, str | dict] = {
    # "theme": "base",
    # "themeVariables": {
    #     "primaryColor": "#BB2528",
    #     "primaryTextColor": "#fff",
    #     "primaryBorderColor": "#7C0000",
    #     "lineColor": "#F8B229",
    #     "secondaryColor": "#006100",
    #     "tertiaryColor": "#fff",
    # },
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "basic"
# html_theme = "alabaster"
# html_theme = "sphinx_rtd_theme"
html_theme = "flask"
html_static_path = ["_static"]
html_context = {
    "project_links": [
        ProjectLink("Octoprobe: Tentacle", "https://www.octoprobe.org/tentacle/"),
        ProjectLink("Octoprobe: Octoprobe", "https://www.octoprobe.org/octoprobe/"),
        ProjectLink(
            "Octoprobe: testbed_showcase", "https://www.octoprobe.org/testbed_showcase/"
        ),
        ProjectLink(
            "Octoprobe: testbed_micropython", "https://www.octoprobe.org/testbed_micropython/"
        ),
        # ProjectLink("Octoprobe: usbhubctl", "https://www.octoprobe.org/usbhubctl/"),
        # ProjectLink("Donate", "https://palletsprojects.com/donate"),
        # ProjectLink("PyPI Releases", "https://pypi.org/project/octoprobe"),
        ProjectLink("Source Code", "https://github.com/octoprobe"),
        ProjectLink("Issue Tracker", "https://github.com/pallets/flask/issues/"),
        # ProjectLink("Chat", "https://discord.gg/pallets"),
    ]
}
# html_sidebars = {
#     "index": ["project.html", "localtoc.html", "searchbox.html", "ethicalads.html"],
#     "**": ["localtoc.html", "relations.html", "searchbox.html", "ethicalads.html"],
# }

# Custom sidebar templates, filenames relative to this file.
# html_sidebars = {
#     # Defaults taken from https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars
#     # Removes the quick search block
#     # '**': ['indexsidebar.html'],
#     # '**': ['indexsidebar.html', 'localtoc.html', 'relations.html', 'customsourcelink.html'],
#     '**': ['indexsidebar.html', 'localtoc.html', 'relations.html',],
#     # 'index': ['indexsidebar.html'],
#     # 'using/windows': ['windows-sidebar.html', 'searchbox.html'],
# }

# html_sidebars = {
#     "index": [
#         "project.html",
#         "localtoc.html",
#         "searchbox.html",
#         "ethicalads.html",
#     ],
#     "**": [
#         "project.html",
#         "localtoc.html",
#         "relations.html",
#         "searchbox.html",
#         "ethicalads.html",
#     ],
# }

html_sidebars = {
    "index": [
        "project.html",
        "localtoc.html",
        "searchbox.html",
        "ethicalads.html",
    ],
    "**": [
        "project.html",
        "localtoc.html",
        "relations.html",
        "searchbox.html",
        "ethicalads.html",
    ],
}
singlehtml_sidebars = {"index": ["project.html", "localtoc.html", "ethicalads.html"]}
html_favicon = "_static/shortcut-icon.png"
html_logo = "_static/octoprobe-vertical.png"
html_title = f"Octoprobe Documentation ({version})"
html_show_sourcelink = False
