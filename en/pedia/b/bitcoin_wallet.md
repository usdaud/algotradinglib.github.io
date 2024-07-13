# Bitcoin Wallet

A [Bitcoin](../b/bitcoin.md) wallet is a device, physical medium, program, or a service which stores the private and public keys for [Bitcoin](../b/bitcoin.md) transactions. In addition to this basic function of storing the keys, a [Bitcoin](../b/bitcoin.md) wallet more often offers functionality such as encrypting and/or signing information. The following comprehensive guide [will](../w/will.md) cover various aspects of [Bitcoin](../b/bitcoin.md) wallets, including types, setup, use cases, [security](../s/security.md) considerations, and relevant service providers.

## Types of Bitcoin Wallets

[Bitcoin](../b/bitcoin.md) wallets come in several forms, each [offering](../o/offering.md) different features and levels of [security](../s/security.md). The major types include:

### Software Wallets

Software wallets are applications installed on a computer or mobile device. They can be:

- **Desktop Wallets**: These wallets are installed directly on a computer. Examples include:
  - **[Bitcoin](../b/bitcoin.md) Core**: The original [Bitcoin](../b/bitcoin.md) wallet, serving as both a full-node data store and wallet for [Bitcoin](../b/bitcoin.md) transactions. (https://bitcoincore.org/)
  - **Electrum**: A lightweight [Bitcoin](../b/bitcoin.md) wallet that provides increased speed by using remote servers to [handle](../h/handle.md) the heaviest parts of the [Bitcoin](../b/bitcoin.md) system. (https://electrum.org/)
  - **Armory**: Known for its advanced [security](../s/security.md) features. (https://btcarmory.com/)
  
- **Mobile Wallets**: Mobile wallets run on a smartphone app. They can be convenient, allowing for QR code scanning and NFC payments. Examples include:
  - **Mycelium**: Focuses on advanced privacy features for the users. (https://mycelium.com/)
  - **Breadwallet**: Simple to use and known for its clean user interface design. (https://breadwallet.com/)
  - **Samourai Wallet**: Renowned for its emphasis on user [security](../s/security.md) and privacy. (https://samouraiwallet.com/)

### Web Wallets

Web wallets store your private keys online on a server controlled by a third-party. This makes them accessible from any device with an internet connection but potentially more vulnerable to attacks and theft.

- **[Coinbase](../c/coinbase.md)**: A major [exchange](../e/exchange.md) that also offers a wallet service. (https://www.[coinbase](../c/coinbase.md).com/)
- **[Blockchain](../b/blockchain_in_trading.md).info**: Known for its simplicity and ease of use. (https://www.[blockchain](../b/blockchain_in_trading.md).com/)
- **Xapo**: Combines a cold-storage vault with a convenient day-to-day wallet. (https://xapo.com/)

### Hardware Wallets

Hardware wallets are physical devices specifically designed to use and secure [Bitcoin](../b/bitcoin.md). Hardware wallets are immune to computer viruses, providing a higher [security](../s/security.md) level. They need to be connected to a computer or mobile phone before Bitcoins can be spent. Examples include:

- **Trezor**: The first [Bitcoin](../b/bitcoin.md) hardware wallet with a screen, designed to protect your private keys from both physical and virtual thefts. (https://trezor.io/)
- **Ledger Nano S/X**: Popular hardware wallets that support [multiple](../m/multiple.md) cryptocurrencies including [Bitcoin](../b/bitcoin.md). (https://www.ledger.com/)
- **KeepKey**: Known for its luxurious design and easy-to-use interface. (https://shapeshift.com/keepkey)

### Paper Wallets

Paper wallets involve printing out the private and public keys onto a physical sheet paper. It's an incredibly secure offline method, but if the paper is lost or damaged, [Bitcoin](../b/bitcoin.md) funds can be irretrievably lost. Examples of services that help create paper wallets include:

- **BitAddress**: An [open](../o/open.md)-source JavaScript client-side Wallet Generator. (https://bitaddress.org/)
- **WalletGenerator.net**: Similar to BitAddress but supports [multiple](../m/multiple.md) cryptocurrencies. (https://walletgenerator.net/)

## How Bitcoin Wallets Work

To understand how [Bitcoin](../b/bitcoin.md) wallets work, it's important to first understand [Bitcoin](../b/bitcoin.md)'s [underlying](../u/underlying.md) technology: the [blockchain](../b/blockchain_in_trading.md). Here’s a simplified breakdown:

1. **Private and Public Keys**: A [Bitcoin](../b/bitcoin.md) wallet contains a pair of cryptographic keys:
    - **Private Key**: A secret key that must remain hidden as it is used to 'sign' transactions, providing a cryptographic proof that they have come from the wallet owner.
    - **Public Key**: Derived from the private key and shared openly. It’s hashed to form an address which others can use to send [Bitcoin](../b/bitcoin.md) to the wallet.
   
2. **Address Generation**: [Bitcoin](../b/bitcoin.md) addresses are generated using the public key. Every time you want to receive [Bitcoin](../b/bitcoin.md), you create a new address within your wallet.

3. **Handling Transactions**:
    - **Sending [Bitcoin](../b/bitcoin.md)**: The wallet uses the private key to sign the [transaction](../t/transaction.md), ensuring only the owner of that private key can move funds from the associated address.
    - **Receiving [Bitcoin](../b/bitcoin.md)**: Others send [Bitcoin](../b/bitcoin.md) to one of the wallet's public addresses. 

4. **Broadcasting to the Network**: Once a [transaction](../t/transaction.md) is signed, it’s broadcast to the [Bitcoin](../b/bitcoin.md) network where miners validate and add it to the [blockchain](../b/blockchain_in_trading.md).

## Setting Up a Bitcoin Wallet

Setting up a [Bitcoin](../b/bitcoin.md) wallet generally follows these steps:

### Software Wallet

1. **Download**: Choose a wallet provider and download the application from their official website or app store.
2. **Install**: Run the installer and follow the on-screen instructions.
3. **Backup**: Once installed, create a backup of the wallet’s private keys. This information is typically provided as a recovery phrase.
4. **Secure**: Set up additional [security](../s/security.md) measures such as a PIN, password, or two-[factor](../f/factor.md) authentication (2FA).
5. **Use**: You can now generate addresses and start sending and receiving [Bitcoin](../b/bitcoin.md).

### Hardware Wallet

1. **Purchase**: Buy a hardware wallet from a reputable vendor.
2. **Initialize**: Setup the device following strict instructions usually via a companion app provided by the hardware wallet manufacturer.
3. **Backup**: Write down the recovery seed—a collection of words that can be used to restore your wallet. Keep this in a safe place.
4. **Secure**: Assign a strong PIN code to the hardware wallet.
5. **Use**: Connect the wallet to a computer or mobile phone when you need to send [Bitcoin](../b/bitcoin.md).

### Web Wallet

1. **Sign Up**: Visit the wallet provider’s website and create an account.
2. **Secure**: Activate [security](../s/security.md) features such as 2FA and create a strong password.
3. **Use**: You can access your wallet from any internet-connected device to send and receive [Bitcoin](../b/bitcoin.md).

## Security Considerations

While [Bitcoin](../b/bitcoin.md) wallets are a secure way to [hold](../h/hold.md) and manage [Bitcoin](../b/bitcoin.md), users must adhere to [best practices](../b/best_practices.md) to ensure their assets remain safe:

- **Backup and Recovery**: Always create backups of your private keys and wallet information. Store recovery phrases securely and never share them.
- **Use Strong Passwords**: Passwords should be long, unique, and contain a mix of characters.
- **2FA**: Enable two-[factor](../f/factor.md) authentication whenever possible.
- **Keep Software Updated**: Regularly update your wallet software and any antivirus programs to protect against vulnerabilities.
- **Beware of Phishing**: Be vigilant about phishing attacks. Never enter your private key on any website or application.
- **Cold Storage**: For large amounts, consider using cold storage methods like hardware or paper wallets.

## Service Providers

There are numerous [Bitcoin](../b/bitcoin.md) wallet service providers, each catering to different needs:

- **[Coinbase](../c/coinbase.md)**: Offers both [exchange](../e/exchange.md) and wallet services with an intuitive user interface. (https://www.[coinbase](../c/coinbase.md).com/)
- **Trezor**: Trusted for its [security](../s/security.md) and easy integration with various online services. (https://trezor.io/)
- **Ledger**: Known for its wide [range](../r/range.md) of supported cryptocurrencies. (https://www.ledger.com/)
- **[Blockchain](../b/blockchain_in_trading.md).com**: Simple, user-friendly web and mobile wallets. (https://www.[blockchain](../b/blockchain_in_trading.md).com/)
- **Exodus**: A desktop wallet with a beautiful design and embedded [exchange](../e/exchange.md) features. (https://www.exodus.com/)

## Conclusion

[Bitcoin](../b/bitcoin.md) wallets are an essential tool for engaging with the [Bitcoin](../b/bitcoin.md) network, providing a secure and convenient means to store, send, and receive [Bitcoin](../b/bitcoin.md). Whether you opt for the convenience of a software wallet, the [security](../s/security.md) of a hardware wallet, or the ease of access provided by web wallets, it’s vital to understand the [trade](../t/trade.md)-offs each type offers. By implementing proper [security](../s/security.md) measures and using reputable service providers, users can effectively safeguard their digital assets and participate in the burgeoning world of cryptocurrencies.