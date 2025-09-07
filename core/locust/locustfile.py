from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        response = self.client.post(
            "/accounts/api/v1/token/create",
            data={
                "email": "admin@gmail.com",
                "password": "123456"
            }
        ).json()
        token = response.get("access")
        if token:
            self.client.headers.update({"Authorization": f"Bearer {token}"})

    @task
    def post_list(self):
        self.client.get("/blog/api/post-list/")  # GET به لیست پست‌ها

    @task
    def category_list(self):
        self.client.get("/blog/api/category/")  # GET به دسته‌بندی‌ها


