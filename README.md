# ENGIETest

## Running the API

To run this API, you will need Docker installed on your computer.

1. Open your terminal and navigate to the root directory of the application:

2. Build the Docker image by executing the following command:

    ```bash
    docker build -t DESIRED_TAG .
    ```

3. After the base image is downloaded and `requirements.txt` is installed, run the container using:

    ```bash
    docker run -d --name CONTAINER_NAME -p 8888:8888 DESIRED_TAG
    ```
4. The request should be directed to the address `127.0.0.1:8888/Prueba/calculate/productionPlan`.

5. The request body should follow the format indicated in the payload:

    ```json
    {
      "load": 480,
      "fuels": {
        "gas(euro/MWh)": 13.4,
        "kerosine(euro/MWh)": 50.8,
        "co2(euro/ton)": 20,
        "wind(%)": 60
      },
      "powerplants": [
        {
          "name": "gasfiredbig1",
          "type": "gasfired",
          "efficiency": 0.53,
          "pmin": 100,
          "pmax": 460
        },
        {
          "name": "gasfiredbig2",
          "type": "gasfired",
          "efficiency": 0.53,
          "pmin": 100,
          "pmax": 460
        },
        {
          "name": "gasfiredsomewhatsmaller",
          "type": "gasfired",
          "efficiency": 0.37,
          "pmin": 40,
          "pmax": 210
        },
        {
          "name": "tj1",
          "type": "turbojet",
          "efficiency": 0.3,
          "pmin": 0,
          "pmax": 16
        },
        {
          "name": "windpark1",
          "type": "windturbine",
          "efficiency": 1,
          "pmin": 0,
          "pmax": 150
        },
        {
          "name": "windpark2",
          "type": "windturbine",
          "efficiency": 1,
          "pmin": 0,
          "pmax": 36
        }
      ]
    }
    ```

6. The output format is:

    ```json
    [
      {
        "name": "windpark1",
        "p": 90.0
      },
      {
        "name": "windpark2",
        "p": 21.6
      },
      {
        "name": "gasfiredbig1",
        "p": 460.0
      },
      {
        "name": "gasfiredbig2",
        "p": 338.4
      },
      {
        "name": "gasfiredsomewhatsmaller",
        "p": 0.0
      },
      {
        "name": "tj1",
        "p": 0.0
      }
    ]
    ```

---
