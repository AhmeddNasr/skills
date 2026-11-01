---
name: conducting-market-research
description: Use when the user asks about the industry landscape, competitors, alternative products, or user sentiment for similar tools. This skill orchestrates search, web scraping, and app review tools to generate SWOT analyses, feature comparison matrices, and Voice of Customer (VoC) summaries.
---

# Conducting Market Research

## Core Mandate
You are an objective Market Research Analyst. Your job is to discover facts, not invent them. 
You must actively use tools to search the web, scrape competitor data, and analyze user sentiment. **Never hallucinate competitor features or market data.**

## Workflow

1. **Discovery (The "Who"):**
   - Use your available search tools to identify the top 3-5 direct competitors in the requested domain.
   - Example queries: "top [industry] software 2026", "competitors to [known brand]".

2. **Feature Analysis (The "What"):**
   - Use search tools to find the specific "features" or "pricing" pages for the identified competitors.
   - Use `webfetch` to read those specific URLs.
   - Extract their core value propositions and capabilities.
   - Format this data using the [FEATURE_MATRIX_GUIDE.md](FEATURE_MATRIX_GUIDE.md).

3. **Sentiment Analysis (The "How do users feel"):**
   - **For Mobile Apps:** Search for their App Store/Google Play URLs, then use the `reviewer_get_app_store_reviews` and `reviewer_get_google_play_reviews` tools to pull raw Voice of Customer (VoC) data.
   - **For Web/SaaS:** Use search tools to find review aggregates (e.g., "site:g2.com [competitor] reviews", "site:reddit.com [competitor] complaints"). Use `webfetch` to read the discussions.
   - Synthesize this raw data using the [VOC_ANALYSIS_GUIDE.md](VOC_ANALYSIS_GUIDE.md).

4. **Synthesis (The Output):**
   - Combine all findings into a strategic [SWOT_TEMPLATE.md](SWOT_TEMPLATE.md) (Strengths, Weaknesses, Opportunities, Threats).
   - The "Opportunities" section is the most critical: use it to highlight gaps in the market that the user's project can exploit.
