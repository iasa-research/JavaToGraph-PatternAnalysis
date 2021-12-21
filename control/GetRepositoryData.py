# imports
from pydriller import RepositoryMining

# class responsible for retreiving data from git repository
class GetRepositoryData:

    def getRepInfo(self, filename, path):
        with open(filename, 'w', newline='', encoding="utf-8") as f:
            f.write(f"filename;developer;commitdate;path;"
                    f"changetype;oldpath;projectname\n")
            for commit in RepositoryMining(path).traverse_commits():
                project_name = commit.project_name
                # for all modifications happened in one commit do
                for m in commit.modifications:
                    f.write(f"{m.filename};{commit.author.name};"
                            f"{commit.author_date};{m.new_path};"
                            f"{m.change_type};{m.old_path};{project_name}\n")

