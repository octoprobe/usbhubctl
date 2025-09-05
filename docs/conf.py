import os
import pathlib
import re
import sys

# `sys.path` has to be extended as
# we want to use `autodoc` in `conf.py`.
_DIRECTORY_REPO = pathlib.Path(__file__).parent.parent
assert (_DIRECTORY_REPO / ".git").is_dir(), _DIRECTORY_REPO
sys.path.insert(0, str(_DIRECTORY_REPO))
sys.path.insert(0, str(_DIRECTORY_REPO / "src"))

# # TODO(hansm): Include the correct version
# from sphinx.locale import _
# from sphinx_rtd_theme import (
#     __version__ as theme_version,
#     __version_full__ as theme_version_full,
# )

project = "Octoprobe"
slug = re.sub(r"\W+", "-", project.lower())
# version = theme_version
# release = theme_version_full
author = "Hans Märki"
copyright = "2024,2025 Hans Märki"
language = "en"

extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxmermaid",
]

todo_include_todos = True
templates_path = ["_templates"]
source_suffix = ".rst"
exclude_patterns = [
    "_build",
    "sandbox",
]
locale_dirs = ["locale/"]
gettext_compact = False

master_doc = "index_top"
suppress_warnings = ["image.nonlocal_uri"]
pygments_style = "default"

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
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only": True,
    "navigation_depth": 5,
    "version_selector": False,
    "language_selector": False,
}
html_context = {
    # TODO(hansm): Are these links still required? How to add them?
    # "project_links": [
    #     ProjectLink("Octoprobe: Tentacle", "https://www.octoprobe.org/tentacle/"),
    #     ProjectLink("Octoprobe: Octoprobe", "https://www.octoprobe.org/octoprobe/"),
    #     ProjectLink(
    #         "Octoprobe: testbed_showcase", "https://www.octoprobe.org/testbed_showcase/"
    #     ),
    #     ProjectLink(
    #         "Octoprobe: testbed_micropython",
    #         "https://www.octoprobe.org/testbed_micropython/",
    #     ),
    #     # ProjectLink("Octoprobe: usbhubctl", "https://www.octoprobe.org/usbhubctl/"),
    #     # ProjectLink("Donate", "https://palletsprojects.com/donate"),
    #     # ProjectLink("PyPI Releases", "https://pypi.org/project/octoprobe"),
    #     ProjectLink("Source Code", "https://github.com/octoprobe"),
    #     ProjectLink("Issue Tracker", "https://github.com/octoprobe/issues/"),
    #     # ProjectLink("Chat", "https://discord.gg/pallets"),
    # ]
}

if "READTHEDOCS" not in os.environ:
    html_static_path = ["_static/"]
    html_js_files = ["debug.js"]
    html_context["DEBUG"] = True
html_favicon = "_static/shortcut-icon.png"
html_logo = "_static/octoprobe-horizontal.png"
html_show_sourcelink = True
html_title = "Octoprobe Documentation"


htmlhelp_basename = slug

latex_documents = [
    ("index", f"{slug}.tex", project, author, "manual"),
]

man_pages = [("index", slug, project, [author], 1)]

texinfo_documents = [
    ("index", slug, project, author, slug, project, "Miscellaneous"),
]


# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        "confval",
        "confval",
        objname="configuration value",
        indextemplate="pair: %s; configuration value",
        doc_field_types=[
            PyField(
                "type",
                label="Type",
                has_arg=False,
                names=("type",),
                bodyrolename="class",
            ),
            Field(
                "default",
                label="Default",
                has_arg=False,
                names=("default",),
            ),
        ],
    )
