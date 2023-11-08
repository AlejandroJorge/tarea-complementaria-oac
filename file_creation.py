import grades
import random

def generate_register(student_id: int) -> str:
  register = f"{student_id}"
  for i in range(grades.Pa_Amount):
    register += f",{random.randint(0,20):02}"
  for i in range(grades.Pb_Amount):
    register += f",{random.randint(0,20):02}"
  for i in range(grades.Ex_Amount):
    register += f",{random.randint(0,20):02}"

  return register

def main():
  with open("grades.csv","w",encoding="utf-8") as f:
    for i in range(200):
      register = generate_register(20230000 + i);
      f.write(register + "\n")

if __name__ == "__main__":
  main()