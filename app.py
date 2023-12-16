from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from espn_api.basketball import League




app = Flask(__name__)



@app.route('/')
def getInfo() :
    my_league = League(league_id=1543737281, year=2024, swid= '{D0EECBE6-9BF6-4CB4-A93B-2F2246F06779}', espn_s2='AEBnwpovnC0mXb0CQXI1yi0%2FZiCd%2FO%2BxCfBbE%2FGHUBadFYp7mCl8m2WcGEF%2Fl0mAfZ7wcqqkJm9J9S3eWmKSROAXyUBd0nffFEPPEMOIla4tFQl3ha4xH1wXj5V2xSkUgVe40S49szU4CbgMNVa1I6DBCwNxXT0da4k%2BHcbd1wTDZlKpRIKPRiLEQ8xZ%2BpSr6L2Imh26F2JGh%2BAdAXsRjCcdMH5fS8%2FGbtiqMrbkhQ9ToCeNS48mDFKpGn33SyABbHN%2F%2FKRnHHr42SEv4Pdve%2FQMo5QYSzVNC1Mo1A%2BgHzpQ%2FA%3D%3D')
    teams = my_league.teams
    return str(teams)




if __name__ == "__main__":
    app.run(debug=True)