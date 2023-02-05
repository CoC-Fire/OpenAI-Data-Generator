"""
AIDataGen.py
Made by CoCFire#1111

Hi, just a basic module that I made. If you're using this, have fun!
Also, please sub to my YT channel at https://youtube.com/@CoCFire
Thanks!

I will be working on this a little bit later, but for now it won't 
stop you on any errors. It's literally just something I spent 5 minutes
to make, so just keep that in mind.
"""

def recdata(filename: str):
    """This is just a function made to simplify the process of recording data"""
    datafil = f"{filename}" + ".jsonl"
    while True:
        line = input("Type 'END' to exit the program, or enter the prompt and desired output using ',,,' to separate them: ")
        if line == "END":
            print(f"Your data has been saved to {datafil}.")
            break
        else:
            prompt, completion = line.split(",,,")
            data = '{"prompt": '+f'"{prompt}"'+', "completion": '+f'"{completion}"'+'}'
            with open(datafil, "a") as file:
                file.write("\n"+data)
                
def main():
    """This runs the actual module, and it includes the option to create a new file or open an existing file"""
    print("AI model fine-tuning data helper v0.0.1\n\n"
          "Made by CoCFire#1111, for use with AI model fine-tuning\n"
          "Was made to make it easier to create a dataset for model training\n"
          "Because i got bored copy/pasting the normal format over and over again\n"
          "This is still experimental, and all data should still be manually reviewed\n"
          "but it should make things a bit easier!\n"
          " ______  ______  ______  _____    __ ________  ________ \n"
          "|      ||      ||   ___||     \  |  |        ||___  ___|\n"
          "|  ||  ||  ||  ||  |___ |  |\  \ |  |   ||   |   |  |   \n"
          "|  ||  ||   ___||   ___||  | \  \|  |   __   |   |  |   \n"
          "|  ||  ||  |    |  |___ |  |  \  |  |  |  |  | __|  |__ \n"
          "|______||__|    |______||__|   \____|__|  |__||________|\n\n"
          "I hope it works well for you!")
    action = input("If you would like to create a new data file, type 'Y', if not, just press enter to edit an existing file: ")
    if action == "Y":
        filename = input("Please enter the name of the data file: ")
        with open(f"{filename}"+".jsonl", "w") as file:
            file.write("\n")
        print(f"Data file was created as '{filename}.jsonl'.")
        recdata(filename)
    else:
        filename = input("Please enter the name of the data file: ")
        recdata(filename)

main()
