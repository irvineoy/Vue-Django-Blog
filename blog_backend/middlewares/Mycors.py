from django.utils.deprecation import MiddlewareMixin

class MyCors(MiddlewareMixin):
    def process_response(self, request, response):
        # response["Access-Control-Allow-Origin"] = ("http://localhost:8080", 'http://127.0.0.1:8080')
        response["Access-Control-Allow-Origin"] = 'http://localhost:8080'
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Headers"] = "Content-Type"
            response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
            response["Access-Control-Allow-Credentials"] = True
        return response