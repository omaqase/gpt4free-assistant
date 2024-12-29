from fastapi import FastAPI

from routers.v1.questions_router import QuestionsRouter

app = FastAPI()

app.include_router(QuestionsRouter)