
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_Triangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    output = ""
   

    # In the following code, we will check to make sure that all three input values are integers. 
    # This verification step was not explicitly mentioned in the requirements specification,
    #  but it is important to ensure that our code is functioning correctly. We will use Python's
    #  "isinstance" function to check the type of each object, and it will return "True" if the 
    # object is of the specified type (in this case, an integer).
    if ( not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int)):
        return 'InvalidInput'
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'  
    # The requirements specification did not mention this information,
    #  but it is essential for ensuring the correct behavior of the program. 
    # In order for a shape to be considered a triangle, 
    # the sum of any two of its sides must be strictly less than the third 
    # side. If this condition is not met, then the shape is not a triangle.
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle
    if((a * a) + (b * b)) == (c * c) or ((a*a)+ (c*c))== (b*b) or ((b*b) + (c*c)) ==(a*a):
        output+= 'Right and '
    if a == b and b == c:
        output+='Equilateral'
    elif (a != b) and  (b != c) and (a != c):
        output+= 'Scalene'
    else:
        output+='Isosceles'

    return output