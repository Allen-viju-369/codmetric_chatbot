import tkinter as tk
from tkinter import scrolledtext

def chatbot_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm functioning perfectly!"

    elif "what is your name" in user_input or "what's your name" in user_input:
        return "I'm CodmetricBot, your rule-based chatbot assistant."

    elif any(bye in user_input for bye in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day ahead."

    elif "who created you" in user_input or "who made you" in user_input:
        return "I was created by Rohith, as part of the Codmetric AI Internship."

    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any more questions, feel free to ask."

    elif "help" in user_input:
        return "Sure! You can ask me things like 'What's your name?', 'How are you?', or just say 'hi'."

    else:
        return "I'm sorry, I didn't understand that. Try asking something else."


# GUI setup
def send_message():
    user_input = entry_field.get()
    if user_input.strip() == "":
        return
   
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n")
    response = chatbot_response(user_input)
    chat_window.insert(tk.END, f"CodmetricBot: {response}\n\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)
    entry_field.delete(0, tk.END)

    if "bye" in user_input.lower():
        root.after(1000, root.destroy)

# Main window
root = tk.Tk()
root.title("CodmetricBot - Rule-Based Chatbot")

# Chat display
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_window.pack(padx=10, pady=10)
chat_window.insert(tk.END, "CodmetricBot: Hello! Type 'bye' to exit.\n\n")
chat_window.config(state=tk.DISABLED)

# Entry field
entry_field = tk.Entry(root, font=("Arial", 14), width=50)
entry_field.pack(padx=10, pady=(0, 10), side=tk.LEFT)
entry_field.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(padx=10, pady=(0, 10), side=tk.RIGHT)

root.mainloop()