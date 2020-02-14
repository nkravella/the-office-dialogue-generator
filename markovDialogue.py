import markovify

# Get raw text as string.
with open("dwight.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# # Print five randomly-generated sentences
# for i in range(5):
#     print(text_model.make_sentence())
#
# # Print three randomly-generated sentences of no more than 280 characters
# for i in range(3):
#     print(text_model.make_short_sentence(280))

#generate the sentences and write to CSV file
for i in range(1000):
    print(text_model.make_short_sentence(140))
    #writer.writerow(text_model.make_short_sentence(140))
