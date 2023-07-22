from perfect_bot import perfect_prompt
from agent_bot import AgentChatBot
from conversation_bot import ConversationChatBot
from config import load_environment
load_environment()
from decision_bot import need_agent
from subjects_and_tools import *


subject = HISTORY
chats = {
    MATHS : "",
    HISTORY : "",
    PORTUGUESE : "",
    ENGLISH : "",
    PHY_CHEM : "",
    BIO : "",
    PHILOSOPHY : ""
}

agents = {
    MATHS : AgentChatBot(MATHS),
    HISTORY : AgentChatBot(HISTORY),
    PORTUGUESE : AgentChatBot(PORTUGUESE),
    ENGLISH : AgentChatBot(ENGLISH),
    PHY_CHEM : AgentChatBot(PHY_CHEM),
    BIO : AgentChatBot(BIO),
    PHILOSOPHY : AgentChatBot(PHILOSOPHY)
}

conversations = {
    MATHS : AgentChatBot(MATHS),
    HISTORY : ConversationChatBot(HISTORY),
    PORTUGUESE : ConversationChatBot(PORTUGUESE),
    ENGLISH : ConversationChatBot(ENGLISH),
    PHY_CHEM : ConversationChatBot(PHY_CHEM),
    BIO : ConversationChatBot(BIO),
    PHILOSOPHY : ConversationChatBot(PHILOSOPHY)
}


def ask_chat(input_prompt, subject):
    if input_prompt == "X":
        return "AAAA "
    new_input_prompt = perfect_prompt(input_prompt)
    answer = agents[subject].ask(new_input_prompt) if need_agent(new_input_prompt) else conversations[subject].ask(new_input_prompt)
    return answer

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<id>', methods=['GET', 'POST'])
def subject(id):
    if request.method == 'POST':
        expr = request.form.get('data')
        chats[id] += "<strong>You: </strong>" + expr + "<p></p>";
        chats[id] += "<strong>" + id + " tutor: <strong>" + ask_chat(expr, id) + "<p></p>"
    return render_template('subject.html',
                            subject=id, conversation=chats[id])



if __name__ == "__main__":
    app.run()