#DASS-21  Scoring	Depression	Anxiety	Stress
#         Normal	    0-4	      0-3 	 0-7
#         Mild        5-6	      4-5	   8-9
#         Moderate    7-10	    6-7	   10-12
#         Severe      11-13	    8-9	   13-16
#Extremely Severe	    14+	      10+	   17+

def classify_depscore(score):
  if score >= 0 and score <= 4:
    return 'Normal'
  elif score >= 5 and score <= 6:
    return 'Mild'
  elif score >= 7 and score <= 10:
    return 'Moderate'
  elif score >= 11 and score <= 13:
    return 'Severe'
  else:
    return 'Extremely Severe'

def classify_anxscore(score):
  if score >= 0 and score <= 3:
    return 'Normal'
  elif score >= 4 and score <= 5:
    return 'Mild'
  elif score >= 6 and score <= 7:
    return 'Moderate'
  elif score >= 8 and score <= 9:
    return 'Severe'
  else:
    return 'Extremely Severe'

def classify_strscore(score):
  if score >= 0 and score <= 7:
    return 'Normal'
  elif score >= 8 and score <= 9:
    return 'Mild'
  elif score >= 10 and score <= 12:
    return 'Moderate'
  elif score >= 13 and score <= 16:
    return 'Severe'
  else:
    return 'Extremely Severe'