import logging
from abc import ABC, abstractmethod # Inheriting from ABC (Abstract Base Class) prevents class from being initiated directly. It serves only as a template.

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        # Abstract method -> enforces consistent interface across different payment types
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount: float):
        # for credit card -> this would also containing api calls for bank
        logging.info(f"[CREDIT CARD] Processing payment of INR {amount:.2f}...")
        logging.info(f"[CREDIT CARD] Transaction successful")

class UPIPayment(Payment):
    def process_payment(self, amount: float):
        # Specific implementation for UPI. This might involve QR code generation or VPA verification.
        logging.info(f"[UPI] Initiating UPI transfer of INR {amount:.2f}...")
        logging.info("[UPI] Payment received ")