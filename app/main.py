import os
from http.server import BaseHTTPRequestHandler, HTTPServer

def student_info():
    name = os.getenv("STUDENT_NAME", "Kanagat")
    surname = os.getenv("STUDENT_SURNAME", "Beken")
    group = os.getenv("STUDENT_GROUP", "IT2-2307")
    student_id = os.getenv("STUDENT_ID", "38052")

    return (
        "DevOps Student Application\n\n"
        f"Name: {name}\n"
        f"Surname: {surname}\n"
        f"Group: {group}\n"
        f"Student ID: {student_id}\n\n"
        "Application is running successfully!\n"
    )

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = student_info().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    print(student_info(), flush=True)
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
