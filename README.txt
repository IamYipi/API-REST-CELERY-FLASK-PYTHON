THIS IS AN USER'S MANUAL FOR RUN THE PROGRAM IN UBUNTU
1-Open a terminal,choose a broker and run it*(1)
docker run -d -p 5672:5672 rabbitmq
2-Run Celery work server
celery -A firstApp.celery worker --loglevel=INFO

3-Open a new terminal and configure Flask
export FLASK_APP=firstApp.py
4-Then run the flask program
flask run







(1)In my case I do with docker a rabbitmq-server,5672 is the number of the port you want to run the server.
Also you can install a rabbbitmq server in your localhost and use it

In this example celery is configured in RPC Result Backend
https://docs.celeryproject.org/en/stable/userguide/tasks.html#task-result-backends
RPC Result Backend (RabbitMQ/QPid)

The RPC result backend (rpc://) is special as it doesn’t actually store the states, but rather sends them as messages. This is an important difference as it means that a result can only be retrieved once, and only by the client that initiated the task. Two different processes can’t wait for the same result.

Even with that limitation, it is an excellent choice if you need to receive state changes in real-time. Using messaging means the client doesn’t have to poll for new states.
