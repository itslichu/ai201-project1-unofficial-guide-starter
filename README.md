# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

--- This project focuses on meal planning and preparation. This project will include information about the aforementioned + cooking skills, nutrition, and food safety recommendations for students and beginner home cooks. This is valuable because information on these topics is scattered across health organization, cooking guides, recipe websites, and online discussions, and it's hard to know where to start and what to keep in mind. 

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
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

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 800 Characters

**Overlap:** 100 Characters

**Why these choices fit your documents:**
Using Recursive strategy, because the outputs have different structures from long informational articles, recipe/meal guides and tutorials to Reddit discussion threads. 800 character maximum should be large enough to preserve context within a section, while the 100 overal prevents information loss

**Final chunk count:**
Total chunks created: 130
Average chunk length: 598.02 characters

**Sample chunks**

Chunk 1: Breakfast Egg Muffins\nStore these egg and veggie muffins in the fridge for up to 3 days for a quick, healthy breakfast.\nOatmeal Breakfast Cookies\nI love starting my day with one of these soft, nourishing breakfast cookies. They keep well at room temperature for a few days, and they freeze perfectly for up to 3 months!\nHomemade Granola\nServe it with your favorite yogurt or a splash ofalmond milkand fresh fruit.\nHealthy banana bread\nStore it at room temperature for up to 3 days. After that, freeze slices to have on hand for busy mornings. ~30 seconds in the microwave are all it takes to thaw a piece of this moist, warmly-spiced bread.\nVegan Breakfast Burrito",
Source: 60 Healthy Meal Prep Ideas

Chunk 2:These food storage tips can help you steer clear of foodborne illnesses.\nStorage Basics\n* Refrigerate or freeze perishables right away.Foods that require refrigeration should be put in the refrigerator as soon as you get them home. Stick to the \"two-hour rule\" for leaving items needing refrigeration out at room temperature. Never allow meat, poultry, seafood, eggs, or produce or other foods that require refrigeration to sit at room temperature for more than two hoursone hour if the air temperature is above 90 F. This also applies to items such as leftovers, \"doggie bags,\" and take-out foods. Also, when putting food away, don't crowd the refrigerator or freezer so tightly that air can't circulate.",
Source: Are you storing your food safely?

Chunk 3: Buying pre-cut vegetables\nMost grocery stores have a wall of prepared produce options, such as already-diced mirepoix, sliced stir-fry vegetables, and spiralized zucchini. When youre pressed for time, the convenience of these products is obvious. However, Bill Peet, executive chef ofTavern On the Greenin New York Citys Central Park, warns that \"One mistake I see all the time is people buying pre-cut or pre-prepared vegetables for convenience. They may look nice, but most of the time theyre much more expensive, sometimes three or four times the price, and theyre not as fresh or ripe as whole produce.\"\nUnderestimating what youll find at the farmers market",
Source: Biggest Produce Shopping Mistakes

Chunk 4: Essential kitchen tools every beginner cook needs\nBefore you start cooking, you need the right tools. You dont need a fully stocked kitchen, but having a fewessential itemswill make cooking easier and more efficient.\nKnives and cutting boards\n* Chefs knife. The most versatile knife. Use it for chopping, slicing, and dicing.\n* Paring knife.Useful for peeling and cutting small ingredients.\n* Serrated knife.Best for slicing bread and soft foods like tomatoes.\nAwood or plastic cutting boardis necessary for a safe chopping surface. Avoid glass or stone boards because they dull knives quickly. Always clean your board properly to prevent bacteria buildup.\nPots and pans\nYou only need a fewbasic cookware piecesto start:",
Source: Cooking Basics for Beginners

