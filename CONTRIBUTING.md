# Contributing

Three ways to help, from easiest to most involved.

## 1. Review items (no code, about 20 minutes)

You read Hindi or Telugu? Open the [review page](https://venumadhav7484.github.io/hinglish-toolbench/review.html) (or `docs/review.html` locally), load a language, and for each request choose:

- **✓ Sounds natural**
- **✎ Rewrite**: type how you would actually say it
- **✗ Wrong meaning**: the request doesn't match the expected call

Export the file and open a PR adding it as `data/reviews/<your-name>.jsonl`, or attach it to an issue. Terminal users can run `uv run htb review --reviewer <you> --variant te_latn` instead.

A rejected item drops its whole scenario, in all 5 languages, so every comparison stays paired.

## 2. Add a model

See [SUBMITTING.md](SUBMITTING.md). CI re-scores your raw outputs.

## 3. Change the harness or the data

- `uv run pytest -q && uv run htb validate && uv run htb verify` must pass.
- A change to scoring must come with a test in `tests/test_score.py`, and every committed run must be re-scored (`htb score`, then `htb leaderboard`).
- A change to the data creates a new version (`data/v2`). Never edit `data/v1` in place: the leaderboard is tied to its sha256.
