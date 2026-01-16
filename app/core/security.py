import base64
import hashlib
import hmac
import logging

logger = logging.getLogger(__name__)


class SignatureService:
    def __init__(self, public_key: str, secret_key: str):
        self.public_key = public_key
        self.secret_key = secret_key

    def generate_signature(self, payload: str, method: str = "POST") -> str:

        if method in ["GET", "DELETE"]:
            data = self.public_key + self.public_key
        else:
            data = self.public_key + payload + self.public_key
        
        hmac_hash = hmac.new(
            self.secret_key.encode("utf-8"),
            data.encode("utf-8"),
            hashlib.sha512
        ).digest()
        
        return base64.b64encode(hmac_hash.hex().encode("utf-8")).decode("utf-8")

    def verify_signature(self, payload: str, received_signature: str, method: str = "POST") -> bool:
        expected = self.generate_signature(payload, method)
        is_valid = hmac.compare_digest(expected, received_signature)

        if not is_valid:
            logger.warning("Signature verification failed")
        else:
            logger.debug("Signature verified successfully")

        return is_valid