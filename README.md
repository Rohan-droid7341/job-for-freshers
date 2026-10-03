# Indian Fresher & New-Grad Jobs

[![CI](https://github.com/Rohan-droid7341/job-for-freshers/actions/workflows/ci.yml/badge.svg)](https://github.com/Rohan-droid7341/job-for-freshers/actions/workflows/ci.yml) ![Open roles](https://img.shields.io/badge/dynamic/json?label=open%20roles&query=open_total&url=https%3A%2F%2Frohan-droid7341.github.io%2Fjob-for-freshers%2Fapi%2Fstats.json&color=2f81f7) ![Updates](https://img.shields.io/badge/updates-every%204h-3fb950) [![RSS](https://img.shields.io/badge/RSS-subscribe-e67e22)](https://rohan-droid7341.github.io/job-for-freshers/feed.xml)

A self-updating engine that tracks **full-time fresher & new-grad tech jobs** for the **2026 & 2027 batch** across India — so you don't have to. Instead of refreshing Naukri, LinkedIn, and a dozen career pages by hand, it reads company hiring feeds directly and keeps one live list, newest roles on top, refreshed automatically throughout the day.

**0 open roles · 0 new this week · 5,293 companies tracked · updated Oct 03, 2026 at 13:54 UTC**

**⭐ Star this repo ⭐** to save it and get notified when new roles land.

**Live:** [dashboard](https://rohan-droid7341.github.io/job-for-freshers/) · [RSS feed](https://rohan-droid7341.github.io/job-for-freshers/feed.xml) (instant alerts in any RSS app) · [JSON API](https://rohan-droid7341.github.io/job-for-freshers/api/jobs.json)

**🔔 New roles in your inbox:** [subscribe by email](https://rohan-droid7341.github.io/job-for-freshers/#subscribe) - one email a day, only when new jobs actually appeared, one-click unsubscribe. (Prefer RSS-to-email? [Feedrabbit works too](https://feedrabbit.com/subscriptions/new?url=https%3A%2F%2Fraw.githubusercontent.com%2FRohan-droid7341%2Fjob-for-freshers%2Fmain%2Fdocs%2Ffeed.xml).)
---

_No matching roles right now — the list fills as companies post fresher openings. ⭐ Star and check back._

## What this is

This is an engine, not a hand-kept list. It polls company career feeds several times a day, detects fresher / new-grad openings using a 4-tier signal detector (batch year → title band → experience range → eligibility signals), removes duplicates, and rebuilds this page automatically. Every link comes straight from the source — no stale copy-paste lists.

## What makes this different

- **🎓 Fresher-specific detection** — finds roles by what companies actually write: `2026 batch`, `Graduate Engineer Trainee`, `0-1 years`, `no active backlogs`, `CGPA ≥ 7.0`, `PPO`, `TCS NQT` — not just title keywords.
- **Real posted dates on every role** — pulled from each ATS directly, so newest-first actually means newest.
- **Skill tags + pay, extracted** — every posting's text is scanned for the stack it wants (Python, Java, C++, SQL, ...) and the CTC / stipend it states — searchable on the [dashboard](https://rohan-droid7341.github.io/job-for-freshers/), included in the CSV and API.
- **Alerts your way** — [email digests](https://rohan-droid7341.github.io/job-for-freshers/#subscribe), [RSS](https://rohan-droid7341.github.io/job-for-freshers/feed.xml), or Discord — plus a [live dashboard](https://rohan-droid7341.github.io/job-for-freshers/) with search and custom filters.
- **Covers the full India fresher ecosystem** — Naukri (fresher filter), Unstop (off-campus drives), Internshala, direct ATS (Greenhouse, Workday, Lever…), and custom scrapers for Flipkart, Swiggy, Razorpay, and more.
- **An engine, not a spreadsheet** — polled every 4 hours across all platforms with full source in this repo.

## Scope

- **Roles:** Full-time entry-level / fresher — Software Engineering, Data Science & ML, and closely related tech roles
- **Batch:** 2026 and 2027 passouts (freshers & final-year)
- **Region:** India & Verified Remote
- **What we detect:** Graduate Engineer Trainee, Associate SWE/SDE, Junior Developer, System Engineer (TCS/Infosys band), Programmer Analyst Trainee (Cognizant), off-campus drives, and any role stating `2026 batch` / `2027 passout` / `0-1 years` in the JD

## About

I built this engine because finding fresher jobs in India is painful — Naukri floods you with spam, LinkedIn shows you senior roles, and off-campus drives close before you even hear about them. This engine watches everything automatically and surfaces only what's relevant for the 2026/2027 batch. Apply early — freshers who apply in the first 48 hours have a significantly higher callback rate.

## How to use

- Roles are grouped by batch year — **newest posting on top, oldest at the bottom.**
- The **Posted** column is the date the company published the role.
- **Flags:** 🆕 = spotted in the last 48 hours — apply immediately.
- The **Pay & Specs** column shows CTC / stipend + experience range + degree.
- Track your applications with [`data/jobs.csv`](data/jobs.csv) (opens in Excel / Google Sheets).
- Missing a company? Adding one takes a single line — see [CONTRIBUTING.md](CONTRIBUTING.md).

---

<a id="drop-radar"></a>

## 📅 Drop Radar — when companies usually post for 2026 batch

Stop refreshing career pages. Every date here is **real or verified** — no third-party list. 🎯 = the engine **saw the drop itself** from the company's own careers API; the rest are hand-checked typical opening windows for marquee names. ✅ = already live in the list above.

> **Heads up:** companies trend *earlier* every cycle, and "~Aug" is a month, not a day. Treat "expected" as when to **start watching**, and "rolling" companies as worth checking year-round.

| Company | Typical opening | Expected this cycle | Status |
|---|---|---|---|
| Amazon | ~Jul | ~Jul · any day now | ⏳ waiting |
| Akuna Capital | ~Aug | ~Aug · any day now | ⏳ waiting |
| Citadel | ~Aug | ~Aug · any day now | ⏳ waiting |
| Citadel Securities | ~Aug | ~Aug · any day now | ⏳ waiting |
| Databricks | ~Aug | ~Aug · any day now | ⏳ waiting |
| DoorDash | ~Aug | ~Aug · any day now | ⏳ waiting |
| DRW | ~Aug | ~Aug · any day now | ⏳ waiting |
| Five Rings | ~Aug | ~Aug · any day now | ⏳ waiting |
| Google | ~Aug | ~Aug · any day now | ⏳ waiting |
| Jane Street | ~Aug | ~Aug · any day now | ⏳ waiting |
| Meta | ~Aug | ~Aug · any day now | ⏳ waiting |
| Optiver | ~Aug | ~Aug · any day now | ⏳ waiting |
| Pinterest | ~Aug | ~Aug · any day now | ⏳ waiting |
| Salesforce | ~Aug | ~Aug · any day now | ⏳ waiting |
| SIG | ~Aug | ~Aug · any day now | ⏳ waiting |
| Snowflake | ~Aug | ~Aug · any day now | ⏳ waiting |
| Tower Research Capital | ~Aug | ~Aug · any day now | ⏳ waiting |
| Uber | ~Aug | ~Aug · any day now | ⏳ waiting |
| Adobe | ~Sep | ~Sep · any day now | ⏳ waiting |
| Airbnb | ~Sep | ~Sep · any day now | ⏳ waiting |
| Bloomberg | ~Sep | ~Sep · any day now | ⏳ waiting |
| Dropbox | ~Sep | ~Sep · any day now | ⏳ waiting |
| Hudson River Trading | ~Sep | ~Sep · any day now | ⏳ waiting |
| Plaid | ~Sep | ~Sep · any day now | ⏳ waiting |
| Point72 | ~Sep | ~Sep · any day now | ⏳ waiting |
| Robinhood | ~Sep | ~Sep · any day now | ⏳ waiting |
| Roblox | ~Sep | ~Sep · any day now | ⏳ waiting |
| Stripe | ~Sep | ~Sep · any day now | ⏳ waiting |
| D.E. Shaw | ~Oct | ~Oct · any day now | ⏳ waiting |
| Coinbase | ~Dec | ~Dec | ⏳ waiting |

_42 companies on the [full radar](https://rohan-droid7341.github.io/job-for-freshers/#radar). "~Aug" = hand-verified typical month, not a promise of the day; "rolling" = posts year-round; "waiting" = not seen in our tracked feeds yet, not a guarantee it isn't out somewhere else._

---

## Hiring timeline

Fresher job postings per week, from each role's real published date — redrawn automatically on every run. When this line takes off, campus season and off-campus drives are in full swing:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/trends-dark.svg">
  <img alt="Fresher jobs posted per week, drawn from real published dates" src="docs/trends-light.svg">
</picture>

## How it stays current

A Python engine reads public company hiring feeds directly, keeps the roles that match the fresher/new-grad scope above, de-duplicates across sources, records each role's published date once (so it never shifts), and regenerates this page through GitHub Actions every 4 hours. It polls every company concurrently (async) with retry/backoff and per-host rate limits. The full source is in this repo.

_Engine (last run): 5,293 companies across 18 ATS platforms · 99% fetch success · completed in 325.5s · median detection latency 655 min · real posted dates on 100% of open roles._

## Platforms Scraped

The engine currently extracts live data from the following platforms:
- **Indian Job Portals:** Naukri (experience=0 / fresher filter), Unstop (off-campus drives + jobs), Internshala, Wellfound
- **Direct ATS (Applicant Tracking Systems):** Greenhouse, Lever, Ashby, SmartRecruiters, Workable, Workday, Breezy, Recruitee, Rippling, Eightfold, Oracle
- **Direct Enterprise & Custom Scrapers:** Amazon (India Jobs), Custom Playwright Scrapers (Flipkart, Swiggy, Razorpay, CRED, InMobi, Rapido, Blinkit, Groww, CARS24, Urban Company, Delhivery)

## Contributing

Adding a company takes one line, see [CONTRIBUTING.md](CONTRIBUTING.md). Suggestions and pull requests are welcome.

## Note on dates

The **Posted** column shows when a role was published, newest at the top. Dates are pulled straight from each job portal. Portals that don't expose a date show a dash (—). Know the real date for a dashed role? Open a PR.

Roles can close at any time — always confirm on the company's own site before applying.
