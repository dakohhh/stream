from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from .skeleton import StreamSkeleton


class StreamApp(FastAPI):
    def __init__(self, title: Union[str, None] = None) -> None:
        super().__init__(docs_url=None, redoc_url=None)

        app = super()

        skeleton = StreamSkeleton(title=title)

        @app.get("/")
        def main(request: Request):

            return HTMLResponse(skeleton.generate_html())
