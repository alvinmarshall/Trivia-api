# Full Stack Trivia API

## Full Stack Trivia
Full stack trivia is a way for Udacity's employees and students to connect with each other. Allowing them to create bonding experiences by placing trivia once a week.

## API Description
1. Displays questions — both by all questions and by category. Questions has the ability to show the question, category and difficulty rating. Answers are hidden and can be shown with the press of a button.
2. Questions can be deleted with the press of a button.
3. Questions can be added, text for question and answer are required.
4. All questions can be searched, based on text query string.
5. The game is played by category or all questions, in a random order.

## Local Requirements
Requires Python 3.7 or later

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend micro-services framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
make init-db
```

## Running the server

From within the `backend` directory first en sure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

## BACKEND API DOCUMENTATION

#### List Categories
```curl
curl http://localhost:5000/categories -X GET -H "Content-Type: application/json"}'
```
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs.

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```
#### List Questions
```curl
curl http://localhost:5000/questions -X GET -H "Content-Type: application/json"}'
```
- Fetches a dictionary of questions, paginated in groups of 10.
- Returns JSON object of categories, questions dictionary with answer, category, difficulty, id and question.
```json
{
   "categories": [
      "Science",
      "Art",
      "Geography",
      "History",
      "Entertainment",
      "Sports"
   ],
   "current_category": [],
   "questions": [
      {
         "answer": "Apollo 13",
         "category": 5,
         "difficulty": 4,
         "id": 2,
         "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
      }
   ],
   "success": true,
   "total_questions": 3
}
```

#### Add Question
- Sends a post request in order to add a new question.
```curl
curl http://localhost:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Foo", "answer":"Bar", "category":"1", "difficulty":"1"}'
```
```json
{
   "categories": [
      "Science",
      "Art",
      "Geography",
      "History",
      "Entertainment",
      "Sports"
   ],
   "current_category": [],
   "questions": [
      {
         "answer": "Apollo 13",
         "category": 5,
         "difficulty": 4,
         "id": 2,
         "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
      }
   ],
   "success": true,
   "total_questions": 3
}
```

#### Search Question
- Search for available question
```curl
curl http://localhost:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"Foo"}'
```
```json
{
   "categories": [
      "Science",
      "Art",
      "Geography",
      "History",
      "Entertainment",
      "Sports"
   ],
   "current_category": [],
   "questions": [
      {
         "answer": "Bar",
         "category": 1,
         "difficulty": 1,
         "id": 1,
         "question": "Foo"
      }
   ],
   "success": true,
   "total_questions": 3
}
```

#### Delete Question
- Deletes a specified question using the id of the question
- Request Arguments: `id` - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code. Optionally can return the id of the question. If you are able to modify the frontend, you can have it remove the question using the id instead of refetching the questions.

```curl
curl -X DELETE http://localhost:5000/question/1
```
```json
{
   "success": true
}
```

#### Category Question
- Fetches questions for a cateogry specified by id request argument
- Request Arguments: `id` - integer
- Returns: An object with questions for the specified category, total questions, and current category string

```curl
curl http://localhost:5000/categories/1/questions
```
```json
{
   "categories": [
      "Science",
      "Art",
      "Geography",
      "History",
      "Entertainment",
      "Sports"
   ],
   "current_category": [],
   "questions": [
      {
         "answer": "Bar",
         "category": 1,
         "difficulty": 1,
         "id": 1,
         "question": "Foo"
      }
   ],
   "success": true,
   "total_questions": 3
}
```

#### Quizzes
- Sends a post request in order to get the next question
```curl
curl http://localhost:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[], "quiz_category":{"type":"Science","id":1}}'
```
```json
{
   "question": {
      "answer": "Bar",
      "category": 1,
      "difficulty": 1,
      "id": 1,
      "question": "Foo"
   },
   "success": true
}
```

---

`GET '/questions?page=${integer}'`

- Fetches a paginated set of questions, a total number of questions, all categories and current category string.
- Request Arguments: `page` - integer
- Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string

```json
{
  "questions": [
    {
      "id": 1,
      "question": "This is a question",
      "answer": "This is an answer",
      "difficulty": 5,
      "category": 2
    }
  ],
  "totalQuestions": 100,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": "History"
}
```
#### Paginated Questions
```curl
curl http://localhost:5000/questions?page=1 -X GET -H "Content-Type: application/json"}'
```
- Fetches a paginated set of questions, a total number of questions, all categories and current category string.
- Request Arguments: `page` - integer
- Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string

```json
{
   "categories": [
      "Science",
      "Art",
      "Geography",
      "History",
      "Entertainment",
      "Sports"
   ],
   "current_category": [],
   "questions": [
      {
         "answer": "Apollo 13",
         "category": 5,
         "difficulty": 4,
         "id": 2,
         "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
      }
   ],
   "success": true,
   "total_questions": 3
}
```
