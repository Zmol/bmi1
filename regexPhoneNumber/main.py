#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip, re


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# TODO: Create email regex.
mailRegex = re.compile(r'''(
    (\w*)           #username
    @               #@-symbol
    (\w*)           #domain
    \.              #dot
    (\w*)           #com or similar
)''', re.VERBOSE)
# TODO: Find matches in clipboard text.
text = pyperclip.paste()
mo = mailRegex.search(text)
print(mo)
# TODO: Copy results to the clipboard.