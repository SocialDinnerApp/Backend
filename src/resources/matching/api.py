from flask_restful import Resource, marshal_with, abort, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src import db
from src.resources import event_participations
from src.resources.event_participations.model import EventParticipation
#from src.resources.matching.args import post_args, update_args
from src.resources.event_team_matching.model import eventTeamMatching
from src.resources.matching.fields import resource_fields
from uuid import uuid4
import datetime
import numpy as np


class TeamMatchingAlgorithmus(Resource):
    
    @marshal_with(resource_fields)
    def get(self, id=None):

        # Alle Events, bei denen bereits Leute teilnehmen
        events = db.session.query(EventParticipation).filter(EventParticipation.eventId == id).all()

        for i in range(0,len(events), 9):
            if len(events) > i and len(events) < i+9:
                pass
            elif len(events) == i+9:
                self.matching(events[i:], id)
            else:
                self.matching(events[i:i+9], id)

    def matching(self, events, id):
        menues = ['S', 'M', 'D']

        
        events_matrix = np.array(events).reshape((3,3))

        x = 0
        for i in range(x,9,3):
            x = i
            if i == 0:
                group_one = events[x:x+3]
                group_one_menues = menues
                group_one_final = []
                for x in range(len(group_one)):
                    group_one_final.append((group_one[x], group_one_menues[x]))

            if i == 3:
                group_two = events[x:x+3]
                group_two_menues = menues[1:3]+list(menues[0])
                group_two_final = []
                for x in range(len(group_two)):
                    group_two_final.append((group_two[x], group_two_menues[x]))

            if i == 6:
                group_three = events[x:x+3]
                group_three_menues = list(menues[2]+menues[0]+menues[1])
                group_three_final = []
                for x in range(len(group_three)):
                    group_three_final.append((group_three[x], group_three_menues[x]))

        starter_group_for_transpose = list([group_one] + [group_two] + [group_three]) 
        # starter_menues = list([group_one_menues] + [group_two_menues] + [group_three_menues])
        starter_group = list([group_one_final] + [group_two_final] + [group_three_final]) 


        main_group_one = []
        main_group_two = []
        main_group_three = []
        for i in range(3):
            main_group_one.append(starter_group[i][0])
            main_group_two.append(starter_group[i][1])
            main_group_three.append(starter_group[i][2])

        main_group = list([main_group_one] + [main_group_two] + [main_group_three])
        starter_group_flated = [item for sublist in starter_group for item in sublist]
        main_group_flated = [item for sublist in main_group for item in sublist]

        dessert_group_one = []
        dessert_group_two = []
        dessert_group_three = []
        for i in range(3):
            dessert_group_one.append(main_group[i][i])


        dessert_group_two.append(main_group[0][1])
        dessert_group_two.append(main_group[1][2])
        dessert_group_two.append(main_group[2][0])


        dessert_group_three.append(main_group[0][2])
        dessert_group_three.append(main_group[1][0])
        dessert_group_three.append(main_group[2][1])

        dessert_group = list([dessert_group_one] + [dessert_group_two] + [dessert_group_three])

        for team in events:
            #Create unique ID
            matching_id = str(uuid4())
            event_Team_Matching = eventTeamMatching(
                matchingId = matching_id,
                teamId = team.teamId, 
                eventId = id,
            )
            #Add event_Team_Matching to database
            db.session.add(event_Team_Matching)
            db.session.commit()

        for group in starter_group:
            host = [c[0] for c in group if c[1] == "S"][0]
            guests = [c[0] for c in group]
            for guest in guests:
                # Update für Gäste deren Zeilen in Eventteammatching mit der HostId
                zeile = eventTeamMatching.query.filter_by(teamId = guest.teamId, eventId = id).first()
                zeile.starterTeamId = host.teamId
                db.session.commit()

        for group in main_group:
            host = [c[0] for c in group if c[1] == "M"][0]
            guests = [c[0] for c in group]
            for guest in guests:
                # Update für Gäste deren Zeilen in Eventteammatching mit der HostId
                zeile = eventTeamMatching.query.filter_by(teamId = guest.teamId, eventId = id).first()
                zeile.mainTeamId = host.teamId
                db.session.commit()

        for group in dessert_group:
            host = [c[0] for c in group if c[1] == "D"][0]
            guests = [c[0] for c in group]
            for guest in guests:
                # Update für Gäste deren Zeilen in Eventteammatching mit der HostId
                zeile = eventTeamMatching.query.filter_by(teamId = guest.teamId, eventId = id).first()
                zeile.dessertTeamId = host.teamId
                db.session.commit()

            
        return events
