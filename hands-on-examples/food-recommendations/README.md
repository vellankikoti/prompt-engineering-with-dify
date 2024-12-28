# Food Recommendations: Weekend Cuisine in Bangalore

In this example, we'll use Dify to generate personalized food recommendations for weekends in Bangalore. 

---

## Objective

Create a list of food options tailored to different tastes and preferences using prompt engineering in Dify.

---

## Steps

1. **Open the Dify Dashboard**  
   Access the Dify dashboard (local or cloud) from your browser.

2. **Select the Model**  
   Choose a model like GPT or Claude for generating recommendations.

3. **Input the Prompt**  
   Use the following prompt:
   ```text
   I am in Bangalore for the weekend. Suggest 5 unique dishes and the best places to try them.
   
4. **Analyze the Output**
Review the generated recommendations and refine the prompt if needed for more specificity.

5. **Iterate and Customize**
Example:

- Add dietary preferences like vegetarian or vegan.
- Specify a budget range or cuisine type.

**Expected Output**
```
A list of 5 dishes with the name of the restaurant, address, and specialty (e.g., "Masala Dosa - Vidyarthi Bhavan, Gandhi Bazaar").
```
---
#### **Table 1: Bad Prompts**
| **Prompt**                     | **Why It’s Bad**                                                                 |
|--------------------------------|----------------------------------------------------------------------------------|
| "What should I eat?"           | Too vague; lacks location, cuisine preferences, or dietary requirements.         |
| "Suggest some food."           | No context, leading to random and unhelpful suggestions.                         |
| "What’s good to eat in Bangalore?" | Too broad; doesn’t specify area, budget, or cuisine.                          |
| "Where to find food?"          | Lacks clarity and purpose, resulting in irrelevant responses.                    |
| "Recommend a restaurant."      | No details provided about location, type of food, or price range.               |

---

#### **Table 2: Bad Prompts People Think Are Good**
| **Prompt**                                             | **Why It’s Misleadingly Bad**                                                      |
|--------------------------------------------------------|-----------------------------------------------------------------------------------|
| "Suggest a restaurant in Bangalore."                  | Appears specific, but lacks information like cuisine, budget, or dietary needs.   |
| "What’s the best South Indian food?"                  | No context or location provided, leading to overly generic responses.             |
| "Where can I eat pizza?"                               | Doesn’t include location, type of pizza, or dining preferences.                   |
| "Find me vegan food."                                  | Too broad; doesn’t specify location, cuisine, or type of meal (breakfast, lunch). |
| "Suggest a place to eat near me."                      | Appears useful but lacks any personalization or specificity.                      |

---

#### **Table 3: Good Prompts**
| **Prompt**                                                                                     | **Why It’s Good**                                                                 |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| "Suggest three budget-friendly South Indian breakfast places in Jayanagar, Bangalore."         | Specific about cuisine, budget, and location.                                    |
| "Find vegan-friendly Italian restaurants in Koramangala, Bangalore, with good reviews."        | Defines dietary needs, cuisine, and area for tailored recommendations.           |
| "Recommend a family-friendly restaurant in Indiranagar with outdoor seating and North Indian food."| Focused on family preferences, seating, location, and cuisine.                   |
| "Where can I find the best biryani in Bangalore under ₹300?"                                   | Includes a specific dish, price range, and location.                             |
| "Suggest three coffee shops in Jayanagar with free Wi-Fi and a quiet atmosphere for working."  | Combines location and preferences for a clear output.                            |

---

#### **Table 4: Very Well, The Great Prompts**
| **Prompt**                                                                                     | **Why It’s Great**                                                               |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| "Recommend 5 vegan-friendly South Indian dishes in Bangalore under ₹200, with restaurant names."| Combines dietary needs, budget, and location with a clear output format.         |
| "Suggest a dinner menu for a vegetarian in Indiranagar, focusing on authentic Rajasthani food."| Defines meal type, dietary preference, location, and cuisine.                    |
| "Find three romantic rooftop restaurants in Bangalore for dinner, with a budget of ₹2,000."   | Highly specific with purpose, budget, and ambiance requirements.                 |
| "Where can I find gluten-free desserts in Bangalore, and how much do they cost?"              | Combines dietary restrictions, location, and price range for actionable results. |
| "Plan a weekend food trail in Bangalore, focusing on iconic street food spots."               | Comprehensive, actionable, and specific to a theme.                              |

---

### **Workshop Use Case**

1. **Interactive Activity for Food Prompts**:
   - **Step 1**: Ask participants to create their own food-related prompts (starting vague).
   - **Step 2**: Improve them using the examples provided in the workshop.
   - **Step 3**: Compare the AI responses to highlight the difference.

2. **Examples for Hands-On**:
   - Start with a vague prompt: “What should I eat?”
   - Improve it to: “Find vegan-friendly South Indian breakfast places in Jayanagar, Bangalore, under ₹200.”
   - Show how the output improves with clarity.

---
