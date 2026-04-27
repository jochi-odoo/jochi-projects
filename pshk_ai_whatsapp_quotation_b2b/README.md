# Ps-Tech Module: pshk_ai_whatsapp_quotation_b2b

##  19.0.1.0.0

## Overview

Automatically creates quotation from received WhatsApp messages using an AI agent. A scheduled job periodically collects new messages and processes them in batch, identifying orders and creating them in Odoo.

## How It Works

### Message Format

Customers send WhatsApp messages in the following format:

```
Customer Name
Product Name 1 x Quantity 1
Product Name 2 x Quantity 2
...
```
The order line format can be slightly different, but must include product name and corresponding quantity

### Processing Flow

1. A **scheduled action** runs every hour and fetches all inbound WhatsApp messages received since the last run.
2. The messages are passed as a batch prompt to the **AI agent** (`WhatsApp Quotation B2B`).
3. The agent identifies which messages are quotation messages (ignoring greetings, unrelated messages, etc.).
4. For each identified order, the agent:
   - Calls **Get Information** to retrieve the list of partners and products with their IDs (called once per batch).
   - Calls **Create Quotation** with the resolved `partner_id`, `product_ids`, and quantities.
   - Calls **Send Inform Message** to reply to the customer's WhatsApp thread with the created order number.

## Components

### Scheduled Action
- **Name:** `Sales Order: Generate quotation from WhatsApp`
- **Model:** `sale.order`
- **Frequency:** Defualt to 1 hour

### AI Agent
- **Name:** `WhatsApp Quotation B2B`
- **Model:** `gpt-4o`
- **Topic:** `Create Quotations from WhatsApp`

### AI Tools

| Tool | Description |
|---|---|
| **Get Information** | Fetches all partners and products from the database with their IDs. Called once per batch. |
| **Create Quotation** | Creates a `sale.order` record with the resolved partner and product IDs. |
| **Send Inform Message** | Posts a WhatsApp reply in the customer's channel with the created order name. |

### Bot User
A dedicated internal user (`WhatsApp AI Bot`) is created and assigned as the salesperson on all quotations created by this module.

## Configuration

- A WhatsApp account is configured under **WhatsApp > Configuration > WhatsApp Accounts**.
- An OpenAI API key is configured under **AI > Configurations > Settings**.


## Notes

- Only **inbound** WhatsApp messages are processed.
- Messages that are not in the quotation format are ignored by the agent.
- The message is sent in free form instead of template, free form message can only be sent within the 24-hour window after receiving messages from the customer. Therefore make sure the scheduled frequecy in less than 24 hours.

5908345
