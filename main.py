from pyscript import display, document

def calculating_grade(e):
    first = document.getElementById('fname').value
    last = document.getElementById('lname').value
    
    # Convert grades to numbers
    sci = float(document.getElementById('science').value or 0)
    eng = float(document.getElementById('english').value or 0)
    math = float(document.getElementById('math').value or 0)
    fil = float(document.getElementById('filipino').value or 0)
    pe = float(document.getElementById('pe').value or 0)
    ict = float(document.getElementById('ict').value or 0)

    document.getElementById('output').innerHTML = ""

    units = [4, 5, 5, 3, 1, 1]

    # Calculate simple average
    avg = round((sci + eng + math + fil + pe + ict) / 6, 2)

    # Calculate weighted sum
    grades = [sci, eng, math, fil, pe, ict]
    weighted_sum = sum(grade * unit for grade, unit in zip(grades, units))
    total_units = sum(units)
    gwa = round(weighted_sum / total_units, 2)

    message = f'Hello, {first} {last}! Your simple average is {avg} and your Grade Weighted Average (GWA) is {gwa}.'
    display(message, target="output")

    if gwa > 74:
        display(f'You have passed the school year!', target="output")
    elif gwa < 75:
        display(f'You have failed the school year.', target="output")

