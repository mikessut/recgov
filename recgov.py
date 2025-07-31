"""
Example of request to determine site ids:
https://www.recreation.gov/api/permitcontent/4675318
"""
import requests
import datetime

URLS = {
    "gates_of_lodore": "https://www.recreation.gov/api/permits/250014/divisions/380/availability?start_date=2025-07-26T06:00:00.000Z&end_date=2025-12-01T00:00:00.000Z&commercial_acct=false&is_lottery=false",
    "westwater_aug": "https://www.recreation.gov/api/permitwbe/621744/availability/monthly?year=2025&start_date=2025-08-01&division_id=744",
    "westwater_sept": "https://www.recreation.gov/api/permitwbe/621744/availability/monthly?year=2025&start_date=2025-09-01&division_id=744",
    "westwater_oct": "https://www.recreation.gov/api/permitwbe/621744/availability/monthly?year=2025&start_date=2025-10-01&division_id=744",
    # "crater_lake_3d": "https://www.recreation.gov/api/permititinerary/4675319/division/4675319029/availability/month?month=8&year=2025",
    "crater_lake_season": "https://www.recreation.gov/api/permititinerary/4675318/division/4675318029/availability/month?month=8&year=2025",
    # "middle_fork": "https://www.recreation.gov/api/permits/234623/divisions/377/availability?start_date=2025-07-29T06:00:00.000Z&end_date=2025-12-31T00:00:00.000Z&commercial_acct=false&is_lottery=false",
    # "main_salmon": "https://www.recreation.gov/api/permits/234622/divisions/376/availability?start_date=2025-07-29T06:00:00.000Z&end_date=2025-12-31T00:00:00.000Z&commercial_acct=false&is_lottery=false",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}

EXCLUDE_DATES = [
    '2025-11-28T00:00:00Z'
]

def get_available(url):
    r = requests.get(url, headers=HEADERS)
    j = r.json()
    available = {}
    if 'date_availability' in j['payload'].keys() and j['payload']['date_availability'] is not None:
        for d in j['payload']['date_availability']:
            if j['payload']['date_availability'][d]['remaining'] > 0:  # and d not in EXCLUDE_DATES:
                short_date = datetime.datetime.fromisoformat(d).strftime("%Y-%m-%d")
                available[short_date] = {'remaining': j['payload']['date_availability'][d]['remaining']}
    elif 'quota_type_maps' in j['payload'].keys() and j['payload']['quota_type_maps'] is not None:
        for d in j['payload']['quota_type_maps']['ConstantQuotaUsageDaily']:
            if j['payload']['quota_type_maps']['ConstantQuotaUsageDaily'][d]['remaining'] > 0: 
                short_date = datetime.datetime.fromisoformat(d).strftime("%Y-%m-%d")
                available[short_date] = {'remaining': j['payload']['quota_type_maps']['ConstantQuotaUsageDaily'][d]['remaining']}
    else:
        return {'error': ''}

    return available


def get_all_available():
    available = {}
    for k, val in URLS.items():
        available[k] = get_available(val)
    return available


def any_available(j: dict):
    for k, v in j.items():
        if len(v) > 0:
            return True
    return False