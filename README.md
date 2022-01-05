
# Bulgarian Matchbox Collection

Welcome to the first and only online catalogue of Matchbox cars made in Bulgaria 
over the years! All cars photographed here are factory made, no re-paints or customs.

Here you will find photos of all color variations I have 
or had in my collection through my entire life.

Each car have a photo and a full description about:

- make
- model
- color
- interior color
- base
- window tint
- tampos

All photos will be hosted on the cloud (AWS S3)
## Run Locally

Clone the project

```bash
  git clone https://github.com/haraGADygyl/flask-bmbxc.git
```

Install dependencies

```bash
  pip install -r requirements.txt
```

## Documentation

### Registered users can:

#### add new cars to the database

```bash
  POST /car/create
```

#### see all cars from the database

```bash
  GET /car
```

#### see car from the database, by ID

```bash
  GET /car/id
```

### Administrators can:

#### edit any added to the database car, by ID

```bash
  PUT /car/edit/id
```

#### delete any car, by ID

```bash
  DELETE /car/delete/id
```
## Tech Stack

- **Client:** In progress

- **Server:** Python, Flask, SQLAlchemy, postgreSQL, AWS S3

## Roadmap

- Frontend functionallity

- Registered users can mark which cars they have in their collection

- Registered users can mark which cars they want in their collection

- Patreon/PayPal donations functionallity

- Monthly e-mail updates when new cars are added


## 🔗 Links

### Follow diecart_customs on Instagram for more photos and updates

[![instagram](https://img.shields.io/badge/instagram-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.instagram.com/diecart_customs/)

