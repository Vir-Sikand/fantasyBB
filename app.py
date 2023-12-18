from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from espn_api.basketball import League




app = Flask(__name__)

#my_league = League(league_id=1543737281, year=2024, swid= '{D0EECBE6-9BF6-4CB4-A93B-2F2246F06779}', espn_s2='AEBnwpovnC0mXb0CQXI1yi0%2FZiCd%2FO%2BxCfBbE%2FGHUBadFYp7mCl8m2WcGEF%2Fl0mAfZ7wcqqkJm9J9S3eWmKSROAXyUBd0nffFEPPEMOIla4tFQl3ha4xH1wXj5V2xSkUgVe40S49szU4CbgMNVa1I6DBCwNxXT0da4k%2BHcbd1wTDZlKpRIKPRiLEQ8xZ%2BpSr6L2Imh26F2JGh%2BAdAXsRjCcdMH5fS8%2FGbtiqMrbkhQ9ToCeNS48mDFKpGn33SyABbHN%2F%2FKRnHHr42SEv4Pdve%2FQMo5QYSzVNC1Mo1A%2BgHzpQ%2FA%3D%3D')


@app.route('/', methods = ["GET", "POST"])
def getInfo() :
    if request.method == "POST" :
        league = request.form.get("league")
        year = request.form.get("year")
        swid = request.form.get("swid")
        espns2 = request.form.get("espns2")
        #my_league = League(league_id=league, year=2024, swid= swid, espn_s2=espns2)
        #teams = my_league.teams
        return printTeams(league, year, swid, espns2)
        
    return render_template("index.html")

def printTeams(league, year, swid, espns2) :
    my_league = League(league_id=league, year=int(year), swid= swid, espn_s2=espns2)
    teams = my_league.teams
    return str(teams)



if __name__ == "__main__":
    app.run(debug=True)