import pdftotext

# Load PDF
with open("190304A.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# How many pages?
print(len(pdf))

# Iterate over all the pages
for page in pdf:
    print(page)

# Read some individual pages
print(pdf[0])
print(pdf[1])

# Read all the text into one string
print("\n\n".join(pdf))

# Save all text to a txt file.
with open('output.txt', 'w') as f:
    f.write("\n\n".join(pdf))
