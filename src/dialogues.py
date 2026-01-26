'''
This file contains popular lines said by teams and players in F1
'''
## STILL NEED TO ADD MORE SAYINGS

import random

class Diaglogues:
    
    ## Race commentary by commentators
    commentary_messages = {
    "START": [
    "Lights out and away we go!",
    "The cars launch off the grid!",
    "What a start to the race!"
    ],


    "INCIDENT": [
    "There has been an incident on track.",
    "The stewards are looking at a collision.",
    "That might be investigated after the race."
    ],


    "STEWARDS": [
    "A penalty has been applied.",
    "No further action from the stewards."
    ],


    "FINISH": [
    "The chequered flag is out!",
    "What a finish to this race!"
    ],


    #need to get better podium messages
    "PODIUM": [
    "What a fantastic podium ceremony!",
    "The drivers celebrate their success!"
    ]

    }


    # generic radio messages used by teams and players
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
                "Car feels loose",         
                "Car feels tight",         
                "Front/rear grip dropping",
                "Brake bite is low/high",  
                "Engine mode is stable"    
            ]
        },
        {
            "type": "Iconic",
            "examples": [
                "Just leave me alone, I know what to do", 
                "Fernando is faster than you",            
                
                "Yabba dabba doo!",                       
                "We're not here to finish 8th",           
                "My tyres are okay, I don't want to stop" 
            ]
        },
        {
            "type": "Acknowledgement",
            "examples": [
                "Copy that",          
                "Understood",            
                "Affirmative",           
                "Negative",              
                "Repeating",             
                "Say again"              
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


    #common radio messages by named drivers
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


    #functions to get dialouges

    @staticmethod
    def get_team_radio(team_name: str) -> list:
        return Diaglogues.F1_Team_Radio.get(team_name, [])
    

    @staticmethod
    def get_driver_radio(driver_name: str) -> list:
        return Diaglogues.F1_Driver_Radio.get(driver_name, [])
    

    @staticmethod
    def get_generic_radio_messages() -> list:
        return Diaglogues.generic_radio_messages
    

    @staticmethod
    def get_commentary_messages(event_type: str) -> list:
        return Diaglogues.commentary_messages.get(event_type, [])
    


    @staticmethod
    def choose_random_message(message_list: list) -> str:
        return random.choice(message_list)


    def get_random_event_commentary(event_type: str) -> str:
        messages = Diaglogues.get_commentary_messages(event_type)
        return Diaglogues.choose_random_message(messages)
