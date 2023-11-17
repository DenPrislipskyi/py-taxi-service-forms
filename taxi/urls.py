from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    DriverListView,
    DriverDetailView,
    ManufacturerListView,
    CarFormatCreateView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    CarFormatUpdateView,
    CarFormatDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturer-list", ),
    path("manufacturers/create/",
         ManufacturerCreateView.as_view(),
         name="manufacturer-create"),
    path("manufacturers/<int:pk>/update/",
         ManufacturerUpdateView.as_view(),
         name="manufacturer-update"),
    path("manufacturers/<int:pk>/delete/",
         ManufacturerDeleteView.as_view(),
         name="manufacturer-delete"),
    path("cars/",
         CarListView.as_view(),
         name="car-list"),
    path("cars/create/",
         CarFormatCreateView.as_view(),
         name="car-create"),
    path("cars/<int:pk>/update/",
         CarFormatUpdateView.as_view(),
         name="car-update"),
    path("cars/<int:pk>/delete/",
         CarFormatDeleteView.as_view(),
         name="car-delete"),
    path("cars/<int:pk>/",
         CarDetailView.as_view(),
         name="car-detail"),
    path("drivers/",
         DriverListView.as_view(),
         name="driver-list"),
    path(
        "drivers/<int:pk>/",
        DriverDetailView.as_view(),
        name="driver-detail"
    ),
]

app_name = "taxi"
