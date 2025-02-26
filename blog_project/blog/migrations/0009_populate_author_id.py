from django.db import migrations
from django.contrib.auth.models import User

def populate_author_id(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        try:
            user = User.objects.get(username=post.author)
            post.author_id = user.id
            post.save()
        except User.DoesNotExist:
            # Handle the case where the user doesn't exist
            # You might want to log an error or set a default user
            print(f"User '{post.author}' not found for post {post.id}")

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_add_missing_author_id'),
    ]

    operations = [
        migrations.RunPython(populate_author_id),
    ]