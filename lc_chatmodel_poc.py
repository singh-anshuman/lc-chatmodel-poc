from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def call_open_ai():
    model = ChatOpenAI(model="gpt-4o-mini")
    # messages = [
    #     SystemMessage("Translate the following from English into German"),
    #     HumanMessage("Hi, Good Morning. This is Anshuman Singh. How are you doing ?"),
    # ]

    system_template = "Translate the following from English into {language}"

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    prompt = prompt_template.invoke({"language": "Italian", "text": "Hey there !"})

    # output = model.invoke(prompt_template)
    for token in model.stream(prompt):
        print(token.content, end="")
    # print(output.content)


if __name__ == "__main__":
    load_dotenv()
    call_open_ai()
