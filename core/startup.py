from time import sleep


def startup_animation(logger):

    modules = [
        "Brain",
        "Voice",
        "Vision",
        "Memory",
        "Automation"
    ]

    for module in modules:
        logger.log(f"Loading {module}...")
        sleep(1)

    logger.log("All systems online.")