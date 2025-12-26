# Hyperledger Composer

> **Note:** Hyperledger Composer was deprecated in 2019 and is no longer actively maintained. New projects should use Hyperledger Fabric directly with its native chaincode development approach. This article is retained for historical reference.

[Hyperledger](../h/hyperledger.md) Composer was an [open](../o/open.md)-source tool that enabled [business](../b/business.md) owners, analysts, system integrators, and developers to create [blockchain](../b/blockchain_in_trading.md) applications and [smart contracts](../s/smart_contracts_in_trading.md) aimed at solving [business](../b/business.md) issues. Developed under the [Hyperledger](../h/hyperledger.md) project by the Linux Foundation, it was a suite of high-level tools designed for building [blockchain](../b/blockchain_in_trading.md) [business](../b/business.md) networks in [Hyperledger Fabric](../h/hyperledger_fabric.md).

[Hyperledger](../h/hyperledger.md) Composer is particularly useful because it speeds up the development process and simplifies the creation of [smart contracts](../s/smart_contracts_in_trading.md), which are digital contracts that are self-executing with the terms of the agreement directly written into code. [Hyperledger](../h/hyperledger.md) Composer significantly reduces the [barriers to entry](../b/barriers_to_entry.md) for [blockchain](../b/blockchain_in_trading.md) application development.

## Key Features of Hyperledger Composer

1. **Modeling Language:**
 - [Hyperledger](../h/hyperledger.md) Composer uses a modeling language to define the structure of the [business](../b/business.md) network, including assets, participants, and transactions. The language is easy to understand and allows developers to describe the [blockchain](../b/blockchain_in_trading.md) logic in a manner that closely resembles [business](../b/business.md) language.

2. **[Business](../b/business.md) Network Archive:**
 - Users can deploy a [business](../b/business.md) network archive (BNA), which is a package containing all the necessary files for a [business](../b/business.md) network. This includes model files (.cto), script files (.js), access control files (.acl), and query files (.qry).

3. **Integration with [Hyperledger Fabric](../h/hyperledger_fabric.md):**
 - [Hyperledger](../h/hyperledger.md) Composer provides a seamless integration with [Hyperledger Fabric](../h/hyperledger_fabric.md). Once developed, the [business](../b/business.md) network can be deployed on [Hyperledger Fabric](../h/hyperledger_fabric.md), allowing for the use of its [robust](../r/robust.md) consensus mechanisms and [security](../s/security.md) features.

4. **Testing:**
 - [Hyperledger](../h/hyperledger.md) Composer includes tools for testing [blockchain](../b/blockchain_in_trading.md) applications. Developers can write unit tests for the [business](../b/business.md) logic and end-to-end tests for the entire [business](../b/business.md) network.

5. **REST API Generation:**
 - One of the significant advantages of [Hyperledger](../h/hyperledger.md) Composer is its auto-generation of REST APIs from the defined [business](../b/business.md) network model. This allows for easy integration with existing systems and enables front-end applications to interact with the [blockchain](../b/blockchain_in_trading.md) without needing to [handle](../h/handle.md) complex [blockchain](../b/blockchain_in_trading.md) transactions.

6. **Command Line Interface (CLI):**
 - [Hyperledger](../h/hyperledger.md) Composer offers a powerful CLI tool that allows developers to interact with the [business](../b/business.md) network. The CLI can be used to deploy, test, and manage the [business](../b/business.md) network, as well as interact with the [blockchain](../b/blockchain_in_trading.md) ledger.

7. **Flexible Deployment:**
 - [Hyperledger](../h/hyperledger.md) Composer provides the flexibility to deploy [business](../b/business.md) networks on various infrastructures, including local machines, clouds, or as part of a Kubernetes cluster. This adaptability ensures that it caters to various organizational needs.

## Components of Hyperledger Composer

### Business Network Definition

A [Business](../b/business.md) Network Definition (BND) in [Hyperledger](../h/hyperledger.md) Composer is a package that defines the declarative and programmatic components of a [business](../b/business.md) network. Each BND is typically composed of [multiple](../m/multiple.md) files, including:

