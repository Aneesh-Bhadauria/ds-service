from app.utils.messageUtil import MessageUtil
from app.service.llmService import LLMService


class MessageService:
    def __init__(self):
        self.messageUtil = MessageUtil()
        self.llmService = LLMService()

    def process_message(self,message):
        if self.messageUtil.isBankSMS(message):
            return self.llmService.runLLm(message)
        else:
            return None