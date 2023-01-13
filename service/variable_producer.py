def produce_captcha(captcha_solver_results):
    if "code" in captcha_solver_results:
        code = captcha_solver_results["code"]
    return code
