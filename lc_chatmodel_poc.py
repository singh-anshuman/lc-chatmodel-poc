from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


def call_open_ai():
    model = ChatOpenAI(model="gpt-4o-mini")
    messages = [
        SystemMessage("Translate the following from English into Marathi"),
        HumanMessage("Hey there, this is Anshuman Singh. How are you doing ?"),
    ]

    output = model.invoke(messages)
    print(output.content)


if __name__ == "__main__":
    load_dotenv()
    call_open_ai()
