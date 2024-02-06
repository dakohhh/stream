class StreamHTMLInput:

    def __init__(self, name: str, input_type) -> None:

        self.name = name
        self.input_type = input_type

    def generate(self):

        form_html = ""

        form_html += f"<label>{self.name}:</label>"

        form_html += f'<input type="{self.input_type}" name="{self.name.lower()}"><br>'

        return form_html


if __name__ == "__main__":

    html_input = StreamHTMLInput("Username", input_type="text")

    print(html_input.generate())
