from flask import Blueprint, render_template, redirect, url_for, request 
from models.calc import Calc

# Creating blueprint!
main = Blueprint("main", __name__)

# My home template! 
@main.route("/")
def home():
    return render_template("home.html")

@main.route("/func", methods = ["POST"])
def func():
    # Using only post method because I'm updating my page!
    if request.method == "POST":
        # Getting my first and second number!
        f_num  = request.form.get("first_num")
        s_num = request.form.get("second_num")

        # Getting my operation so that server knows what calculation should perform!
        operation = request.form["operation"]

        
        if operation == "+":
            result = Calc.addition(f_num, s_num)
            return render_template("home.html", result = result)
        
        elif operation == "-":
            result = Calc.subtraction(f_num, s_num)
            return render_template("home.html", result=result)
        
        elif operation == "X":
            result = Calc.multiplication(f_num, s_num)
            return render_template("home.html", result=result)

        elif operation == "/":
            result = Calc.divide(f_num, s_num)
            return render_template("home.html", result=result)
