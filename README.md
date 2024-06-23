# Movie-Recommendation-System
<b>This is a Content-based recommendation system based on tmbd_5000_movies and tmbd_5000_credits datasets.</b>
<br>
<b>I used Streamlit to showcase my Recommendation System which some glimpses are given below.</b><br><br>

Steps that have taken<br>
Step 01: Initially I merged both the datasets on 'title', then took only those features which will facilitate me to apply Bag-of-Word(BOW).<br>
step 02: After finishing the dataset, I did some preprocessing and feature extraction to draw clear data.<br>
step 03: After cleaning the data, I applied text preprocessing(lower, stemming).<br>
step 04: Applied CountVectorizer and then extracted similarity from cosine similarity.<br>
step 05: Formulate the function by matching the index of the similarity matrix that gives 5 recommended movies based on the input movie name.<br>
step 06: Dumping similarity data and new dataframe through pickle.<br>
step 07: Load both the files in vscode and use them in streamlit syntax.<br>

![image](https://github.com/Komalprasad132/Movie-Recommedation-System/assets/166751126/0932fbb2-dfdf-4c84-96be-eebf0977ba90)

![Screenshot (67)](https://github.com/Komalprasad132/Movie-Recommedation-System/assets/166751126/322d004d-5f65-4e85-9e08-a779fc16e39d)
![Screenshot (68)](https://github.com/Komalprasad132/Movie-Recommedation-System/assets/166751126/20cfd7f8-7556-449b-a910-f9cb3c01c371)
![Screenshot (69)](https://github.com/Komalprasad132/Movie-Recommedation-System/assets/166751126/85434484-d9b9-4755-b2e4-b28b7c4f9cef)



Author: Komal Prasad