Chunk 5: - Place meat, poultry, seafood, and eggs in plastic bags at checkout\n- Keep produce and other ready-to-eat foods in a separate area of the refrigerator from meat, poultry, seafood, and eggs\n- Refrigerate food within 2 hours of grocery shopping, or 1 hour if kept in air temperatures above 90 degrees Fahrenheit\n- Set refrigerator temperature to 40 degrees Fahrenheit or below and freezer at 0 or below \n- Defrost food in the refrigerator, in cold water, or in the microwave and cook immediately\nDont:\n- Choose meat, poultry, or seafood in damaged or leaking packaging\n- Buy eggs with cracked shells or damaged cartons\n- Remove eggs from carton or keep them in the refrigerator door\n- Place raw meat, poultry, or seafood on upper shelves of the refrigerator where they can drip onto other foods",
Source: Food Safety in Your Kitchen

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
all-MiniLM-L6-v2 from sentence-transformers
because it is lightweight, high-performing embedding model that can run locally without requiring an API key or paid service but still sufficiently retrieve relevant information to capture semantic meaning. I believe this is suitable for a small project.

**Production tradeoff reflection:**
Since this model is lightweight and fast to run locally, the subsequent tradeoffs include retrieval accuracy, multilingual support (in case sources or user queries are multilingual), context length, and latency. A larger model could better capture subtle relationships between meal prep concepts. However, larger models would require more computational resources and increase response times. 
---

Retrieval Test Results:

Example 1: 

All three except the last one show relevant chunks to answer the question. However not all information from the relevant documents is included despite the last irrelevant being included -> missing context when chunking leading to higher distance scoring.

QUERY:
What food safety practices should be followed when preparing meals in advance?
================================================================================

Result #1 --> directly contains info to answer the question
Source: Food Safety in Your Kitchen.txt
Title: Food Safety in Your Kitchen
Chunk Position: 75
Distance Score: 0.5430

Chunk Text:
----------------------------------------
Food Safety in Your Kitchen
FDA (March 2018)
When you prepare meals and snacks for yourself, your family, and your friends, it is important to follow simple food safety tips to help prevent foodborne illness, also known as food poisoning. Whether you are a home cook, a professional chef, or a recipe writer, there are some easy steps you can take to help keep your food safe all the way from the grocery store tothe kitchen table.
Remember that food safety starts at the grocery store. Check out these lists of DOs and DONTs to help keep food safe from the grocery cart to the refrigerator.
Food Safe Shopping, Storage and Meal Prep
Do:
- Keep Produce separate from meat, poultry, seafood, and eggs
...
----------------------------------------

Result #2 -> also directly answers the question
Source: Are you storing your food safely.txt
Title: Are you storing your food safely
Chunk Position: 20
Distance Score: 0.7499

Chunk Text:
----------------------------------------
* Use ready-to-eat foods as soon as possible.Refrigerated ready-to-eat foods such as luncheon meats should be used as soon as possible. The longer they're stored in the refrigerator, the more chanceListeria, a bacterium that causes foodborne illness, can grow, especially if the refrigerator temperature is above 40 F (4 C).
* Be alert for spoiled food.Anything that looks or smells suspicious should be thrown out. Mold is a sign of spoilage. It can grow even under refrigeration. Mold is not a major health threat, but it can make food unappetizing. The safest practice is to discard food that is moldy.
----------------------------------------

Result #3 -> also directly answers the question
Source: Are you storing your food safely.txt
Title: Are you storing your food safely
Chunk Position: 21
Distance Score: 0.8027

Chunk Text:
----------------------------------------
* Be aware that food can make you very sick even when it doesn't look, smell, or taste spoiled.That's because foodborne illnesses are caused by pathogenic bacteria, which are different from the spoilage bacteria that make foods "go bad." Many pathogenic organisms are present in raw or undercooked meat, poultry, seafood, milk, and eggs; unclean water; and on fruits and vegetables. Keeping these foods properly chilled will slow the growth of bacteria.
* Following the other recommended food handling practiceswill further reduce your risk of getting sick clean your hands, surfaces and produce, separate raw foods from ready-to-eat foods, and cook to safe temperatures.
Refrigeration Tips
----------------------------------------

Result #4 -> not quite relevant to the question 
Source: 60 Healthy Meal Prep Ideas.txt
Title: 60 Healthy Meal Prep Ideas
Chunk Position: 14
Distance Score: 0.8143

