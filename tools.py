tools = [{
    "type": "function",
    "function": {
        "name": "trainingFromJson",
        "description": "training plan from json",
    
        "parameters": {
                "type": "object",
                "properties": {
                    "^week [1-4]+$":{
                        "^day [1-7]+$": {
                            "type": "object",
                            "properties": {
                                "gymWorkout": {
                                    "type": "array",
                                    "description": "array of workouts",
                                    "items":{
                                        "properties":{
                                            "exerciseName": {
                                                "type": "string",
                                                "description": "name of exercise"
                                            },
                                            "numberOfSets":{
                                                "type": "number",
                                                "description": "number of sets"
                                            },
                                            "numberOfReps": {
                                                "type": "number",
                                                "description": "number of reps"
                                            },
                                            "duration": {
                                                "type": "number",
                                                "description": "duration in minutes"
                                            },
                                            "description": {
                                                "type": "string",
                                                "description": "instructions about the exercise"
                                            }
                                        },
                                        "required": ["numberOfSets", "numberOfReps", "duration", "description"]
                                    }
                                }
                            }
                        }
                }
            }
        }
}}
]