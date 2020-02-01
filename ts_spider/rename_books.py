import os

"""
rename some books, remove some head info eg:

ePUBw.COM+-+论爱美.（法）夏尔•佩潘.南海出版公司.2019-8.epub
论爱美.（法）夏尔•佩潘.南海出版公司.2019-8.epub
"""


def rename_books(base_dir):
    os.chdir(base_dir)
    for f in os.listdir(base_dir):
        filename, suffix = os.path.splitext(f)
        if suffix == '.epub':
            # print(f)
            # print(filename[12:] + suffix)
            # print()

            os.rename(f, filename[12:] + suffix)

    print("Done!")


if __name__ == '__main__':
    base_dir = "/home/fc/Desktop"
    rename_books(base_dir)


