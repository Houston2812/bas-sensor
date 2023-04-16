from http.server import BaseHTTPRequestHandler, HTTPServer
from  project_logger import logger
import json 

connection = ("0.0.0.0", 5000)

class Sensor(BaseHTTPRequestHandler):
    def do_GET(self):
        X_Payload_Id = self.headers.get('X-Payload-Id')
        payload = self.path[ self.path.index('payload') : ]
        
        logger.info(f"Get request;\nHeaders: 'X-Payload-Id' : {X_Payload_Id};\nPath: {payload.split('=')}")

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("X-Payload-Id", X_Payload_Id)
        self.end_headers()
        self.wfile.write(json.dumps({"status" : "Received", 'payload' : payload.split('=')[1]}).encode("utf-8"))

        logger.info("Request was received")

    def do_POST(self):
        try:

            X_Payload_Id = self.headers.get('X-Payload-Id')
            content_length = int(self.headers['Content-Length']) 
            
            request_body = self.rfile.read(content_length).decode().split("=")

            logger.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                    str(self.path), str(self.headers), request_body)

            payload = request_body[1]
            logger.info(f"Payload : {payload}")

            self.send_response(200)
            self.end_headers()

            response_body = f"payload={payload}"
            self.wfile.write(bytes(response_body, 'utf8'))
        except Exception as e:
            raise e
        
if __name__ == "__main__":        

    logger.info("Sensor started")
    
    webServer = HTTPServer(connection, Sensor)
    logger.debug("Server started http://%s:%d" % connection)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    logger.debug("Server stopped.")


