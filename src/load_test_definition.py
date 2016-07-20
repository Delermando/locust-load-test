from locust import TaskSet, task, HttpLocust

class Tasks(TaskSet):
    @task
    def index(self):
        self.client.get('/')

class MyHostLoadTest(HttpLocust):
    host = "http://seudominio.com"
    task_set = Tasks
    min_wait = 2000
    max_wait = 5000