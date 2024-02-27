# Ampersand (&) v.0.0.01

## Organizational Structure

### Base Classes for Core Functionalities
1. **1_ConversationalInterface**: Handles the UX, interpreting user inputs and generating responses.
    - **Attributes**: stores knowledge base, user context
    - **Methods**: `parse_input()`, `generate_response()`
2. **2_DataAnalytics**: Data analysis capabilities.
     - **Attributes**: stores dataframes, analysis results
     - **Methods**: `load_data()`, `summarize_data()`, `perform_test()`, `interpret_results()`

### Subclasses for Specific Functionalities
- **2.1_InputPreprocessing** (`DataAnalytics` Subclass): Manages file input and output operations.
    - **Methods**: `read_file()`, `write_file()`
- **2.2_Statistician** (`DataAnalytics` Subclass): Performs statistical tests and analysis.
    - **Methods**: `choose_test()`, `execute_test()`
- **2.3_DataSurvey** (`DataAnalytics` Subclass): Conducts basic exploration for further understanding.
    - **Methods**: `explore_columns()`, `calculate statistics()`, `identify_missing_values()`
- **2.4_BusinessIntelligence**: Generates insights from data analysis.
    - **Methods**: `pattern_recognition()`, `highlight_key_findings()`, `suggestive_action_exhortation()`
- **1.1_UserSession** (`ConversationalInterface` Subclass): Manages individual sessions, storing context and history
    - **Attributes**: `user_id`, `session_history`
    - **Methods**: `update_context()`, `retrieve_history()`
- **1.2_NaturalLanguageUnderstanding** (`ConversationalInterface` Subclass): Processes natural language nput to understand user queries.
    - **Methods**: `extract_intent()`, `extract_entities()`
- **1.3_ResponseGenerator** (`ConversationalInterface` Subclass): (A.K.A. Natural Language Generation) Creates natrual language responses based on analysis resutls and user queries.
    - **Methods**: `formulate_reply()`, `response_template()`
- **1.4_ConversationManager** (`ConversationalInterface` Subclass): Orchestrates the flow of the conversation; decides when to ask the user for more information, and mediates the interaction between `NaturalLanguageUnderstanding` and `ResponseGenerator`. Tracks the conversation history as it happens, but also cross-references information from past conversations with methods that call from `1.1_UserSession` so that it can also provide the user with information and prompt for further clarification. Invokes methods within NaturalLanguageUnderstanding to initiate dialog with the user, and then based on that information, interprets the user's request and identifies gaps in the information provided.
### Utility Classes
- **DataVisualization**: Generates graphs and results that are human-readable.
    - **Methods**: `plot_data()`, `create_chart()`, `pivot_table()`, etc.
- **LearningModule**: Facilitates learning from user interactions to improve response accuracy and relevance.
    - **Methods**: `update_knowledge_base()`, `train_model()`

### Integration Class
- **ampersand**: The main class that integrates all functionalities and serves as the entry point for user interactions.
    - **Attributes**: Incorporates instances of other classes as needed (composition).
    - **Methods**: `handle_interaction()`... orchestrates the interaction flow by leveraging other classes.

## Integration with Bot Framework Composer and Azure Machine Learning Studio

### Step 1: Expose Python Logic as a Service

1. **Wrap Logic**: Encapsulate the logic of Ampersand (data analysis, conversation management, etc.) in a web service. My understanding is that in order to expose the Python code as RESTful APIs, frameworks like Flask or FastAPI can be used (this is all based off of surface-level Googling). The intent is to create endpoints for different functionalities: processing user input, having a conversation with the user (which is different than just simply taking information from the user), performing data analysis, and generating meaninful results.
2. **API Endpoints**: Design endpoints that correspond to the Ampersand functionalities I need to be accessible by users.
    - Endpoint: Accept user messages and return Ampersand's response.
    - Endpoint: Handles requests to analyze data (in the form of data payloads) and then returns processed information or inference. 
        - https://medium.com/@einsteinmunachiso/rest-api-implementation-in-python-for-model-deployment-flask-and-fastapi-e80a6cedff86
        - https://towardsdatascience.com/understanding-flask-vs-fastapi-web-framework-fe12bb58ee75

### Step 2: Develop Ampersand in Bot Framework Composer

1. **Setup**: This is done already; installed the application in macOS (not Parallels Windows 11) and created Ampersand.
2. **Design Conversational Flows**: Triggers, dialogs and actions correspond to the anticipated interactions between users and Ampersand.
3. **Integration of Ampersand Functionalities**: For all interactions that require Ampersand logic (data analysis, follow-up questions, etc.) I want to use HTTP actions within Composer to call Amersand service endpoints.
    - Congfigure HTTP request actions to interact with service endpoints, passing user inputs and recieving responses.
    - Use responses from servce to guide Ampersand's next steps, like asking more questions, presenting data visualizations, or making inferences.

