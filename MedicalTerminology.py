#made by Darrien Drake
#Published on 20260903

from WordRoots import WordRoot
from Prefixes import Prefix
from Suffixes import Suffix

print("Welcome to the Medical Terminology Program! The format is: prefix, suffix, wordroot/combining form.")

prefix = input("Enter a prefix (or leave blank): ").strip().lower()
suffix = input("Enter a suffix (or leave blank): ").strip().lower()
root = input("Enter a word root/combining form (or leave blank): ").strip().lower()

if prefix:
    try:
        Prefix.definition(prefix)
    except KeyError:
        pass

if root:
    try:
        WordRoot.definition(root)
    except KeyError:
        pass

if suffix:
    try:
        Suffix.definition(suffix)
    except KeyError:
        pass
