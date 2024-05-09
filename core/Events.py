from typing import Callable
from fastapi import FastAPI
from loguru import logger


def startup(app: FastAPI) -> Callable:
    """
    FastAPI启动完成事件
    :param app: FastAPI
    :return: start_app
    """
    async def app_start() -> None:
        logger.info("FastAPI项目已启动")
    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastAPI APP停止事件
    :param app:
    :return:
    """
    async def stop_app() -> None:
        logger.info("FastAPI项目已停止")
    return stop_app
