from application import db

class Publisher(db.Model):
    id = db.Column()
    name = db.Column()
    industry = db.Column()
    website = db.Column()
    email = db.Column()
    url_logo = db.Column()
    campaigns_lauched = db.Column()



    def __str__(self):
        return self.id


class Creators(db.Model):
    id = db.Column()
    first_name = db.Column()
    last_name = db.Column()
    nick_name = db.Column()
    url_picture = db.Column()
    email = db.Column()
    topics = db.Column()
    instagram = db.Column()
    tik_tok = db.Column()
    facebook = db.Column()
    twitter = db.Column()
    youtube = db.Column()
    total_followers = db.Column()
    campaigns_done = db.Column()

    def __str__(self):
        return self.id

class Campaigns(db.Model):
    id = db.Column()
    name = db.Column()
    start_date = db.Column()
    last_date = db.Column()
    budget = db.Column()
    sources = db.Column()
    description = db.Column()

    id_creator = 
    id_publisher =