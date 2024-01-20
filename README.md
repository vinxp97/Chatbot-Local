# Chatbot-Local
A frontend to create a personal assistant that can access local data, perform actions, make code, remember things, and help you answer inquiries using documents. To start, it supported using Excel files and utilized Pandas, Langchain, and Azure OpenAI to read through a file.

The system message is auto-generated based on the selected filetype -- this opens the door to allow any file within a shared repository to be analyzed with accuracy by GPT-4, even guessing the reason for columns in a file's schema. By taking a small sample of the records in a dataset, you can let the model infer the reason for each column.
