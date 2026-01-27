# Devfile Python Shell Coverage Demo

This project demonstrates **complete Devfile command execution coverage** using a Python-based workflow.
It shows how different shell syntaxes are normalized and executed by the TaskProvider.

---

## What this demo proves

This setup covers **100% of Devfile command execution patterns**:

| Feature                                  | Covered |
|-----------------------------------------|:------:|
| Implicit `&&` (newline normalization)   | ✅ |
| Explicit `&&`                  | ✅ |
| OR operator (\|\|)                        | ✅ |
| Semicolon (;)                  | ✅ |
| Pipe (\|)                                | ✅ |
| POSIX multiline `\`                     | ✅ |
| Windows escaped multiline `\\`          | ✅ |
| Argument preservation                   | ✅ |
| Subshell grouping `( )`                 | ✅ |
| Background jobs `&` + `wait`            | ✅ |
| Composite sequential commands           | ✅ |
| Composite parallel commands             | ✅ |
| Cyclic composite detection (rejection)  | ✅ |
| Real data generation & validation flow  | ✅ |

---

