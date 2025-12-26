# Hyperledger Explorer

[Hyperledger](../h/hyperledger.md) Explorer is an [open](../o/open.md)-source [blockchain](../b/blockchain_in_trading.md) module within the larger [Hyperledger](../h/hyperledger.md) project umbrella hosted by The Linux Foundation. It serves as a powerful browser for viewing, managing, and monitoring [blockchain](../b/blockchain_in_trading.md) deployments. This [blockchain](../b/blockchain_in_trading.md) viewer is specifically designed to allow users to create a user-friendly web application for searching, querying, and visualizing data on a [Hyperledger Fabric](../h/hyperledger_fabric.md) [blockchain](../b/blockchain_in_trading.md) network.

This comprehensive guide delves into the various components and functionalities of [Hyperledger](../h/hyperledger.md) Explorer, elucidating its importance, architecture, use cases, and more.

## Introduction to Hyperledger Explorer

[Hyperledger](../h/hyperledger.md) Explorer provides a user interface for visual analytics and drill-down capabilities to understand and monitor different aspects of [blockchain](../b/blockchain_in_trading.md) activity. It's an essential tool for anyone working with [Hyperledger Fabric](../h/hyperledger_fabric.md) who needs to track chaincodes, transactions, and blocks across [multiple](../m/multiple.md) nodes.

## Core Features

[Hyperledger](../h/hyperledger.md) Explorer offers numerous features that make it a valuable tool for developers, administrators, and [business](../b/business.md) stakeholders.

### Real-Time Monitoring

One of the core features is the real-time monitoring of [blockchain](../b/blockchain_in_trading.md) activity. This includes the ability to view real-time data for blocks, transactions, and network [performance metrics](../p/performance_metrics.md), allowing for fast identification and resolution of issues.

### Comprehensive Dashboard

[Hyperledger](../h/hyperledger.md) Explorer presents data in a user-friendly dashboard. This dashboard gives a bird's eye view of the [blockchain](../b/blockchain_in_trading.md) network, encompassing details such as the current block, [transaction](../t/transaction.md) count, and node status.

### Drill-Down Capabilities

Through its drill-down capabilities, users can dig deeper into the data by clicking on various items in the dashboard. You can explore specific blocks, transactions, and their contents comprehensively.

### Querying and Searching

[Hyperledger](../h/hyperledger.md) Explorer’s querying and searching features allow users to locate specific transactions and blocks easily. This can be useful for audits and compliance, as well as troubleshooting and debugging purposes.

### API Integration

[Hyperledger](../h/hyperledger.md) Explorer offers API integration, making it easier to pull in data from other systems or push Explorer's analytics to other platforms.

### Block, Chaincode, and Transaction Details

Detailed information about blocks, deployable chaincodes, and transactions can be accessed. This includes timestamp, [transaction](../t/transaction.md) types, [transaction](../t/transaction.md) IDs, payloads, and endorsements.

## Architecture

[Hyperledger](../h/hyperledger.md) Explorer has a modular and layered architecture making it scalable and flexible. Here’s a detailed look at the different layers:

### User Interface Layer

The user interface layer is built using modern web development frameworks such as Angular or React. This layer is responsible for rendering the visual components of the dashboard.

### Middleware Layer

The middleware layer handles communication between the user interface and the [blockchain](../b/blockchain_in_trading.md) network. This layer is developed using Node.js and Express.js, providing RESTful APIs for ease of integration and enhancing performance.

### Blockchain Platform Layer

This layer includes the [Hyperledger Fabric](../h/hyperledger_fabric.md) SDK and other [blockchain](../b/blockchain_in_trading.md) interaction modules. It's responsible for interfacing directly with the [blockchain](../b/blockchain_in_trading.md) nodes, endorsers, and orderers to fetch the necessary data.

### Data Storage

Data is stored in a relational database like PostgreSQL. This allows for efficient querying, [indexing](../i/indexing.md), and storage of [blockchain](../b/blockchain_in_trading.md) data.

## Installation and Setup

