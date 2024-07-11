# Luhn Algorithm

The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate a variety of identification numbers, most notably credit card numbers. This algorithm is designed to identify simple errors in the accidental keying of a series of numbers. It detects errors such as a single digit being altered or two adjacent digits being transposed.

## History

Developed by a scientist at IBM, Hans Peter Luhn, the algorithm was granted a patent in 1960. Since then, it has become a standard in the verification of credit card numbers, IMEI numbers, National Provider Identifier numbers in the United States, and various other identification numbers.

## How it Works

The Luhn algorithm works by performing a series of simple mathematical operations on the digits of a number. It takes into consideration the digit's position and applies a specific set of rules to generate a checksum. This checksum is then used to verify the integrity of the number.

### Step-by-Step Explanation

1. **Reverse the Digits:** Start from the rightmost digit (the check digit) and move to the left, reversing the entire sequence of numbers.
   
2. **Double Every Second Digit:** Starting with the first digit on the left (which was originally the second-last digit), double every second digit.

3. **Subtract 9 if More Than 9:** If any of the doubled values are greater than 9, subtract 9 from them.

4. **Sum the Digits:** Sum all the digits, including those that were not doubled.

5. **Calculate the Checksum:** The total sum should be a multiple of 10. If it is, the number is valid according to the Luhn algorithm.

### Example Calculation

To illustrate, let’s take the credit card number `4539 1488 0343 6467` and validate it with the Luhn algorithm.

1. **Reverse the Digits:** `7 6 4 6 3 4 3 0 8 8 4 1 9 3 5 4`

2. **Double Every Second Digit:**
   - 7 (unchanged)
   - 12 (6 doubled)
   - 4 (unchanged)
   - 12 (6 doubled)
   - 3 (unchanged)
   - 8 (4 doubled)
   - 3 (unchanged)
   - 0 (0 doubled)
   - 8 (unchanged)
   - 16 (8 doubled)
   - 4 (unchanged)
   - 2 (1 doubled)
   - 9 (unchanged)
   - 6 (3 doubled)
   - 5 (unchanged)
   - 8 (4 doubled)

3. **Subtract 9 if More Than 9:**
   - 7
   - 3 (12 - 9)
   - 4
   - 3 (12 - 9)
   - 3
   - 8
   - 3
   - 0
   - 8
   - 7 (16 - 9)
   - 4
   - 2
   - 9
   - 6
   - 5
   - 8

4. **Sum the Digits:** `7 + 3 + 4 + 3 + 3 + 8 + 3 + 0 + 8 + 7 + 4 + 2 + 9 + 6 + 5 + 8 = 80`

5. **Calculate the Checksum:** `80 % 10 = 0`. Since the result is zero, the credit card number is valid according to the Luhn algorithm.

## Applications

The Luhn algorithm is predominantly used in the following areas:

- **Credit Card Validation:** Most major credit card companies, including Visa, MasterCard, and American Express, use the Luhn algorithm to validate card numbers.
  
- **IMEI Numbers:** The International Mobile Equipment Identity (IMEI) numbers, used to identify mobile devices, utilize the Luhn algorithm.
  
- **National Provider Identifier:** In the United States, healthcare providers are assigned NPIs, which must pass the Luhn algorithm.

- **Canadian Social Insurance Numbers:** These numbers also employ the Luhn algorithm for validity checks.

## Security and Limitations

While the Luhn algorithm is effective in detecting errors such as mistyped or transposed digits, it is not impervious to deliberate tampering. It does not offer protection against more sophisticated forms of fraud, such as the use of specially crafted counterfeit numbers.

### Pros

- **Simplicity:** The algorithm is easy to implement and understand.
- **Speed:** Requires minimal computations, making it efficient for real-time validation.
- **Coverage:** Effective at catching common input errors like single-digit entry errors or transpositions.

### Cons

- **Security:** Offers no protection against skewed data and does not replace cryptographic validations.
- **Limited Error Detection:** Can only catch simple mistakes and not more sophisticated fraud.

## Implementation

### Python Example

Here is a simple Python implementation of the Luhn algorithm to validate a number:

```python
def luhn_check(number):
    digits = [int(digit) for digit in str(number)][::-1]
    checksum = 0

    for i, digit in enumerate(digits):
        if i % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit -= 9
        checksum += digit

    return checksum % 10 == 0

# Example Usage
credit_card_number = 4539148803436467
print(luhn_check(credit_card_number))  # Output: True
```

### JavaScript Example

Here is a JavaScript implementation of the Luhn algorithm:

```javascript
function luhnCheck(number) {
    let arr = (number + '')
        .split('')
        .reverse()
        .map(x => parseInt(x));
    let checksum = arr
        .map((digit, idx) => idx % 2 !== 0 ? digit * 2 : digit)
        .map(digit => digit > 9 ? digit - 9 : digit)
        .reduce((acc, digit) => acc + digit, 0);
    return checksum % 10 === 0;
}

// Example Usage
const creditCardNumber = 4539148803436467;
console.log(luhnCheck(creditCardNumber)); // Output: true
```

## Conclusion

The Luhn algorithm plays a critical role in modern finance and telecommunications as a tool for simple validation of numbers. Its simplicity and efficiency make it a widely adopted method for error detection in various identification numbers. However, it is important to recognize its limitations, particularly relating to security, and use it in conjunction with more robust fraud detection mechanisms where necessary.