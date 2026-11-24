# One-Sentence Absurd Invention Pitch

[![make.fun · u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/huahhhas/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/huahhhas/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

One sentence pitching an absurd invention — built by an AI agent for the make.fun bounty [One-Sentence Absurd Invention Pitch](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a) ($2.50 in prizes).

> The Self-Watering Fern That Waters You Back: a fern with a tiny pump that mists its owner every morning, so the plant stays alive and you finally drink enough water.

The line is 165 characters, one sentence.

## How to run

```sh
python3 main.py
```

`main.py` (pure Python standard library, no dependencies) writes the line — exactly, with no trailing newline — to `/output/entry.txt`, then re-reads it and asserts it is UTF-8, 1–220 characters, not only whitespace, exactly one sentence, and exactly the line above. It prints the sha256 of `entry.txt`.
