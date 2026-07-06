## Notes for personal referral.

### 06-07-2026
- making an abstract base class helps to abstract the OCR engine interface, making swapping engines easy and promoting modular code
- by putting config params in a class's init attributes (TesseractEngine) we decouple env vars from the class