Chunk Text:
----------------------------------------
Basic Healthy Meal Prep Ideas
Up to this point, Ive shared healthy meal prep recipes for complete dishes. But one of my favorite ways to meal prep is actually by preparingcomponents not full recipes that I can use in a variety of ways throughout the week.A pot of rice,baked tofu, a flavorful sauce
I recommend this method if you dont want to eat the exact same thing every day of the week. Here are some of my favorite components to prepare, along with my go-to ways to use them:
Whole Grains
Perfect for bulking up grain bowls and salads, serving with curries and stir-fries, or tossing into fried rice. These grains are the ones I meal prep most often:
* Quinoa
* Farro
* Wheat Berries
* Brown Ric
...
----------------------------------------

Example 2:

QUERY:
What advice is given to beginners who want to learn how to cook?
================================================================================
All the retrieved chunks are relevant to answer the question

Result #1
Source: Reddit Learning to Cook.txt
Title: Reddit Learning to Cook
Chunk Position: 119
Distance Score: 0.3708

Chunk Text:
----------------------------------------
Learning to cook (Reddit)
TITLE: How do you actually LEARN to cook?

ORIGINAL POST SUMMARY:

The discussion begins with a frustrated home cook who feels stuck following recipes without understanding why certain techniques work. The poster explains that many of their meals turn out poorly and that recipes often assume knowledge they do not have. They want to understand concepts such as seasoning, browning, cooking temperatures, texture, and how to identify what went wrong when a dish tastes bad. Rather than simply collecting more recipes, they are looking for ways to build foundational cooking knowledge and intuition.

KEY THEMES FROM THE DISCUSSION:

Learning by Practice
----------------------------------------

Result #2
Source: Reddit Learning to Cook.txt
Title: Reddit Learning to Cook
Chunk Position: 120
Distance Score: 0.3980

Chunk Text:
----------------------------------------
KEY THEMES FROM THE DISCUSSION:

Learning by Practice

Many participants emphasize that cooking is a practical skill that improves through repetition. Commenters note that mistakes are an important part of learning and that even experienced cooks frequently make errors. Several people recommend choosing a small number of simple dishes and preparing them repeatedly until the techniques become familiar.

Start Simple

A common recommendation is to avoid complicated recipes and instead focus on mastering basic foods. Examples include eggs, rice, roasted vegetables, pasta dishes, soups, and simple chicken recipes. These dishes help beginners learn core techniques such as heat control, seasoning,
...
----------------------------------------

Result #3
Source: Cooking Basics for Beginners.txt
Title: Cooking Basics for Beginners
Chunk Position: 43
Distance Score: 0.5345

Chunk Text:
----------------------------------------
Cooking Basics for Beginners: Learn How to Cook
Updated on 27/02/2025 by Yovelina Minkova
If you want to learn how to cook, the first step is understanding the basics. Many beginners think that memorizing recipes will teach them how to cook, but thats not the case. Recipes give instructions for specific dishes, but they dont explain why certain ingredients behave the way they do or how different cooking methods affect food. Without this knowledge, youll struggle to cook without following step-by-step directions.
----------------------------------------

Result #4
Source: Cooking Basics for Beginners.txt
Title: Cooking Basics for Beginners
Chunk Position: 44
Distance Score: 0.6251

Chunk Text:
----------------------------------------
This guide focuses oncore cooking techniquesrather than individual recipes. Youll learn how to handle ingredients, control heat, and use different cooking methods. By understanding these basics, youll be able to cook confidently, adjust dishes to your taste, and fix mistakes when they happen.
Table of Contents
* Essential kitchen tools every beginner cook needs
* Learning about the heat and cooking techniques
* Building your knife skills
* How to season food and develop flavor
* The next steps to improve your cooking skills

Example 3:

QUERY:
What are the basic steps involved in creating a meal plan?
================================================================================

Result #1
Source: How to Meal Plan.txt
Title: How to Meal Plan
Chunk Position: 112
Distance Score: 0.5225

