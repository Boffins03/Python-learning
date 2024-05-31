def mad_libs():
    # Welcome message
    print("Welcome to Mad Libs! Let's create a funny story.")

    # Get user input for various parts of speech
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    # Generate the story using user input
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."
    
    # Display the story
    print("\nHere's your Mad Libs story:")
    print(story)

# Call the function to run the Mad Libs game
mad_libs()
