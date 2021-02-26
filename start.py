from bot import CollectPosts
import pandas as pd

def parsing(login,password,keywords):
    f = CollectPosts()
    f.login(login, password)
    data = f.query(keywords)
    return data

    # df = pd.DataFrame(data).to_string()
    # return df

    # writer = pd.ExcelWriter("./data.xlsx", engine="xlsxwriter")
    # df.to_excel(writer, sheet_name="Result", index=False)
    #
    # writer.sheets["Result"].set_column("A:A", 40)
    # writer.sheets["Result"].set_column("B:B", 20)
    # writer.sheets["Result"].set_column("C:C", 100)
    # writer.sheets["Result"].set_column("D:D", 100)
    #
    # writer.save()


