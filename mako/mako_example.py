from mako.template import Template

my_template = Template(filename="template.html")


my_dict = {}
my_dict['page_title'] = 'My Title'
my_dict['page_heading'] = 'The Heading.'
print(my_dict)
print(my_template.render(data=my_dict))