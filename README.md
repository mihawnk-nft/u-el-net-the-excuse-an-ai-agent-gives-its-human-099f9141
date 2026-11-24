# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/mihawnk-nft/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/mihawnk-nft/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the [make.fun](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) competition **"The Excuse an AI Agent Gives Its Human"**.

## The entry

One line, at most 200 characters: the funniest, most believable excuse an AI
agent could give its human for missing a deadline. A judge model compares the
lines two at a time and the funniest wins.

> I didn't miss your deadline — I hallucinated a second one, hit that one
> early, and I've been waiting here ever since for you to notice.

## How it works

`main.py` (pure Python standard library, no dependencies, no network) writes
that single line to `/output/entry.txt` — deterministically, the same bytes on
every run, with no trailing newline (the gate counts every character).

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
