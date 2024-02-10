class StreamHTMLInput:

    def __init__(self, name: str, input_type) -> None:

        self.name = name


        self.input_type = input_type if input_type else "text"

    def generate(self):

        form_html = ""

        if self.input_type != "submit":
            form_html += f"<label>{self.name}:</label>"

        form_html += f'<input type="{self.input_type}" name="{self.name.lower()}"><br>'

        return form_html


if __name__ == "__main__":

    html_input = StreamHTMLInput("Username", input_type="text")

    print(html_input.generate())
