import google.generativeai as genai
from serpapi import GoogleSearch


genai.configure(api_key="[Api Key]")
model = genai.GenerativeModel("gemini-2.0-flash")


serpapi_key ="[Api key]"

def google_search(query):
    params = {
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": serpapi_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    if "organic_results" in results:
        return "\n".join([res["snippet"] for res in results["organic_results"][:5]])
    return "No results found."

def chat_with_gemini(chat_history, user_query, search_result=None):
    prompt = f"""
    Here is the conversation so far:
    {chat_history}

    The user just asked: "{user_query}".

    Additional real-time info (if available):
    {search_result if search_result else "No additional info."}

    Based on this, please give a helpful and concise answer.
    """
    response = model.generate_content(prompt)
    return response.text

def requires_realtime(query):
    keywords = ["current", "today", "price", "weather", "latest", "now"]
    return any(word in query.lower() for word in keywords)


chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    chat_history.append(f"User: {user_input}")

    
    search_result = None
    if requires_realtime(user_input):
        search_result = google_search(user_input)

    
    ai_response = chat_with_gemini("\n".join(chat_history), user_input, search_result)
    chat_history.append(f"AI: {ai_response}")
    print(f"AI: {ai_response}")

print("Chat History:")
print("\n".join(chat_history))
