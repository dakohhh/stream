from .input import StreamHTMLInput

class StreamHTMLForm:
    def __init__(self, action="", method="POST"):
        self.action = action
        self.method = method
        self.fields = []

    def add_field(self, label, name, input_type="text"):
        field = {"label": label, "name": name, "type": input_type}
        self.fields.append(field)

    def generate_form(self):
        form_html = f'<form action="{self.action}" method="{self.method}">'
        for field in self.fields:
            form_html += f'<label>{field["label"]}:</label>'
            form_html += f'<input type="{field["type"]}" name="{field["name"]}"><br>'
        form_html += '<input type="submit" value="Submit">'
        form_html += "</form>"
        return form_html


# Example usage
    

if __name__ == "__main__":
    my_form = StreamHTMLForm(action="/submit_form", method="POST")
    my_form.add_field(label="Username", name="username")
    my_form.add_field(label="Password", name="password", input_type="password")

    html_code = my_form.generate_form()
    print(html_code)
