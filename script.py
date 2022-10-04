# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo1 = git.Repo("C:/Users/vicpi/Documents/GitHub/Tamarel")
repo2 = git.Repo("C:/Users/vicpi/Documents/GitHub/website-vv-tamar")
# Your mock repo
mock_repo = git.Repo("C:/Users/vicpi/Documents/GitHub/Tamarsite-commit-mocker")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.import_repository()