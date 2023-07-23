# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo1 = git.Repo("C:/Users/vicpi/Documents/GitHub/Tamarel")
repo2 = git.Repo("C:/Users/vicpi/Documents/GitHub/website-vv-tamar")
# Your mock repo
mock_repo = git.Repo("C:/Users/vicpi/Documents/GitHub/Tamarsite-commit-mocker")
importer1 = Importer([repo1], mock_repo)
importer2 = Importer([repo2], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer1.set_author(['myprivateemail@email.com', 'myvolleyballemail@email.com'])
importer1.set_ignore_before_date(1687305600) # next time running this, change this to 2023-11-22 03:54:00 into UTC epoch time
importer1.import_repository()
importer2.set_author(['myprivateemail@email.com', 'myvolleyballemail@email.com'])
importer2.set_ignore_before_date(1687305600)
importer2.import_repository()