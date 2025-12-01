# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))

# bmi = weight / (height **2)

# print("Your BMI is:", round(bmi, 2))

# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 25:
#     print("You have a normal weight.")
# elif 25 <= bmi < 30:
#     print("You are overweight.")


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi():
    result = ""
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi_value = weight / (height ** 2)

        # Determine BMI category
        if bmi_value < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi_value < 24.9:
            category = "Normal weight"
        elif 25 <= bmi_value < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result = f"Your BMI is {bmi_value:.2f} ({category})"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)






















