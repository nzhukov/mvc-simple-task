

def render_client(client)->str:

	from jinja2 import Template 
	

	# template = env.get_template('layout.html')
	

	template = Template('<html><head><title> {{title}} </title><meta charset="utf-8"></head><body><form method="POST"><input type="text" value="{{ cl.full_name }}"> <input type="submit"></form></body></html>')
	s = template.render(title="Индексная страница", cl=client)

	# s = f'<html><head><meta charset="utf-8"></head>Hello, {str(client)}</html>'

	return s