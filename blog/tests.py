from django.test import TestCase
from django.utils import timezone
from blog.models import Post
from django.core.urlresolvers import reverse

#Factory method to create posts
def create_post(title, author, slug, body):
  """ 
  Creates a post with the given info.
  """
  return Post.objects.create(title=title,pub_date=timezone.now(),author=author,
      slug=slug,body=body)

  class PostIndexViewTests(TestCase):
    def test_index_view_with_a_post(self):
      """ 
    The index view should create a link with the title as a link.
    """
    new_post = create_post(title="New Post",author="Emil Abraham",
        slug="new-post",body="This is the body")
    response = self.client.get(reverse('blog:index'))
    self.assertQuerysetEqual(
        response.context['all_posts'],
        ['<Post: New Post>']
        )   

    def test_index_view_with_future_post(self):
      """
      The index view should be empty and display: No posts available
      """
    future_post = create_post(title="Future Post", author="Emil Abraham",
        slug="future-post",body="This is the future body",
        pub_date=timezone.now()+20)
    response = self.client.get(reverse('blog:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No posts are available")

    def test_index_view_without_posts(self):
      """
      The index view should return No posts available
      """
      response = self.client.get(reverse('blog:index'))
      self.assertEqual(reponse.status_code, 200)
      self.assertContains(response, "No posts are available")