Chunk Text:
----------------------------------------
Ahead, well share our top tips and resources for how to meal plan, including a step-by-step meal planning routine and tips and tricks for budget and family meal planning
How to meal plan for beginners
One of the best things about meal planning is that even if you think youve never meal planned before, you probably already have. After all, meal planning just means planning out your meals ? whether thats dinner for the evening or lunch for the work week ahead.
But theres a difference between planning a meal here and there and actually incorporating meal planning into your routine. So, if youre ready to meal plan regularly, heres a step-by-step guide on how to meal plan.
Step 1 | Figure out a p
...
----------------------------------------

Result #2
Source: How to Meal Plan.txt
Title: How to Meal Plan
Chunk Position: 114
Distance Score: 0.5684

Chunk Text:
----------------------------------------
Step 3 | Pick a few recipes
Once you know how many days you want to meal plan for and which meals youre including in your plan, the next step is to choose your recipes. If your plan is only for a few days or meals, you can experiment with recipes ? but for bigger meal plans, aim to keep it simple.
Step 4 | Make a grocery list
Now that you have all of your recipes planned out ahead of time, you can save even more time by planning out your grocery list, too. And as youre planning out your shopping list, dont forget to mark off any ingredients you already have at home.
Step 5 | Shop, prep, and store
----------------------------------------

Result #3
Source: How to Meal Plan.txt
Title: How to Meal Plan
Chunk Position: 113
Distance Score: 0.5719

Chunk Text:
----------------------------------------
Step 1 | Figure out a plan
Before you jump into creating your first meal plan, think about what you want to get out of meal planning. Is your goal to get more nutritious food on your plate, or do you just want to spend less on groceries? When you have a goal in mind, meal planning is much easier.
Step 2 | Note what you have
As you get a better idea of what you want to meal plan, consider using ingredients you already have at home as the inspiration for your recipes. Frozen ingredients, leftovers, and pantry staples are a great place to start if you want to keep grocery costs low.
Step 3 | Pick a few recipes
----------------------------------------

Result #4
Source: How to Meal Plan.txt
Title: How to Meal Plan
Chunk Position: 118
Distance Score: 0.5790

Chunk Text:
----------------------------------------
* Get the entire family involved in the meal planning process by asking for help with tasks like planning recipes, grocery shopping, and cooking.
Takeaway
If one of your goals is to spend less time and energy deciding what to cook and eat every day, meal planning can help you meet that goal. Even if youve never meal planned before, all it takes is a little time and effort and you can have your meals planned out and ready to go for the day, week, or even month.   
----------------------------------------

----------------------------------------

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
The system uses a strict prompt that tells the model to answer only from the retrieved context:

"Answer the user's question using ONLY the information contained in the provided context. Do NOT use outside knowledge. If the context does not contain enough information to answer the question, respond exactly: 'I don't have enough information on that.'"

Also, the system only passes the top 4 retrieved chunks, concatenated into a context block and supplied with user's question to prevent irrelevant information / information overload.

The system was also tested with an out-of-domain question ("What are the best restaurants in New York City?"), where the expected response is "I don't have enough information on that."

**How source attribution is surfaced in the response:**

Source attribution is handled programmatically. After retrieval, the system extracts the source filenames stored in the metadata of each chunk used during retrieval. These sources are then displayed separately in the Gradio interface under a dedicated "Sources" section. 

**Examples**

QUESTION:
What food safety practices should be followed when preparing meals in advance?

ANSWER:
To follow food safety practices when preparing meals in advance, you should:
- Keep Produce separate from meat, poultry, seafood, and eggs in shopping carts and bags
- Place meat, poultry, seafood, and eggs in plastic bags at checkout
- Use ready-to-eat foods as soon as possible
- Be alert for spoiled food and discard anything that looks or smells suspicious, including moldy food
- Keep foods properly chilled to slow the growth of bacteria
- Follow other recommended food handling practices, including cleaning your hands, surfaces, and produce, separating raw foods from ready-to-eat foods, and cooking to safe temperatures.

