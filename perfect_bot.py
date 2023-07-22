from langchain.chat_models import AzureChatOpenAI

from config import load_environment
load_environment()

# You must also ask for the answer to be in a specific format, that best fits the question or request, for example, using bullet points or an ordered list. You MUST choose the formatation on your own. \


better_prompt_llm = AzureChatOpenAI(deployment_name="gpt35-team-3-0301", temperature= 0.2)

def perfect_prompt(prompt):
    return better_prompt_llm.predict(
        f"""\
        The AI is going to receive a prompt from the user, delimited by ```. \
        The AI must process the prompt and alter it in order to make it more accurate and understandable for any LLM model. \
        The context and idea of the given prompt MUST remain inaltered. \
        The new prompt may include new additional text that is predictable to be presented by the human in the future. \
        \
        Prompt: \
        ```\
        {prompt}\
        ```\
        \
        You MUST only return the new prompt, and nothing else.\
        """
    )