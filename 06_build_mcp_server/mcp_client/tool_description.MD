
# MCP Tools Documentation

## 1. **get_ticker_data**

**a) Description:**  
Provides a comprehensive report for a given stock ticker including:
- Company overview  
- Financial news  
- Key performance metrics  
- Important dates  
- Analyst recommendations  
- Upgrade/downgrade history  

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_ticker_data",
  "args": {
    "ticker": "AAPL"
  }
}
```
</details>

---

## 2. **get_price_history**

**a) Description:**  
Fetches historical price data for a given period, including:
- OHLCV data  
- Technical indicators (via `ta-lib`)  
- Risk metrics  
- Pattern recognition  
- Fibonacci levels  
- Smart sampled data for LLMs  

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_price_history",
  "args": {
    "ticker": "TSLA",
    "period": "3mo"
  }
}
```
</details>

---

## 3. **get_financial_statements**

**a) Description:**  
Retrieves financial statements for a company, including:
- Income statements  
- Balance sheets  
- Cash flow statements  
With options for **quarterly** or **annual** frequency.

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_financial_statements",
  "args": {
    "ticker": "GOOG",
    "statement_type": "income",
    "frequency": "annual"
  }
}
```
</details>

---

## 4. **get_earnings_history**

**a) Description:**  
Provides a company’s historical earnings with:
- Estimated EPS  
- Actual EPS  
- Earnings surprise data  

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_earnings_history",
  "args": {
    "ticker": "NFLX"
  }
}
```
</details>

---

## 5. **get_insider_trades**

**a) Description:**  
Retrieves recent insider trading activity for a given company.

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_insider_trades",
  "args": {
    "ticker": "MSFT"
  }
}
```
</details>

---

## 6. **get_ticker_news_tool**

**a) Description:**  
Fetches recent Yahoo Finance news articles related to a specific ticker. Useful for current sentiment and developments.

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_ticker_news_tool",
  "args": {
    "ticker": "NVDA"
  }
}
```
</details>

---

## 7. **super_option_tool**

**a) Description:**  
Analyzes and summarizes options data for a ticker. Includes:
- Greeks  
- Open interest  
- Volume  
- Implied volatility  
- Summary digest  

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "super_option_tool",
  "args": {
    "ticker": "AMD"
  }
}
```
</details>

---

## 8. **get_holdings_summary**

**a) Description:**  
Analyzes 13F/13D/G filings to extract institutional holdings for a ticker over the past 6 months. Returns a formatted summary.

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_holdings_summary",
  "args": {
    "ticker": "META"
  }
}
```
</details>

---

## 9. **get_overall_sentiment_tool**

**a) Description:**  
Returns a combined sentiment snapshot using:
- CNN Fear & Greed Index  
- Market RSI  
- VIX Volatility Index  

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_overall_sentiment_tool",
  "args": {}
}
```
</details>

---

## 10. **get_historical_fng_tool**

**a) Description:**  
Retrieves CNN Fear & Greed Index values for a specified number of past days.

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_historical_fng_tool",
  "args": {
    "days": 30
  }
}
```
</details>

---

## 11. **analyze_fng_trend**

**a) Description:**  
Analyzes trend direction and metrics from the CNN Fear & Greed Index over a time period.

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "analyze_fng_trend",
  "args": {
    "days": 14
  }
}
```
</details>

---

## 12. **calculate**

**a) Description:**  
Evaluates mathematical expressions using Python's math syntax and NumPy. Can compute expressions, means, sin/cos, etc.

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "calculate",
  "args": {
    "expression": "2 * (3 + 5) + np.mean([1, 2, 3])"
  }
}
```
</details>

---

## 13. **get_current_time**

**a) Description:**  
Returns the current time in ISO 8601 format (UTC timestamp).

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_current_time",
  "args": {}
}
```
</details>

---

## 14. **get_fred_series**

**a) Description:**  
Fetches a time series from the FRED (Federal Reserve Economic Data) API based on a series ID (e.g., "GDP", "CPIAUCSL").

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "get_fred_series",
  "args": {
    "series_id": "GDP"
  }
}
```
</details>

---

## 15. **search_fred_series**

**a) Description:**  
Searches for relevant FRED data series by keyword (e.g., "inflation", "employment").

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "search_fred_series",
  "args": {
    "query": "CPI"
  }
}
```
</details>

---

## 16. **cnbc_news_feed**

**a) Description:**  
Returns the latest world financial news headlines from CNBC, BBC, and SCMP. Also includes Fed Watch rate predictions.

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "cnbc_news_feed",
  "args": {}
}
```
</details>

---

## 17. **social_media_feed**

**a) Description:**  
Returns trending topics, stocks, and investor sentiment based on social media discussions.

<details>
<summary><strong>b) How to Invoke</strong></summary>

```json
{
  "tool": "social_media_feed",
  "args": {}
}
```
</details>

---
