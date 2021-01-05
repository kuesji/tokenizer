def tokenize(text):
	operators = (
		'+','-','/','*','%',
		'=','!','<','>','&','^','|',
		'<=','>=','==','!=',
		'&&','||'
	)

	parenthesis = (
		'(',')','[',']','{','}'
	)

	specials = (
		'.',',',':',';'
	)

	text += ' '
	tokens = []
	current_type = None
	current_value = ''

	for c in text:
		if current_type != None:
			if current_type == 'number':
				if not c.isnumeric():
					if c == '.' and '.' not in current_value:
						current_value += c
					else:
						tokens.append(('number',current_value))
						current_type,current_value = None,''
				else:
					current_value += c

			elif current_type == 'operator':
				if current_value+c == '/*':
					current_type, current_value = 'comment',current_value+c
				elif current_value+c not in operators:
					tokens.append(('operator',current_value))
					current_type, current_value = None,''
				else:
					current_value += c

			elif current_type == 'parenthesis':
				if current_value+c not in parenthesis:
					tokens.append(('parenthesis',current_value))
					current_type, current_value = None,''
				else:
					current_value += c

			elif current_type == 'special':
				if current_value+c not in specials:
					tokens.append(('special',current_value))
					current_type, current_value = None,''
				else:
					current_value += c

			elif current_type == 'name':
				if c.isalnum() or c == '_':
					current_value += c
				else:
					tokens.append(('name',current_value))
					current_type, current_value = None,''

			elif current_type == 'string':
				if c == '"':
					# check for escape via counting slash symbol. \" is escape and \\" is not
					slash_count = 0
					for cx in current_value[::-1]:
						if cx != '\\':
							break
						slash_count += 1
					if slash_count % 2 == 0:
						tokens.append(('string',current_value))
						current_type, current_value = None,''
						# bypass current character
						continue
					else:
						current_value += c
				else:
					current_value += c

			elif current_type == 'comment':
				if ( len(current_value) == 1 and c != '*' ) or ( c == '/' and current_value[-1] != '*' ):
					return [('error','comments starts with /* and ends with */')]
				elif c == '/':
					tokens.append(('comment',current_value))
					current_type, current_value = None,''
					# bypass current character
					continue
				else:
					current_value += c

		if current_type == None:
			if c.isnumeric():
				current_type, current_value = 'number',c
			elif c.isalpha() or c == '_':
				current_type, current_value = 'name',c
			elif c == '"':
				current_type, current_value = 'string',''
			elif c in operators:
				current_type, current_value = 'operator',c
			elif c in parenthesis:
				current_type, current_value = 'parenthesis',c
			elif c in specials:
				current_type, current_value = 'special',c
			elif c == '/':
				current_type, current_value = 'comment',c
			elif c in (' ','\n','\t'):
				# i don't care whitespaces
				continue
			else:
				return [('error','unknown char {}'.format(c))]

	return tokens
