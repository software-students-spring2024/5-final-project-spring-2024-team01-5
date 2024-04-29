## TODO: Add CI/CD badge

# Grade Manager App

## Description

This app is designed to allow users to keep track of their school grades. Users can upload data for their courses, denoting the name, grade, credits, semester, and instructor for each course. After uploading their course data, a user can view a dashboard displaying their courses and their current GPA for the semester. If a user is looking to reach some target grade in the class, our app allows someone to calculate the required final exam grade for it.

## Create Docker network

```
docker network create mynetwork
```

## TODO: How to run MongoDB

## How to run Docker for web app

1. Build the Docker container for web app

```
cd app
docker build -t app .
```

2. Run the Docker container for the app

```
docker run --name app -d --network mynetwork -p 5001:5001 app
```

3. Access the web app at http://127.0.0.1:5001 or http://localhost:5001/

## Team Members

- [Nathanuel Dixon](https://github.com/nathanuel0322)
- [Aarav Sawlani](https://github.com/aaravsawlani)
- [Joshua Forlenza](https://github.com/joshforlenza)
- [Eugene Chang](https://github.com/egnechng)