### Step 3: Conversational Data Analysis
1. **User Inputs**: When Ampersand recieves input that requires deeper analysis or decision making, we trigger an HTTP request to the corresponding endpoint of the service that is hosted on Azure.
2. **Processing & Response**: The service processes the request, performs the action (analyze data or determines what question to ask and in what UI format), and then sends the response back to the bot. This inclides what the bot should convey to the user next.

### Step 4: Testing & Refinement
- Authentication of APIs is essential to ensure that only Bot Framework Ampersand can call the Ampersand Azure Service endpoints.
- The management of unexpected inputs, outputs, system errors, and API failures needs to be tracked and have some sort of reporting system for UI.
- Store and process historical conversations for improvement and testing.

## Microsoft Azure ML Studio

### In Layman's Terms

1. **Predictive Model**: Imagine you're a weather forecaster trying to predict whether it'll rain tomorrow. You look at patterns like cloud coverage and wind speed from the past and use them to make your prediction. A predictive model in machine learning does something similar: it looks at past data to predict future events, such as whether a customer will buy a product or not.
   - **Technical Explanation**: Predictive modeling involves using statistical techniques and machine learning algorithms to forecast future outcomes based on historical data. This process includes selecting and training a model using historical data, where the model learns the relationship between input variables (features) and the outcome (target variable). Once trained, the model can predict the outcome for new, unseen data. Common predictive modeling techniques include regression analysis for predicting continuous outcomes (e.g., sales volume) and decision trees for categorical outcomes (e.g., binary classification of "will buy" vs. "will not buy").
       - **How this is leveraged by Ampersand**: Eventually, I want it to get to a point where it is doing forecasts of data and making inferences.
2. **Classifier**: Think of organizing your music into different genres (rock, pop, jazz). You listen to a new song and decide which genre it belongs to based on its characteristics, like beat and instruments. A classifier in machine learning works similarly by categorizing data into different groups. For example, it can look at emails and classify them as "spam" or "not spam" based on their content.
   - **Technical Explanation**: Classification is a subset of supervised learning in machine learning, where the task is to predict the category or class of an instance based on its features. This involves training a classifier on a labeled dataset, where each instance is tagged with the correct class. The classifier learns the relationship between the features of the instances and their corresponding classes. Once trained, it can classify new instances into one of the categories it has learned. Techniques include logistic regression for binary classification, support vector machines (SVMs) for margin-based classification, and neural networks for complex, non-linear classification boundaries.
       - **How this is leveraged by Ampersand**: This can be used in several different ways. For one, I want to give it a business scenario with many different options and also define what the best course of action is and why. When given a dataset or document, Ampersand should be able to categorize this information based on the kind of tests it can perform on it.
           - So for categorical data, it would check off Chi-square as a possible test, whereas an uploded spreadsheet containing numerical data about the temperature and pressure of a manufacturing process (as well as the product quality) might warrant linear regression.
           - It should also be comfortable handling datasets where the distribution is unknown. When the user uploads data on product specifications, defects, performance metrics, or data that may not follow a normal distribution, Ampersand should know that Chebyshev's theorem can be used to help establish tolerance limits and asses the variability of the process output.
               - https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/chebyshevs-theorem-inequality/
        - It is imperative to note, however, that there is a differerence between what kinds of statistical tests **can** be performed on data, versus the use of pattern recognition techniques to suggest what tests **should** be performed by Ampersand. So it gives the user a menu to choose from and asks them "Well, what do you want to know?" I think user interface elements (maybe more upscaled versions of `IPyWidgets`) would really elevate this beyond the user experience offered by OpenAI with ChatGPT.
3. **Data Analysis Algorithm**: Consider you're trying to understand your spending habits. You look through your bank statements to see where you're spending the most money and identify any trends, like increasing restaurant bills. Data analysis algorithms sift through large datasets to find patterns, trends, and relationships, helping us draw conclusions or make decisions based on data.
   - **Technical Explanation**: Data analysis algorithms are a broad set of techniques used to uncover patterns, correlations, and insights from data. These can range from simple descriptive statistics that summarize data aspects (mean, median, variance) to complex machine learning algorithms that identify patterns or groupings in data without being explicitly programmed (unsupervised learning, like clustering algorithms). Data analysis algorithms also include dimensionality reduction techniques (e.g., PCA) that simplify data without losing critical information, enabling easier visualization and understanding of complex datasets.
        - **How this is leveraged by Ampersand**: Classification of data as it is uploded by the user might employ some of these techniques.

