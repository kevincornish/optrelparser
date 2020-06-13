import pdftotext

# open PDF
with open("190304A.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

# print pages
print(len(pdf))

# split each page in the pdf
for page in pdf:
    print(page)

# read individual pages
print(pdf[0])
print(pdf[1])

# join all text into one string
print("\n\n".join(pdf))

# save joined txt to a output file
with open('output.txt', 'w') as f:
    f.write("\n\n".join(pdf))