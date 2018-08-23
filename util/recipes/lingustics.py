import linguistictagger as lt
text = 'Python is pretty awesome.'
results = lt.tag_string(text, lt.SCHEME_LEMMA)
for tag, substring, range in results:
	if tag != 'Whitespace':
		print(substring + ": " + tag)
		
		
SCHEME_NAME_TYPE_OR_LEXICAL_CLASS
