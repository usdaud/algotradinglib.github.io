# Hash

## Definition
A **hash** is a function that converts an input (or 'message') into a fixed-size string of bytes, typically representing the input data in a way that appears random. The output is commonly referred to as a hash [value](../v/value.md), hash code, or simply a hash.

## Key Components
1. **Input (Message)**: The original data that needs to be hashed. It can be of any length, such as a file, string, or any other form of data.
2. **Hash Function**: A mathematical algorithm that transforms the input data into a fixed-size hash [value](../v/value.md).
3. **Hash [Value](../v/value.md) (Digest)**: The fixed-size string of characters that results from applying the hash function to the input data.

## Characteristics
1. **Deterministic**: The same input [will](../w/will.md) always produce the same hash [value](../v/value.md).
2. **Fixed Size**: Hash values have a fixed length, regardless of the size of the input data.
3. **Efficient**: The hash function should be quick to compute.
4. **Pre-image Resistance**: It should be computationally infeasible to reverse the hash function (i.e., to obtain the original input from the hash [value](../v/value.md)).
5. **Collision Resistance**: It should be difficult to find two different inputs that produce the same hash [value](../v/value.md).
6. **Avalanche Effect**: A small change in the input should produce a significantly different hash [value](../v/value.md).

## Applications
1. **Data Integrity**: Hashes ensure that data has not been altered. For example, file integrity checks use hashes to verify that a file has not been corrupted or tampered with.
2. **Cryptography**: Hash functions are fundamental in various cryptographic algorithms, including digital signatures, message authentication codes, and hash-based message digests.
3. **Password Storage**: Storing passwords as hash values instead of plain text enhances [security](../s/security.md).
4. **[Blockchain](../b/blockchain_in_trading.md)**: Hashing is a core component of [blockchain](../b/blockchain_in_trading.md) technology, used to link blocks and ensure the integrity of transactions.
5. **Hash Tables**: Used in computer science to implement data structures like hash maps, which allow fast data retrieval.

## Common Hash Functions
1. **MD5 (Message Digest Algorithm 5)**: Produces a 128-bit hash [value](../v/value.md), commonly represented as a 32-character hexadecimal number. Although widely used, it is now considered insecure due to vulnerabilities.
2. **SHA-1 (Secure Hash Algorithm 1)**: Produces a 160-bit hash [value](../v/value.md). It is also considered insecure due to vulnerabilities.
3. **SHA-256 (Secure Hash Algorithm 256-bit)**: Part of the SHA-2 family, it produces a 256-bit hash [value](../v/value.md) and is widely used in [security](../s/security.md) applications, including [blockchain](../b/blockchain_in_trading.md).
4. **SHA-3**: The latest member of the Secure Hash Algorithm family, designed to provide higher [security](../s/security.md).

## Example Scenario
### File Integrity Check
1. **Original File**: A software developer hashes a file using SHA-256 before [distribution](../d/distribution.md), producing a hash [value](../v/value.md) of `abc123...`.
2. **File Transfer**: The file is downloaded by a user.
3. **Integrity Verification**: The user hashes the downloaded file using SHA-256 and compares the result with the original hash [value](../v/value.md) provided by the developer.
4. **Verification Result**: If the hash values match, the file is verified as intact. If they do not match, the file may have been corrupted or tampered with.

## Conclusion
Hash functions play a critical role in various fields of computer science and cybersecurity. They ensure data integrity, secure password storage, and enable the functionality of technologies like [blockchain](../b/blockchain_in_trading.md). Understanding the characteristics and applications of hash functions is essential for developing secure systems and protecting data.

