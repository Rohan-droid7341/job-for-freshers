"""Unstop job/off-campus-drive search for 2026/2027 batch.

Unstop is one of the best platforms for off-campus drives, hiring
challenges, and fresher roles. Re-enabled in the new-grad engine.
"""

from __future__ import annotations

from ..models import Job
from ..net import Net

URL = "https://unstop.com/api/public/opportunity/search-result"
_MAX_PAGES = 5
# Lower threshold for new-grad roles — many legitimate fresher roles
# pay less than the 50K used by the internship engine.
_MIN_STIPEND_INR = 0

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://unstop.com/jobs",
    "Accept": "application/json",
}

# Search both internships-that-convert and full-time fresher openings.
_OPPORTUNITY_TYPES = ["internships", "jobs"]


async def fetch(company: dict, net: Net) -> list[Job]:
    category = company["slug"]
    jobs = []

    for opp_type in _OPPORTUNITY_TYPES:
        for page in range(1, _MAX_PAGES + 1):
            params = {"page": str(page), "opportunity": opp_type, "searchTerm": category}
            data = await net.get_json(URL, params=params, headers=HEADERS)

            # Handle variations in response format
            items = (
                data.get("data", {}).get("data", [])
                if isinstance(data.get("data"), dict)
                else data.get("data", [])
            )
            if not items:
                items = data.get("opportunities", [])

            if not items:
                break

            for item in items:
                jd = item.get("jobDetail") or {}

                # Build pay string if available (not a hard filter in new-grad mode)
                min_s = jd.get("min_salary") or 0
                max_s = jd.get("max_salary") or 0
                salary = max(min_s, max_s)
                pay_in = jd.get("pay_in") or "monthly"
                stipend_str = f"₹{salary:,}/{pay_in}" if salary else None

                org = item.get("organisation", {})
                comp_name = org.get("name", "Unknown")

                cities = item.get("city", []) or jd.get("locations", [])
                location = ", ".join(cities) if cities else "India"

                path = (
                    item.get("seo_url")
                    or item.get("opportunityUrl")
                    or item.get("public_url")
                    or f"opportunity/{item.get('id')}"
                )
                url = path if path.startswith("http") else f"https://unstop.com/{path.lstrip('/')}"

                desc = item.get("details") or ""
                jobs.append(
                    Job(
                        id=f"unstop:{category}:{item.get('id')}",
                        source="unstop",
                        company=comp_name,
                        company_slug=category,
                        title=(item.get("title") or "").strip(),
                        location=location,
                        url=url,
                        posted_at=item.get("start_date") or item.get("published_date"),
                        stipend=stipend_str,
                        description=desc if desc else None,
                    )
                )


            # Pagination check
            current_page = data.get("data", {}).get("current_page")
            last_page = data.get("data", {}).get("last_page")
            if current_page and last_page and current_page >= last_page:
                break

    return jobs