- **Model Files (.cto):** These define the structure of the [business](../b/business.md) network, describing assets, participants, transactions, and relationships using the Composer Modeling Language.

- **Script Files (.js):** These contain [transaction](../t/transaction.md) logic for the [business](../b/business.md) network and are written in JavaScript.

- **Access Control Files (.acl):** These specify the rules for permissions and access control within the [business](../b/business.md) network, determining who can read or write to the ledger.

- **Query Files (.qry):** These define complex queries that can be executed on the [blockchain](../b/blockchain_in_trading.md) ledger using [Hyperledger](../h/hyperledger.md) Composer's query language.

### Composer Modeling Language

The modeling language in [Hyperledger](../h/hyperledger.md) Composer is crucial for defining the elements of the [business](../b/business.md) network. It allows users to describe:

- **Participants:** Represent individuals or organizations that interact with the [business](../b/business.md) network.

- **Assets:** Represent tangible or intangible items that the [business](../b/business.md) network tracks.

- **Transactions:** Define valid activities that can occur within the [business](../b/business.md) network, affecting assets and participants.

- **Events:** Notification mechanisms that can be emitted by transactions and received by participants.

### Composer Playground

The Composer Playground ( is a web-based interface that allows users to model, define, and test their [business](../b/business.md) networks without needing extensive setup. It provides a user-friendly environment to create BNDs, manage identities, and simulate transactions.

### Fabric Integration

[Hyperledger](../h/hyperledger.md) Composer utilizes [Hyperledger Fabric](../h/hyperledger_fabric.md) ( as the [underlying](../u/underlying.md) [blockchain](../b/blockchain_in_trading.md) platform, which provides a modular architecture for distributed ledger solutions. The integration includes seamless deployment of BNDs on a Fabric network, leveraging Fabric’s [robust](../r/robust.md) features like consensus mechanisms, channels, MSP (Membership Service Provider), and more.

## Developing a Hyperledger Composer Application

### Step-by-Step Guide

1. **Set Up the Development Environment:**
 - Install pre-requisites including Node.js, npm, and Docker.
 - Install [Hyperledger](../h/hyperledger.md) Composer CLI tools using npm.
 ```bash
 npm install -g generator-[hyperledger](../h/hyperledger.md)-composer
 ```

2. **Create a [Business](../b/business.md) Network:**
 - Use Yeoman generator to create a [Business](../b/business.md) Network Definition.
 ```bash
 yo [hyperledger](../h/hyperledger.md)-composer:businessnetwork
 ```

3. **Define Models:**
 - Create `.cto` files to define the participants, assets, and transactions.
 ```plaintext
 // Example model file (models/org.example.basic.cto)
 namespace org.example.basic

 [asset](../a/asset.md) SampleAsset identified by assetId {
 o String [value](../v/value.md)
 }

 participant SampleParticipant identified by participantId {
 }

 [transaction](../t/transaction.md) SampleTransaction {
 --> SampleAsset [asset](../a/asset.md)
 }
 ```

4. **Implement Logic:**
 - Write [transaction](../t/transaction.md) processor functions in `.js` files.
 ```javascript
 // Example script file (lib/logic.js)
 /**
 * Sample [transaction](../t/transaction.md) processor function
 * @param {org.example.basic.SampleTransaction} tx - the sample [transaction](../t/transaction.md)
 * @[transaction](../t/transaction.md)
 */
 async function sampleTransaction(tx) {
 tx.[asset](../a/asset.md).[value](../v/value.md) = tx.newValue;
 let assetRegistry = await getAssetRegistry('org.example.basic.SampleAsset');
 await assetRegistry.update(tx.[asset](../a/asset.md));
 }
 ```

5. **Define Access Controls:**
 - Create `.acl` files to manage permissions.
 ```plaintext
 // Example access control file (permissions.acl)
 rule ParticipantAccess {
 description: "Allow all participants to read all assets"
 participant: "org.example.basic.SampleParticipant"
 operation: READ
 resource: "org.example.basic.*"
 action: ALLOW
 }
 ```

6. **Deploy the [Business](../b/business.md) Network:**
 - Package the network and deploy it on [Hyperledger Fabric](../h/hyperledger_fabric.md).
 ```bash
 composer archive create --sourceType dir --sourceName.
 composer network install --card PeerAdmin@hlfv1 --archiveFile <network-name>.bna
 composer network start --networkName <network-name> --networkVersion 0.0.1 --card PeerAdmin@hlfv1 --networkAdmin admin --networkAdminEnrollSecret adminpw
 ```

7. **Run a REST API Server:**
 - Generate and start a REST API server to interact with the [business](../b/business.md) network.
 ```bash
 composer-rest-server -c admin@<network-name> -n always -u true -w true
 ```

8. **Test and Iterate:**
 - Conduct tests using Composer Playground or Postman to simulate transactions and validate [business](../b/business.md) logic.

## Advantages of Using Hyperledger Composer

### Rapid Development

[Hyperledger](../h/hyperledger.md) Composer allows for quick and efficient development of [blockchain](../b/blockchain_in_trading.md) applications by providing high-level abstractions and tools that abstract away many low-level details. This rapid development cycle means businesses can prototype, test, and iterate solutions more quickly.

### Simplified Modeling

With the Composer Modeling Language, defining the structure and behavior of [blockchain](../b/blockchain_in_trading.md) applications becomes straightforward and intuitive, enabling [business](../b/business.md) analysts and developers to collaborate more effectively.

### Strong Integration with Enterprise Systems

The tool’s ability to auto-generate REST APIs from the defined [business](../b/business.md) network simplifies the integration of [blockchain](../b/blockchain_in_trading.md) applications with existing enterprise systems and front-end applications, promoting interoperability and extensibility.

### Flexible Deployment Options

[Hyperledger](../h/hyperledger.md) Composer supports various deployment [options](../o/options.md), ranging from local development environments to cloud-based [infrastructure](../i/infrastructure.md) and Kubernetes clusters, ensuring that solutions can scale according to [business](../b/business.md) needs.

### Community and Support

Being part of the [Hyperledger](../h/hyperledger.md) project under the Linux Foundation, [Hyperledger](../h/hyperledger.md) Composer benefits from a strong community, abundant resources, and regular updates, ensuring that it remains a reliable and cutting-edge tool for [blockchain](../b/blockchain_in_trading.md) development.

## Challenges and Limitations

Despite its [robust](../r/robust.md) features, [Hyperledger](../h/hyperledger.md) Composer has certain limitations:

1. **Dependency on [Hyperledger Fabric](../h/hyperledger_fabric.md):** [Hyperledger](../h/hyperledger.md) Composer is tightly coupled with [Hyperledger Fabric](../h/hyperledger_fabric.md), which may not be ideal for all types of [blockchain](../b/blockchain_in_trading.md) use cases.
2. **[Learning Curve](../l/learning_curve.md):** While the tool abstracts many complexities, there remains a [learning curve](../l/learning_curve.md) associated with understanding both Composer and Fabric’s functionalities and [best practices](../b/best_practices.md).
3. **Transition to Fabric [Transaction](../t/transaction.md) Language:** With the focus shifting towards Fabric’s native capabilities, the Composer toolset may face less emphasis in future developments.

## Conclusion

[Hyperledger](../h/hyperledger.md) Composer is a pioneering tool that accelerates the development of [blockchain](../b/blockchain_in_trading.md) solutions by providing high-level abstractions and tools tailored for [business](../b/business.md) applications. Its strong integration with [Hyperledger Fabric](../h/hyperledger_fabric.md), comprehensive modeling language, and the ability to generate REST APIs make it an invaluable [asset](../a/asset.md) for enterprises looking to [leverage](../l/leverage.md) [blockchain](../b/blockchain_in_trading.md) technology efficiently. Despite some limitations, its advantages in rapid development, simplified modeling, and flexible deployment create significant [value](../v/value.md) for businesses.

For more information and resources, consult the [Hyperledger](../h/hyperledger.md) Composer documentation.
