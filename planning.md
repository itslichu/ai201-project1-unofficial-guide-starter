# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

--- This project focuses on meal planning and preparation. This project will include information about the aforementioned + cooking skills, nutrition, and food safety recommendations for students and beginner home cooks. This is valuable because information on these topics is scattered across health organization, cooking guides, recipe websites, and online discussions, and it's hard to know where to start and what to keep in mind. 

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
|1| How to Meal Plan: A Complete Beginner's Guide | Explains the fundamentals of meal planning, including setting goals, creating meal schedules, and organizing grocery lists | https://www.healthline.com/health/nutrition/how-to-meal-plan |
|2| Food Safety in Your Kitchen | FDA guide covering safe food handling, cooking, cleaning, and preventing foodborne illness | https://www.fda.gov/food/buy-store-serve-safe-food/food-safety-your-kitchen |
|3| 8 Produce Shopping Mistakes to Avoid, According to Chefs | Provides practical advice for selecting, storing, and purchasing fresh produce while reducing waste | https://www.foodandwine.com/biggest-produce-shopping-mistakes-according-to-chefs-11988097 |
|4| 60 Healthy Meal Prep Ideas | Collection of meal prep recipes and strategies for preparing healthy meals in advance | https://www.loveandlemons.com/healthy-meal-prep-ideas/ |      
|5| Cooking Basics for Beginners | Introduces essential cooking techniques, kitchen tools, and foundational skills for new cooks | https://www.hrcacademy.com/en/blog/cooking-basics-for-beginners/ |
|6| Healthy Weekday Meal Prep for Students | Step-by-step guide showing students how to prepare affordable and healthy meals for an entire week | https://www.instructables.com/Healthy-Weekday-Meal-Prep-for-Students/ |
|7| Healthy Eating Plate | Harvard Nutrition Source guide describing balanced meal composition and evidence-based nutrition recommendations | https://nutritionsource.hsph.harvard.edu/healthy-eating-plate/ |
|8| Are You Storing Food Safely? | FDA resource explaining proper food storage practices, refrigerator organization, and food preservation | https://www.fda.gov/consumers/consumer-updates/are-you-storing-food-safely |
|9| How Do You Actually Learn to Cook? | Reddit discussion where users share personal experiences, advice, and strategies for developing cooking skills | https://www.reddit.com/r/Cooking/comments/xfqokr/how_do_you_actually_learn_to_cook/ |
|10| People Who Meal Prep Their Food Don't Save Time | Reddit discussion presenting opinions and experiences about the benefits and drawbacks of meal prepping | https://www.reddit.com/r/unpopularopinion/comments/1nqrrmc/people_who_meal_prep_their_food_dont_save_time/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
800 characters

**Overlap:**
100 characters

**Reasoning:**
Use Recursive strategy, because the outputs have different structures from long informational articles, recipe/meal guides and tutorials to Reddit discussion threads. 800 character maximum should be large enough to preserve context within a section, while the 100 overal prevents information loss

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2 from sentence-transformers

**Top-k:**
Retrieve top 4 most relevant chunks. This is because the corpus contains only ten source documents, each touching upong a different topic around meal planning, so having 4 will allow the system to combine information from multiple sources to deliver a comprehensive answer

**Production tradeoff reflection:**
This model is lightweight and fast to run locally, which is suitable for a small project. The subsequent tradeoffs include retrieval accuracy, multilingual support (in case sources or user queries are multilingual), context length, and latency. A larger model could better capture subtle relationships between meal prep concepts. However, larger models would require more computational resources and increase response times. 
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What are the basic steps involved in creating a meal plan? | A meal plan should begin with identifying goals and dietary needs, selecting meals for the week, creating a grocery list, and preparing ingredients in advance |
| 2 | What should a balanced meal consist of? | A balanced meal should emphasize vegetables and fruits, include whole grains, contain healthy protein sources, and use healthy oils while limiting sugary drinks |
| 3 | What food safety practices should be followed when preparing meals in advance? | Food should be cooked to safe temperatures, refrigerated promptly, stored in appropriate containers, and handled using clean utensils and surfaces to prevent contamination |
| 4 | What advice is given to beginners who want to learn how to cook? | Beginners should start with simple recipes, practice basic cooking techniques, cook regularly, learn from mistakes, and gradually expand their skills and recipe repertoire |
| 5 | What are some common benefits and criticisms of meal prepping? | Benefits include saving time during the week, reducing food waste, supporting healthy eating habits, and controlling portions. Criticisms include spending significant time preparing food upfront, eating repetitive meals, and concerns that meal prepping may not save time for everyone |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Noisy or inconsistent information across sources
The sources include both authorative sources and user-generated discussions, which could provide conflicting advice or opinions.

2. Missing or unclear source attribution
When information from multiple retrieved chunks is combined into a single answer, it might be difficult to identify which source contributed what, to allow users to verify recommendations and distinguish between expert guidance and community opinions.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
I will give ChatGPT my Chunking Strategy section and ask it to help me implement code for loading source documents and chunking. I will verify output manually by checking resulting chunk size and overlap.

**Milestone 4 — Embedding and retrieval:**
I will give ChatGPT my Retrieval Approach section and ask it to generate code for creating embeddings and retrieving the top 5 most relevant chunks.  

**Milestone 5 — Generation and interface:**
I will use ChatGPT to generate code for a question-answering interface with constructed RAG pipeline. I will manually verify the output by comparing responses to the expected answers in my evaluation plan.