Predictive models, classifiers, and data analysis algorithms leverage computational statistics and machine learning to process and analyze data, each serving specific purposes in the broader context of data science and artificial intelligence. They help in automating decision-making processes, understanding underlying patterns, and making data-driven predictions or classifications.

Yes, you can design a bot within Bot Framework Composer that allows users to upload spreadsheets and then perform classification of statistical tests based on the data in those spreadsheets. Here's a general outline of how you might approach this:

1. **User Input**: Design a dialog in the bot that prompts the user to upload a spreadsheet containing their data. You can use Bot Framework Composer's built-in file upload capabilities for this purpose.

2. **Data Processing**: Once the user uploads a spreadsheet, you'll need to extract and process the data from the spreadsheet. This may involve parsing the spreadsheet file format (e.g., Excel, CSV) and loading the data into a suitable data structure for analysis.

3. **Data Analysis**: Implement logic within the bot to analyze the data and determine which statistical tests are appropriate based on the characteristics of the data. This might involve examining factors such as the types of variables (e.g., continuous, categorical), the number of groups or variables, and the research question or hypothesis being investigated.

4. **Statistical Test Classification**: Based on the analysis of the data, classify the appropriate statistical tests that could be performed. This could include tests such as t-tests, ANOVA, regression analysis, chi-square tests, etc., depending on the nature of the data and the user's research objectives.

5. **Bot Response**: Finally, design the bot to provide a response to the user indicating which statistical tests are recommended for their data. You can present this information in a user-friendly format, such as a list of recommended tests along with brief explanations of each test and when they are typically used.

It's important to note that the accuracy and effectiveness of the statistical test classification will depend on the complexity and variability of the data, as well as the sophistication of the analysis logic implemented in the bot. You may need to refine and iterate on your bot's design based on user feedback and real-world usage to improve its performance over time. Additionally, consider providing users with options for further customization or refinement of the suggested statistical tests based on their specific requirements and preferences.

## An Object-Oriented Application
Ampersand is developed using an **object-oriented** approach. Using classes and objects, this method allows a complex system like Ampersand to have different functionalities like conversational interfaces, data analysis, and file handling. These featrues are partitioned within separate classes. Each class defines the attributes and behaviors (methods) relevant to that specific functionality, and objects (instances of classes) intereact with each other to perform the overall task. In so doing, this achieves:
- **Encapsulation**: Each class in the project encapsulates specific data and methods related to that functionality, hiding the internal implementation details from ohter parts of the program. For example, the `DataAnalysis` class encapsulates methods or analyzing data without exposing the intricacies of its processes to the rest of the system.
    - **Keeping Secrets**: Imagine you have a recipe box. Each recipe card inside the box contains a list of ingredients and instructions on how to make a dish. You don't need to know all the details of every recipe to understand what's for dinner; you just need to know the name of the dish. In programming, encapsulation is like this recipe box. It's a way of keeping some details (like the ingredients and instructions) hidden inside "recipe cards" (classes), showing only what's necessary (like the dish name, or in programming, the methods you can use). This helps prevent accidental changes to the data or misuse of the internal workings of a component.
- **Inheritance**: This approach allows for the use of inheritance, where specific classes can extend or modify the behavior of existing classes. For exampl,e the `StatisticalTests` class could inherit from the `DataAnalyzer` class, adding specific methods for statistical analysis while still retaining general data analysis capabilities.
    - **Family Traits**: Inheritance in programming can be compared to how children inherit traits from their parents. Just as a child might inherit their parents' eye color or height, in object-oriented programming, a class (let's call it a "child class") can inherit attributes and behaviors (methods) from another class (known as the "parent class"). This means you can create a new class that automatically has many of the same features as another class and then add or modify as needed, just like a child might have the same eye color as their parent but learn different skills.
- **Polymorphism**: Classes can define methods that have the same name but behave differetnly based on the object that invokes them. This allows objects to be treated as instances of their parent class rather than their actual class, simplifying the interaction between components.
    - **Many Forms**: Polymorphism is like being able to speak different languages depending on who you're talking to. In programming, polymorphism allows methods to do different things based on what class is using them, even if the methods share the same name. It's the concept that you can call the same method on different objects, and each object can respond in its own way.
- **Modularity**: The system is broken down into distinct modules (classes), where each is responsible for a part of the functionality. This modular design makes the system more manageable for easier testing, maintenance, and scalability.
    - **Building Blocks**: Think of modularity like playing with LEGO blocks. Each block is designed to connect with others, but you can assemble them in countless ways to build different things, from cars and houses to entire cities. In programming, modularity involves breaking down a software project into smaller, manageable parts (modules or classes). Each part handles a specific piece of the program's functionality, and you can combine them to build complex systems. This makes it easier to understand, maintain, and update your code.
