
# Which Flower Are You? Quiz
# Focus on : Dictionary 
# Set of Questions
# A dictionary with an options list in it

questions = [
    {
    "Q": "What's your ideal weekend activity?",
    "options": ["A.Visiting an art gallery.",
                "B. Hosting a cozy dinner party.",
                "C. Dancing at a vibrant party.",
                "D.Going on a romantic dinner date."]
    },
{
    "Q": "How do you usually handle stress?",
    "options": ["A. Create art or write in a journal.",
                "B. Talk to a close friend about it.",
                "C. Go for a run or exercise.",
                "D.Take a relaxing bath with candles."]
    },
{
    "Q": "What’s your dream vacation spot?",
    "options": ["A. Turkey",
                "B. Japan",
                "C. Bali",
                "D. France"]
    },
{
    "Q": "What’s your favorite way to express yourself?",
    "options": ["A. Painting",
                "B. Knitting/Handicraft",
                "C. Singing",
                "D. Dancing"]
    },

{
    "Q" : "What type of weather do you love most?",
    "options": ["A. A soft, misty rain.",
                "B. A calm, breezy day.",
                "C. A warm, sunny afternoon.",
                "D. A cozy, golden sunset."]
    },
{
    "Q" : "Which describes your personality best?",
    "options": ["A. Mysterious, creative, and independent.",
                "B. Kind, nurturing, and gentle.",
                "C. Optimistic, energetic, and outgoing. ",
                "D. Romantic, passionate, and elegant. "]
    },
{
    "Q" : "What’s your favorite type of celebration?",
    "options": ["A. A low-key gathering with close friends and creative activities.",
                "B. A family dinner filled with warmth and connection.",
                "C. A fun outdoor picnic or festival.",
                "D. A grand event with romantic vibes. "]
    }
]

# quiz function

def quiz(questions):
    # variables to store the score
    orchid = 0
    lily = 0
    sunflower = 0
    rose = 0
    print("Welcome to the 'Which Flower Are You?' Quiz !!! ")
    for question in questions:
        print(question["Q"]) # printing each question
        #print(question["options"]) # this will just return the entire options list
        for option in question["options"]: # printing each question's options one by one
            print(option)
        answer = input("Enter your answer: ")
        if answer not in ("A" , "B" , "C" , "D"):
            raise ValueError("Invalid Character, please enter A, B, C or D")
        if answer == "A":
            orchid += 1
        elif answer == "B":
            lily += 1
        elif answer == "C":
            sunflower += 1
        elif answer == "D":
            rose += 1

    # Store variables in a dictionary
    scores = {"a Rose": rose, "a Sunflower": sunflower, "a Lily": lily, "an Orchid": orchid}

    # Find the key with the highest value
    highest_flower = max(scores, key=scores.get) # key=scores.get helps get the relevant key, max key in
    # print(scores)
    print("You are", highest_flower, "!")


quiz(questions)


