import pandas as pd
import numpy as np
import sqlite3
from pydantic import BaseModel


N_samples = 2500
np.random.seed(42)

# Teacher Configuration
weight_attendance = 0.15  # 15%
weight_homework = 0.35    # 35%
weight_exams = 0.50       # 50%

#0 - 10 hours of study per week
testStudyHours = np.random.uniform(0, 10, N_samples)

#0 - 10 hours of homework devoted time
homework_hours  = np.random.uniform(0, 10, N_samples)

#Scores conversion
homework_scores = homework_hours * 10  # Convert hours to scores (0-100)
test_scores = testStudyHours * 10        # Convert hours to scores (0-100

#Noise to add some variability to the grades, simulating real-world factors that might affect performance
noise = np.random.normal(0, 5, N_samples)

#Attendence rate out of `100` ex: if they attend 80% of the classes, 
# the attendence rate is `80` ,and this should affect their grade results
attendence = np.random.uniform(0, 100, N_samples)

#grades -- attendence *1.5 becuase attendence is 150 points out of 1000
grades = (attendence * weight_attendance) + (homework_scores * weight_homework) + (test_scores * weight_exams) + noise
#clipped
grades = np.clip(grades, 0, 100)