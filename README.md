# genai-final
GenAI Final Project Source Code

Tech Stack

I am utilizing OpenAI's LLMs for advanced conversation capabilities, RAG for real-time Wikipedia data retrieval, Llama index for data access efficiency, and Chainlit , an open-source Python package, for tech integration. I will also employ the ReAct (Reasoning and Act) prompt framework  to guide our agent through intelligent data retrieval and response generation, ensuring a seamless user interaction. The source code will be written in Python language. 

Task One: Set Up (/apikeys.yml) (/utils.py)

Description

The initial step involves preparing the development environment for building a chat assistant powered by RAG and LLMs, utilizing Wikipedia for factual information. This setup process includes storing the OpenAI API key, configuring Python modules for the project, and creating scripts to facilitate the interaction with the ChatGPT API and manage Wikipedia page indexing. This foundational setup ensures that all necessary components are in place for the chat assistant to utilize the OpenAI API for generating responses, with Wikipedia as the knowledge base.

Task Two: Index Wikipedia Pages (/index_wikipages.py)

Description

This task revolves around writing a script to index Wikipedia pages, enabling the chat assistant to fetch real-time data from these pages. It involves importing various libraries and classes for data validation, indexing, and querying, as well as interacting with the Wikipedia API. Key steps include creating data structures to manage Wikipedia page lists , using the ChatGPT API to process user requests for indexing specific Wikipedia pages, and then loading these pages into an in-memory document store for efficient retrieval . The process then creates an in-memory vector store to facilitate semantic searches on the indexed pages, transforming text into numerical embeddings that capture semantic meanings. This setup ensures the conversational agent can access and utilize up-to-date information from Wikipedia, enhancing its ability to provide factual and relevant responses.

Task Three: Create Chat Assistant Interface (/chat_agent.py)

Description

This task focuses on building the chat assistant interface using the chat_agent.py script, which involves importing necessary libraries, initializing settings menus, creating a Wikipedia search engine, setting up a ReAct agent , and defining user-agent interaction functions. Key steps include setting up a selection panel for model choice, allowing users to input Wikipedia page requests, transforming the indexed Wikipedia pages into a query engine, and initializing a ReAct agent that uses this query engine to process user queries. The agent's workflow involves selecting tools, using the LLM for reasoning, and iteratively addressing the query until resolved. The interface is constructed using Chainlit   , facilitating interactive settings and query processing, thereby providing a user-friendly platform for accessing information from indexed Wikipedia pages.

Task Four: Chainlit Run

Description

The final step to launch the chat agent involves executing the chat_agent.py script via the Chainlit framework in the terminal. This process activates the conversational application, allowing it to interact with users through a browser interface. Users can index Wikipedia pages and enable the agent to use this indexed information for answering queries. To demonstrate the agent's capabilities, see below examples. This task not only tests the agent's ability to provide accurate responses based on indexed Wikipedia content but also showcases the practical application of integrating LLMs with RAG for creating knowledgeable and interactive chat agents.

Within the terminal, key in the command chainlit run chat_agent.py. 






