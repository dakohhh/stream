from fastapi import FastAPI
import uvicorn

from typing import Union
from .app import StreamApp



class Stream:
    def __init__(self, title: Union[str, None] = None) -> None:
        self.app = StreamApp(title)

    

    def add_input(self, name, input_type:Union[str, None]=None):

        if input_type == "submit":
            raise Exception("use the 'submit' function")

        self.app.input(name, input_type)


    def add_submit(self):

        self.app.input("Login", input_type="submit")
    



        

    def start(self):
        uvicorn.run(self.app, host="127.0.0.1", port=53000)








