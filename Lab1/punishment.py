print("Enter a sentence: ")
sent = input()
print("Enter the number of times the sentence should be repeated: ")
rep = int(input())
with open("CompletedPunishment.txt", "w") as file:
    while rep > 0:
        file.write(sent + "\n")
        rep = rep - 1
