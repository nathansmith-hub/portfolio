# AI Agent

[< Back Home](/)

![Prompts image](/images/Prompts-cropped.png)

## Overview

[AI Agent](https://en.wikipedia.org/wiki/AI_agent) is an LLM-powered command-line tool that can read, update, and run Python code autonomously using the Gemini API. It was my third [Boot.dev](https://www.boot.dev/courses/build-ai-agent-python) project and explores how large language models can be used as the basis for agentic coding tools, where the model doesn't just respond but takes actions across a codebase.

## How It Was Built

The tool is built in Python and connects to Google's Gemini API. It uses a loop where the model is given a task, selects from a set of available functions, executes them, and feeds the results back into the next iteration. The available functions allow the agent to read files, write files, and execute Python scripts across multiple directories.

### To Do:

- Investigate and fix compatibility with the current Gemini API, which has changed since the project was completed
- Explore swapping or adding support for other LLM providers
- Extend the set of available functions the agent can call

**GitHub**: [https://github.com/nathansmith-hub/ai-agent](https://github.com/nathansmith-hub/ai-agent)