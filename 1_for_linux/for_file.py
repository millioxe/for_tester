import os


class File_implement:
    def __init__(self):
        pass
    def implement_cmd(self,cmd_parm):
        return cmd_parm



if __name__ == '__main__':
    implement=File_implement()
    end_text=implement.implement_cmd("ls")
    print(end_text)
