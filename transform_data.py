import pandas as pd

def to_data_frame(raw_data):
    
    data = pd.DataFrame(raw_data)
    data['_id'] = data['_id'].astype(str)
    return data

def get_project_details(data:pd.DataFrame):

    project_details = pd.DataFrame([{}])
    project_details = data[['_id', 'project_id', 'project_name', 'technologies', 'status']].copy()

    return project_details

def get_client(data:pd.DataFrame):

    test_clients = pd.DataFrame(list(data['client']))
    test_clients_2 = pd.DataFrame(list(test_clients['location']))

    client = pd.concat([
        data['project_id'],
        test_clients[['name', 'industry']],
        test_clients_2[['city', 'country']]
    ], axis=1)

    index = []
    for i in range(1,len(client)+1):
        index.append(i)

    index_1 = {'client_id': index}
    index = pd.DataFrame(index_1)

    index = index.reset_index(drop=True)
    client = client.reset_index(drop=True)

    client = pd.concat([index,
                        client
                        ],axis=1)

    return client

def get_milestones(data:pd.DataFrame):

    milestones = data[['project_id', 'milestones']].explode('milestones')
    milestones = pd.concat([milestones[['project_id']],
                            milestones['milestones'].apply(pd.Series)],
                            axis=1)
    index = []
    for i in range(1,len(milestones)+1):
        index.append(i)

    index_1 = {'milestone_id': index}
    index = pd.DataFrame(index_1)

    index = index.reset_index(drop=True)
    milestones = milestones.reset_index(drop=True)

    milestones = pd.concat([index,milestones],axis=1)


    return milestones

def get_teams(data:pd.DataFrame):

    Teams = data[['project_id', 'team']].copy()
    Teams[['project_manager', 'members']] = Teams['team'].apply(pd.Series)
    Teams = Teams.drop(columns=['team'])
    Teams = Teams.explode('members')
    members_expanded = Teams['members'].apply(pd.Series)
    Teams = pd.concat(
        [Teams[['project_id', 'project_manager']], members_expanded],
        axis=1
    )

    index = []
    for i in range(1,len(Teams)+1):
        index.append(i)

    index_1 = {'emp_id': index}
    index = pd.DataFrame(index_1)

    index = index.reset_index(drop=True)
    Teams = Teams.reset_index(drop=True)

    Teams = pd.concat([index,Teams],axis=1)

    return Teams

def get_fact_table(project: pd.DataFrame, client: pd.DataFrame, teams: pd.DataFrame, milestones: pd.DataFrame):
    fact = pd.DataFrame({
        'project_id': project['_id'],
        'client_id': client['client_id'],
        'emp_id': teams['emp_id'],
        'milestone_id': milestones['milestone_id']
    })
    
    return fact
