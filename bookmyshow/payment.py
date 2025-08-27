class Payment:
    """
    Represents a payment for a booking.
    
    This class encapsulates payment information for a booking. Currently,
    it only stores a payment ID, but can be extended to include payment
    method, amount, status, and other payment-related details.
    
    Attributes:
        _payment_id (int): Unique identifier for the payment
    """
    _payment_id: int

    def __init__(self, payment_id: int):
        """
        Initialize a payment with a unique identifier.
        
        Args:
            payment_id (int): The unique identifier for the payment
        """
        self._payment_id = payment_id

    def get_payment_id(self):
        """
        Get the unique identifier of the payment.
        
        Returns:
            int: The payment ID
        """
        return self._payment_id

    def set_payment_id(self, payment_id: int):
        """
        Set the unique identifier for the payment.
        
        Args:
            payment_id (int): The unique identifier to assign to the payment
        """
        self._payment_id = payment_id
