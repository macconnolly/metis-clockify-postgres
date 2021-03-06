import sys

sys.path.append("../")
from models import Member
from datetime import datetime


def main():
    print("Type the name of the members who are no longer active.")
    print("Example: 'Mac Connolly, Roberto Irizarry'")
    acronyms = input("").lower().split(",")
    for acronym in acronyms:
        member = Member.where("acronym", acronym).first()
        if member is not None:
            member.is_active = False
            date_deactivated_str = input(
                "Type the date of when {} got deactived. Format=DD/MM/YYYY, example: 15/03/2020\n".format(
                    member.acronym
                )
            )
            member.date_deactivated = datetime.strptime(
                date_deactivated_str, "%d/%m/%Y"
            )
            member.update()
            print("Member with name {} updated".format(acronym))
        else:
            print("Member with name {} not found".format(acronym))


if __name__ == "__main__":
    main()
