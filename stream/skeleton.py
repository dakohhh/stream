from typing import Union


class StreamSkeleton:
    def __init__(self, title: Union[str, None]=None):
        self.title = title
        self.head_content = ""
        self.body_content = ""

    def add_head_content(self, content):
        self.head_content += content

    def add_body_content(self, content):
        self.body_content += content

    def generate_html(self):
        html = f"<!DOCTYPE html>\n<html>\n<head>\n<title>{self.title}</title>\n{self.head_content}\n</head>\n<body>\n{self.body_content}\n</body>\n</html>"
        return html

# Example usage
skeleton = StreamSkeleton(title="Steam App")
skeleton.add_head_content('<meta charset="UTF-8">')
skeleton.add_head_content('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
skeleton.add_body_content('<h1>Hello, World!</h1>')
skeleton.add_body_content('<p>This is a sample HTML page generated with a Python class.</p>')

