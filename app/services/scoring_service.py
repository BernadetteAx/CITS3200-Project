
def build_result_state(session):
    mission = session.get("mission")
    recorded_result = session.get("mission_result")

    # expose final results once mission has finished.
    if (
        not mission
        or mission.get("status") != "complete"
        or recorded_result is None
    ):
        return None

    auction = session.get("auction", {})
    outcomes = recorded_result["outcomes"]
    challenges = mission.get("challenges", [])

    challenge_results = []

    for outcome in outcomes:
        index = outcome["challengeIndex"]

        challenge = (
            challenges[index]
            if 0 <= index < len(challenges)
            else {}
        )

        item = outcome.get("item")

        challenge_results.append({
            "challengeId": outcome["challengeId"],
            "challengeIndex": index,
            "name": challenge.get("name", f"Challenge {index + 1}"),
            "success": outcome["success"],
            "penalty": outcome["penalty"],
            "title": outcome.get("title", ""),
            "description": outcome.get("description", ""),
            "itemUsed": dict(item) if item is not None else None,
        })

        # Challenge Card Detail - START
        # Pass-through only, for the results card. No scoring uses these.
        # Added conditionally, matching the "type" key below, so the payload
        # shape is unchanged for challenges with no point copy recorded.
        if outcome.get("pointDesc"):
            challenge_results[-1]["pointDesc"] = outcome["pointDesc"]

        if outcome.get("pointValue") is not None:
            challenge_results[-1]["pointValue"] = outcome["pointValue"]
        # Challenge Card Detail - END

        if challenge.get("type"):
            challenge_results[-1]["type"] = challenge["type"]

    purchased_items = [
        dict(item)
        for item in session.get(
            "purchased_items",
            auction.get("purchased_items", []),
        )
    ]

    inventory_by_id = {
        item["id"]: item
        for item in mission.get("inventory", [])
    }

    used_items = []

    for item_id in mission.get("used_items", []):
        item = inventory_by_id.get(item_id)

        used_items.append(
            dict(item)
            if item is not None
            else {"id": item_id, "name": item_id}
        )

    passed_count = sum(
        1 for outcome in outcomes if outcome["success"] is True
    )

    failed_count = sum(
        1 for outcome in outcomes if outcome["success"] is False
    )

    return {
        "missionName": mission.get("mission_name", ""),
        "location": mission.get("location", ""),
        "finalScore": recorded_result["score"],
        "leftoverMoney": auction.get("budget"),
        "totalPenalties": recorded_result["penalties"],
        "totalChallenges": len(challenges),
        "challengesCompleted": len(outcomes),
        "challengesPassed": passed_count,
        "challengesFailed": failed_count,
        "challenges": challenge_results,
        "itemsPurchased": purchased_items,
        "itemsUsed": used_items,
        "completionStatus": mission["status"],
        # mission does not currently record an overall win/loss, (potential added later)
        "missionOutcome": None,
    }
