### Framing the Problem

YouTube has over 2 billion active monthly users and over 122 million active daily users watching over a billion hours per day. As the world's second most visited website with over 26 Billion videos, it's clear how impactful the platform is.

Since clickbait may be interpreted differently by different people, the definition used in this project is: a piece of content that uses an extreme title and thumbnail to mislead the viewer into clicking the video that dosen't deliver on what was promised by the title and thumbnail

Objective: Reduce time and save attention waisted watching misleading YouTube videos.
Solution will be used by any YouTube user in the form of a web application. Since more than 70% of YouTube watch time comes from mobile devices, the UI of our web app will be suited to mobile devices (though works fine on desktop)
There is a paper that examines this issue, but dosen't provide a concrete solution
Classification problem using supervised learning done online
Performance is measured using:

- A minimum of 85% accuracy is needed

### Getting the data

The data will be retrieved from the YouTubeDataV3 api
Since there are over 26 Billion total YouTube videos (that's just in 2020, likely to have risen in 2021), ideally we would have at least a Billion examples, but since the YouTube API limits our requests, we would likely have several thousand

I ran into a Catch 22 Loop: In order to automatically collect clickbait and non-clickbait videos, I needed an ML system already created which would
be trained on data collected by another ML system, and so on. Thus, I needed to manually select most of the clickbait videos

A clickbait video was determined by its title and thumbnail combination, and was manually selected by 2 different humans to reduce bias. Different genres were sampled as to not give too much weight to any single topic.

Non-clickbait videos were automatically selected from the YouTube API, and then looked over afterwards to make sure none of them were considered clickbait. To further balance the data, videos with comparable views were quereyed from the API.

## Data Collected:

- Video Title
- viewCount
- likeCount
- dislikeCount
- dislike/like ratio
- favoriteCount

### Exploring the Data

Create a copy of a small sample of the data
Target: Clickbait/NotClickbait
Study correlations between numerical values

### Training Data:

- Views, Likes, Dislikes, Dislike/Like Ratio, Favorites(maybe remove?)

- Video Title (consider using news headlines)

ML Models:

- Ensemble of ML Model estimators using soft voting (as we want to display probabilities on our web app)
- Feedforward Neural Network for NLP using the Google Universal Sentence Encoder (an encoder with with 512 dimensional embeddings trained by a DAN encoder for language classification tasks. It is a 1GB model, so it takes a while to load at first) for the first layer, and then a hidden layer followed by an output layer.
  https://tfhub.dev/google/universal-sentence-encoder/4

- Combining both with my own custom Ensemble model
  https://www.montana.edu/rotella/documents/502/Prob_odds_log-odds.pdf <-- Used this to convert logits to logs>

**Note**: You may want to remove all emoji's and nonascii characters (and characters that you can't name files with on Windows) as it may have a better accuracy

## Dataset Link:

https://www.kaggle.com/thelazyaz/youtube-clickbait-classification

# Skills Learned:

- Fetching & Parsing through JSON data with online API's (YouTube API)
- Creating a pleasing, yet functional Front End with React.js and Bootstrap CSS
- Ensembling Machine Learning Estimators and Tensorflow Hub NLP models together

# Future Scalability:

- If I had more resources (Infinite YouTube API Requests, more powerful TPUS to train with) then I would use millions and millions of YouTube Videos as training data
  - Though, you would run into the problem of what I call: "Meta-Clickbait" where the video itself isn't clickbait, but is instead designed to look like clickbait for comedic purposes of making fun of clickbait
- I could also used Unsupervised Learning to cluster together videos likely/not likely to be clickbait and use them as training examples with Self-Supervised Learning
- I tried to use the thumbnails as possible training features, however, I've found that I get very low accuracy when using them. This is because there are plenty of videos that appear to be clickbait (have contrasting colors, suprised facial expression, punctual shapes) that aren't actually clickbait but may appear to be depending on the viewer.

## If any of you are able to collect more clickbait data, then please let me know, as the project is open-sourced on github, more data will improve my model's performance, and I will credit you in the github and a future youtube video
