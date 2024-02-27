def convert(feet,inches): #takes in feet and inches values
    feet_to_inches = feet * 12 #convert to inches
    total = feet_to_inches + inches
    meters = total * 0.0254 #convert to meters
    return(meters)
