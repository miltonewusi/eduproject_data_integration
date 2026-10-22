validation_results = []

validation_results.append({
    "check": "Missing School Names",
    "count": integrated["school_name"].isnull().sum()
})

validation_results.append({
    "check": "Duplicate Records",
    "count": integrated.duplicated().sum()
})

validation_results.append({
    "check": "Missing Budgets",
    "count": integrated["budget_usd"].isnull().sum()
})

validation_results.append({
    "check": "Negative Budgets",
    "count": (
        integrated["budget_usd"] < 0
    ).sum()
})

validation_results.append({
    "check": "Budget Exceeded",
    "count": (
        integrated["actual_spend_usd"]
        >
        integrated["budget_usd"]
    ).sum()
})

validation_report = pd.DataFrame(
    validation_results
)

print(validation_report)