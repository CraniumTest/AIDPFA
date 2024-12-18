from transformers import pipeline

class FinanceChatbot:
    def __init__(self):
        self.qa_pipeline = pipeline('question-answering')

    def answer_question(self, context, question):
        return self.qa_pipeline({'context': context, 'question': question})

# Example:
# chatbot = FinanceChatbot()
# response = chatbot.answer_question(context="Long context of user finances...", question="What is a good budget?")
