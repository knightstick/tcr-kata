# TCR (Test && Commit || Revert) - Reference

## Overview
TCR is a software development practice where developers run tests, and:
- If tests pass, the code is automatically committed
- If tests fail, the code is automatically reverted to the last working state

## Origin
Originated from an experiment by Lars Barlindhaug, Oddmund Strømme, Ole Johannessen, and Kent Beck.

## Key Characteristics
1. Forces developers to write code in extremely small, incremental steps
2. Designed to challenge developers to work in smaller, more manageable chunks
3. Provides immediate feedback on code changes

## Benefits
- Encourages writing code in tiny increments
- Provides immediate feedback on code changes
- Increases test coverage
- Makes continuous integration more effective
- Supports remote pair/mob programming
- Helps developers recognize their fatigue levels

## Basic Implementation
- Basic command: `<test command> && git commit -am "TCR" || git restore`
- Can be implemented via a simple script
- Multiple open-source tools exist to facilitate TCR

## Practitioner Reports
- Makes practice sessions more enjoyable
- Improves sustainable work pace
- Provides rapid feedback on code quality

## Recommended Approach
- Start practicing on coding katas
- Use open-source TCR tools
- Gradually integrate into production work, starting with refactoring phases

## Key Insight
The practice challenges developers to be more precise, disciplined, and conscious of their coding process.

---

*Source: InfoQ article "How Practicing TCR (Test && Commit || Revert) Reduces Batch Size"*
*Original Medium article by Kent Beck (paywalled): https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864*