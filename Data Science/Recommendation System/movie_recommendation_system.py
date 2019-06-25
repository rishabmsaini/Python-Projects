import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#Here are some few good datasets:https://gist.github.com/entaroadun/1653794 
#used to fetch movie data with a minimum rating of 4
#"data" variable contains the movie data that is divided into many categories test and train
data = fetch_movielens(min_rating=4.0)

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
model = LightFM(loss='warp')

# function that process this data to recommend movies for any number of users
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):

    #number of users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendations for each user we input
    for user_id in user_ids:

        #known positives or the movies users liked
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]

        #movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))

        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out the results
        print("User %s:-" % user_id)
        print("\tKnown positives:")

        for x in known_positives[:3]:
            print("\t    %s" % x)

        print("\tRecommended:")

        for x in top_items[:3]:
            print("\t    %s" % x)
            
sample_recommendation(model, data, [6, 21, 351])
