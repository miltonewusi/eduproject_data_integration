from datetime import datetime
import pandas as pd

programme = pd.read_csv(
    "data/raw/programme_data.csv"
)

finance = pd.read_csv(
    "data/raw/finance_data.csv"
)

print("\nPROGRAMME DATA")
print(programme.head())

print("\nFINANCE DATA")
print(finance.head())

print("\nPROGRAMME SHAPE")
print(programme.shape)

print("\nFINANCE SHAPE")
print(finance.shape)

print("\nPROGRAMME INFO")
print(programme.info())

print("\nFINANCE INFO")
print(finance.info())

#check for missing values
print("\nPROGRAMME MISSING VALUES")
print(programme.isnull().sum())

print("\nFINANCE MISSING VALUES")
print(finance.isnull().sum())

# check for duplicates
print("\nPROGRAMME DUPLICATES")
print(programme.duplicated().sum())

print("\nFINANCE DUPLICATES")
print(finance.duplicated().sum())


#standardize school names
programme["school_name"] = (
    programme["school_name"]
    .str.upper()
    .str.strip()
)

finance["school_name"] = (
    finance["school_name"]
    .str.upper()
    .str.strip()
)

print(
    programme["school_name"]
    .head()
)


# identfiying matching issues
programme_schools = set(
    programme["school_name"]
)

finance_schools = set(
    finance["school_name"]
)

missing_matches = (
    programme_schools -
    finance_schools
)

print(
    "\nUNMATCHED SCHOOLS:"
)

for school in missing_matches:
    print(school)


# generate matching suggestions
from rapidfuzz import process

for school in missing_matches:

    result = process.extractOne(
        school,
        finance_schools
    )

    print(
        school,
        "->",
        result
    )

# creating match loop
match_lookup = {
    "RISING STAR ACADEMY":
    "RISING STAR ACAD.",

    "STAR OF HOPE SCHOOL":
    "STAR OF HOPE SCH."
}

programme["school_name"] = (
    programme["school_name"]
    .replace(match_lookup)
)


#integrateing datasets
integrated = programme.merge(
    finance,
    on=[
        "school_name",
        "year"
    ],
    how="left"
)

print(
    integrated.head()
)


#checking integration quality
print(
    integrated["budget_usd"]
    .isnull()
    .sum()
)


#Creating KPIs
integrated[
    "cost_per_child"
] = (

    integrated[
        "actual_spend_usd"
    ]

    /

    integrated[
        "children_reached"
    ]
)

integrated[
    "budget_utilisation"
] = (

    integrated[
        "actual_spend_usd"
    ]

    /

    integrated[
        "budget_usd"
    ]

) * 100


# District summary
district_summary = (

    integrated

    .groupby("district")

    .agg({

        "children_reached":"sum",

        "budget_usd":"sum",

        "actual_spend_usd":"sum"

    })

    .reset_index()

)

print(
    district_summary
)

# building deliverables
integrated.to_excel(
    "data/outputs/integrated_dataset.xlsx",
    index=False
)

district_summary.to_excel(
    "data/outputs/district_summary.xlsx",
    index=False
)


#validation checks
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


#exporting validation report
validation_report.to_excel(
    "data/outputs/validation_report.xlsx",
    index=False
)



#school summary
school_summary = (

    integrated

    .groupby(
        "school_name"
    )

    .agg({

        "children_reached":"sum",

        "mothers_trained":"sum",

        "budget_usd":"sum",

        "actual_spend_usd":"sum"

    })

    .reset_index()

)


#school summary KPIs
school_summary["cost_per_child"] = (

    school_summary["actual_spend_usd"]

    /

    school_summary["children_reached"]

)

school_summary["budget_utilisation"] = (

    school_summary["actual_spend_usd"]

    /

    school_summary["budget_usd"]

) * 100


#exporting school summary
school_summary.to_excel(
    "data/outputs/school_summary.xlsx",
    index=False
)


#top 10 schools by children reached
top_schools = (

    school_summary

    .sort_values(
        "children_reached",
        ascending=False
    )

    .head(10)

)


# lowest cost per child
efficient_schools = (

    school_summary

    .sort_values(
        "cost_per_child"
    )

    .head(10)

)

#exporting top schools 
top_schools.to_excel(
    "data/outputs/top_schools.xlsx",
    index=False
)


#summary statistics
total_children = (
    integrated["children_reached"]
    .sum()
)

total_budget = (
    integrated["budget_usd"]
    .sum()
)

total_spend = (
    integrated["actual_spend_usd"]
    .sum()
)

average_cost_per_child = (
    total_spend /
    total_children
)

print("\nEXECUTIVE SUMMARY")

print(
    f"Children Reached: {total_children}"
)

print(
    f"Approved Budget: ${total_budget:,.2f}"
)

print(
    f"Actual Spend: ${total_spend:,.2f}"
)

print(
    f"Cost Per Child: ${average_cost_per_child:.2f}"
)


#audit log
with open(
    "logs/run_log.txt",
    "a"
) as log:

    log.write(
        f"""

EXECUTION DATE:
{datetime.now()}

PROGRAMME RECORDS:
{len(programme)}

FINANCE RECORDS:
{len(finance)}

INTEGRATED RECORDS:
{len(integrated)}

TOTAL CHILDREN:
{total_children}

TOTAL SPEND:
{total_spend}

STATUS:
SUCCESS

------------------------------------------------

"""
    )

#creating final package
with pd.ExcelWriter(
    "data/outputs/reporting_pack.xlsx",
    engine="xlsxwriter"
) as writer:

    integrated.to_excel(
        writer,
        sheet_name="IntegratedData",
        index=False
    )

    district_summary.to_excel(
        writer,
        sheet_name="DistrictSummary",
        index=False
    )

    school_summary.to_excel(
        writer,
        sheet_name="SchoolSummary",
        index=False
    )

    validation_report.to_excel(
        writer,
        sheet_name="Validation",
        index=False
    )