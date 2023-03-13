import re

long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""

pattern = r"^(.*)\n(\w{20})$"
match = re.search(pattern, long_text, re.MULTILINE)

name = match.group(1)
lei = match.group(2)

pattern = r"^\d+\. (.*)\n((?:LU\d{10}\n)+)"
sub_fund_matches = re.findall(pattern, long_text, re.MULTILINE)

sub_fund_list = []
for sub_fund_match in sub_fund_matches:
    title = sub_fund_match[0]
    isin_list = sub_fund_match[1].strip().split("\n")
    sub_fund = {"title": title, "isin": isin_list}
    sub_fund_list.append(sub_fund)

data = {"name": name, "lei": lei, "sub_fund": sub_fund_list}

print(data)

