def test(output, expected):
    import colorama
    from colorama import Fore
    if output != expected:
        print(Fore.RED + "FAIL :(")
        print(f"expected: \"{expected}\"")
        print(f"got: \"{output}\"")
    else:
        print(Fore.GREEN + "PASS :)")
        print(f"output: {output}", Fore.WHITE)
    print("=======================================")
