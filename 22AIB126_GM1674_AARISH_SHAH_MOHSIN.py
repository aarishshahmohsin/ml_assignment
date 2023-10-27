'''
    @author: AARISH SHAH MOHSIN
    @class: A2-AI 
    @faculty_no: 22AIB126
    @enrol_no: GM1674
    @submitted_to: Dr. ASRAFUL HAQUE
'''

# calculate average
def average(ar):
    n = len(ar)
    sum = 0
    for i in ar:
        sum += i
    sum /= n
    return sum

# slope = Σ[(Xi-X_mean)(Yi-Ymean)] / Σ((Xi-X_mean)^2)
def slope(x_ar, y_ar):
    x_mean = average(x_ar)
    y_mean = average(y_ar)

    numerator = 0
    for i in range(len(x_ar)):
        numerator += (x_ar[i]-x_mean)*(y_ar[i]-y_mean)

    denominator = 0
    for i in range(len(x_ar)):
        denominator += (x_ar[i]-x_mean)**2

    if denominator == 0:
        print("Enter valid values")
        exit()

    return (numerator / denominator)

# intercept = y_mean - (slope * x_mean)
def intercept(x_ar, y_ar):
    x_mean = average(x_ar)
    y_mean = average(y_ar)

    intercept = y_mean - (slope(x_ar, y_ar) * x_mean)
    return intercept

# predicting by putting it in the equation
def predict(x, x_ar, y_ar):
    result = slope(x_ar, y_ar) * x + intercept(x_ar, y_ar)
    return result

# declaring the arrays for the coordinates
cr_x = []
cr_y = []

print("Enter the number of points you want to enter: ")
n = int(input())

for i in range(n):
    print("enter the value of X{}".format(i+1))
    x = float(input())
    print("enter the value of Y{}".format(i+1))
    y = float(input())
    cr_x.append(x)
    cr_y.append(y)

print("The Resulting Equation is:")
print("y = {} * x + {}".format(round(slope(cr_x, cr_y), 4), round(intercept(cr_x, cr_y), 4)))

while True:
    print("do you want to predict any point (Y/y or N/n)")
    option = input()

    if option == 'Y' or option == 'y':
        print("Enter the x coordinate: ")
        x = float(input())
        ans = predict(x, cr_x, cr_y)
        print("Your answer is : {}".format(ans))

    elif  (option == 'N' or option == 'n'):
        break

    else:
        print("You should have entered a valid option")
    
