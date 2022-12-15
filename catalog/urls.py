#from django.urls import path
from . import views
from django.urls import  re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),#(?P<pk>\d+)$
]
urlpatterns += [
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),#(?P<pk>\d+)$
]

urlpatterns += [
    re_path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]


urlpatterns += [
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]



urlpatterns += [
    re_path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    re_path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    re_path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]
