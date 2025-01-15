this_should_raise_Q003 = "This is a \"string\""
this_is_fine = "'This' is a \"string\""
this_is_fine = 'This is a "string"'
this_is_fine = '\'This\' is a "string"'
this_is_fine = r"This is a \"string\""
this_is_fine = R"This is a \"string\""
this_should_raise = (
    "This is a"
    "\"string\""
)

# Same as above, but with f-strings
f"This is a \"string\""
f"'This' is a \"string\""
f'This is a "string"'
f'\'This\' is a "string"'
fr"This is a \"string\""
fR"This is a \"string\""
foo = (
    f"This is a"
    f"\"string\""
)

# Nested f-strings (Python 3.12+)
#
# The first one is interesting because the fix for it is valid pre 3.12:
#
#   f'"foo" {"nested"}'
#
# but as the actual string itself is invalid pre 3.12, we don't catch it.
f"\"foo\" {"foo"}"  # Q003
f"\"foo\" {f"foo"}"  # Q003
f"\"foo\" {f"\"foo\""} \"\""  # Q003

f"normal {f"nested"} normal"
f"\"normal\" {f"nested"} normal"  # Q003
f"\"normal\" {f"nested"} 'single quotes'"
f"\"normal\" {f"\"nested\" {"other"} normal"} 'single quotes'"  # Q003
f"\"normal\" {f"\"nested\" {"other"} 'single quotes'"} normal"  # Q003
