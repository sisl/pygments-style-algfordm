# -*- coding: utf-8 -*-
"""
    pygments.styles.algfordm
    ~~~~~~~~~~~~~~~~~~~~~~~

    :license: MIT
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal

class AlgForDMStyle(Style):
    """
    This style is for the Algorithms for Decision Making book.
    """

    background_color = "#f8f8f8"
    default_style = ""

    styles = {
        Whitespace:                "#bbbbbb",
        Comment:                   "italic #0b5075",
        Comment.Preproc:           "noitalic #BC7A00",

        Keyword:                   "bold #0072B2",
        Keyword.Pseudo:            "nobold",
        Keyword.Type:              "nobold #0072B2",
        Keyword.Reserved           "#19177C",
        Keyword.Other:             "bold #73C6F2",
        Other:                     "bold #73C6F2",


        Operator:                  "#999999",
        Operator.Word:             "bold #AA22FF",


        Name.Builtin:              "#0072B2",
        Name.Function:             "#56B4E9",
        Name.Class:                "bold #56B4E9",
        Name.Namespace:            "bold #56B4E9",
        Name.Exception:            "bold #D2413A",
        Name.Variable:             "#19177C",
        Name.Constant:             "#880000",
        Name.Label:                "#A0A000",
        Name.Entity:               "bold #999999",
        Name.Attribute:            "#7D9029",
        Name.Tag:                  "bold #0072B2",
        Name.Decorator:            "#FF48CF",

        String:                    "#F5615C",
        String.Doc:                "italic",
        String.Interpol:           "bold #BB6688",
        String.Escape:             "bold #BB6622",
        String.Regex:              "#F5615C",
        String.Symbol:             "#F3453F",
        String.Other:              "#0072B2",
        Number:                    "#666666",

        Generic.Heading:           "bold #000080",
        Generic.Subheading:        "bold #800080",
        Generic.Deleted:           "#A00000",
        Generic.Inserted:          "#00A000",
        Generic.Error:             "#FF0000",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold #0F6FA3",
        Generic.Output:            "#888",
        Generic.Traceback:         "#04D",

        Error:                     "border:#FF0000"
    }
