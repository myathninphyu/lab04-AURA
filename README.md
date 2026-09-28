# lab04-AURA
## Who Did What
| Member | GitHub Username | File |
|---|-----------------|---|
| Lin Akari | LinAkari-Grace  | test_deposit.py |
| Thel Thiri Thu | Heleniverse | test_withdraw.py |
| Myat Hnin Phyu | myathninphyu    | test_teardown.py |
| Lin Akari | LinAkari-Grace  | conftest.py |
| Dora | 6805140056-art  | test_shared.py |

## Our Merge Conflict
```text```
```text| Member | GitHub Username | File |```
```text|---|-----------------|---|```
```text<<<<<<< HEAD```
```text| Myat Hnin Phyu | myathninphyu    | test_teardown.py |```
```text=======```
```text| Lin Akari | LinAkari-Grace  | test_deposit.py |```
```text>>>>>>> origin/main```

we manually deleted the conflict markers, and and kept both contributions rather than picking one over the other. We then arranged the rows sequentially so that Lin Akari's test assignment was listed first, followed by Myat Hnin Phyu's assignment. Once the text was cleanly ordered, we staged the file with git add and finalized the merge with a clean commit. After resolving the conflict of those two members, our team decided to add the rows one by one to README file rather than doing it at the same time. This helps us to avoid more conflict.

Git could not automatically resolve the merge conflict because both the local branch and the remote branch made different changes to the same part of the README.md file. Git cannot determine which version is correct or whether both changes should be kept. Therefore, Git marks the conflicting section with <<<<<<<, =======, and >>>>>>> and requires the user to manually choose or combine the changes. In this case, the local branch added information about Myat Hnin Phyu, while the remote branch added information about Lin Akari, so Git needed the user to decide how these entries should appear in the final README file.

# Git Contribution Summary
5  myathninphyu
3  Heleniverse
3  Lin Akari @ Grace
2  dora

# Reflection Questions
Answer each question in one or two sentences:
1. Why was your push rejected, and how did you fix it?
The push was rejected because the remote repository had newer commits that were not on our local machine yet. We fixed it by running git pull, manually resolving the conflict in VS Code, staging the file, and committing before pushing again.

2. Why could Git not resolve the README conflict automatically?
Git could not automatically resolve the merge conflict because both the local branch and the remote branch made different changes to the same part of the README.md file. Git cannot determine which version is correct or whether both changes should be kept. Therefore, Git marks the conflicting section with <<<<<<<, =======, and >>>>>>> and requires the user to manually choose or combine the changes. In this case, the local branch added information about Myat Hnin Phyu, while the remote branch added information about Lin Akari, so Git needed the user to decide how these entries should appear in the final README file.

3. What is the difference between committing and pushing?
Committing saves the changes locally on our computer in Git, while pushing uploads those saved commits to GitHub for everyone to see.

4. How do fixtures reduce duplicated setup code in tests?
Fixtures let you create the test data or objects once in a single function, so you don't have to rewrite the same setup code inside every single test.