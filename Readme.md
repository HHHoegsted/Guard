# 🛡️ Guard — Simple, Expressive Argument Validation for Python

**Guard** is a lightweight, zero-dependency utility class that makes argument validation in Python
clean, explicit, and expressive. It provides a set of static methods that help enforce
assumptions about function inputs — making your code more predictable, readable, and robust.

---

## 💡 Why Use Guards?

Most bugs don’t come from bad logic — they come from **bad data** entering your functions.  
Guard clauses stop problems early by **failing fast** when inputs don’t meet expectations.

Using guards helps you:

- ✅ **Fail fast** – detect invalid input immediately  
- 🧠 **Clarify intent** – `Guard.against_none(x)` reads better than `if x is None:`  
- ♻️ **Reduce repetition** – reuse consistent validation patterns across your project  
- 🧩 **Improve maintainability** – keep validation logic centralized and uniform  
- 🧱 **Write defensive, self-documenting code**  

---

## 🚀 Installation

No external dependencies — just drop the file into your project.

```bash
# Clone or copy into your project
git clone https://github.com/hhhoegsted/guard.git