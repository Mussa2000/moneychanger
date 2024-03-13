from time import sleep

import requests


class ERPAPIHandler(object):
    """Base class for `ERP API http methods`.

    Args:
        headers (dict): Headers for the requests.
        url (str): The url of the endpoint.
        timeout (int): Number of Seconds representing the connection.
        retries (int): Number of retries when connection fails with timeout
    Raises:
        `Validation errors.`
       ` Response errors.`
    Returns:
        requests.Response: The response object for request sent.
    """

    headers: dict
    url: str
    timeout: int = 300
    retries: int = 5

    def post(self, doctype: str, payload: dict) -> requests.Response:
        """Post request handler that hits ERPNext POST endpoint

        Args:
            doctype (str): The doctype to post data to.
            payload (dict): Body of the request.

        Returns:
            Response: Response object from the request.
        """
        for retry in range(self.retries):
            try:
                response = requests.post(
                    url=f"{self.url}/api/method/{doctype}",
                    headers=self.headers,
                    timeout=self.timeout,
                    json=payload,
                )
                return response
            except requests.exceptions.ConnectTimeout:
                sleep(1)
            except Exception as er:
                raise er

    def get(self, doctype: str, name: str) -> requests.Response:
        """Get request handler that hits ERPNext Get endpoint

        Args:
            doctype (str): The doctype to get data from.
            name (str): The name of the entity to retrieve data for.

        Returns:
            Response: Response object from the request.
        """
        for retry in range(self.retries):
            try:
                response = requests.get(
                    url=f"{self.url}/api/resource/{doctype}/{name}",
                    headers=self.headers,
                    timeout=self.timeout,
                )
                return response
            except requests.exceptions.ConnectTimeout:
                sleep(1)
            except Exception as er:
                raise er

    def put(self, doctype: str, name: str, payload: dict) -> requests.Response:
        """PUT request handler that hits ERPNext PUT endpoint

        Args:
            doctype (str): The doctype to update data in.
            name (str): The name of the entity to update data for.
            payload (dict): Body of the request.

        Returns:
            requests.Response: Response object from the request.
        """
        for retry in range(self.retries):
            try:
                response = requests.put(
                    url=f"{self.url}/api/resource/{doctype}/{name}",
                    headers=self.headers,
                    timeout=self.timeout,
                    json=payload,
                )
                return response
            except requests.exceptions.ConnectTimeout:
                sleep(1)
            except Exception as er:
                raise er
    
    def list_documents(self, doctype):
        response = requests.get(
                    url=f"{self.url}/api/method/{doctype}",
                    headers=self.headers,
                    timeout=self.timeout,
                )
        return response

    def delete(self, doctype: str, name: str) -> requests.Response:
        """Delete request handler that hits ERPNext DELETE endpoint

        Args:
            doctype (str): The doctype to delete data from.
            name (str): The name of the entity to delete.

        Returns:
            Response: Response object from the request.
        """
        for retry in range(self.retries):
            try:
                response = requests.delete(
                    url=f"{self.url}/api/resource/{doctype}/{name}",
                    headers=self.headers,
                    timeout=self.timeout,
                )
                return response
            except requests.exceptions.ConnectTimeout:
                sleep(1)
            except Exception as er:
                raise er
