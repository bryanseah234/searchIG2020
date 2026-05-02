# PRD: searchIG2020

## Overview
A Python script that uses Google search to discover Instagram profiles matching specific bio keywords. Constructs targeted Google dorks (`site:instagram.com inbio:keyword`) to find Instagram users with particular interests, and saves discovered profile URLs to a text file. Built in 2020 for OSINT/research purposes.

## Goals
- Accept a list of target keywords
- Construct Google search queries targeting Instagram profiles
- Extract Instagram profile URLs from search results
- Save discovered URLs to output file

## Non-Goals
- Scraping Instagram profile content (followers, posts, DMs)
- Automated follow/like/comment actions
- Real-time monitoring

## User Stories
- As a researcher, I want to find Instagram users who mention a specific interest in their bio.
- As a marketer, I want to discover potential influencers in a niche via keyword search.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: `requests` or `selenium`, `BeautifulSoup` (scraping Google results)

## Architecture
```
searchIG2020/
└── scrape instagram code.py   # Main scraper
```

## Deployment / Run
```bash
pip install -r requirements.txt
python "scrape instagram code.py"
```

## Constraints & Notes
- **Legal**: Instagram's Terms of Service prohibit automated scraping; Google Search also prohibits automated queries — use only for personal/research purposes
- **Google reCAPTCHA**: automated Google queries are likely to hit captchas; script may require manual intervention or proxy rotation
- **Instagram scraping**: profile content beyond what appears in Google snippets requires Instagram session — this script targets Google results, not Instagram directly
- **2020 accuracy**: Google's `inbio:` operator behavior may have changed; accuracy of results not guaranteed
