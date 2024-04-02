import os
from exa_py import Exa
from langchain.agents import tool

class ExaSearchTool:
	@tool
	def search(query: str):
		"""Search for a webpage based on the query."""
		return ExaSearchTool._exa().search(f"{query}", use_autoprompt=True, num_results=3)

	@tool
	def find_similar(url: str):
		"""Search for webpages similar to a given URL.
		The url passed in should be a URL returned from `search`.
		"""
		return ExaSearchTool._exa().find_similar(url, num_results=3)

	@tool
	def get_contents(ids: str):
		"""Get the contents of a webpage.
		The ids must be passed in as a list, a list of ids returned from `search`.
		"""
		ids = eval(ids)
		contents = str(ExaSearchTool._exa().get_contents(ids))
		print(contents)
		contents = contents.split("URL:")
		contents = [content[:1000] for content in contents]
		return "\n\n".join(contents)

	def tools():
		return [ExaSearchTool.search, ExaSearchTool.find_similar, ExaSearchTool.get_contents]

	def _exa():
		return Exa(api_key=os.environ["EXA_API_KEY"])
	

	

from langchain.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())


from langchain_community.tools import YouTubeSearchTool

youtube = YouTubeSearchTool()

from langchain_community.tools.google_scholar import GoogleScholarQueryRun
from langchain_community.utilities.google_scholar import GoogleScholarAPIWrapper

scholar_search = GoogleScholarQueryRun(api_wrapper=GoogleScholarAPIWrapper())
