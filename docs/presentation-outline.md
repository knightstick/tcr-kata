# Presentation Outline

## Overview
- Duration: 5 minutes
- Audience: Work colleagues
- Topic: A quirky side project exploring Claude Code and TCR
- Presenters: Chris Jewell & Claude
- Vibe: Casual, fun, "here's a weird thing I tried"

## Structure

### Slide 1: Title
- "Experimenting with Claude Code"
- Subtitle: A TCR Kata Adventure
- Chris Jewell & Claude, 10th July 2025

### Slide 2: "So I heard about this weird thing called TCR..."
- Kent Beck experiment (mention the legend!)
- Test && Commit || Revert
- "What happens if you can NEVER have broken code?"
- Originally for tiny steps, pair programming

### Slide 3: "Then I saw this Anthropic talk about Claude Code..."
- They said: "Give Claude Code tools to gather feedback"
- Make it observable - let it see what works and what doesn't
- I thought: "What's the ULTIMATE feedback loop?"
- TCR! Every few minutes: pass/fail, commit/revert
- Perfect experiment for human + AI pair programming

### Slide 4: GitHub Walkthrough - "The TCR Flow in Action"
- Show commit history: https://github.com/knightstick/tcr-kata/commits/main
- Scroll through the TCR rhythm: "TCR: 15:32:13", "TCR: 15:38:41", etc.
- Point out: Look at all those tiny automated commits!
- Show specific commits: file & memory repos, then SQLite repo
- Demonstrate the pattern: small change → test → commit → repeat

### Slide 5: "Plot twist: The AI actually gets better with feedback"
- Claude Code learns from our back-and-forth
- When I tell it "that didn't work", it adjusts
- CLAUDE.md file = giving the AI context
- The more we interact, the better it gets

### Slide 6: "TCR: Brilliantly impractical?"
- Forces you to think: "What do I ACTUALLY know works?"
- Tiny steps = less risk
- But realistically? Probably not for production
- Great for learning though!

### Slide 7: "Your turn to experiment"
- Try Claude Code on something small
- Give it feedback when it messes up
- Share what you learn
- AI tools are moving fast - jump in!

### Demo (Optional - if we have time)
- Quick run through of the todo CLI
- Show the TCR script in action
- Maybe a failed test → revert example
- "Here's what we built together"

## Key Messages
- You should be experimenting with Claude Code
- Giving an AI ways of getting feedback makes these tools better
- TCR is a fun thought experiment that helps you think about what you know for sure, but not sure about production use

## Notes
- Keep each slide focused and minimal
- Use bullet points, not paragraphs
- Practice timing - aim for ~45 seconds per slide