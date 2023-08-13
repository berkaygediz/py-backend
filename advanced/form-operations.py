from modules.form import Form
from modules.form_elements import TextField, Button

# Creating a form
form = Form()

# Adding fields
name_field = TextField("Name")
form.add_field(name_field)

submit_button = Button("Submit")
form.add_field(submit_button)

# Creating and printing the HTML form
html_form = form.create()
print(html_form)
