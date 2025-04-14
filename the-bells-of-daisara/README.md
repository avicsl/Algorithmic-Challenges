# The Bells of Daisara

Long ago, before floodwaters scarred the mountains and the stars faded from the skies, the city of Daisara stood proud among the high cliffs. Its guardians were not warriors or mages, but bells—tall towers of sky-iron rising above the mist. These bells did not ring by hand. They were linked through ancient threads of resonance, unseen yet unbreakable.

When one bell was struck, its vibration passed to nearby bells. The sound moved outward with purpose, traveling only to those it was connected to. The pulse followed a strict rhythm. Bells closest to the source echoed first. Only after they had sung could the next layer awaken. When two bells were the same distance from the source, the one with the older name in the Registry of the Ring would chime first.

Then came the silence. Bridges collapsed. Towers fell. The threads snapped. One by one, the bells grew quiet, and the city was forgotten.

Now, centuries later, the last bellkeeper returns. You carry the scrolls of your ancestors, and a tuning rod passed down through generations. Among the ruins, you find that some of the old connections remain. A few bells still resonate when touched.

You do not need to fix them all. What matters is this: if you strike a single bell, in what order will the rest respond?

The awakening must begin at the chosen bell. From there, the resonance will ripple outward, reaching the closest bells first. If several are equal in distance, the one with the earliest name will ring first.

This is how the harmony must return. You must map the order in which the bells reawaken. The chime of Daisara waits to be heard again.

---

### **Input Format**
- The first line contains two integers `n` and `m`:  
  `n` — the number of bells (each labeled by a unique uppercase letter)  
  `m` — the number of intact resonance bridges.

- The next `m` lines contain two uppercase letters `a` and `b`, representing a two-way resonance link between bell `a` and bell `b`.

- The final line contains a single uppercase letter `s`, the bell where the awakening begins.

---

### **Constraints**
- `2 ≤ n ≤ 26`
- `1 ≤ m ≤ n × (n − 1) / 2`
- Bell labels are uppercase English letters (A–Z), randomly assigned
- All bells are connected directly or indirectly
- When multiple bells are available at the same level, awaken the one with the **lexicographically smallest** name first

---

### **Output Format**
- Print a single line of bell labels, space-separated, indicating the **order in which they resonate**

---

### **Sample Input**
```
6 5
M R
M C
C Y
R K
Y B
M
```

### **Sample Output**
```
M C R Y K B
```

---

### **Explanation**

The signal begins at bell `M`.  
From there, it reaches bells `C` and `R`. `C` comes first due to its earlier alphabetical name.  
`C` then passes the wave to `Y`. `R` triggers `K`.  
Finally, `Y` reaches `B`.

This chain respects both proximity and registry order.

The correct order is:
```
M → C → R → Y → K → B
```
