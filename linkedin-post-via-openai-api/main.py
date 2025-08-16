# user input => AI (LLM) to generate LinkedIn post => output post

def generate_linkedin_post(user_input):
    print(f"Generating LinkedIn post for topic: {user_input}")

def main():
    user_input = input("Enter your LinkedIn post topic? ")
    linkedin_post = generate_linkedin_post(user_input)
    print("Generated LinkedIn post")
    print(linkedin_post)

if __name__ == "__main__":
    main()
