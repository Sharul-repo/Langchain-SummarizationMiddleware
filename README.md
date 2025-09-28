# 🚀Langchain SummarizationMiddleware (LangChain 1.0 alpha)

If you've been building AI agents, you know the pain:
Every time your agent calls the LLM, it sends the entire conversation history for context. Great for continuity — terrible for cost and latency. 

---

🔥 Enter LangGraph Summarization Middleware

It lets you define exactly when to summarize (max_tokens_before_summary), how much recent memory to retain (messages_to_keep), and how summaries are generated (summary_prompt), all powered by a smaller, cheaper model (model="openai:gpt-4o-mini").

That means full context... without full cost.

---
🆚 Old Way vs New Way — The Difference Is Massive

Context handling: Previously, every single message was sent; now only summaries + recent messages are sent.

Token usage: Previously grew with every message; now it’s bounded and optimized.

Cost: Previously exploded over long conversations; now predictable and significantly lower.

Latency: Previously slower due to huge context; now lightweight and faster.

Control: Previously none; now full control over when and how context is retained.
---

💡 Why this matters

Most AI agents today are brute force:

“Here’s everything we’ve ever talked about. Good luck.”

With LangGraph Middleware, agents become strategic:

“Here’s only what’s relevant — the rest is efficiently summarized.”

Smarter context. Lower latency. Lower cost.
This unlocks scalable, long-running, and enterprise-grade AI agents.
---


