def check_food_quality(food_type, hours_passed):
    if hours_passed > 6:
        return "❌ Unsafe"
    elif hours_passed > 3:
        return "⚠ Consume Soon"
    else:
        return "✅ Safe"
