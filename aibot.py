import nltk
from neuralintents import BasicAssistant

nltk.download('omw-1.4', '/usr/local/nltk_data')
nltk.download('punkt_tab', '/usr/local/nltk_data')
chatbot = BasicAssistant('intents2.json')
chatbot.fit_model(epochs=50)
chatbot.save_model()