- **Inter-object communication**: Objects (instances of classes) interact with each other through methods, enabling the complex behaviors necessary for Ampersand to function as a conversational data analyst. This interaction pattern is a hallmark of object-oriented design.
    - **Teamwork**: Imagine a group of people working together on a project. Each person has a specific job, but they need to talk to each other to coordinate their efforts and complete the project successfully. In object-oriented programming, inter-object communication is similar: objects (representing the team members) send messages to each other, asking for data or actions to be performed. This communication allows different parts of a program to work together seamlessly, each doing its part to contribute to the overall goal.



An **API (Application Programming Interface)** is a set of protocols, routines, and tools for building software and applications. It specifies how software components should interact and allows different software entities to communicate with each other. In the context of your project with Ampersand and Bot Framework Composer, an API serves as a bridge between the conversational logic and functionalities you've developed in Python and the bot interface that interacts with users.

For Ampersand, you would expose specific functionalities (e.g., parsing user inputs, generating responses based on data analysis, managing user sessions) as API endpoints. These endpoints can be called by Bot Framework Composer through HTTP requests, enabling Ampersand to process data, perform analyses, and send back responses that the bot can relay to the user.

**API Endpoints Based on the Directory Structure:**

Based on your directory structure, the API endpoints might reflect the functionalities encapsulated within your modules. Here's an example of what these endpoints could look like:

- **Natural Language Understanding Endpoint:**
  - `/api/nlu/parse` - POST request that takes user input and returns the interpreted intent and entities.

- **Response Generation Endpoint:**
  - `/api/response/generate` - POST request that takes a context or a specific query and returns a natural language response.

- **User Session Management Endpoint:**
  - `/api/session/manage` - GET/POST requests to retrieve or update the state of a user's session.

- **Question Logic Endpoint:**
  - `/api/question/logic` - POST request that determines the next question to ask based on the current conversation context.

Each of these endpoints would correspond to the logic contained within your Python modules, making your bot's conversational capabilities accessible via HTTP requests.

(3) **Managing the Code as an Azure Function:**

Azure Functions is a serverless compute service that lets you run event-triggered code without having to explicitly provision or manage infrastructure. It's ideal for APIs, since it can automatically scale to meet demand and you only pay for the compute time you use.

To manage your Ampersand logic as Azure Functions:

- **Prepare the Environment:**
  - Ensure your Python code is organized in a way that each core functionality (natural language understanding, response generation, etc.) can be triggered as a function. This might involve some refactoring to fit the Azure Functions programming model.

- **Create Azure Functions:**
  - For each API endpoint, create a corresponding Azure Function. This involves defining a function trigger (HTTP trigger for APIs) and the logic that should execute when the function is invoked.

- **Deploy to Azure:**
  - Package your functions and deploy them to Azure. You can use the Azure CLI, Azure Portal, or Visual Studio Code with the Azure Functions extension for deployment.

- **Configure Endpoints in Bot Framework Composer:**
  - Once your functions are deployed, they'll be accessible via HTTP endpoints. Configure Bot Framework Composer to call these endpoints as needed, based on user interactions.

- **Testing and Monitoring:**
  - Azure provides tools for monitoring your functions, including execution logs and performance metrics. Use these tools to ensure your API is performing as expected and to troubleshoot any issues.

By following these steps, you integrate your Python logic with Bot Framework Composer through Azure Functions, enabling a seamless conversational experience powered by your custom analytics and conversation management logic.

ampersand/
│
├── notebooks/
│   ├── data_preparation.ipynb
│   ├── model_training.ipynb
│   └── model_evaluation.ipynb
│
├── data/
│   ├── raw/
│   │   ├── ML_training_data/
│   │   └── user_interaction_data/
│   └── processed/
│       ├── ML_training_data/
│       ├── user_interaction_data/
│       └── knowledge_base/
│
├── models/
│
├── src/
│   ├── ampersand.py
│   ├── api_integration/
│   │   ├── __init__.py
│   │   └── external_api_manager.py
│   ├── conversational_interface/
│   │   ├── __init__.py
│   │   ├── conversational_interface.py
│   │   ├── natural_language_understanding.py
│   │   ├── response_generator.py
│   │   └── user_session.py
│   │
│   ├── data_analytics/
│   │   ├── __init__.py
│   │   ├── input_preprocessing.py
│   │   ├── statistician.py
│   │   ├── baseline_assessment.py
│   │   ├── business_intelligence.py
│   │   └── statistical_tests.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── learning_module.py
│
├── templates/
│   ├── greetings.txt
│   └── questions.txt
│
├── config/
│   ├── bot_config.json
│   └── azure_config.json
│
└── requirements.txt


```python

```


```python

```
