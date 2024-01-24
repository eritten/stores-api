from locust import HttpUser, task


class User(HttpUser):
    @task
    def fetch_products_performance_test(self):
        self.client.get('/api/products/')
