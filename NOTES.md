## Notes for personal referral.

### 06-07-2026
- making an abstract base class helps to abstract the OCR engine interface, making swapping engines easy and promoting modular code
- by putting config params in a class's init attributes (TesseractEngine) we decouple env vars from the class

### 13-07-2026
- remember, when we test, we are testing for behaviour, not implementation. Behaviour is what the function does. Implementation is how the function does what it does. We don't care about how, we care about what.