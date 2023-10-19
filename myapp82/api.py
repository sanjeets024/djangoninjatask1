from django.contrib.auth import get_user
from ninja import Router
from .models import Post
from ninja import Router, Query
from typing import List
from ninja import NinjaAPI


api = NinjaAPI(title="postapi")

@api.post("/create-post")
def create_post(request, title: str, content: str):

    user = get_user(request)


    post = Post.objects.create(user=user, title=title, content=content)

    return {"id": post.id, "title": post.title, "content": post.content, "created_at": post.created_at}





@api.post("/associate-tags/{post_id}")
def associate_tags(request, post_id: int, tags: List[int]):
    try:
        post = Post.objects.get(id=post_id)
        post.tags.add(*tags)
        return {"message": "Tags associated with the post successfully"}
    except Post.DoesNotExist:
        return {"error": "Post not found"}

@api.get("/posts-by-tags")
def get_posts_by_tags(request, tags: List[int] = Query(...)):
    posts = Post.objects.filter(tags__in=tags).distinct()
   
    return posts
