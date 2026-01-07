def risk_check(vix_change, loss_streak):
    if vix_change > 0.15:
        return False
    if loss_streak >= 3:
        return False
    return True

