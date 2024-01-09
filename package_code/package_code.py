# Function to calculate the average between two operands

def calc_average(a: float, b: float) -> float:
    ''' calculate the average '''
    return (a + b) / 2

# Function to calculate the minimum between two operands
def calc_min(a: float, b: float) -> float:
    ''' calculate the minimum '''
    if (a <= b):
        return a
    else:
        return b
