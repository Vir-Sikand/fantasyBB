from flask import Flask, render_template, url_for, request
from flask import session
from flask_sqlalchemy import SQLAlchemy
from espn_api.basketball import League
from gptRec import getRec


app = Flask(__name__)
app.secret_key = '1234'

#my_league = League(league_id=1543737281, year=2024, swid= '{D0EECBE6-9BF6-4CB4-A93B-2F2246F06779}', espn_s2='AEBnwpovnC0mXb0CQXI1yi0%2FZiCd%2FO%2BxCfBbE%2FGHUBadFYp7mCl8m2WcGEF%2Fl0mAfZ7wcqqkJm9J9S3eWmKSROAXyUBd0nffFEPPEMOIla4tFQl3ha4xH1wXj5V2xSkUgVe40S49szU4CbgMNVa1I6DBCwNxXT0da4k%2BHcbd1wTDZlKpRIKPRiLEQ8xZ%2BpSr6L2Imh26F2JGh%2BAdAXsRjCcdMH5fS8%2FGbtiqMrbkhQ9ToCeNS48mDFKpGn33SyABbHN%2F%2FKRnHHr42SEv4Pdve%2FQMo5QYSzVNC1Mo1A%2BgHzpQ%2FA%3D%3D')


@app.route('/', methods = ["GET", "POST"])
def getInfo() :
    if request.method == "POST" :
        session['league'] = request.form.get("league")
        session['year'] = request.form.get("year")
        session['swid'] = request.form.get("swid")
        session['espns2'] = request.form.get("espns2")
        return render_template("posButtons.html")
        
    return render_template("index.html")

def printTeams(league, year, swid, espns2) :
    my_league = League(league_id=league, year=int(year), swid= swid, espn_s2=espns2)
    teams = my_league.teams
    return str(teams)

def getTop10(my_league, position) :
    freeAgents = my_league.free_agents()
    ten = []
    gptFeed = []
    for player in freeAgents :
        pts = player.avg_points
        s = player.name
        status = player.injuryStatus
        if player.position == position or position == "ANY":
            ten.append((pts, s, status))
            gptFeed.append((pts, player))

    ten.sort()
    ten.reverse()
    gptFeed.sort()
    gptFeed.reverse()
    gptFeed = gptFeed[0:10]

    reccomendation = getRec(gptFeed)

    toRet = ten[0:10]
    ranking = formattedList(toRet)

    return ranking + "<br>" + "<br>" + str(reccomendation)


@app.route('/get_position', methods=["POST"])
def get_position() :
    position = request.form.get("position")
    league = session.get('league')
    year = session.get('year')
    swid = session.get('swid')
    espns2 = session.get('espns2')

    my_league = League(league_id=league, year=int(year), swid= swid, espn_s2=espns2)

    return getTop10(my_league, position)

def formattedList(arr) :
    count = 1
    s = ""
    for item in arr :
        s += str(count) + "." + " " + str(item) + "<br>" + "<br>"
        count += 1
    
    return s

if __name__ == "__main__":
    app.run(debug=True)