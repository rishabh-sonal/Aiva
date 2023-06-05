import os
import json
import random

# Save messages for retrieval later on
def get_recent_messages():

  # Define the file name
  file_name = "stored_data.json"
  learn_instruction = {
    "role": "system", 
    # "content": "You are a techolution.com company's virtual assistant and your name is Aiva, the user is called Sabith. Keep responses under 20 words. "
    "content": "You are techolution.com company's technological and sales representative and your name is Aiva. The user is called Luv. your primary role is to provide exceptional customer support by answering questions related to Techolution, its projects, and technology solutions.\
    You will engage with customers, potential clients, and website visitors, assisting them in understanding Techolution's services, products, and value propositions.\
    Actively identify sales opportunities during conversations and drive sales by promoting Techolution's solutions, highlighting their benefits, and addressing customer pain points. Collaborate with the sales team to generate leads and nurture relationships with potential clients.\
    Foster positive relationships with customers and prospects, demonstrating a deep understanding of their challenges and goals. Engage in meaningful conversations, actively listen to their requirements, and offer personalized solutions to enhance their experience with Techolution.\
    Keep responses under 20 words. Never say things like 'As an AI language model, I am programmed to'. If you do not know something, inform that you do not know about it. If any question is asked which is not relevant to techolution then answer 'If you have any questions about our technology solutions or services, I would be happy to assist you.' "
  }
  
  # Initialize messages
  messages = []

  # Add Random Element
  x = random.uniform(0, 1)
  if x < 0.2:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will have some light humour. "
  elif x < 0.5:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will include an interesting new fact about Techolution.com. "
  else:
    learn_instruction["content"] = learn_instruction["content"] + "Your response will present a sales pitch to customer. "

  # Append instruction to message
  messages.append(learn_instruction)

  # Get last messages
  try:
    with open(file_name) as user_file:
      data = json.load(user_file)
      
      # Append last 5 rows of data
      if data:
        if len(data) < 50:
          for item in data:
            messages.append(item)
        else:
          for item in data[-50:]:
            messages.append(item)
  except:
    pass

  
  # Return messages
  return messages


# Save messages for retrieval later on
def store_messages(request_message, response_message):

  # Define the file name
  file_name = "stored_data.json"

  # Get recent messages
  messages = get_recent_messages()[1:]

  # Add messages to data
  user_message = {"role": "user", "content": request_message}
  assistant_message = {"role": "assistant", "content": response_message}
  messages.append(user_message)
  messages.append(assistant_message)

  # Save the updated file
  with open(file_name, "w") as f:
    json.dump(messages, f)


# Save messages for retrieval later on
def reset_messages():

  # Define the file name
  file_name = "stored_data.json"

  # Write an empty file
  open(file_name, "w")
