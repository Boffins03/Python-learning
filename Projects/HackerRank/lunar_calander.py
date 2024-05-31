from lunardate import LunarDate

def gregorian_to_chinese(year, month, day):
    lunar_date = LunarDate.fromSolarDate(year, month, day)
    return lunar_date

# Example usage
gregorian_date = (2005, 1, 21)
chinese_date = gregorian_to_chinese(*gregorian_date)
print("Gregorian Date:", "/".join(map(str, gregorian_date)))
print("Chinese Date:", chinese_date)
