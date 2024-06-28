from models.exercises import Exercise, ExercisePerformed
from models.request import TrainingInput
from models.training import Training, TrainingEvaluation
from utils.training_score import effective_sets


class TrainingService:

    def __init__(self):
        standard_exercises = {0: {'name': 'Bench Press',
                                  'engagements': {'Chest': 100, 'Triceps': 80, 'Shoulders': 60}},
                              1: {'name': 'Squats',
                                  'engagements': {'Quads': 100, 'Hamstrings': 50, 'Glutes': 80}},
                              2: {'name': 'Deadlifts',
                                  'engagements': {'Hamstrings': 100, 'Lower_back': 80, 'Glutes': 70}},
                              3: {'name': 'Overhead Press',
                                  'engagements': {'Shoulders': 100, 'Triceps': 60, 'Upper_back': 40}},
                              4: {'name': 'Pull-Ups',
                                  'engagements': {'Upper_back': 100, 'Biceps': 70, 'Forearms': 30}},
                              5: {'name': 'Bent-Over Rows',
                                  'engagements': {'Upper_back': 100, 'Traps': 70, 'Biceps': 50}},
                              6: {'name': 'Lunges',
                                  'engagements': {'Quads': 100, 'Hamstrings': 40, 'Glutes': 80}},
                              7: {'name': 'Leg Press',
                                  'engagements': {'Quads': 100, 'Hamstrings': 25, 'Glutes': 60}},
                              8: {'name': 'Dips',
                                  'engagements': {'Chest': 100, 'Triceps': 80, 'Shoulders': 30}},
                              9: {'name': 'Barbell Curl', 'engagements': {'Biceps': 100, 'Forearms': 20}},
                              10: {'name': 'Tricep Pushdowns',
                                   'engagements': {'Triceps': 100, 'Chest': 20, 'Shoulders': 10}},
                              11: {'name': 'Leg Curls',
                                   'engagements': {'Hamstrings': 100, 'Glutes': 25, 'Calfs': 10}},
                              12: {'name': 'Plank',
                                   'engagements': {'Abs': 100, 'Shoulders': 30, 'Lower_back': 20}},
                              13: {'name': 'Lat Pulldowns',
                                   'engagements': {'Upper_back': 100, 'Biceps': 60, 'Forearms': 20}},
                              14: {'name': 'Romanian Deadlifts',
                                   'engagements': {'Hamstrings': 100, 'Lower_back': 70, 'Glutes': 80}},
                              15: {'name': 'Incline Bench Press',
                                   'engagements': {'Chest': 100, 'Triceps': 80, 'Shoulders': 40}},
                              16: {'name': 'Russian Twists',
                                   'engagements': {'Abs': 100, 'Obliques': 60, 'Lower_back': 20}},
                              17: {'name': 'Calf Raises', 'engagements': {'Calfs': 100}},
                              18: {'name': 'Face Pulls',
                                   'engagements': {'Upper_back': 100, 'Traps': 40, 'Shoulders': 60}},
                              19: {'name': 'Bicycle Crunches', 'engagements': {'Abs': 100, 'Obliques': 60}},
                              20: {'name': 'Chest Flyes',
                                   'engagements': {'Chest': 100, 'Shoulders': 40, 'Triceps': 30}},
                              21: {'name': 'Hammer Curls', 'engagements': {'Biceps': 100, 'Forearms': 40}},
                              22: {'name': 'Lateral Raises',
                                   'engagements': {'Shoulders': 100, 'Traps': 40, 'Upper_back': 20}},
                              23: {'name': 'Reverse Flyes',
                                   'engagements': {'Upper_back': 100, 'Traps': 30}},
                              24: {'name': 'Hack Squats',
                                   'engagements': {'Quads': 100, 'Glutes': 60, 'Hamstrings': 30}},
                              25: {'name': 'Arnold Press',
                                   'engagements': {'Shoulders': 100, 'Triceps': 50, 'Upper_back': 30}},
                              26: {'name': 'Front Squats',
                                   'engagements': {'Quads': 100, 'Glutes': 70, 'Hamstrings': 30}},
                              27: {'name': 'Close Grip Bench Press',
                                   'engagements': {'Triceps': 100, 'Chest': 30, 'Shoulders': 20}},
                              28: {'name': 'Sumo Deadlifts',
                                   'engagements': {'Hamstrings': 100, 'Glutes': 80, 'Lower_back': 70}},
                              29: {'name': 'Chin-Ups',
                                   'engagements': {'Upper_back': 100, 'Biceps': 70, 'Forearms': 30}},
                              30: {'name': 'T-Bar Rows',
                                   'engagements': {'Upper_back': 100, 'Traps': 60, 'Biceps': 40}},
                              31: {'name': 'Step-Ups',
                                   'engagements': {'Quads': 100, 'Glutes': 60, 'Hamstrings': 20}},
                              32: {'name': 'Skull Crushers',
                                   'engagements': {'Triceps': 100, 'Chest': 20, 'Shoulders': 10}},
                              33: {'name': 'Good Mornings',
                                   'engagements': {'Hamstrings': 100, 'Lower_back': 70, 'Glutes': 60}},
                              34: {'name': 'Cable Crunches',
                                   'engagements': {'Abs': 100, 'Obliques': 40, 'Lower_back': 20}},
                              35: {'name': 'Leg Extensions',
                                   'engagements': {'Quads': 100, 'Hamstrings': 10, 'Glutes': 10}},
                              36: {'name': 'Cable Rows',
                                   'engagements': {'Upper_back': 100, 'Biceps': 40, 'Traps': 30}},
                              37: {'name': 'Seated Leg Press',
                                   'engagements': {'Quads': 100, 'Glutes': 40, 'Hamstrings': 20}},
                              38: {'name': 'Dumbbell Pullovers',
                                   'engagements': {'Upper_back': 100, 'Chest': 30}},
                              39: {'name': 'Dumbbell Lunges',
                                   'engagements': {'Quads': 100, 'Hamstrings': 40, 'Glutes': 70}},
                              40: {'name': 'Hanging Leg Raises',
                                   'engagements': {'Abs': 100, 'Lower_back': 20}},
                              41: {'name': 'Reverse Lunges',
                                   'engagements': {'Quads': 100, 'Hamstrings': 30, 'Glutes': 60}},
                              42: {'name': 'Side Plank',
                                   'engagements': {'Obliques': 100, 'Abs': 40, 'Shoulders': 20}},
                              43: {'name': 'Incline Dumbbell Press',
                                   'engagements': {'Chest': 100, 'Shoulders': 40, 'Triceps': 30}},
                              44: {'name': 'Zottman Curls', 'engagements': {'Biceps': 100, 'Forearms': 50}},
                              45: {'name': 'Dumbbell Shrugs',
                                   'engagements': {'Traps': 100, 'Upper_back': 40, 'Shoulders': 30}},
                              46: {'name': 'Leg Raises', 'engagements': {'Abs': 100, 'Lower_back': 20}},
                              47: {'name': 'Pec Deck Machine',
                                   'engagements': {'Chest': 100, 'Shoulders': 30, 'Triceps': 20}},
                              48: {'name': 'Cable Bicep Curls',
                                   'engagements': {'Biceps': 100, 'Forearms': 30}},
                              49: {'name': 'Face Pulls',
                                   'engagements': {'Upper_back': 100, 'Traps': 40, 'Shoulders': 60}},
                              50: {'name': 'Hyperextensions',
                                   'engagements': {'Lower_back': 100, 'Glutes': 30, 'Hamstrings': 20}},
                              51: {'name': 'Side Lateral Raises',
                                   'engagements': {'Shoulders': 100, 'Traps': 40, 'Upper_back': 20}},
                              52: {'name': 'Standing Calf Raises', 'engagements': {'Calfs': 100}},
                              53: {'name': 'Decline Bench Press',
                                   'engagements': {'Chest': 100, 'Triceps': 70, 'Shoulders': 40}},
                              54: {'name': 'Sissy Squats',
                                   'engagements': {'Quads': 100, 'Glutes': 30, 'Hamstrings': 20}},
                              55: {'name': 'Preacher Curls',
                                   'engagements': {'Biceps': 100, 'Forearms': 30}},
                              56: {'name': 'Bent Over Dumbbell Rows',
                                   'engagements': {'Upper_back': 100, 'Traps': 60, 'Biceps': 40}},
                              57: {'name': 'Leg Curl Machine',
                                   'engagements': {'Hamstrings': 100, 'Glutes': 30, 'Calfs': 20}},
                              58: {'name': 'Russian Twists',
                                   'engagements': {'Abs': 100, 'Obliques': 60, 'Lower_back': 20}},
                              59: {'name': 'Incline Leg Press',
                                   'engagements': {'Quads': 100, 'Glutes': 40, 'Hamstrings': 20}},
                              60: {'name': 'Tricep Dips',
                                   'engagements': {'Triceps': 100, 'Chest': 30, 'Shoulders': 20}},
                              61: {'name': 'Cable Woodchoppers',
                                   'engagements': {'Obliques': 100, 'Abs': 40, 'Shoulders': 20}},
                              62: {'name': 'Machine Rows',
                                   'engagements': {'Upper_back': 100, 'Biceps': 40, 'Traps': 30}},
                              63: {'name': 'Machine Chest Press',
                                   'engagements': {'Chest': 100, 'Triceps': 70, 'Shoulders': 40}},
                              64: {'name': 'Walking Lunges',
                                   'engagements': {'Quads': 100, 'Hamstrings': 30, 'Glutes': 60}},
                              65: {'name': 'Hamstring Curls',
                                   'engagements': {'Hamstrings': 100, 'Glutes': 30, 'Calfs': 20}},
                              66: {'name': 'Russian Twists', 'engagements': {'Abs': 100, 'Lower_back': 20}},
                              67: {'name': 'Bent Over Dumbbell Rows',
                                   'engagements': {'Upper_back': 100, 'Traps': 60, 'Biceps': 40}},
                              68: {'name': 'Neck Flexion', 'engagements': {'Neck': 100}},
                              69: {'name': 'Neck Extension', 'engagements': {'Neck': 100}},
                              70: {'name': 'Neck Lateral Flexion', 'engagements': {'Neck': 100}},
                              71: {'name': 'Neck Rotation', 'engagements': {'Neck': 100}},
                              72: {'name': 'Shrugs',
                                   'engagements': {'Upper_back': 100, 'Traps': 100, 'Shoulders': 30}}}
        self.standard_exercises = {i: Exercise(**el) for i, el in standard_exercises.items()}

    def analyse_training(self, training: TrainingInput) -> TrainingEvaluation:
        training = Training(exercises=[ExercisePerformed(**self.standard_exercises[i].dict(), sets=j) for i, j in
                                       training.exercises.items()])
        return TrainingEvaluation(effective_sets=effective_sets(training))
