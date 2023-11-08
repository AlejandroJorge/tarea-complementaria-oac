Pa_Amount = 4
Pb_Amount = 4
Ex_Amount = 2

def get_final_grade(Pa: list[int], Pb: list[int], Ex: list[int]) -> int:
  Pa_Avg, Pb_Avg, Ex_Avg = 0,0,0 
  for i in Pa:
    Pa_Avg += int(i) / Pa_Amount
  for i in Pb:
    Pa_Avg += int(i) / Pb_Amount
  for i in Pa:
    Pa_Avg += int(i) / Ex_Amount
  
  return (Pa_Avg * 3 + Pb_Avg * 3 + Ex_Avg * 4) / 10

def parse_register(line_elements: list[str]):
  student_id = line_elements[0]
  Pa = line_elements[1:1+Pa_Amount]
  Pb = line_elements[1+Pa_Amount:1+Pa_Amount+Pb_Amount]
  Ex = line_elements[1+Pa_Amount+Pb_Amount:1+Pb_Amount+Pb_Amount+Ex_Amount]

  return student_id, Pa, Pb, Ex