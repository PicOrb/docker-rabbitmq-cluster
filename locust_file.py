from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/login", {"username":"ellen_key", "password":"education"})

def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {index:2}

    def on_start(self):
        pass #login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait=50
    max_wait=90
