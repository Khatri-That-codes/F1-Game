'''
This file contains popular lines said by teams and players in F1
'''
## STILL NEED TO ADD MORE SAYINGS



popular_lines_by_players = {
    "Lewis Hamilton" : [
        "Still not over 7",
        "My car is faster than yours",
        
    ],

    "Max Verstappen" : [
        "Max Attack!",
        "I am the future of F1",
        
    ],

    "Charles Leclerc" : [
        "Forza Ferrari!",
        "I will win for Ferrari",
        
    ],

}

generic_radio_messages = [
    {
        "type": "Strategy",
        "examples": [
            "Box, box",                 
            "Box opposite",            
            "Push now",                
            "Target lap time X",       
            "Plan A / Plan B",         
            "Maintain delta",          
            "Overcut / Undercut window" 
        ]
    },
    {
        "type": "Car Handling",
        "examples": [
            "Car feels loose",         # Loose means oversteer
            "Car feels tight",         # Tight means understeer
            "Front/rear grip dropping",# Typical tire feedback
            "Brake bite is low/high",  # Braking feedback
            "Engine mode is stable"    # Refers to power unit setting
        ]
    },
    {
        "type": "Iconic",
        "examples": [
            "Just leave me alone, I know what to do", # Kimi Raikkonen’s classic response
            "Fernando is faster than you",             # Famous Ferrari team order
            
            "Yabba dabba doo!",                        # George Russell’s celebratory phrase
            "We're not here to finish 8th",           # Hamilton pushing for result
            "My tyres are okay, I don't want to stop"  # Hamilton expressing strategy disagreement
        ]
    },
    {
        "type": "Acknowledgement",
        "examples": [
            "Copy that",              # Confirmation of message received (common radio lingo)
            "Understood",             # Acknowledging instruction
            "Affirmative",            # Yes/confirm — formal radio term
            "Negative",               # No/decline instruction
            "Repeating",              # Repeating a message back for clarity
            "Say again"               # Asking to repeat
        ]
    }
]



#acknowledging chatGPT for the messages
F1_Team_Radio = {
        "f1" : [
        "Formula 1 is the pinnacle of motorsport",
        "Lights out and away we go!",
    ],

    "Red Bull Racing": [
        "Simply, simply lovely!",
        "Millimeter, millimeter!",
        "Childish!",
        "Push now!",
        "Box, box!",
        "Maintain delta",
        "Target lap time 1:21.3",
        "Understood",
        "Affirmative",
        "Negative"
    ],
    "Mercedes": [
        "Get in there, Lewis!",
        "George, you can win this!",
        "It's hammer time!",
        "Maintain delta",
        "Target lap time 1:21.5",
        "Push now!",
        "Box, box!",
        "Copy that",
        "Understood",
        "Affirmative"
    ],
    "Ferrari": [
        "I have the seat full of water, like, full of water.",
        "Fernando is faster than you",
        "Must be the water",
        "Box, box!",
        "Push, push, push!",
        "Maintain position",
        "Target lap time 1:22.0",
        "Copy that",
        "Understood",
        "Affirmative"
    ],
    "McLaren": [
        "Pizza, pizza, pizza",
        "Smooth Operator!",
        "Ok, what damage do you have? Talent",
        "Box opposite",
        "Target lap time 1:22.0",
        "Push now!",
        "Maintain delta",
        "Copy that",
        "Understood",
        "Affirmative"
    ],
    "Alpine": [
        "GP2 engine! GP2… Argh!",
        "Push, push!",
        "Box, box!",
        "Maintain position",
        "Target lap time 1:23.1",
        "Copy that",
        "Understood",
        "Affirmative",
        "Negative",
        "Repeating"
    ],
    "Williams": [
        "Copy that",
        "Affirmative",
        "Negative",
        "Repeating",
        "Say again",
        "Box, box!",
        "Push now!",
        "Maintain delta",
        "Target lap time 1:24.0",
        "Understood"
    ],
    "Haas": [
        "Stay cool, stay focused",
        "Box, box!",
        "Push now!",
        "Maintain delta",
        "Target lap time 1:24.2",
        "Copy that",
        "Understood",
        "Affirmative",
        "Negative",
        "Repeating"
    ],
    "AlphaTauri": [
        "Multi-21",
        "Box, box!",
        "Push, push!",
        "Copy that",
        "Target lap time 1:23.5",
        "Maintain delta",
        "Understood",
        "Affirmative",
        "Negative",
        "Repeating"
    ]
}


## Acknowledging chatGPT for the messages
F1_Driver_Radio = {
    "Max Verstappen": [
        "Simply, simply lovely!",
        "They gave me blue flags!",
        "Let's focus now.",
        "Box, box!",
        "Maintain pace."
    ],
    "Lewis Hamilton": [
        "Get in there, Lewis!",
        "I think I'm going to let him go.",
        "Leave me to it, please.",
        "My tyres are gone.",
        "We need to pick up the pace."
    ],
    "Charles Leclerc": [
        "I have the seat full of water, like full of water.",
        "Must be the water.",
        "Let's add that to the words of wisdom."
    ],
    "Carlos Sainz": [
        "Smooth Operator!",
        "Vamos! Best podium in my career.",
        "This is my first smooth operation in Williams."
    ],
    "Lando Norris": [
        "Ok, what damage do you have? Talent.",
        "I love you guys, thank you for everything.",
        "It's Friday then, it's Saturday... WHAT?"
    ],
    "George Russell": [
        "Yabba dabba doo!",
        "Just let me drive!",
        "You can win this, George!"
    ],
    "Daniel Ricciardo": [
        "Pizza, pizza, pizza.",
        "And for anyone who thought I left… I never left.",
        "I like 'em vulnerable."
    ],
    "Fernando Alonso": [
        "GP2 engine! GP2!",
        "All the time you have to leave a space!",
        "No more radio for the rest of the race!"
    ],
    "Valtteri Bottas": [
        "Valtteri, it's James.",
        "Maintain position.",
        "Copy that."
    ],
    "Oscar Piastri": [
        "I'm looking forward to some maple syrup on my pancakes.",
        "Box, box!",
        "Target lap time."
    ],
    "Other_Drivers_General": [
        "Copy that",
        "Affirmative",
        "Negative",
        "Target lap time X",
        "Maintain delta"
    ]
}
