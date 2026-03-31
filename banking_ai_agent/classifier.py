def classify_message(message):
    message = message.lower()

    positive_keywords = [
        "thanks", "thank you", "appreciate", "great", "helpful",
        "resolved", "fixed", "good job", "grateful"
    ]

    negative_keywords = [
        "not working", "issue", "problem", "hasn’t", "has not",
        "delay", "still", "complaint", "frustrated", "angry",
        "didn't", "did not", "late", "missing", "failed"
    ]

    query_keywords = [
        "status", "ticket", "check", "update", "track",
        "where is", "can you check", "what is the status"
    ]

    positive_score = sum(1 for word in positive_keywords if word in message)
    negative_score = sum(1 for word in negative_keywords if word in message)
    query_score = sum(1 for word in query_keywords if word in message)

    scores = {
        "positive": positive_score,
        "negative": negative_score,
        "query": query_score
    }

    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:
        return "query"

    return best_category