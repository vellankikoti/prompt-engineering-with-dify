# **Travel Plan: From Bangalore to New York**

This example demonstrates how to use **Dify** to create a personalized travel plan. It dynamically generates an itinerary including flights, hotels, and activities based on user input.

---

## **Objective**

Create an AI-powered travel planning app using Dify that generates personalized itineraries based on user preferences.

---

## **How It Works**

1. Users input details like their origin, destination, budget, and preferences.
2. Dify processes the input using a GPT-based model and generates a detailed travel plan.
3. The output includes recommendations for flights, accommodations, and activities.

---

## **Steps to Create and Test**

### **Step 1: Open the Dify Dashboard**
1. Log in to your **Dify** instance.
   - For cloud-hosted: Visit [Dify Cloud](https://dify.ai/).
   - For self-hosted: Open your local URL (e.g., `http://localhost:8080`).

---

### **Step 2: Configure the App**
1. **Create a New App**:
   - Click on **Create New App** → Choose **Text Generator**.
   - Name your app (e.g., `Travel Plan App`).

2. **Add Variables**:
   - In the **Variables** section, add the following:
     - `origin`: "Enter your origin city."
     - `destination`: "Enter your destination city."
     - `budget`: "Enter your budget in USD."
     - `preferences`: "What are your interests (e.g., cultural, adventure)?"

3. **Design the Prompt**:
   - Go to the **Orchestrate** tab → **Prefix Prompt**.
   - Paste the following prompt:
     ```text
     Plan a {{preferences}} trip from {{origin}} to {{destination}} with a budget of {{budget}}. Include recommendations for flights, hotels, and activities.
     ```

4. **Configure the Model**:
   - Go to the **Model Settings** tab.
   - Select the model (e.g., `gpt-4` for detailed outputs or `gpt-3.5-turbo` for faster responses).
   - Set the parameters:
     - Temperature: `0.7` (balanced creativity).
     - Max Tokens: `500` (for a detailed response).

---

### **Step 3: Test the Prompt**
1. Navigate back to the **Orchestrate** tab.
2. Click **Test Input**:
   - Input sample values for variables:
     - **Origin**: Bangalore
     - **Destination**: New York
     - **Budget**: $5000
     - **Preferences**: Adventure and cultural experiences
3. Click **Generate** and review the AI-generated travel plan.

---

### **Step 4: Publish the App**
1. Go to the **Publish** tab.
2. Provide a public name and description:
   - Name: `Travel Plan App`
   - Description: "Plan your travel effortlessly with personalized AI recommendations."
3. Click **Publish** to generate a sharable app link.

---

## **Sample Input and Output**

### **Input Example**
- Origin: Bangalore  
- Destination: New York  
- Budget: $5000  
- Preferences: Adventure and cultural experiences  

### **Generated Output Example**
```text
Here’s a 5-day itinerary for your trip from Bangalore to New York:

Day 1:
- Morning: Flight from Bangalore to New York (Economy, $1200)
- Afternoon: Check into "The Plaza Hotel" ($300/night)
- Evening: Visit Times Square and enjoy dinner at Carmine’s (Italian cuisine)

Day 2:
- Morning: Explore Central Park with a guided tour
- Afternoon: Visit the Museum of Modern Art (MoMA)
- Evening: Attend a Broadway show (e.g., The Lion King)

Day 3:
- Morning: Take a day trip to the Statue of Liberty and Ellis Island
- Afternoon: Stroll through SoHo for shopping and cafes
- Evening: Try local street food at Smorgasburg market

Day 4:
- Morning: Explore Brooklyn Bridge and Dumbo area
- Afternoon: Lunch at Grimaldi’s Pizzeria
- Evening: Enjoy a sunset cruise around Manhattan

Day 5:
- Morning: Last-minute shopping at Macy’s
- Afternoon: Return flight to Bangalore
```

---

## **Next Steps**
- Experiment with different inputs (e.g., budget constraints or unique preferences like "beach holidays").
- Explore advanced workflows by adding follow-up questions for more personalized plans.

---
