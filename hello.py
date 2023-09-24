#!/usr/bin/env python3

"""Hello World Multi Language

Depending on the ambient language, the program shows the corresponding 
language.

How to use:

Have the LANG variable configured, example:

    export LANG=pt_BR

execution:

    python 3 hello.py
    or
    ./hello.py 
"""
__version__ = "0.0.1"
__author__ = "Matheus Mozer"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg ="Olá, Mundo!"
elif current_language == "de_DE":
    msg ="Hallo, Welt!"
elif current_language == "it_IT":
     msg ="Ciao, Mondo!"
elif current_language == "fr_FR":
     msg ="Bonjour, Monde!"
    
    
print(msg)

