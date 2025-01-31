ver=1.0.5
docker build -t scholtz2/vote-coin-chatbot-base:$ver-stable -f dockerfile-base .
docker push scholtz2/vote-coin-chatbot-base:$ver-stable

docker build -t scholtz2/vote-coin-chatbot:$ver-stable -f dockerfile-app .
docker push scholtz2/vote-coin-chatbot:$ver-stable