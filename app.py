from flask import Flask, request, jsonify
import pickle
# import pandas

new_df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

app = Flask(__name__)


def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    dist = similarity[movie_index]
    res = []
    movies_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        res.append(new_df.iloc[i[0]].title)
    return res


@app.route('/')
def home():
    return "hello"


@app.route('/predict', methods=['POST'])
def predict():
    movie = request.form.get('movie')
    # movies = {'movies': movie}

    return recommend(movie)
    # except:
    #     return 'no movie found'


if __name__ == '__main__':
    app.run(debug=True)
