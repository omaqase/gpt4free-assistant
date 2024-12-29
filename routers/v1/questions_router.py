from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel
from llm.llm import LLM

QuestionsRouter = APIRouter(
    prefix="/api/v1/question", tags=["question"]
)

llm = LLM()

class QuestionRequest(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    answer: str

@QuestionsRouter.post("/", response_model=QuestionResponse, status_code=status.HTTP_200_OK)
async def ask_question(request: QuestionRequest):
    try:
        answer = llm.process(request.question)
        return QuestionResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