SOURCES:
- Food Safety in Your Kitchen.txt
- Are you storing your food safely.txt
- 60 Healthy Meal Prep Ideas.txt

--------------------------------------------------------------------------------

QUESTION:
What advice is given to beginners who want to learn how to cook?

ANSWER:
The advice given to beginners who want to learn how to cook is to start simple, focus on mastering basic foods such as eggs, rice, and simple chicken recipes, and to understand core cooking techniques rather than just memorizing recipes. Additionally, it is recommended to learn by practice, repeating simple dishes until the techniques become familiar, and to not be afraid of making mistakes, as they are an important part of the learning process.

SOURCES:
- Reddit Learning to Cook.txt
- Cooking Basics for Beginners.txt

--------------------------------------------------------------------------------

QUESTION:
What are the best restaurants in New York City?

ANSWER:
I don't have enough information on that.

SOURCES:
- Biggest Produce Shopping Mistakes.txt
- 60 Healthy Meal Prep Ideas.txt
- Cooking Basics for Beginners.txt

## Query Interface
Input: user query -> Ask Button -> Output: generated answer + sources

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
1. What are the basic steps involved in creating a meal plan?

Expected: A meal plan should begin with identifying goals and dietary needs, selecting meals for the week, creating a grocery list, and preparing ingredients in advance

System: The basic steps involved in creating a meal plan are:

1. Figure out a plan
2. Note what you have
3. Pick a few recipes
4. Make a grocery list
5. Shop, prep, and store 

These steps are part of a step-by-step meal planning routine.

How to Meal Plan.txt

Retrieval: Relevant | Accuracy: Accurate

2. What should a balanced meal consist of?

Expected: A balanced meal should emphasize vegetables and fruits, include whole grains, contain healthy protein sources, and use healthy oils while limiting sugary drinks

System: A balanced meal should consist of a grain, a protein, and some vegetables.

Healthy Eating Plate.txt
Healthy Weekday Meal Prep for Students.txt

