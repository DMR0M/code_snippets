from datetime import datetime
import pymongo


# Database Route
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["dev_db"]
collection = db["code_snippets"]


# Test Data For Insertion
sample_data = [
    {
      "Coder": "RR",
      "Language": "Python",
      "Code Snippet": """print("Hello, World!")""",
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "RR",
      "Language": "Java",
      "Code Snippet": """System.out.println("Hello, World!");""",
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "RR",
      "Language": "Javascript",
      "Code Snippet": """console.log("Hello, World!");""",
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "Mari",
      "Language": "Java",
      "Code Snippet": """List<String> strList = new ArrayList<String>();
      strList.add("Item1");\nstrList.add("Item2");\nstrList.add("Item3");
      for(String item : strList) {
        System.out.println(item);
      }""",
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
]


def main():
    result = collection.insert_many(sample_data)
    print("Inserted document IDs:", result.inserted_ids)


if __name__ == '__main__':
    main()
    