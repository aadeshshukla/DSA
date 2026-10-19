import os
import sys
from openai import OpenAI

# Initialize client; picks up OPENAI_API_KEY automatically from the environment
client = OpenAI()

def run_chatbot():
    # System prompt defines personality, guidelines, and constraints
    conversation_history = [
        {
            "role": "system",
            "content": "You are a helpful, clear, and concise AI assistant.",
        }
    ]

    print("=" * 50)
    print("AI Chatbot Initialized. Type 'exit' or 'quit' to stop.")
    print("=" * 50 + "\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit"}:
                print("\nEnding session. Goodbye!")
                break

            # 1. Append user's turn to conversation history
            conversation_history.append({"role": "user", "content": user_input})

            print("\nAI: ", end="", flush=True)

            # 2. Call the API with streaming enabled
            stream = client.chat.completions.create(
                model="gpt-4o-mini",  # Fast and cost-efficient
                messages=conversation_history,
                stream=True,
                temperature=0.7,
            )

            # 3. Stream output tokens as they arrive
            assistant_reply = []
            for chunk in stream:
                delta = chunk.choices[0].delta.content or ""
                print(delta, end="", flush=True)
                assistant_reply.append(delta)

            full_reply = "".join(assistant_reply)
            print("\n")

            # 4. Append assistant's answer so future turns retain context
            conversation_history.append({"role": "assistant", "content": full_reply})

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\n[Error]: {e}\n")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY environment variable is not set.")
    run_chatbot()
