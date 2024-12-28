# Prompt Engineering with Dify

## **Introduction**
Prompt engineering is the art of crafting precise inputs to extract meaningful and relevant outputs from large language models (LLMs). It's not just about words—it's about structuring your input to get the most effective and accurate results.

### **Why Prompt Engineering?**
- Unlock the true potential of AI.
- Solve real-world problems effectively.
- Develop applications with minimal technical debt.

This guide will equip you with the knowledge to master prompt engineering and build AI-powered apps with Dify. Even if you're a beginner, we'll take you step by step, ensuring a fun and insightful learning experience.

---
## Workshop Outline

1. **Introduction to Prompt Engineering**
   - Importance and applications.

2. **Introduction to Dify**
   - What is Dify and why use it?

3. **Understanding Supported Models**
   - Overview of models supported by Dify.
   - When and why to use each model.

4. **Setting Up Dify**
   - Cloud-hosted and self-hosted setups.

5. **Exploring Dify Features**
   - Key tools and functionalities.

6. **Hands-On Examples**
### **Example 1: Travel Planning (Bangalore to New York)**
1. **Define Workflow**:
   - Create a new workflow named `Travel Planner`.
   - Add a text input node: "I want to travel from Bangalore to New York."
   - Add an agent node to suggest flights, visas, and accommodations.
2. **Run Workflow**:
   - Test the workflow and observe the results on the dashboard.

### **Example 2: Weekend Food Recommendations**
1. **Define Workflow**:
   - Create a new workflow named `Food Recommendations`.
   - Add a text input node: "Suggest foods I can enjoy in Bangalore this weekend."
   - Add an agent node to retrieve local food suggestions.
2. **Run Workflow**:
   - Test the workflow and refine the prompt as needed.

7. **Observability in Dify**
   - Monitoring and optimizing prompts.

8. **Conclusion**
   - Inspiring you to explore more!
---

## **Prerequisites**
1. Basic understanding of terminal commands (no prior coding experience required).
2. Installed software:
   - Docker
   - Docker Compose

If you're new to Docker, don't worry! We'll guide you through it in the next section.

---

---

## **1. Getting Started with Workshop**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/vellankikoti/prompt-engineering-with-dify.git

```
---
## **2. Setiing up Dify**

## **3. Exploring Dify's Features**

### **Quick Walkthrough**
- **Workflow Canvas**: Visualize and create workflows seamlessly.
- **Prompt IDE**: Test and refine prompts in real time.
- **RAG Pipeline**: Retrieve and use relevant information for context-aware responses.
- **Agent Tools**: Pre-built agents for tasks like web search or data retrieval.

---

## Repository Structure

- **`prerequisites/`**: Docker and Docker Compose setup.
- **`dify-setup/`**: Instructions for Dify installation.
- **`models-overview/`**: Supported models and their use cases.
- **`hands-on-examples/`**: Step-by-step examples.
- **`observability/`**: Monitoring and debugging prompts.
- **`assets/`**: Screenshots and outputs.

### **1. Generic Prompts Tables**


---

#### **Table 1: Bad Prompts**
| **Prompt**                          | **Why It’s Bad**                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| "Tell me about AI."                 | Too broad, resulting in a generic response.                                             |
| "Explain Kubernetes."               | Lacks context and scope, leading to an overly broad explanation.                        |
| "Plan my trip."                     | No details provided, so the AI can’t tailor the response.                               |
| "What should I eat?"                | Too vague; doesn’t specify location, cuisine, or dietary preferences.                   |
| "Write a blog."                     | Doesn’t specify the topic, audience, or length, resulting in a generic and useless output.|

---

#### **Table 3: Bad Prompts People Think Are Good**
| **Prompt**                                               | **Why It’s Misleadingly Bad**                                                      |
|----------------------------------------------------------|-----------------------------------------------------------------------------------|
| "Explain DevOps in detail."                              | Appears good but is too broad; lacks an audience or context.                      |
| "Tell me something interesting about AI."                | Sounds engaging but is too vague, leading to irrelevant responses.               |
| "What are the best practices for software development?"  | Too generic and lacks specificity about the type of software or audience.        |
| "What should I do to become successful?"                 | Subjective and unclear; lacks context, goals, or a timeframe.                    |
| "Plan a weekend getaway for me."                         | Appears good but doesn’t specify location, preferences, or budget.               |

---

#### **Table 3: Good Prompts**
| **Prompt**                                                                                     | **Why It’s Good**                                                                 |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| "Explain DevOps to a 10-year-old using a toy factory as an example."                           | Clear, uses a relatable analogy, and sets a tone for simplicity.                |
| "Suggest 5 online resources to learn Python for beginners, ranked by user ratings."           | Specific about the resources and includes a ranking criterion.                  |
| "Write a professional resignation letter explaining I am moving for career growth."           | Specific goal and context provided for generating a tailored response.          |
| "What are the latest AI trends in 2024, focusing on LLMs and ethical concerns?"               | Narrow scope and focus on specific aspects of AI.                               |
| "How can Kubernetes simplify microservices management, with examples?"                       | Specific topic with a clear expectation for examples.                           |

---

#### **Table 4: Very Well, The Great Prompts**
| **Prompt**                                                                                   | **Why It’s Great**                                                               |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| "Explain Kubernetes to a non-technical audience, using the analogy of a delivery company."  | Clear audience, relatable analogy, and focused topic.                            |
| "List the top 5 AI breakthroughs in 2024, highlighting their impact on healthcare."         | Specific, time-bound, and focuses on a niche domain.                             |
| "Write a 500-word blog about DevOps benefits for startups, including cost savings."         | Defines length, audience, topic, and focus.                                      |
| "Suggest 3 relaxing weekend getaways from Bangalore under ₹10,000, with scenic views."      | Clear location, budget, and user preferences provided.                           |
| "Generate a list of 5 South Indian dishes in Bangalore, suitable for vegans, under ₹200."   | Includes location, cuisine, dietary restrictions, and budget details.           |


---
