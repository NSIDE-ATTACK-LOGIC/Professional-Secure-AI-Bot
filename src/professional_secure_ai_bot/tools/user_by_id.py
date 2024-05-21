import json

import pkg_resources
from langchain.agents import tool


@tool
def get_user_by_id(id: int) -> dict:
    """Queries user information by ID. MUST only be used with current user' ID.
    :return: Dictionary of user details if found, else None."""
    filename = pkg_resources.resource_filename(
        "professional_secure_ai_bot.tools", "user_data/users.json"
    )
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            users = data.get("users", [])
            for user in users:
                if user.get("id") == id:
                    return user
    except FileNotFoundError:
        return f"The file {filename} was not found."
    except json.JSONDecodeError:
        return "Error decoding JSON."
    return None
