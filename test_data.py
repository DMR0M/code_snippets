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
      "Description": "Printing Hello World in Python",
      "Code Snippet": """print("Hello, World!")""",
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "RR",
      "Language": "Java",
      "Description": "Printing Hello World in Java",
      "Code Snippet": """System.out.println("Hello, World!");""",
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "RR",
      "Language": "Javascript",
      "Description": "Printing Hello World in Javascript",
      "Code Snippet": """console.log("Hello, World!");""",
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "Mari",
      "Language": "Java",
      "Description": "Creating an ArrayList in Java",
      "Code Snippet": 
      """
        import java.util.List;
        import java.util.ArrayList;
      
        List<String> strList = new ArrayList<String>();
        strList.add("Item1");
        strList.add("Item2");
        strList.add("Item3");
        
        for(String item : strList) {
          System.out.println(item);
        }
      """,
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "Mari",
      "Language": "Java",
      "Description": "Ternary Operator Assignment in Java",
      "Code Snippet": 
      """
        // variable flag ternary assignment
        int num = 15;
        boolean isEven = num % 2 == 0 ? true : false;
      """,
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "RR",
      "Language": "Python",
      "Description": "List Comprehensions in Python",
      "Code Snippet": """
        even_numbers = [
          n 
          for n in range(1, 101) 
          if n % 2 == 0
        ]
        
        odd_numbers = [
          n 
          for n in range(1, 101) 
          if n % 2 != 0
        ]
      """,
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "RR",
      "Language": "Python",
      "Description": "Map function in Python",
      "Code Snippet": """
        # Map Using Defined Functions
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        def fizzbuzz(n):
          if n % 3 == 0:
            return 'fizz'
          return 'buzz'
        
        fizzbuzz_list = list(map(fizzbuzz, num_list))
        print(fizzbuzz_list)
      """,
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "RR",
      "Language": "Python",
      "Description": "Map function in Python",
      "Code Snippet": """
        # Map Using Lambda Expression
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        binary_list = list(map(lambda x: 1 if x % 2 == 0 else 0, num_list))
        print(binary_list)
      """,
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "RR",
      "Language": "Python",
      "Description": "Filter function in Python",
      "Code Snippet": """
        # Filter Using Defined Function
        nums_to_100 = [n for n in range(1, 101)]
        
        def is_prime(num):
          f_count = 0
          
          for n in range(1, num+1):
            if num % n == 0:
              f_count += 1
          
          return f_count <= 2
        
        prime_nums = list(filter(is_prime, nums_to_100))
        print(prime_nums)
      """,
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
    {
      "Coder": "Mari",
      "Language": "Java",
      "Description": "Using Interfaces in Java",
      "Code Snippet": 
      """
      interface Polygon {
        void getArea(int length, int breadth);
      }

      // implement the Polygon interface
      class Rectangle implements Polygon {

      // implementation of abstract method
      public void getArea(int length, int breadth) {
          System.out.println("The area of the rectangle is " + (length * breadth));
        }
      }
      """,
      "Created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    },
]


def main():
    result = collection.insert_many(sample_data)
    print("Inserted document IDs:", result.inserted_ids)


if __name__ == '__main__':
    main()
    