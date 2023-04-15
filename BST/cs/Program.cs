using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;


class Program
{

    static List<int> GetAddNumbers()
    {
        string content = File.ReadAllText("/datasets/add.txt");
        List<int> numbers = content.Split().Select(ParseInt32).ToList();
        return numbers;
    }

    static List<int> GetCheckNumbers()
    {
        string content = File.ReadAllText("/datasets/check.txt");
        List<int> numbers = content.Split().Select(ParseInt32).ToList();
        return numbers;
    }

    static int ParseInt32(string value)
    {
        if (int.TryParse(value, out int result))
        {
            return result;
        }
        else
        {
            Console.WriteLine($"Failed to parse '{value}' as an integer.");
            Environment.Exit(1);
            return 0; // This line is unreachable but required by the compiler.
        }
    }

    public static void Main(string[] args){
        int amount = int.Parse(args[0]);
        
        List<int> addNumbers = GetAddNumbers().Take(amount).ToList();
        List<int> checkNumbers = GetCheckNumbers().Take(amount).ToList();

        Tree bst = new Tree();
        
        // Add elements
        DateTime startTime = DateTime.Now;
        foreach (int i in addNumbers){
            bst.add(i);
        }
        DateTime endTime = DateTime.Now;
        Console.WriteLine($"ADD_TEST:{(endTime - startTime).TotalSeconds}");

        // Check elements
        startTime = DateTime.Now;
        foreach (int i in checkNumbers){
            bst.contain(i);
        }
        endTime = DateTime.Now;
        Console.WriteLine($"CHECK_TEST:{(endTime - startTime).TotalSeconds}");

        // Len elements
        startTime = DateTime.Now;
        for (int j = 0; j < 10; j++){
            bst.length();
        }
        endTime = DateTime.Now;
        Console.WriteLine($"LEN_TEST:{(endTime - startTime).TotalSeconds / 10}");

        // Height elements
        startTime = DateTime.Now;
        for (int k = 0; k < 10; k++){
            bst.height();
        }
        endTime = DateTime.Now;
        Console.WriteLine($"HEIGHT_TEST:{(endTime - startTime).TotalSeconds / 10}");

        Console.WriteLine($"VALIDATION:{bst.length()}:{bst.height()}");
        }
}
