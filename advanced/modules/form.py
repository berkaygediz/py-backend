from .form_elements import TextField, Button


class Form:
    def __init__(self):
        self.fields = []

    def add_field(self, field):
        self.fields.append(field)

    def create(self):
        form_html = "<form>"
        for field in self.fields:
            form_html += field.create()
        form_html += "</form>"
        return form_html
