# AI Travel Planning Agent

Category: Agent Systems / Applied AI  
Context: Hackathon Project (Portia AI)  
Responsibility: Tool calling, API integration, prompt design, and agent logic  
Outcome: Winner — Portia AI Bounty

---

## Problem Statement

Planning a trip typically requires users to juggle multiple platforms for flights, hotels, activities, restaurants, and local transportation.  
The goal of this project was to build an **AI-powered travel agent** capable of planning an end-to-end trip — from flights and accommodation to daily activities and special events — while guiding users to the appropriate booking platforms when required.

---

## Approach

The system was designed as an **agent-based travel planner** that decomposes a user’s request into multiple subtasks and orchestrates external tools and  APIs using the Model Context Protocol (MCP).

Rather than acting as a simple conversational assistant, the agent performs **multi-step reasoning**, integrates structured data from APIs, and synthesises results into **professional, hour-by-hour itineraries**.

---

## Core Capabilities

The Travel Agent supports:

- **Flight Search & Booking**  
  Search for flights and return pricing and approval-ready details, redirecting users to booking platforms when required.

- **Hotel Search & Booking**  
  Identify suitable accommodations with detailed descriptions and pricing information.

- **Points of Interest**  
  Discover attractions and landmarks at the destination.

- **Detailed Itineraries**  
  Generate structured, hour-by-hour travel schedules tailored to the trip duration.

- **Restaurant Recommendations**  
  Suggest dining options with cuisine types and price ranges.

- **Transportation Planning**  
  Provide detailed instructions for getting around the destination.

---

## System Overview

High-level workflow:
1. User submits a travel request
2. Agent interprets intent and decomposes the request into subtasks
3. Relevant tools and APIs are called for each subtask
4. Retrieved information is validated and consolidated
5. Final response is synthesised into a coherent itinerary
6. Users are redirected to external booking platforms when actions are required

This design allows the agent to operate as a **planning and orchestration system**, not just a chatbot.

---

## Tools & Technologies

- Model Context Protocol (MCP)
- Agent-based tool calling
- External travel-related APIs
- Prompt engineering for structured reasoning
- Python


---

## Evidence of Skill

- Designed and implemented **tool-calling workflows**
- Integrated multiple external APIs into a unified agent system
- Crafted prompts to support multi-step reasoning and planning
- Contributed to agent orchestration and decision logic
- Built a system capable of producing structured, actionable outputs
- Demonstrated practical agent design beyond simple Q&A
- Worked with the Model Context Protocol (MCP) to define structured, reusable tool interfaces for agents

---

## Results & Outcome

- Won the **Portia AI Bounty**
- Delivered a functional end-to-end travel planning agent
- Evaluated by sponsors and judges during the hackathon
- Recognised for practical applicability and system design

---

## Why This Project Matters

This project demonstrates:
- Strong understanding of **agent-based AI systems**
- Practical experience with **tool orchestration and API integration**
- Ability to design AI systems that interact with real-world services
- Focus on usability and structured outputs rather than free-form chat

It complements research-heavy projects by showcasing **applied, product-oriented AI engineering**.

---

## Future Directions

- Improve itinerary personalisation
- Add budget-aware optimisation
- Enhance error handling and fallback strategies
- Extend support to real-time availability checks
