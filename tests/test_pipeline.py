from datetime import UTC

from intern_engine.pipeline import _detection_latency, _parse_iso


class TestParseIso:
    def test_z_suffix_is_utc_aware(self):
        dt = _parse_iso("2026-07-15T21:00:00Z")
        assert dt.tzinfo is not None
        assert dt.utcoffset().total_seconds() == 0

    def test_naive_and_date_only_assumed_utc(self):
        # Some ATS feeds ship timestamps with no offset (or a bare date);
        # they must come back aware or datetime arithmetic explodes.
        for raw in ("2026-07-15T18:00:00", "2026-07-15"):
            dt = _parse_iso(raw)
            assert dt.tzinfo is UTC

    def test_offset_normalized_to_utc(self):
        dt = _parse_iso("2026-07-15T14:00:00-04:00")
        assert dt.hour == 18
        assert dt.tzinfo is not None

    def test_garbage_is_none(self):
        assert _parse_iso("not a date") is None
        assert _parse_iso(None) is None


class TestDetectionLatency:
    def test_mixed_naive_and_aware_does_not_crash(self):
        # Regression: a single offset-less posted_at next to a Z-suffixed
        # first_seen_at crashed every run with TypeError (2026-07-15 outage).
        existing = {
            "a": {
                "posted_at": "2026-07-15T18:00:00",  # naive from the ATS
                "first_seen_at": "2026-07-15T21:00:00Z",
            },
            "b": {"posted_at": "2026-07-15T10:00:00Z", "first_seen_at": "2026-07-15T11:00:00Z"},
        }
        out = _detection_latency(existing)
        assert out["sample_size"] == 2
        assert out["median_minutes"] == 120.0  # median of 180 and 60

    def test_empty_store(self):
        out = _detection_latency({})
        assert out == {"median_minutes": None, "sample_size": 0, "window_days": 7}

    def test_old_backfills_outside_window_excluded(self):
        existing = {
            "old": {"posted_at": "2026-01-01T00:00:00Z", "first_seen_at": "2026-07-15T00:00:00Z"},
        }
        assert _detection_latency(existing)["sample_size"] == 0


class TestStickyBatch:
    """A batch label already on record wins over re-derivation (_keep_matching)."""

    CFG = {
        "target_batches": ["2026", "2027"],
        "regions": ["India", "Remote"],
        "role_scope": "tech",
    }

    def _results(self, title="Associate Software Engineer", location="Bangalore, India"):
        from datetime import UTC, datetime

        from intern_engine.models import Job
        job = Job(
            id="greenhouse:acme:1",
            source="greenhouse",
            company="Acme",
            company_slug="acme",
            title=title,
            location=location,
            url="https://x",
            posted_at=datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
        return [{"ats": "greenhouse", "slug": "acme", "name": "Acme"}, [job], None]

    def _results_list(self, title="Associate Software Engineer", location="Bangalore, India"):
        return [self._results(title, location)]

    def _keep(self, results, existing=None):
        from intern_engine.pipeline import _keep_matching
        kept, *_ = _keep_matching(results, self.CFG, {}, existing or {})
        return kept

    def test_fresher_title_is_kept(self):
        kept = self._keep(self._results_list())
        assert len(kept) == 1
        assert kept[0].season == "new_grad"

    def test_explicit_batch_year_in_description_is_kept(self):
        from datetime import UTC, datetime

        from intern_engine.models import Job
        job = Job(
            id="naukri:tcs:1",
            source="naukri",
            company="TCS",
            company_slug="tcs",
            title="Software Developer",
            location="Chennai, India",
            url="https://x",
            posted_at=datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
            description="Eligible batch: 2026. B.Tech CSE.",
        )
        results = [({"ats": "naukri", "slug": "tcs", "name": "TCS"}, [job], None)]
        kept = self._keep(results)
        assert len(kept) == 1
        assert kept[0].season == "2026"

    def test_sticky_batch_from_store_is_reused(self):
        # Job was already tagged "2026" from description last run; no description this run.
        from datetime import UTC, datetime

        from intern_engine.models import Job
        job = Job(
            id="greenhouse:acme:1",
            source="greenhouse",
            company="Acme",
            company_slug="acme",
            title="Software Developer",  # no fresher signal in title alone
            location="Bangalore, India",
            url="https://x",
            posted_at=datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
        existing = {"greenhouse:acme:1": {"season": "2026", "season_inferred": False}}
        results = [({"ats": "greenhouse", "slug": "acme", "name": "Acme"}, [job], None)]
        kept = self._keep(results, existing)
        assert len(kept) == 1
        assert kept[0].season == "2026"

    def test_senior_role_is_dropped(self):
        kept = self._keep(self._results_list("Senior Software Engineer"))
        assert kept == []

    def test_stale_undated_non_fresher_dropped(self):
        from intern_engine.models import Job
        job = Job(
            id="greenhouse:acme:2",
            source="greenhouse",
            company="Acme",
            company_slug="acme",
            title="Software Engineer",  # no fresher signal
            location="Bangalore, India",
            url="https://x",
        )
        results = [({"ats": "greenhouse", "slug": "acme", "name": "Acme"}, [job], None)]
        assert self._keep(results) == []


class TestRegionConfig:
    """regions config must be honored end-to-end (India+Remote is the new default)."""

    def _results(self, location):
        from datetime import UTC, datetime

        from intern_engine.models import Job
        job = Job(
            id="greenhouse:acme:1",
            source="greenhouse",
            company="Acme",
            company_slug="acme",
            title="Associate Software Engineer",  # passes both is_tech() and detect_new_grad()

            location=location,
            url="https://x",
            posted_at=datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        )
        return [({"ats": "greenhouse", "slug": "acme", "name": "Acme"}, [job], None)]

    def _keep(self, results, regions):
        from intern_engine.pipeline import _keep_matching
        cfg = {"target_batches": ["2026", "2027"], "regions": regions, "role_scope": "tech"}
        kept, *_ = _keep_matching(results, cfg, {}, {})
        return kept

    def test_india_only_keeps_india(self):
        kept = self._keep(self._results("Bangalore, Karnataka, India"), ["India"])
        assert len(kept) == 1

    def test_india_only_drops_us(self):
        assert self._keep(self._results("New York, NY"), ["India"]) == []

    def test_india_and_remote_keeps_india(self):
        kept = self._keep(self._results("Mumbai, India"), ["India", "Remote"])
        assert len(kept) == 1

    def test_india_and_remote_keeps_worldwide_remote(self):
        kept = self._keep(self._results("Worldwide Remote"), ["India", "Remote"])
        assert len(kept) == 1



