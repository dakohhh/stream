from fastapi import FastAPI
import uvicorn

from typing import Union
from .app import StreamApp
from .skeleton import skeleton



class Stream:
    def __init__(self, title: Union[str, None] = None) -> None:
        self.app = StreamApp()

        self.skeleton = skeleton
        skeleton.title = title
         

    def start(self):
        uvicorn.run(self.app, host="127.0.0.1", port=8000)








