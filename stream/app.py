
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from .skeleton import StreamSkeleton
from fastapi.templating import Jinja2Templates




class StreamApp(FastAPI):
    def __init__(self) -> None:
    
        super().__init__(docs_url=None, redoc_url=None)

        app = super()

        skeleton = StreamSkeleton("The Machine Learning App")
        skeleton.add_head_content('<meta charset="UTF-8">')
        skeleton.add_head_content('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
        skeleton.add_body_content('<h1>Hello, World!</h1>')
        skeleton.add_body_content('<p>This is a sample HTML page generated with a Python class.</p>')

        @app.get("/")

        def main(request:Request):

            return HTMLResponse(skeleton.generate_html())
        






    