from openai import OpenAI

OpenAI.api_keys = "sk-proj-bFmvHG6PsTIhoWs9bfvvT3BlbkFJZZ4cUHKESLlEKInvOFaY"

def chat_with_gpt(prompt):
    response = OpenAI.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user", "content":prompt}]
    )
    return response.choice[0].message.content.strip()

if "__name__" == "__main__":
    # while True:
        user_input = "largest city"
        # if user_input.lower() in ["quit","exit","bye"]:
            # break
        
        response = chat_with_gpt(user_input)
        print("chatbot:",response)

        


