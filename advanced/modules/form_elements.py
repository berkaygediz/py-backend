class TextField:
    def __init__(self, label):
        self.label = label

    def create(self):
        return f'<label>{self.label}:</label><br><input type="text"><br>'


class Button:
    def __init__(self, label):
        self.label = label

    def create(self):
        return f'<button>{self.label}</button>'
