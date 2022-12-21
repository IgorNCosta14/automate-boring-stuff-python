import re, pyperclip
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d)))? # area code(opcional)
(\s|-) # first separator
\d\d\d first 3 digits
-    #separator
\d\d\d\d # last 3 digits
(((ext (\.)?\s) |x) # extension word-part (optional)
(\d{2,5}))?  # extension number-part (optional)
)
''', re.VERBOSE)

emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+  # name aprt
@                #@ symbol
[a-zA-Z0-9_.+]+  #domain name part
''', re.VERBOSE)

text = pyperclip.past()

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in aextractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n'.join(extractedEmail)
