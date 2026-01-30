from django.core.management.base import BaseCommand  # type: ignore[import]
from core.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', members=['Iron Man', 'Captain America', 'Thor'])
        dc = Team.objects.create(name='DC', members=['Superman', 'Batman', 'Wonder Woman'])

        # Create users
        u1 = User.objects.create(username='ironman', email='ironman@marvel.com', team='Marvel')
        u2 = User.objects.create(username='cap', email='cap@marvel.com', team='Marvel')
        u3 = User.objects.create(username='thor', email='thor@marvel.com', team='Marvel')
        u4 = User.objects.create(username='superman', email='superman@dc.com', team='DC')
        u5 = User.objects.create(username='batman', email='batman@dc.com', team='DC')
        u6 = User.objects.create(username='wonderwoman', email='wonderwoman@dc.com', team='DC')

        # Create activities
        Activity.objects.create(user='ironman', type='run', duration=30)
        Activity.objects.create(user='cap', type='cycle', duration=45)
        Activity.objects.create(user='thor', type='swim', duration=60)
        Activity.objects.create(user='superman', type='fly', duration=120)
        Activity.objects.create(user='batman', type='run', duration=50)
        Activity.objects.create(user='wonderwoman', type='jump', duration=40)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', score=135)
        Leaderboard.objects.create(team='DC', score=210)

        # Create workouts
        Workout.objects.create(name='Push Ups', description='Do 20 push ups', difficulty='Easy')
        Workout.objects.create(name='Sit Ups', description='Do 30 sit ups', difficulty='Medium')
        Workout.objects.create(name='Squats', description='Do 40 squats', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
