import markovify
directory_path = 'D:/Nicolas GAL/Melun/'
file_name = 'melun'
file_extension = '.txt'

# Specify the path to your text file
text_file_path = 'D:/Nicolas GAL/Melun/TrainingData.txt'

# Read the contents of the text file
with open(text_file_path, 'r', encoding='utf-8') as text_file:
    text_data = text_file.read()




# Combine the directory path and file name


# Open the file in write mode
for i in range(1):
    file_path = directory_path + file_name + str(i)+ file_extension
    with open(file_path, 'w',encoding='utf-8') as file:
        # Create a Markov chain model
        text_model = markovify.Text(text_data)
        # Generate a sentence
        for i in range(100000):
            generated_sentence = text_model.make_sentence()
            if generated_sentence != None:
                file.write(generated_sentence)
                print(f"File '{file_name + str(i)+ file_extension}' created in the directory '{directory_path}'.")


