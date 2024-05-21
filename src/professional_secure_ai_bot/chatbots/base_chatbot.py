from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad.openai_tools import (
    format_to_openai_tool_messages,
)
from langchain.agents.output_parsers.openai_tools import OpenAIToolsAgentOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from professional_secure_ai_bot.ai_tools.ai_llm import get_llm

llm = get_llm()


def chatbot_answer(
    question: str, tools: list, user_prompt: str = "", system_prompt: str = ""
) -> str:
    """Provides a basic, reusable implementation of a chatbot that can use tools without history."""
    tools = tools

    # Do security stuff in user prompt, because it does not give a F about system prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            ("user", user_prompt + "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )
    llm_with_tools = llm.bind_tools(tools)
    agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_tool_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt
        | llm_with_tools
        | OpenAIToolsAgentOutputParser()
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)
    return agent_executor.invoke(
        {"input": question, "user_prompt": user_prompt},
        return_only_outputs=True,
    )["output"]

    # Stuff below can be used to debug the bot.
    # Must change verbose to true for agent debugging in agent_executor and comment out the return
    # list(agent_executor.stream({"input": question}))
