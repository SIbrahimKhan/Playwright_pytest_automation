DEFAULT_PASSWORD = "secret_sauce"

USERS = {
    "standard": {"username": "standard_user", "password": DEFAULT_PASSWORD},
    "locked_out": {"username": "locked_out_user", "password":DEFAULT_PASSWORD},
    "problem": {"username": "problem_user", "passwoord":DEFAULT_PASSWORD},
    "performance_glitch": {"username": "performance_glitch_user", "passwoord":DEFAULT_PASSWORD},
    "error": {"username": "error_user", "passwoord":DEFAULT_PASSWORD},
    "visual": {"username": "visual_user", "passwoord":DEFAULT_PASSWORD},
}

PRODUCTS = {
    "backpack": "sauce-labs-backpack",
    "bike_light": "sauce-labs-bike-light",
    "bolt_tshirt": "sauce-labs-bolt-t-shirt",
    "fleece_jacket": "sauce-labs-fleece-jacket",
    "onesie": "sauce-labs-onesie",
    "red_tshirt": "test.allthethings()-t-shirt-(red)",
}

CHECKOUT_INFO = {
    "valid": {"first_name":"jane", "last_name":"patrick", "postal_code":"94107"},
}

ERROR_MESSAGES = {
    "locked_out": "Epic sadface: Sorry, this user has been locked out.",
    "invalid_credentials": "Epic sadface: Username and password do not match any user in this service",
    "missing_username": "Epic sadface: Username is required",
    "missing_password": "Epic sadface: Password is required",
    "missing_first_name": "Error: First Name is required",
    "missing_last_name": "Error: Last Name is required",
    "missing_postal_code": "Error: Postal Code is required",
}