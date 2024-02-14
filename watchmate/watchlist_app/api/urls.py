from django.contrib import admin
from django.urls import path,include
from watchlist_app.api.views import WatchListAV,WatchDetailAV,StreamingListAV,StreamingDetailAV,ReviewListAV,ReviewDetailAV

urlpatterns = [
    
    path('list/',WatchListAV.as_view(),name='movie_list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('streamlist/',StreamingListAV.as_view(),name="streaming-detail"),
    path('stream/<int:pk>/',StreamingDetailAV.as_view(),name="individual details"),
#     path('review/',ReviewListAV.as_view(),name="Reviw-list"),
#     path('review/<int:pk>/',ReviewDetailAV.as_view(),name='review-detail')

    path('stream/<int:pk>/review',ReviewListAV.as_view(),name="review-list"),
    path('stream/review/<int:pk>',ReviewDetailAV.as_view(),name='review-detail')
]