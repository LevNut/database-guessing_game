from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os, json, redis

# App
application = Flask(__name__)

# connect to MongoDB
mongoClient = MongoClient(
    'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ[
        'MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_AUTHDB'])
db = mongoClient[os.environ['MONGODB_DATABASE']]

# connect to Redis
redisClient = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=os.environ.get("REDIS_PORT", 6379),
                          db=os.environ.get("REDIS_DB", 0))

games_collection = db.games
count = 0
state = 0
oa = []
ia = []
hint = ["*", "*", "*", "*"]


@application.route('/')
def index():
    games_collection.delete_many({})
    return render_template('index.html')


@application.route('/game')
def game():
    games_collection.insert_one({
        "count": count,
        "input_ans": ia,
        "output_ans": oa,
        "check": False,
        "state": state,
        "hint": hint,
    })

    gg = games_collection.find_one({"check": False})
    return render_template('game.html', game=gg)


@application.route('/case-a')
def a_case():
    gg = games_collection.find_one({"check": False})
    ia = gg["input_ans"]
    oa = gg["output_ans"]
    state = gg["state"]
    count = gg["count"]
    hint = gg["hint"]

    if 0 <= state < 4:
        # setup input
        ia.append("A")
        state += 1
        games_collection.update_one({"check": False}, {"$set": {"input_ans": ia, "state": state}})

    elif 4 <= state < 8:
        count += 1
        # setup output
        if "A" == ia[state-4]:
            oa.append("A")
            state += 1
            hint.pop(0)
            games_collection.update_one({"check": False}, {"$set": {"count": count, "state": state, "output_ans": oa, "hint": hint}})
        else:
            games_collection.update_one({"check": False}, {"$set": {"count": count}})

    gg = games_collection.find_one({"check": False})
    return render_template('game.html', game=gg)


@application.route('/case-b')
def b_case():
    gg = games_collection.find_one({"check": False})
    ia = gg["input_ans"]
    oa = gg["output_ans"]
    state = gg["state"]
    count = gg["count"]
    hint = gg["hint"]

    if 0 <= state < 4:
        # setup input
        ia.append("B")
        state += 1
        games_collection.update_one({"check": False}, {"$set": {"input_ans": ia, "state": state}})

    elif 4 <= state < 8:
        count += 1
        # setup output
        if "B" == ia[state-4]:
            oa.append("B")
            state += 1
            hint.pop(0)
            games_collection.update_one({"check": False}, {"$set": {"count": count, "state": state, "output_ans": oa, "hint": hint}})
        else:
            games_collection.update_one({"check": False}, {"$set": {"count": count}})

    gg = games_collection.find_one({"check": False})
    return render_template('game.html', game=gg)


@application.route('/case-c')
def c_case():
    gg = games_collection.find_one({"check": False})
    ia = gg["input_ans"]
    oa = gg["output_ans"]
    state = gg["state"]
    count = gg["count"]
    hint = gg["hint"]

    if 0 <= state < 4:
        # setup input
        ia.append("C")
        state += 1
        games_collection.update_one({"check": False}, {"$set": {"input_ans": ia, "state": state}})

    elif 4 <= state < 8:
        count += 1
        # setup output
        if "C" == ia[state-4]:
            oa.append("C")
            state += 1
            hint.pop(0)
            games_collection.update_one({"check": False}, {"$set": {"count": count, "state": state, "output_ans": oa, "hint": hint}})
        else:
            games_collection.update_one({"check": False}, {"$set": {"count": count}})

    gg = games_collection.find_one({"check": False})
    return render_template('game.html', game=gg)


@application.route('/case-d')
def d_case():
    gg = games_collection.find_one({"check": False})
    ia = gg["input_ans"]
    oa = gg["output_ans"]
    state = gg["state"]
    count = gg["count"]
    hint = gg["hint"]

    if 0 <= state < 4:
        # setup input
        ia.append("D")
        state += 1
        games_collection.update_one({"check": False}, {"$set": {"input_ans": ia, "state": state}})

    elif 4 <= state < 8:
        count += 1
        # setup output
        if "D" == ia[state-4]:
            oa.append("D")
            state += 1
            hint.pop(0)
            games_collection.update_one({"check": False}, {"$set": {"count": count, "state": state, "output_ans": oa, "hint": hint}})
        else:
            games_collection.update_one({"check": False}, {"$set": {"count": count}})

    gg = games_collection.find_one({"check": False})
    return render_template('game.html', game=gg)


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("FLASK_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("FLASK_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
