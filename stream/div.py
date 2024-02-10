from typing import Union


class StreamDiv:
    def __init__(self, element_id:Union[str, None], class_name: Union[str, None] = None):
        self.class_name = class_name
        self.element_id = element_id
        self.content = ""

    def add_body_content(self, content):
        self.content += content

    def generate(self):
        class_and_id = f'class="{self.class_name}"' + (f' id="{self.element_id}"' if self.element_id else '')
        html = f"<div {class_and_id}>\n{self.content}\n</div>"
        return html
    




    


    




class DivElement:
    def __init__(self, class_name: str, element_id: Union[str, None] = None):
        self.class_name = class_name
        self.element_id = element_id
        self.content = ""

    def add_content(self, content):
        self.content += content

   