def myAdd(a, b):
    """
    Adds two numbers together

    Parameters
    ----------
    a : int or float
        First of two numbers to add together
    b : int or float
        Second of two numbers to add together

    Returns
    -------
    int or float
        Returns the sum of the two parameters
    """
    x = a+b
    return x

def mySub(a, b):
    """
    Find the absolute difference between the two inputs

    Parameters
    ----------
    a : int or float
        First number
    b : int or float
        Second number

    Returns
    -------
    int or float
        Returns the difference between the two inputs
    """
    diff = 0
    if a>b:
        diff = a-b
    elif b>a:
        diff = b-a
    else:
        diff = 0
    return diff

class performCalcs():
    """
    Adds and subtracts two numbers

    Parameters
    ----------
    a : int or float
        The first of two numbers to perform the calculation
    b : int or float
        The second of two numbers to perform the calculation
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def myAdd(self):
        """
        Adds the class' two numbers together

        Returns
        -------
        int or float
            Returns the sum of the class' two numbers
        """
        return self.a+self.b

    def mySub(self):
        """
        Find the absolute difference between the two numbers in the object

        Parameters
        ----------
        a : int or float
            First number
        b : int or float
            Second number

        Returns
        -------
        int or float
            Returns the absolute difference between the two numbers in the object
        """
        a, b = self.a, self.b
        if a>b:
            return a-b
        elif b>a:
            return b-a
        else:
            return 0
