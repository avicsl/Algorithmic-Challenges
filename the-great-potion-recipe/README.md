# Problem I  
**Echoes of the Hollow Depth**

In the shattered lands of Milos lies a forgotten temple whispered about in riddles. They call it the *Whispering Curse*—a madness that begins with a murmur and ends in silence. You, the Seeker of Hollow Depths, must follow the Whisper’s path. But beware: it never turns back, never splits, and always follows the deepest path.

You raise your torch and descend.

---

### **Problem Statement**

You are given a network of chambers connected by passages. Starting from a specific chamber, the Whisper explores the chambers by always going to the **lowest-numbered unvisited adjacent chamber**. Once it can go no further, it backtracks and continues this rule.

Your task is to determine the exact order in which the Whisper visits the chambers.

---

### **Input Format**
- The first line contains two integers `n` and `m` (`2 ≤ n ≤ 100`), where `n` is the number of chambers and `m` is the number of passages.
- The next `m` lines each contain two integers `u` and `v`, representing a bidirectional tunnel between chambers `u` and `v`.
- The last line contains a single integer `s` — the starting chamber.

---

### **Constraints**
- Chambers are numbered from `1` to `n`.
- The network is fully connected.
- If multiple unvisited chambers can be visited, always choose the **lowest-numbered one first**.

---

### **Output Format**
- Output a single line of space-separated integers representing the order of chambers visited by the Whisper.

---

### **Sample Input**
```
6 5
1 2
1 3
2 4
2 5
3 6
1
```

### **Sample Output**
```
1 2 4 5 3 6
```

---

### **Explanation**

The Whisper starts in chamber `1`.  
From there, it visits `2` (the lowest neighbor), then `4`, then `5`.  
It then backtracks and proceeds to `3`, and finally `6`.

The full trail is:
```
1 → 2 → 4 → 5 → 3 → 6
```