The process to install and set up [Hyperledger](../h/hyperledger.md) Explorer can be broken down into several steps. Here’s a high-level overview:

### Prerequisites

- Node.js and npm
- PostgreSQL
- Docker and Docker Compose (if using Docker for [Hyperledger Fabric](../h/hyperledger_fabric.md) setup)
- A running [Hyperledger Fabric](../h/hyperledger_fabric.md) network

### Clone Repository

```bash
git clone cd [blockchain](../b/blockchain_in_trading.md)-explorer
```

### Configure Database

Set up PostgreSQL and create a database and user for [Hyperledger](../h/hyperledger.md) Explorer.

```sql
CREATE DATABASE fabricexplorer;
CREATE USER explorer WITH ENCRYPTED PASSWORD 'explorerpw';
[GRANT](../g/grant.md) ALL PRIVILEGES ON DATABASE fabricexplorer TO explorer;
```

### Environment Configuration

Set up the environment variables by copying the sample configuration files provided within the repository.

```bash
cp app/platform/fabric/config.json app/platform/fabric/config_local.json
```

Update the `config_local.json` file with your network configuration.

### Install Dependencies and Run

Install the necessary dependencies and start the Explorer:

```bash
npm install
cd client/
npm install
```

Run the Explorer:

```bash
cd ..
./start.sh
```

Visit ` to see [Hyperledger](../h/hyperledger.md) Explorer in action.

## Use Cases

[Hyperledger](../h/hyperledger.md) Explorer is immensely versatile and can be used across various [industry](../i/industry.md) verticals. Here are a few examples:

### Financial Services

Banks and financial institutions can use [Hyperledger](../h/hyperledger.md) Explorer for [transaction](../t/transaction.md) monitoring, ensuring quick identification and resolution of discrepancies.

### Supply Chain

Enterprises can monitor the flow of goods through their [supply chain](../s/supply_chain.md), ensuring full [transparency](../t/transparency.md) and traceability from source to destination.

### Healthcare

With stricter compliance regulations, healthcare organizations can use [Hyperledger](../h/hyperledger.md) Explorer for auditing and ensuring compliance with data protection laws like HIPAA.

### Governance

Governments can use it for maintaining transparent and tamper-proof records of various public service initiatives.

## Integrations and Extensibility

[Hyperledger](../h/hyperledger.md) Explorer can be easily integrated with other systems through its RESTful APIs. This allows enterprises to extend its functionalities, feeding data into other analytics tools or integrating with legacy systems.

## Security Considerations

Since [Hyperledger](../h/hyperledger.md) Explorer interacts closely with your [blockchain](../b/blockchain_in_trading.md) data, securing it is crucial. Here are a few measures:

### Secure Configuration

Ensure your environment configuration files do not store sensitive information in plaintext. Use environment variables or encrypted storage where possible.

### Authentication and Authorization

Implement authentication mechanisms to ensure that only authorized users have access to the Explorer.

### Network Security

Use firewalls, VPNs, and other network [security](../s/security.md) measures to safeguard the server hosting [Hyperledger](../h/hyperledger.md) Explorer from unauthorized access.

## Community and Support

### Community

The [Hyperledger](../h/hyperledger.md) community is highly active, [offering](../o/offering.md) support through mailing lists, forums, and chat platforms like Discord and Rocket.Chat.

### Hyperledger Explorer GitHub Repository

All code and documentation are [open](../o/open.md)-source and housed on GitHub. Contributions are welcomed, and issues or feature requests can be logged here:


## Conclusion

[Hyperledger](../h/hyperledger.md) Explorer is a highly effective tool for anyone looking to [gain](../g/gain.md) insights and maintain oversight of their [Hyperledger Fabric](../h/hyperledger_fabric.md) [blockchain](../b/blockchain_in_trading.md) network. Its user-friendly interface, real-time monitoring capabilities, and detailed analytics make it indispensable for technical and non-technical users alike. Whether you are an admin looking to monitor performance or a [business](../b/business.md) user aiming to derive actionable insights, [Hyperledger](../h/hyperledger.md) Explorer offers the functionalities necessary to meet those needs.