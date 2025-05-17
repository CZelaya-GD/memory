# 🧠 Sonar Memory App

Welcome to **Sonar Memory App** – a persistent, searchable memory base for your AI prompts and outputs!  
This project lets you interactively store, search, and recall prompt-output pairs, powered by [Perplexity Sonar-Pro](https://www.perplexity.ai/) and backed by a robust SQLite database.  
Run it anywhere with Docker for a fast, reliable, and private AI memory assistant.

---

## 🚀 Current Capabilities

- **Automatic LLM Output:** Enter a prompt, and Sonar-Pro generates and stores the output for you.
- **Persistent Memory:** All prompt-output pairs are stored in a local SQLite database for durability.
- **Search & Retrieve:** Instantly search or retrieve previous prompts and their outputs.
- **Memory Management:** List all memories, delete specific ones, or clear the database.
- **Portable & Secure:** Runs in Docker, with your API key managed via `.env` and your data stored locally.

---

## 📁 File Structure

<pre>
your_project/
├── app/
│   ├── __init__.py       # (empty, for package structure)
│   ├── main.py           # Main CLI application logic
│   └── memory.py         # MemoryDB class for storage/search
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container build instructions
├── .env                  # Your Perplexity API key (never commit this!)
├── data/                 # (Created at runtime) Persistent SQLite DB
└── README.md             # This documentation
</pre>

---

## 🛠️ How to Run

### 1. **Clone the Repository**

      git clone <your-repo-url>
      cd your_project


### 2. **Set Your Perplexity API Key**

Create a file called `.env` in the project root:

      PERPLEXITY_API_KEY=your_actual_api_key_here


### 3. **Build the Docker Image**

      docker build -t sonar-memory-app .


### 4. **Create the Data Directory**

      mkdir -p ./data


### 5. **Run the App**

      docker run --rm -it --env-file .env -v "$(pwd)/data":/data sonar-memory-app


> **Note:**  
> Your prompt-output memories are stored in `./data/memory.sqlite` and persist between runs.

---

## 🕹️ Usage Guide

When running, you’ll see a menu:

      Choose action: [store/retrieve/search/list/delete/exit]:


- **store:** Enter a new prompt. The app queries Sonar-Pro and saves the output.
- **retrieve:** Enter a prompt to recall its output.
- **search:** Find all memories containing a keyword.
- **list:** See all stored prompt-output pairs.
- **delete:** Remove a specific prompt from memory.
- **exit:** Safely close the app and database.

---

## 🌟 Recommended Next Steps

- **Add a Web or API Interface:** Build a simple web UI or REST API for easier access and integration.

- **Enhance Search:** Implement fuzzy or semantic search for smarter memory recall.

- **Analytics & Insights:** Track prompt frequency, trends, or visualize your memory usage.

- **Export/Import:** Add tools to export or import memories (e.g., to CSV or JSON).

- **User Authentication:** If multi-user, add authentication and user-specific memory spaces.

- **Scheduled Backups:** Automate backups of your SQLite database for extra safety.

---

## 🧩 Extending the Project

- **Integrate with other LLMs:** Swap in different OpenAI-compatible models.
- **Advanced Memory Management:** Add memory expiration, tagging, or categorization.
- **Deploy to the Cloud:** Use Docker Compose or Kubernetes for scalable deployments.

---

## 🤝 Contributing

Pull requests and ideas are welcome!  
Please open an issue to discuss your feature or bugfix before submitting a PR.

---

## 📝 License

MIT License (or your preferred license).

---

## 💬 Questions?

Open an issue or contact the maintainer for support.

---

**Happy Prompting! 🚀**