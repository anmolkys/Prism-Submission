from tempfile import TemporaryDirectory

from langchain_community.agent_toolkits import FileManagementToolkit

from langchain.tools import tool

working_directory = TemporaryDirectory()

tools = FileManagementToolkit(
    root_dir=r"C:\Users\Naveen\Desktop\HackFirst" + str(working_directory.name),
    selected_tools=["read_file", "write_file", "list_directory"],
).get_tools()



read_tool, write_tool, list_tool = tools



class fileSystem():

    @tool("Write into file")
    def write(data):

        """
        Useful to write into a file.
        The input should be in markdown format.
        """

        write_tool.invoke({"file_path": "example.txt", "text": data})
        

    @tool("Read a file")
    def read(data):
        """
        Useful to read a file.
        The input should be only the file name.
        """
        read_tool.invoke({"file_path": data})