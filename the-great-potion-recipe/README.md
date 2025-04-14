# The Great Potion Recipe

In a magical kingdom, there lived a skilled alchemist named Elara. She was renowned for her potions that could heal the sick, grant strength, and even make people fly. However, there was a catch—every potion required a specific number of rare ingredients, and each ingredient had a unique identifier. Elara had recently discovered a mysterious ancient scroll that contained a list of all the ingredients needed for her most powerful potion yet.

As Elara prepared for her big potion-making day, she gathered all the ingredients she had available. Unfortunately, in her excitement, she accidentally spilled some of the ingredients on the floor, causing a few to roll away and become lost. To make matters worse, the ancient scroll had a note that mentioned which ingredients were supposed to be included, but some of them were missing from her collection.

Your task is to help Elara identify which ingredients she is missing. The list of required ingredients consists of consecutive integers, each representing a different ingredient. You need to determine which ingredients Elara must still find to complete her potion.

---

### **Input Format**
- The first line contains two integers `N` and `M` (`1 ≤ N ≤ 1000`), where `N` is the total number of unique ingredients required and `M` is the number of ingredients Elara currently possesses.
- The second line contains `M` integers, representing the identifiers of the ingredients Elara has.

---

### **Constraints**
- The ingredient identifiers are unique and between `1` and `N`.
- At least one ingredient is missing.

---

### **Output Format**
- Output the missing ingredient identifiers in **ascending order**, each on a new line.

---

### **Sample Input**
```
8 5
2 3 5 1 6
```

### **Sample Output**
```
4
7
8
```

---

### **Explanation**

In the first example, Elara needs a total of 8 ingredients, but she currently has 5. The missing ingredient identifiers are 4, 7, and 8.  