Retrieval: Relevant | Accuracy: Partially Accurate (but not detailed enough, potentially because chunking may have split related information across multiple chunks and the other chunks weren't ranked highly enough)

3. What food safety practices should be followed when preparing meals in advance?

Expected: Food should be cooked to safe temperatures, refrigerated promptly, stored in appropriate containers, and handled using clean utensils and surfaces to prevent contamination

System: To follow food safety practices when preparing meals in advance, you should: 
- Keep Produce separate from meat, poultry, seafood, and eggs in shopping carts and bags
- Place meat, poultry, seafood, and eggs in plastic bags at checkout
- Use ready-to-eat foods as soon as possible
- Be alert for spoiled food and discard anything that looks or smells suspicious, including moldy food
- Keep foods properly chilled to slow the growth of bacteria
- Follow other recommended food handling practices, including cleaning your hands, surfaces, and produce, separating raw foods from ready-to-eat foods, and cooking to safe temperatures.

Food Safety in Your Kitchen.txt
Are you storing your food safely.txt
60 Healthy Meal Prep Ideas.txt

Retrieval: Partially Relevant (60 Healthy Meal Prep irrelevant but might be because relevant documents were too short, so their chunks weren't enough to satisfy top 4) | Accuracy: Accurate

4. What advice is given to beginners who want to learn how to cook? 

Expected: Beginners should start with simple recipes, practice basic cooking techniques, cook regularly, learn from mistakes, and gradually expand their skills and recipe repertoire

System: The advice given to beginners who want to learn how to cook is to start simple, focus on mastering basic foods such as eggs, rice, and simple chicken recipes, and to understand core cooking techniques rather than just memorizing recipes. Additionally, many participants recommend learning by practice, choosing a small number of simple dishes and preparing them repeatedly until the techniques become familiar. It's also emphasized that mistakes are an important part of learning and that understanding the basics, such as handling ingredients, controlling heat, and using different cooking methods, is key to cooking confidently and being able to adjust dishes to your taste.

Reddit Learning to Cook.txt
Cooking Basics for Beginners.txt

Retrieval: Relevant | Accuracy: Accurate

5. What are some common benefits and criticisms of meal prepping?

Expected: Benefits include saving time during the week, reducing food waste, supporting healthy eating habits, and controlling portions. Criticisms include spending significant time preparing food upfront, eating repetitive meals, and concerns that meal prepping may not save time for everyone

System: Some common benefits of meal prepping include time savings, convenience, health benefits, and cost reduction. It can support healthier eating habits, reduce decision fatigue, and make it easier to eat regularly, especially during busy schedules. Additionally, meal prep can help control calorie intake, monitor protein consumption, and reduce food spending by buying ingredients in bulk and avoiding restaurant meals.

On the other hand, some common criticisms of meal prepping include concerns about food quality and repetition. Preparing large amounts of food in advance can result in repetitive meals and leftovers that become less appealing over time. Some people also question whether the time spent on meal prep is truly efficient.

Reddit Meal Prep Opinions.txt

Retrieval: Relevant | Accuracy: Accurate

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Failure Case:** What should a balanced meal consist of?

**Expected Answer:** A balanced meal should emphasize vegetables and fruits, include whole grains, contain healthy protein sources, and use healthy oils while limiting sugary drinks.

**System Answer:** A balanced meal should consist of a grain, a protein, and some vegetables.

**Retrieved Sources:** Healthy Eating Plate.txt, Healthy Weekday Meal Prep for Students.txt

**Analysis:** Retrieval was successful because the system returned relevant documents, including the Healthy Eating Plate guide that contains the correct information. However, the generation stage did not fully utilize the retrieved context. The model produced a simplified summary and omitted important details such as fruits, healthy oils, whole grains, and limiting sugary drinks. As a result, the answer was only partially accurate. This failure is primarily a generation issue rather than a retrieval issue, since the relevant information was available in the retrieved documents but was not completely reflected in the final response.

**How to Fix**
- Increase top k to ensure model sees all details
- Strengthen prompt so that model provides details, doesn't summarize or omit information excessively

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

The planning document provided a clear blueprint for building the entire pipeline before any coding began. Defining the domain, chunking strategy, embedding model, retrieval approach, and evaluation questions in advance made it easier for me to implement and iterate each stage systematically, especially with AI-assited coding, and verify that the final system matched the original design.

**One way your implementation diverged from the spec, and why:**

One difference was that the generation stage required additional grounding instructions beyond what was originally specified. During testing, some responses were overly brief or omitted important details from the retrieved documents, so the prompt had to be strengthened to encourage the model to rely more closely on the retrieved context. This change improved answer quality while still following the overall architecture described in the planning document.


**One way your implementation diverged from the spec, and why:**

Spec didn't involve thinking through a lot of bigger integration questions. For instance,initially, following the plan, I treated the retrieval and generation stages as separate components, but during implementation I refactored the code so that the Gradio interface directly imported and reused the retrieval function from the embedding and retrieval module to also ensure a persistent ChromaDB database.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

* *What I gave the AI:*
  I provided my full ingestion and chunking requirements from `planning.md`

* *What it produced:*
  The AI generated a complete Python script (`ingest_and_chunk.py`) that loaded `.txt` files, cleaned text, created LangChain `Document` objects, applied recursive chunking, and saved the output to `chunks.json` with metadata.

* *What I changed or overrode:*
  I modified the script to improve robustness, including handling encoding errors (`errors="ignore"`) and adding additional summary statistics (min/max chunk size and sample chunk previews) to better evaluate the quality of chunking.

---

**Instance 2**

* *What I gave the AI:*
  I provided a prompt describing the full RAG generation stage

* *What it produced:*
  The AI generated a complete `app.py` file integrating retrieval from ChromaDB, context construction, prompt templating, Groq API calls, evaluation tests, and a working Gradio interface.

* *What I changed or overrode:*
  I refactored parts of the retrieval integration to reuse a centralized `retrieve()` function from the embedding module instead of duplicating logic. 

