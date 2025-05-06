# Regulator Dashboard

## Overview
The **Regulator Dashboard** is a key component of the Money Changer System. It provides regulators with a comprehensive view of the platform's operations, including statistics, transaction volumes, and detailed tables for proposals, transactions, and exchange rates.

---

## Features
### 1. **Overall Statistics**
- **Total Proposals**: Displays the total number of proposals submitted by users.
- **Total Agreements**: Shows the total number of agreements reached between buyers and sellers.
- **Transaction Volume**: Highlights the total transaction volume in USD.
- **Active Users**: Indicates the number of active users on the platform.

### 2. **Daily Transaction Volume Chart**
- A line chart visualizing daily transaction volumes in USD.
- Helps regulators monitor trends and identify anomalies.

### 3. **Detailed Tables**
#### a. **Latest Exchange Rates**
- Displays the most recent exchange rates, including:
  - Base and target currencies.
  - Exchange rate.
  - Source of the rate.
  - Date of the rate.

#### b. **Recent Proposals**
- Provides details about recent proposals, including:
  - Buyer and seller usernames.
  - Base and target currencies.
  - Proposed rate, amount, and total.
  - Status of the proposal.
  - Creation date.

#### c. **Recent Transactions**
- Lists recent transactions with details such as:
  - Buyer and seller usernames.
  - Transaction type.
  - Base and target currencies.
  - Amount, rate, and received amount.
  - Transaction date.

---

## Technologies Used
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django (Python)
- **Charts**: Chart.js for visualizing transaction data

---

## How to Use
1. **View Overall Statistics**:
   - Access key metrics like total proposals, agreements, transaction volume, and active users.

2. **Analyze Daily Transaction Volume**:
   - Use the line chart to monitor daily transaction trends.

3. **Review Detailed Tables**:
   - Inspect the latest exchange rates, recent proposals, and transactions for insights.

---

## Chart.js Integration
The dashboard uses Chart.js to render the daily transaction volume chart. The chart is configured with:
- **Type**: Line chart
- **Data**: Transaction dates and volumes
- **Options**: Scales starting at zero for better visualization

---

## Future Enhancements
- Add filtering options for tables (e.g., date range, user-specific data).
- Include more advanced analytics for regulators.
- Implement real-time updates for statistics and charts.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.