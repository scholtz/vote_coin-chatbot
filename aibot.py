import nltk
from neuralintents import GenericAssistant

nltk.download('omw-1.4')
chatbot = GenericAssistant('intents2.json')
chatbot.train_model()
chatbot.save_model()