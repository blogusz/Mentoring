def premium_required(func):
    func.is_premium = True
    return func
