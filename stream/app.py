
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Sequence, Type, Union
from typing_extensions import Annotated, Doc, deprecated
from fastapi import FastAPI, Request, APIRouter
from fastapi.datastructures import Default
from fastapi.routing import APIRoute
from fastapi.utils import generate_unique_id
from starlette.responses import JSONResponse, Response
from starlette.routing import BaseRoute
from starlette.types import ASGIApp, Lifespan



class StreamApp(FastAPI):
    def __init__(self) -> None:
    
        super().__init__(docs_url=None, redoc_url=None)

        super().add_api_route("/", Response())


    def main(request:Request):
            return {"homw": "H!"}





    