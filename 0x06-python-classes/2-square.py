class Square:
    def __init__(self, size=0):
        self.__size = size
        """
        Initialize a Square object.

        Parameters:
        - size (int, optional): The size of the square. Defaults to 0.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        try:
            # Type check
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
        except:
            # Value check
            if (0 < size):
                raise ValueError("size must be >= 0")
