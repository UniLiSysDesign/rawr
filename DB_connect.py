# Import Packages
from crate import client # database package
import nltk # text preprocessing package
import gensim # topic modeling package


# Create connection
crate_host = "192.168.56.101:4200"
connection = client.connect(crate_host)

# Open Cursor
cursor = connection.cursor()
cursor.execute("SELECT * FROM rawrs")

# Print Result
result = cursor.fetchone()
print(result)

# Close Cursor
cursor.close()

# Close Database Connection
connection.close()