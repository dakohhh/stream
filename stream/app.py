from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from .skeleton import StreamSkeleton
from .input import StreamHTMLInput


class StreamApp(FastAPI):
    def __init__(self, title: Union[str, None] = None) -> None:
        super().__init__(docs_url=None, redoc_url=None)

        self.app = super()

        self.skeleton = StreamSkeleton(title=title)



        @self.app.get("/")
        def main(request: Request):

            return HTMLResponse(self.skeleton.generate_html())
        

        @self.app.post("/")
        def main_post(request: Request):

            return {"data": "yeahh success"}
        

    
    def input(self, name, input_type:Union[str, None]=None):

        stream_input = StreamHTMLInput(name, input_type)

        self.skeleton.add_body_content(stream_input.generate())


    

    def submit():

        pass
