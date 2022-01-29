# Syntax version of this config file.
syntaxver = "1.1-0"

# After updating CP, you might want to delete this file and have CP generate a new one conforming to the newer syntax
# standards. Below are some config options. They are Python lists; be sure to use correct syntax.

# Disabled commands:
discomm = []
# Automatically import modules:
impor = ["cpfm", ]
# Run commands on startup:
autorun = ["ver", "help", ]

# Top/Bottom Borders of coolBorder messages
cbh = "="
# Left Side
cbvl = "]]]"
# Right Side (There's some cheating going on here to make the backslashes work.)
cbvr = "[[["
#a = ""
#cbvr = f"\\{a}\\{a}\{a}"


def main():
    print(f"CP Config File; Syntax version {syntaxver}.")
    print("To change config settings, edit this Python file in a text editor.")


newcomms = {}

if __name__ == "__main__":
    main()
